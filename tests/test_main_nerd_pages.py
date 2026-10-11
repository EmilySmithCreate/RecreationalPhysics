"""The web pages of paper 1 are generated from the papers' LaTeX: the converter must turn the mathematics it
claims to understand into the right HTML, refuse what it does not know, and the two pages must link to anchors
that exist."""
import collections
import html
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build_main_nerd_pages as build  # noqa: E402
import main_nerd_latex as tex  # noqa: E402
import main_nerd_site as site  # noqa: E402


@pytest.mark.parametrize("source, expected", [
    (r"\lambda = 1.25", "<i>λ</i> = 1.25"),
    (r"4(\lambda-1)", "4(<i>λ</i> − 1)"),
    (r"4\times L", "4 × <i>L</i>"),
    (r"N=64,96,144,192", "<i>N</i> = 64,96,144,192"),
    (r"e^{-12/g}", "<i>e</i><sup>−12/<i>g</i></sup>"),
    (r"\Delta E^\ddagger = 32 - 16\lambda", "Δ<i>E</i><sup>‡</sup> = 32 − 16<i>λ</i>"),
    (r"f_{200}\ge0.75", "<i>f</i><sub>200</sub> ≥ 0.75"),
    (r"\lambda>1", "<i>λ</i> &gt; 1"),
    (r"-0.7", "−0.7"),
    (r"1\tfrac12", "1½"),
])
def test_simple_mathematics_becomes_plain_html(source, expected):
    assert tex.simple_math(source) == expected


@pytest.mark.parametrize("source", [r"\sum_e (S_e-2)_+", r"\binom{M+C-1}{C-1}", r"\widehat\tau", r"\frac{3}{2N}"])
def test_other_mathematics_is_left_for_the_typesetter(source):
    assert tex.simple_math(source) is None
    assert tex.math_inline(source).startswith(r"\(")


def test_inline_text():
    conv = tex.Converter({"a": 1, "b": 2}, {"fig:x": ("3", "#fig-3")})
    out = conv.inline(r"\emph{One} and \textbf{two}~\cite{b,a}, Figure~\ref{fig:x}; 5\% of ``it'' -- done.")
    assert "<em>One</em>" in out and "<strong>two</strong>" in out
    assert '[<a class="cite" href="#src-1">1</a>, <a class="cite" href="#src-2">2</a>]' in out
    assert '<a href="#fig-3">3</a>' in out and "5%" in out and "“it”" in out and "–" in out
    with pytest.raises(tex.Unknown):
        conv.inline(r"\somethingelse{x}")


def test_table_rows_split_outside_mathematics():
    conv = tex.Converter({}, {})
    out = conv.table(r"\toprule A & B \\ \midrule $x & y$ & 2 \\ \bottomrule")
    assert out.count("<th>") == 2 and out.count("<td>") == 2


@pytest.fixture(scope="module")
def pages():
    sizes = collections.defaultdict(lambda: (640, 360))
    technical = build.convert_technical(sizes)
    plain = build.convert_plain(sizes)
    return (site.page_plain(plain, technical, build.CHAPTER_TO_SECTION),
            site.page_technical(technical, plain, build.SECTION_TO_CHAPTERS), plain, technical)


def test_the_pages_hold_the_whole_of_both_papers(pages):
    plain_html, tech_html, plain, technical = pages
    assert [c["num"] for c in plain["chapters"]] == list(range(1, 12)) and plain["n_figures"] == 31
    assert [s["roman"] for s in technical["sections"]] == ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", ""]
    for page in (plain_html, tech_html):
        body = re.sub(r"<script.*?</script>|<pre>.*?</pre>|\\\(.*?\\\)|\\\[.*?\\\]", " ", page[page.index("<body"):],
                      flags=re.S)
        text = html.unescape(re.sub(r"<[^>]+>", " ", body))
        assert not re.search(r"\\[a-zA-Z]+|\$", text)                # no LaTeX left in the reading text


def test_every_cross_link_lands_on_an_anchor(pages):
    plain_html, tech_html, _plain, _technical = pages
    ids = {"plain": set(re.findall(r'\sid="([^"]+)"', plain_html)),
           "tech": set(re.findall(r'\sid="([^"]+)"', tech_html))}
    for name, page in (("plain", plain_html), ("tech", tech_html)):
        for href in re.findall(r'href="([^"]+)"', page):
            if href.startswith("#"):
                assert href[1:] in ids[name], href
            elif href.startswith(site.TECH + "#"):
                assert href.split("#")[1] in ids["tech"], href
            elif href.startswith(site.BASE + "#"):
                assert href.split("#")[1] in ids["plain"], href
    # every chapter points across, and every numbered section points back
    assert plain_html.count('class="xlink"') == 11 and tech_html.count('class="xlink"') == 9
    assert re.search(r'PL, Chs\.\u00a0<a href="/mainnerd/01thecurledtorusburpsPL/#ch2"', tech_html)


def test_the_frame_keeps_its_promises(pages):
    plain_html, tech_html, _plain, _technical = pages
    # every chapter carries one searched question as a heading, and its answer never claims the paper settles it
    assert plain_html.count('<div class="ask"><h3 id="ch') == 11
    assert set(site.CHAPTER_QUESTIONS) == set(range(1, 12))
    for question, answer in site.BIG_QUESTIONS:
        assert question.endswith("?") and html.escape(question) in plain_html
    joined = " ".join(a for _q, a in site.BIG_QUESTIONS)
    assert "Nobody knows" in joined and "not yet reviewed by a physicist" in joined and "toy" in joined
    # advertisements are labelled with the one word, the jokes carry the logo, and one asks for a reader
    for page in (plain_html, tech_html):
        labels = re.findall(r'<span class="ad-label">([^<]*)</span>', page)
        assert labels and set(labels) == {"ADVERTISEMENT"}
        assert "Volunteer to be a reader" in page and "mailto:" + site.AUTHOR_EMAIL in page
    # two of the plain page's four show Ither's phones in the logo's place: one in the sidebar, a pair mid-article
    assert plain_html.count('class="ad-logo"') == 2 and tech_html.count('class="ad-logo"') == 1
    phones = re.findall(r'<span class="ad-phone (\w+)"><img src="([^"]*)" alt="([^"]*)"', plain_html)
    assert [which for which, _src, _alt in phones] == ["talk", "talk", "report"] and "ad-phone" not in tech_html
    assert all(src == site.HERO and alt.startswith("A phone showing") and "Ither" in alt for _w, src, alt in phones)
    for which in ("talk", "report"):                       # each phone has its cut-out rule in the stylesheet
        assert ".ad-phone.%s img{" % which in site.CSS
    # the guestbook exists where the buttons point, and the PDFs are served beside the pages
    assert 'id="guestbook"' in plain_html and site.BASE + "#guestbook" in tech_html
    assert site.PDF_PLAIN in plain_html and site.PDF_TECH in tech_html
    assert "github.com" not in site.PDF_PLAIN + site.PDF_TECH


def test_links_back_to_side_nerd_carry_the_campaign(pages):
    plain_html, tech_html, _plain, _technical = pages
    links = [u for u in re.findall(r'href="(https://sidenerdapps\.com/[^"]*)"', plain_html + tech_html)
             if "/mainnerd" not in u.split("?")[0]]               # the pages' own addresses are not adverts
    assert len(links) >= 6
    for link in links:
        assert "utm_source=mainnerd" in link and "utm_medium=owned-media" in link
        assert "utm_campaign=physics-01-curled-torus-burps" in link and "utm_content=" in link


def test_post_navigation_always_has_somewhere_to_go(pages):
    plain_html, tech_html, _plain, _technical = pages
    soon_html, index_html = site.page_coming_soon(), site.page_index()

    def nav(page):
        found = re.search(r'<div class="postnav">(.*?)</div>', page, flags=re.S)
        return re.findall(r'href="([^"]+)">([^<]+)</a>', found.group(1)) if found else []

    for page in (plain_html, tech_html):                              # a post: the list, and on to the next post
        assert nav(page) == [(site.BLOG, "all posts"), (site.SOON, "next post »")]
    assert nav(soon_html) == [(site.BASE, "« previous post"), (site.BLOG, "all posts")]
    assert nav(index_html) == [] and "Web Ring" not in plain_html + tech_html + soon_html + index_html
    # the placeholder says plainly that nothing is there, stays out of search results and is not tagged as a paper
    assert "nothing to read here yet" in soon_html and 'content="noindex, follow"' in soon_html
    assert "citation_" not in soon_html and "citation_" not in index_html
    assert "citation_title" in plain_html and "citation_title" in tech_html
    # the cow belongs to the torus paper: on both editions, not on the blog's front page
    assert "sleepy-cow.gif" in plain_html and "sleepy-cow.gif" in tech_html and "sleepy-cow.gif" not in index_html


def test_the_interactive_companion_is_hosted_whole_and_unchanged(pages):
    plain_html, tech_html, _plain, _technical = pages
    source = build.COMPANION.read_text(encoding="utf-8")
    page = site.page_knobs(source)
    # one document, one title, and every part of the companion carried over as written
    assert page.startswith("<!DOCTYPE html>") and page.count("<title>") == 1 and page.count("</head>") == 1
    style = re.search(r"<style>.*?</style>", source, flags=re.S).group(0)
    script = source[source.index("<script>"):].strip()
    markup = source[source.index("</style>") + len("</style>"):source.index("<script>")].strip()
    assert style in page and script in page and markup in page
    assert page.index(style) < page.index("</head>") < page.index(markup) < page.index(script)
    for link in re.findall(r"<link\b[^>]*>", source):                 # its fonts, now in the head
        assert link in page[:page.index("</head>")]
    # the blog's own style sheet stays off this page: the two would restyle each other
    assert site.STYLESHEET not in page and 'class="mnb"' in page and "Main Nerd" in page
    assert not re.search(r"<(p|h1|h2|header|section|table)\b[^>]*mnb", page)   # the bar uses no element the tool styles
    # the editions link to the blog's copy, not to the artifact, and the companion links back
    assert site.KNOBS in plain_html and site.ARTIFACT not in plain_html + tech_html + page
    assert 'href="%s"' % site.BASE in page and 'href="%s"' % site.TECH in page and 'href="%s"' % site.BLOG in page
