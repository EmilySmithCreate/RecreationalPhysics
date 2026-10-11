"""Build the web pages of paper 1, "The curled torus burps", for the Side Nerd Blog at
sidenerdapps.com/mainnerd/. Usage:

    python scripts/build_main_nerd_pages.py --tectonic PATH/TO/tectonic

Writes docs/public/mainnerd/:

    index.html                            the blog's front page: the list of posts
    comingsoon/index.html                 where "next post" lands while the next post is not up yet
    01thecurledtorusburpsPL/index.html    the plain-language edition, chapter by chapter
    01thecurledtorusburps/index.html      the technical manuscript, section by section
    01thecurledtorusburpsKnobs/index.html the interactive companion, from docs/public/curling_ladder_tube.html
    assets/main-nerd.css               the stylesheet, shared by every post
    assets/01thecurledtorusburps/         this paper's figures (SVG), both PDFs, the mascot GIF, the share image

The two pages are made from the LaTeX sources of the two editions (docs/papers/curled_torus/), so the text and the
numbers on the pages are the papers' own; nothing is retyped. Each chapter of the plain page links to the matching
section of the technical page and back, so that the two can be read side by side. The pages are plain static HTML,
meant to be copied by the site's owner into sites/sidenerdapps/mainnerd/ of the Side Nerd marketing
repository. Their links are root-absolute (/mainnerd/...), so preview them with a web server rooted at
docs/public:   python -m http.server --directory docs/public   then open http://localhost:8000/mainnerd/

Needs Tectonic (to render the figures) and PyMuPDF (to turn them into SVG). The figures of the plain edition are
drawn in the LaTeX source; they are compiled once more with the `preview` package, which puts each figure on its
own tightly cropped page.
"""
import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from main_nerd_latex import (Converter, environments, match_brace, read_args, roman, slug,   # noqa: E402
                               strip_comments)
from main_nerd_site import (ASSETS as ASSET_URL, BASE, CSS, PDF_PLAIN_NAME, PDF_TECH_NAME, SLUG,   # noqa: E402
                            STYLESHEET, TECH, page_coming_soon, page_index, page_knobs, page_plain,
                            page_technical)

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/curled_torus"
OUT = ROOT / "docs/public/mainnerd"            # the blog; one folder per post, named by SLUG
SHARED_DIR = OUT / "assets"
ASSETS = SHARED_DIR / SLUG                        # this paper's figures, PDFs and pictures
FIGURE_SIZES = OUT.parent / "mainnerd_figures.json"      # kept outside the folder that gets published
COMPANION = ROOT / "docs/public/curling_ladder_tube.html"   # the interactive companion's source

# which section of the technical paper goes with which chapter of the plain edition, and back
CHAPTER_TO_SECTION = {1: "sec-intro", 2: "sec-model", 3: "sec-model", 4: "sec-cost", 5: "sec-exit",
                      6: "sec-conversion", 7: "sec-sealed", 8: "sec-sealed", 9: "sec-lambda",
                      10: "sec-discussion", 11: "sec-discussion"}
SECTION_TO_CHAPTERS = {"sec-intro": [1], "sec-model": [2, 3], "sec-cost": [4], "sec-exit": [5],
                       "sec-conversion": [6], "sec-sealed": [7, 8], "sec-lambda": [9],
                       "sec-discussion": [10, 11], "sec-methods": [10]}
PLAIN_PAGE, TECH_PAGE = BASE, TECH                    # root-absolute: see main_nerd_site.py


# ------------------------------------------------------------------ figures
def render_figures(tectonic):
    """SVG files for every figure of both editions; returns {name: (width, height)} in CSS pixels."""
    try:
        import pymupdf
    except ImportError:                                    # pragma: no cover
        raise SystemExit("PyMuPDF is needed to write the figures: pip install pymupdf")
    sizes = {}
    ASSETS.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for f in PAPER.glob("fig*.pdf"):
            shutil.copy(f, tmp / f.name)
        tex = (PAPER / "paper_plain_language.tex").read_text(encoding="utf-8")
        hook = (r"\usepackage[active,tightpage]{preview}" "\n" r"\setlength\PreviewBorder{3pt}" "\n"
                r"\renewenvironment{figure}[1][]{\begin{preview}\begin{minipage}{\textwidth}\centering" "\n"
                r"  \renewcommand{\caption}[2][]{}\renewcommand{\label}[1]{}}{\end{minipage}\end{preview}}" "\n")
        assert tex.count(r"\begin{document}") == 1
        (tmp / "figs.tex").write_text(tex.replace(r"\begin{document}", hook + r"\begin{document}"),
                                      encoding="utf-8", newline="\n")
        run = subprocess.run([tectonic, "figs.tex"], cwd=tmp, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if run.returncode:
            raise SystemExit(run.stdout.decode("utf-8", errors="replace")[-2000:])
        doc = pymupdf.open(tmp / "figs.pdf")
        for i, page in enumerate(doc, 1):
            name = "plain-fig-%02d.svg" % i
            (ASSETS / name).write_text(page.get_svg_image(text_as_path=True), encoding="utf-8", newline="\n")
            sizes[name] = (round(page.rect.width * 4 / 3), round(page.rect.height * 4 / 3))
        doc.close()
    for stem in ("fig_tori", "fig1", "fig_lambda"):
        doc = pymupdf.open(PAPER / (stem + ".pdf"))
        page = doc[0]
        name = "tech-%s.svg" % stem.replace("_", "-")
        (ASSETS / name).write_text(page.get_svg_image(text_as_path=True), encoding="utf-8", newline="\n")
        sizes[name] = (round(page.rect.width * 4 / 3), round(page.rect.height * 4 / 3))
        doc.close()
    FIGURE_SIZES.write_text(json.dumps(sizes, indent=1) + "\n", encoding="utf-8", newline="\n")
    return sizes


# ------------------------------------------------------------------ shared pieces
class Blocks:
    """Finished pieces of HTML held out of the text while the rest is converted."""

    def __init__(self):
        self.items = []

    def hold(self, text, own_paragraph=True):
        self.items.append(text)
        token = "\x00%d\x00" % (len(self.items) - 1)
        return "\n\n%s\n\n" % token if own_paragraph else token

    def restore(self, text):
        return re.sub("\x00(\\d+)\x00", lambda m: self.restore(self.items[int(m.group(1))]), text)


def plain_text(fragment):
    text = re.sub(r"<[^>]+>", "", fragment)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def first_sentence(fragment, limit=220):
    text = plain_text(re.sub(r'<span class="tag[^>]*>[^<]*</span>', "", fragment))
    m = re.match(r"(.{20,%d}?[.?!])(\s|$)" % limit, text)
    return (m.group(1) if m else text[:limit]).strip()


def bibliography(conv, inner, heading_id="sources"):
    items = []
    for chunk in inner.split(r"\bibitem{")[1:]:
        key, body = chunk.split("}", 1)
        items.append((key, conv.inline(body.strip())))
    out = ['<ol class="sources" id="%s">' % heading_id]
    for n, (key, body) in enumerate(items, 1):
        out.append('<li id="src-%d" value="%d">%s</li>' % (n, n, body))
    out.append("</ol>")
    return "\n".join(out)


def tabular_body(env_text):
    """The rows of a tabular or tabularx, its column specification removed."""
    m = re.search(r"\\begin\{(tabularx?)\}", env_text)
    i = m.end()
    _, i = read_args(env_text, i, 2 if m.group(1) == "tabularx" else 1)
    j = env_text.index("\\end{%s}" % m.group(1))
    return env_text[i:j]


def paragraphs(conv, blocks, body, id_prefix=""):
    """The text between blank lines as <p> elements; a held block alone in a paragraph stands by itself."""
    out = []
    for chunk in re.split(r"\n\s*\n", body):
        chunk = chunk.strip()
        if not chunk:
            continue
        if re.fullmatch("\x00\\d+\x00", chunk):
            out.append(chunk)
            continue
        text = conv.inline(chunk).strip()
        if not text:
            continue
        ident = ""
        m = re.match(r"<em>([^<]{3,80}?)\.?</em>", text)             # a run-in head gets an anchor
        if m and id_prefix:
            ident = ' id="%s%s"' % (id_prefix, slug(m.group(1)))
            text = '<em class="runin">' + text[4:]
        out.append("<p%s>%s</p>" % (ident, text))
    return "\n".join(out)


# ------------------------------------------------------------------ the plain-language edition
def convert_plain(sizes):
    tex = strip_comments((PAPER / "paper_plain_language.tex").read_text(encoding="utf-8"))
    body = tex.split(r"\begin{document}", 1)[1].split(r"\end{document}")[0]
    body = body[body.index("Everything you have ever seen"):]          # the title block is the page's own header
    body = re.sub(r"\\renewcommand\{\\(arraystretch|refname)\}\{[^}]*\}", "", body)

    keys = re.findall(r"\\bibitem\{([^}]+)\}", body)
    cites = {k: n for n, k in enumerate(keys, 1)}
    labels, figures = {}, environments(body, "figure")
    for n, (_a, _b, inner) in enumerate(figures, 1):
        m = re.search(r"\\label\{([^}]+)\}", inner)
        if m:
            labels[m.group(1)] = (str(n), "#fig-%d" % n)

    def cite_href(key, num):
        return TECH_PAGE if key == "tech" else "#src-%d" % num

    conv = Converter(cites, labels, cite_href)
    blocks = Blocks()

    # figures, last first so that positions stay valid
    for n in range(len(figures), 0, -1):
        a, b, inner = figures[n - 1]
        i = inner.index(r"\caption")
        (cap,), _ = read_args(inner, i + len(r"\caption"), 1)
        cap_html = conv.inline(cap)
        name = "plain-fig-%02d.svg" % n
        w, h = sizes[name]
        fig = ('<figure class="fig" id="fig-%d"><img src="%s%s" width="%d" height="%d" loading="lazy" '
               'alt="%s"><figcaption><b>Figure %d.</b> %s</figcaption></figure>'
               % (n, ASSET_URL, name, w, h, html.escape("Figure %d: %s" % (n, first_sentence(cap_html))), n,
                  cap_html))
        body = body[:a] + blocks.hold(fig) + body[b:]

    def display(m):
        conv.used_mathjax = True
        return blocks.hold('<span class="eq">\\[%s\\]</span>' % html.escape(m.group(1).strip(), quote=False),
                           own_paragraph=False)

    body = re.sub(r"\\\[(.*?)\\\]", display, body, flags=re.S)

    for a, b, inner in reversed(environments(body, "center")):
        if r"\begin{tabular" in inner:
            piece = conv.table(tabular_body(inner))
        else:
            piece = '<p class="pull">%s</p>' % conv.inline(inner.strip())
        body = body[:a] + blocks.hold(piece) + body[b:]
    for a, b, inner in reversed(environments(body, "tabularx")):
        whole = body[a:b]
        body = body[:a] + blocks.hold(conv.table(tabular_body(whole), ident="translations", cls="glossary")) + body[b:]
    for a, b, inner in reversed(environments(body, "itemize")):
        inner = re.sub(r"\\setlength\{[^}]*\}\{[^}]*\}", "", inner)
        items = [conv.inline(x.strip()) for x in re.split(r"\\item(?![a-zA-Z])", inner)[1:]]
        body = body[:a] + blocks.hold("<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in items)) + body[b:]
    for a, b, inner in reversed(environments(body, "thebibliography")):
        inner = inner[inner.index(r"\bibitem"):]
        body = body[:a] + blocks.hold('<h2 id="sources-head">Sources</h2>\n' + bibliography(conv, inner)) + body[b:]

    body = re.sub(r"\\par\\Needspace\{[^}]*\}\\vspace\{[^}]*\}\s*\{\\color\{ink\}\\LARGE\\bfseries ([^}]*)\}\\par\s*"
                  r"\\vspace\{[^}]*\}",
                  lambda m: blocks.hold('<h2 id="continuing">%s</h2>' % conv.inline(m.group(1))), body)

    # chapter openers, sub-headings and boxes
    chapters, chapter, seen = [], [0], set()

    def block_macro(name, n_args, make):
        nonlocal body
        pos = 0
        while True:
            i = body.find("\\" + name + "{", pos)
            if i < 0:
                return
            args, j = read_args(body, i + len(name) + 1, n_args)
            piece = blocks.hold(make(*args))
            body = body[:i] + piece + body[j:]
            pos = i + len(piece)

    def make_chapter(kicker, title):
        num = int(kicker.split()[0])
        name = conv.inline(kicker.split(r"\enspace", 1)[1].strip())
        chapters.append(dict(num=num, kicker=name, title=conv.inline(title)))
        return "\x01CHAPTER %d\x01" % num

    block_macro("chapterpage", 2, make_chapter)
    # sub-headings need to know their chapter, so walk the text in order
    out, pos = [], 0
    for m in re.finditer(r"\x00(\d+)\x00|\\sub\{", body):
        if m.group(1) is not None:
            item = blocks.items[int(m.group(1))]
            if item.startswith("\x01CHAPTER"):
                chapter[0] = int(item.strip("\x01").split()[1])
            continue
        if m.start() < pos:
            continue
        j = match_brace(body, m.end() - 1)
        title = conv.inline(body[m.end():j])
        ident = "ch%d-%s" % (chapter[0], slug(title)) if chapter[0] else slug(title)
        while ident in seen:
            ident += "-2"
        seen.add(ident)
        out.append(body[pos:m.start()])
        out.append(blocks.hold('<h3 id="%s">%s</h3>' % (ident, title)))
        pos = j + 1
    body = "".join(out) + body[pos:]
    block_macro("takeaway", 1, lambda x: '<aside class="takeaway"><b>The point to keep:</b> %s</aside>'
                % conv.inline(x))
    block_macro("whyhere", 1, lambda x: '<p class="why"><b>Why we went here.</b> %s</p>' % conv.inline(x))

    text = blocks.restore(paragraphs(conv, blocks, body))
    # split into the opening, the chapters and the back matter
    parts = re.split("\x01CHAPTER (\\d+)\x01", text)
    opening = parts[0]
    for k in range(1, len(parts), 2):
        num = int(parts[k])
        next(c for c in chapters if c["num"] == num)["html"] = parts[k + 1]
    last = chapters[-1]
    cut = last["html"].index('<h2 id="continuing">')
    last["html"], back = last["html"][:cut], last["html"][cut:]
    notes = "".join('<li id="fn-%d">%s <a href="#fnref-%d" aria-label="back to the text">↩</a></li>' % (k, t, k)
                    for k, t in enumerate(conv.footnotes, 1))
    return dict(opening=link_up_plain(opening), chapters=[dict(c, html=link_up_plain(c["html"])) for c in chapters],
                back=link_up_plain(back), notes=notes, mathjax=conv.used_mathjax, n_figures=len(figures))


TECH_SECTION_BY_ROMAN = {}


def link_up_plain(text):
    """Chapter mentions become links within the page; mentions of the technical paper's sections link across."""
    text = re.sub(r"(Chapters?)\u00a0(\d+)((?:, \d+)*)( and\u00a0(\d+))?",
                  lambda m: _chapter_links(m), text)
    text = re.sub(r"Section\u00a0([IVX]+)\b",
                  lambda m: '<a href="%s#%s" target="mn-technical">Section\u00a0%s</a>'
                  % (TECH_PAGE, TECH_SECTION_BY_ROMAN.get(m.group(1), ""), m.group(1))
                  if m.group(1) in TECH_SECTION_BY_ROMAN else m.group(0), text)
    return text


def _chapter_links(m):
    def one(n):
        return '<a href="#ch%s">%s</a>' % (n, n)
    out = "%s\u00a0%s" % (m.group(1), one(m.group(2)))
    for extra in re.findall(r"\d+", m.group(3) or ""):
        out += ", " + one(extra)
    if m.group(5):
        out += " and\u00a0" + one(m.group(5))
    return out


# ------------------------------------------------------------------ the technical manuscript
def convert_technical(sizes):
    tex = strip_comments((PAPER / "paper.tex").read_text(encoding="utf-8"))
    body = tex.split(r"\begin{document}", 1)[1].split(r"\end{document}")[0]
    meta = {}
    for name in ("title", "author", "email", "affiliation", "date"):
        i = body.index("\\%s{" % name)
        (meta[name],), j = read_args(body, i + len(name) + 1, 1)
        body = body[:i] + body[j:]
    body = body.replace(r"\maketitle", "")
    (a, b, abstract), = environments(body, "abstract")
    body = body[:a] + body[b:]

    keys = re.findall(r"\\bibitem\{([^}]+)\}", body)
    cites = {k: n for n, k in enumerate(keys, 1)}

    # numbers: sections, figures, tables, equations
    labels, sections = {}, []
    pos, count = 0, 0
    for m in re.finditer(r"\\section(\*?)\{", body):
        j = match_brace(body, m.end() - 1)
        title = body[m.end():j]
        after = re.match(r"\s*\\label\{([^}]+)\}", body[j + 1:])
        label = after.group(1) if after else None
        numbered = not m.group(1)
        if numbered:
            count += 1
        ident = ("sec-" + label.split(":")[1]) if label else "sec-" + slug(title.split()[0])
        if title.startswith("Methods"):
            ident = "sec-methods"
        if title == "Introduction":
            ident = "sec-intro"
        sections.append(dict(start=m.start(), end=j + 1 + (after.end() if after else 0), title=title, id=ident,
                             roman=roman(count) if numbered else ""))
        if label:
            labels[label] = (roman(count), "#" + ident)
        if numbered:
            TECH_SECTION_BY_ROMAN[roman(count)] = ident
    n_fig = n_tab = n_eq = 0
    for m in re.finditer(r"\\begin\{(figure\*?|table\*?|equation)\}", body):
        end = body.index("\\end{%s}" % m.group(1), m.end())
        lab = re.search(r"\\label\{([^}]+)\}", body[m.end():end])
        kind = m.group(1).rstrip("*")
        if kind == "figure":
            n_fig += 1
            if lab:
                labels[lab.group(1)] = (str(n_fig), "#fig-" + lab.group(1).split(":")[1])
        elif kind == "table":
            n_tab += 1
            if lab:
                labels[lab.group(1)] = (roman(n_tab), "#tab-" + lab.group(1).split(":")[1])
        else:
            n_eq += 1
            if lab:
                labels[lab.group(1)] = (str(n_eq), "#eq-" + lab.group(1).split(":")[1])

    conv = Converter(cites, labels)
    blocks = Blocks()
    abstract_html = conv.inline(abstract.strip())

    def replace_envs(name, make):
        nonlocal body
        for a2, b2, inner in reversed(environments(body, name)):
            body = body[:a2] + make(inner) + body[b2:]

    fig_no = [n_fig + 1]

    def make_figure(inner):
        fig_no[0] -= 1
        stem = re.search(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", inner).group(1).replace(".pdf", "")
        name = "tech-%s.svg" % stem.replace("_", "-")
        (cap,), _ = read_args(inner, inner.index(r"\caption") + len(r"\caption"), 1)
        lab = re.search(r"\\label\{fig:([^}]+)\}", inner).group(1)
        cap_html = conv.inline(cap)
        w, h = sizes[name]
        return blocks.hold('<figure class="fig wide" id="fig-%s"><img src="%s%s" width="%d" height="%d" '
                           'loading="lazy" alt="%s"><figcaption><b>FIG. %d.</b> %s</figcaption></figure>'
                           % (lab, ASSET_URL, name, w, h,
                              html.escape("Figure %d: %s" % (fig_no[0], first_sentence(cap_html))),
                              fig_no[0], cap_html))

    replace_envs("figure*", make_figure)
    tab_no = [n_tab + 1]

    def make_table(inner):
        tab_no[0] -= 1
        (cap,), _ = read_args(inner, inner.index(r"\caption") + len(r"\caption"), 1)
        lab = re.search(r"\\label\{tab:([^}]+)\}", inner).group(1)
        caption = "<b>TABLE %s.</b> %s" % (roman(tab_no[0]), conv.inline(cap))
        return blocks.hold(conv.table(tabular_body(inner), caption=caption, ident="tab-" + lab))

    # tables come in two environments; number them in document order
    spans = sorted([(a2, b2, inner) for a2, b2, inner in environments(body, "table*")]
                   + [(a2, b2, inner) for a2, b2, inner in environments(body, "table")])
    for a2, b2, inner in reversed(spans):
        body = body[:a2] + make_table(inner) + body[b2:]

    eq_no = [n_eq + 1]

    def make_equation(inner):
        eq_no[0] -= 1
        conv.used_mathjax = True
        lab = re.search(r"\\label\{eq:([^}]+)\}", inner)
        inner = re.sub(r"\\label\{[^}]+\}", "", inner).strip()
        return blocks.hold('<span class="eq"%s>\\[%s \\tag{%d}\\]</span>'
                           % ((' id="eq-%s"' % lab.group(1)) if lab else "", html.escape(inner, quote=False),
                              eq_no[0]), own_paragraph=False)

    replace_envs("equation", make_equation)

    def display(m):
        conv.used_mathjax = True
        return blocks.hold('<span class="eq">\\[%s\\]</span>' % html.escape(m.group(1).strip(), quote=False),
                           own_paragraph=False)

    body = re.sub(r"\\\[(.*?)\\\]", display, body, flags=re.S)
    replace_envs("acknowledgments", lambda inner: blocks.hold(
        '<h2 id="acknowledgments">Acknowledgments</h2>\n<p>%s</p>' % conv.inline(inner.strip())))
    replace_envs("thebibliography", lambda inner: blocks.hold(
        '<h2 id="references-head">References</h2>\n'
        + bibliography(conv, inner[inner.index(r"\bibitem"):], "references")))

    # cut into sections (positions were taken before the replacements, so find the headings again)
    pieces, heads = [], list(re.finditer(r"\\section(\*?)\{", body))
    for k, m in enumerate(heads):
        j = match_brace(body, m.end() - 1)
        after = re.match(r"\s*\\label\{([^}]+)\}", body[j + 1:])
        start = j + 1 + (after.end() if after else 0)
        end = heads[k + 1].start() if k + 1 < len(heads) else len(body)
        sec = sections[k]
        text = blocks.restore(paragraphs(conv, blocks, body[start:end], id_prefix=sec["id"].replace("sec-", "") + "-"))
        pieces.append(dict(id=sec["id"], roman=sec["roman"], title=conv.inline(sec["title"]),
                           html=link_up_technical(text)))
    return dict(meta={k: conv.inline(v) for k, v in meta.items()}, abstract=link_up_technical(abstract_html),
                sections=pieces, mathjax=conv.used_mathjax)


def link_up_technical(text):
    """'PL, Ch. 5' and 'PL, Chs. 2 and 3' become links to those chapters of the plain page."""
    def chapters(m):
        out = "PL, %s\u00a0" % m.group(1)
        out += '<a href="%s#ch%s" target="mn-plain">%s</a>' % (PLAIN_PAGE, m.group(2), m.group(2))
        if m.group(3):
            out += ' and\u00a0<a href="%s#ch%s" target="mn-plain">%s</a>' % (PLAIN_PAGE, m.group(3), m.group(3))
        return out
    return re.sub(r"PL, (Chs?\.)\u00a0(\d+)(?: and\u00a0(\d+))?", chapters, text)


# ------------------------------------------------------------------ main
def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tectonic", default="tectonic")
    parser.add_argument("--skip-figures", action="store_true", help="reuse the SVG files already in assets/")
    args = parser.parse_args()
    if args.skip_figures:
        sizes = {k: tuple(v) for k, v in json.loads(FIGURE_SIZES.read_text()).items()}
    else:
        sizes = render_figures(args.tectonic)
    technical = convert_technical(sizes)             # first: the plain page links to its section anchors
    plain = convert_plain(sizes)
    pages = {OUT / (SLUG + "PL") / "index.html": page_plain(plain, technical, CHAPTER_TO_SECTION),
             OUT / SLUG / "index.html": page_technical(technical, plain, SECTION_TO_CHAPTERS),
             OUT / (SLUG + "Knobs") / "index.html": page_knobs(COMPANION.read_text(encoding="utf-8")),
             OUT / "index.html": page_index(),
             OUT / "comingsoon" / "index.html": page_coming_soon(),
             SHARED_DIR / STYLESHEET: CSS.lstrip("\n")}
    for path, text in pages.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    # the two PDFs travel with the pages, so their links do not depend on which branch a repository shows
    shutil.copyfile(PAPER / "paper_plain_language.pdf", ASSETS / PDF_PLAIN_NAME)
    shutil.copyfile(PAPER / "paper.pdf", ASSETS / PDF_TECH_NAME)
    for needed in ("sleepy-cow.gif", "og-image.png"):
        if not (ASSETS / needed).exists():
            print("NOTE: %s is missing from %s; the pages refer to it" % (needed, ASSETS))
    print("plain page: %d chapters, %d figures, MathJax %s" % (len(plain["chapters"]), plain["n_figures"],
                                                                "needed" if plain["mathjax"] else "not needed"))
    print("technical page: %d sections, MathJax %s" % (len(technical["sections"]),
                                                       "needed" if technical["mathjax"] else "not needed"))
    print("written to", OUT)


if __name__ == "__main__":
    main()
