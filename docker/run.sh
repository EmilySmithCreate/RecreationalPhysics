#!/bin/sh
# Run one config through one runner and put what it produced in S3.
#
#   run.sh <runner script, without scripts/ or .py> <config name, without configs/ or .json>
#
# Both are named explicitly rather than inferred: a config does not record which runner it belongs
# to, and guessing that from its keys is the kind of cleverness that silently runs the wrong chain.
#
# Nothing here writes to the repository. A result becomes a result when a person downloads it and
# commits it, which is what keeps rule 5 true -- results are append-only, and each one has a config
# and a runner behind it that a reader can check.
set -eu

if [ $# -ne 2 ]; then
    echo "usage: run.sh <runner> <config>" >&2
    exit 2
fi

RUNNER="$1"
CONFIG="$2"
DEST="s3://${RESULTS_BUCKET}/${CONFIG}"

if [ ! -f "scripts/${RUNNER}.py" ]; then
    echo "no such runner: scripts/${RUNNER}.py" >&2
    exit 2
fi
if [ ! -f "configs/${CONFIG}.json" ]; then
    echo "no such config: configs/${CONFIG}.json" >&2
    exit 2
fi

# On any failure -- including a Fargate Spot reclaim, which arrives as a TERM -- keep whatever the
# run had written. A .partial is scratch, so it goes under partial/, which the bucket expires.
save_partial() {
    echo "--- run did not finish; saving scratch to ${DEST}"
    for f in "results/${CONFIG}.csv.partial" "results/${CONFIG}.meta.json"; do
        [ -f "$f" ] && aws s3 cp "$f" "s3://${RESULTS_BUCKET}/partial/${CONFIG}/$(basename "$f")"
    done
    exit 1
}
trap save_partial TERM INT

echo "--- ${RUNNER} on ${CONFIG}"
python "scripts/${RUNNER}.py" "configs/${CONFIG}.json" || save_partial

echo "--- uploading to ${DEST}"
for f in "results/${CONFIG}.csv" "results/${CONFIG}.meta.json"; do
    if [ -f "$f" ]; then
        aws s3 cp "$f" "${DEST}/$(basename "$f")"
    else
        echo "expected ${f} and it is not there" >&2
        exit 1
    fi
done

# The tempering runner also writes one .npz of (S, X) histograms per replica and rung.
if [ -d "results/${CONFIG}_hist" ]; then
    aws s3 cp --recursive "results/${CONFIG}_hist" "${DEST}/${CONFIG}_hist"
fi

echo "--- done"
