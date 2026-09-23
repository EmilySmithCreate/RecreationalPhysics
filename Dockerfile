# The versions are pinned to exactly what the .meta.json of every run on the record already says:
# python 3.12.10, numpy 2.0.0, numba 0.67.0. That is the point of the image. A result computed
# here has to be comparable with one computed on the laptop, and `tests/test_cqg.py` pins the
# capped kernel bit for bit, a check that has been run Linux against Windows. Changing a version
# here is changing the instrument, so it belongs in a commit that says so.
FROM python:3.12.10-slim

RUN pip install --no-cache-dir \
      numpy==2.0.0 \
      numba==0.67.0 \
      networkx==3.2.1 \
      awscli==1.34.0

WORKDIR /app

COPY pyproject.toml ./
COPY src ./src
COPY scripts ./scripts
COPY configs ./configs

# --no-deps: the versions above are the pinned ones, and pyproject's floors would let pip move them.
RUN pip install --no-cache-dir --no-deps -e . && mkdir -p results

COPY docker/run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh

ENTRYPOINT ["/usr/local/bin/run.sh"]
