"""The page shell for the web pages of paper 1 on the Side Nerd Blog, sidenerdapps.com/mainnerd/: each edition
is a post, at /mainnerd/01thecurledtorusburpsPL/ (plain language) and /mainnerd/01thecurledtorusburps/
(technical), drawn as a 1990s home page in Side Nerd's colors, with a few advertisements (for Side Nerd, the author's
company, which sponsors the pages, and one that asks for a scientist to read the work), the mascot GIF, a
guestbook that runs on
e-mail, and the blocks search engines and AI assistants read (summary, question headings, quick answers, glossary,
how to cite, JSON-LD).

Everything about the paper on these pages comes from the papers' own text (scripts/build_main_nerd_pages.py);
what is written here is the frame around it. The questions and answers restate the plain-language edition and
carry its numbers; change them there first. The headings that echo common searches ("What was there before the
Big Bang?") are bridges to the paper, and each answer says what the work does not show.

Links are root-absolute because the site serves a folder with and without a trailing slash, and a relative
link breaks without one. The post's folder name is SLUG; change it there and nowhere else.
"""
import html
import json
import re
from urllib.parse import quote

SITE = "https://sidenerdapps.com"
BLOG = "/mainnerd/"                             # the blog: one folder per post
SLUG = "01thecurledtorusburps"                     # post 01; the plain-language edition adds "PL"
BASE = BLOG + SLUG + "PL/"                         # the plain-language edition
TECH = BLOG + SLUG + "/"                           # the technical edition
SHARED = BLOG + "assets/"                          # the stylesheet, shared by every post
ASSETS = SHARED + SLUG + "/"                       # this paper's figures, PDFs, mascot and share image
STYLESHEET = "main-nerd.css"
SOON = BLOG + "comingsoon/"                        # where "next post" goes while the next post is not up yet
KNOBS = BLOG + SLUG + "Knobs/"                     # the interactive companion, "The Tube's Curling Ladder"
REPO = "https://github.com/EmilySmithCreate/RecreationalPhysics"
PAPER_DIR = REPO + "/tree/main/docs/papers/curled_torus"
PDF_PLAIN_NAME = "the-curled-torus-burps-plain-language.pdf"      # copied beside the pages by the build
PDF_TECH_NAME = "the-curled-torus-burps-technical.pdf"
PDF_PLAIN, PDF_TECH = ASSETS + PDF_PLAIN_NAME, ASSETS + PDF_TECH_NAME
# The companion was first published as a Claude artifact, and the papers' PDFs link to it there. The blog hosts
# its own copy, built from the same source file, and the web pages link to that.
ARTIFACT = "https://claude.ai/artifact/F4sBf955J5ZT7rCq8uebW8"
LADDER = KNOBS
LOGO = "https://sidenerd-marketing-assets.s3.us-east-1.amazonaws.com/sidenerdapps/logo-original.png"
AUTHOR_EMAIL = "emilysmithcreate@gmail.com"                      # the address printed on the technical paper
PUBLISHED = "2026-10-10"
TITLE = "The curled torus burps"
SUBTITLE = "A small push, a large release, and the question of what survives"


def utm(slot, path="/"):
    """A link back to Side Nerd, tagged the way the site's other links are (lowercase, hyphenated)."""
    return ("%s%s?utm_source=mainnerd&utm_medium=owned-media&utm_campaign=physics-01-curled-torus-burps"
            "&utm_content=%s" % (SITE, path, slot))


def mailto(subject):
    return "mailto:%s?subject=%s" % (AUTHOR_EMAIL, quote(subject))


# ------------------------------------------------------------------ the advertisements
# Ither, Side Nerd's volunteer-hours product, in the two advertisements that show a phone. The site has one
# Ither picture: three tilted phones side by side, 1000 x 500 (on /capture-work and textither.com). The style
# sheet cuts one phone out of it and stands it upright (.ad-phone), so nothing is copied into this repository.
HERO = "https://sidenerd-marketing-assets.s3.us-east-1.amazonaws.com/sidenerdapps/ither-3phones-hero.png"
PHONE_ALT = {
    "talk": "A phone showing a text conversation with Ither: a volunteer texts the hours they gave, and the replies "
            "log each entry and send a link to a report.",
    "report": "A phone showing the Ither Volunteer Activity Report: 61 volunteer hours, 20 entries, 9 organizations, "
              "and a bar chart of hours by month.",
}


def phone(which):
    return ('<span class="ad-phone %s"><img src="%s" alt="%s" width="1000" height="500" loading="lazy"></span>'
            % (which, HERO, html.escape(PHONE_ALT[which])))


PHONE_TALK = phone("talk")                                              # the sidebar panel: the conversation
PHONE_PAIR = ('<span class="ad-pair">%s<span class="ad-arrow" aria-hidden="true">»</span>%s</span>'
              % (phone("talk"), phone("report")))                       # mid-article: text in, report out


def ad(slot, kind, headline, body, button, picture=None):
    """An advertisement for Side Nerd, with its logo or, where `picture` is given, phone screenshots of a product
    in the logo's place. The humor is the 1990s banner; the product is real."""
    if picture is None:
        picture = '<img class="ad-logo" src="%s" alt="Side Nerd" width="72" height="72" loading="lazy">' % LOGO
    return ('<aside class="ad ad-%s" aria-label="Advertisement">'
            '<span class="ad-label">ADVERTISEMENT</span>'
            '<a href="%s" rel="noopener">%s<span class="ad-copy"><span class="ad-head">%s</span>'
            '<span class="ad-body">%s</span><span class="ad-btn">%s</span></span></a></aside>'
            % (kind, html.escape(utm(slot)), picture, headline, body, button))


AD_TOP = ad("top-banner", "banner", "TIRED OF LEARNING NEW SOFTWARE?",
            "So is everyone you work with. Side Nerd turns a plain text message into a finished record. "
            "If they can text, they can use it.", "CLICK HERE!!")
AD_MID = ad("mid-article", "box", "4,000 TUBES. ZERO FORMS FILLED OUT.",
            "The simulations on this page ran without a single login, portal or training session. Your team "
            "deserves the same. Side Nerd: messy input in, structured data out.", "Stop asking people to learn "
            "your software »", picture=PHONE_PAIR)
AD_SIDE = ad("sidebar", "tower", "SOFTWARE PEOPLE ACTUALLY USE",
             "No app. No portal. No login. If they can text, they can use it. Day one, no training.", "SEE HOW",
             picture=PHONE_TALK)
AD_FOOT = ad("footer-banner", "banner", "THIS PHYSICS IS BROUGHT TO YOU BY CONVERSATIONAL FORMS",
             "Side Nerd pays the computing bills. It makes software for people who will not use software: "
             "they text, the record writes itself.", "Book a demo »")
AD_TECH = ad("technical-footer", "banner", "YOU READ A TECHNICAL PAPER.",
             "Your users will not read a manual. Side Nerd: they text what happened, and the "
             "structured record appears where it belongs.", "See how »")
# the work has had no scientific reader yet
AD_READER = ('<aside class="ad ad-wanted" aria-label="Advertisement">'
             '<span class="ad-label">ADVERTISEMENT</span>'
             '<a href="%s"><span class="ad-copy">'
             '<span class="ad-head">REAL PHYSICIST, MATHEMATICIAN OR RELEVANT SCIENTIST?</span>'
             '<span class="ad-body">Volunteer to be a reader! No physicist has reviewed this work yet, and you '
             'could be the first. Compensation: sincere thanks, and first rights to say what is wrong with it.'
             '</span><span class="ad-btn">E-MAIL THE AUTHOR »</span></span></a></aside>'
             % html.escape(mailto("Volunteer reader: The curled torus burps")))

TICKER = ("★ NEW POST! The curled torus burps ★ Twelve units opens a tube ★ What opens a space? ★ No physicist "
          "has reviewed this page (volunteers wanted) ★ Sign the guestbook ★")


# ------------------------------------------------------------------ what the answer engines read
SUMMARY = (
    "<p><b>In one paragraph.</b> <i>The curled torus burps</i> is a computational physics paper about a "
    "hypothetical sharp change in which flat space emerges from something more curled up. It uses a toy model of "
    "space as a network of dots and links. The toy is the paper's own: a close cousin of the published model "
    "called combinatorial quantum gravity, with one knob turned above the published value, and not that model "
    "itself. In the paper's toy, a tube (a torus curled to four steps around) sits above the flat sheet in energy "
    "and is stable for now. The paper counts what it costs to start the change (12 units at the main setting, for "
    "every size of tube tested), predicts how long the tube waits by counting its exits, watches the flat arrangement "
    "spread, seals the system to see where the released energy (the burp) goes, and counts what is left behind "
    "(about one four-dot scrap). A toy can show that a mechanism is possible or impossible within a class of "
    "models; that is the whole claim.</p>")

# One searched question per chapter, as a heading, with a bridge to what the chapter does. Each bridge is true
# of the plain-language edition's chapter and claims no more than it does.
CHAPTER_QUESTIONS = {
    1: ("What was there before the Big Bang?",
        "Nobody knows. This chapter sets up one way to study the question without a time machine: treat space "
        "as one arrangement of something deeper, and ask what kind of change could have produced it."),
    2: ("Is space made of something smaller?",
        "Some physicists think so. This chapter describes one published model, combinatorial quantum gravity, "
        "in which space is a network of dots and links and nothing else, and then the toy this paper works in: "
        "a close cousin of that model with one knob turned up, not that model itself."),
    3: ("What existed before space?",
        "The author's hypothesis is that it was not nothing and not chaos, but a specific curled-up arrangement. "
        "This chapter builds a stand-in for that arrangement inside the toy model."),
    4: ("What could have set off the Big Bang?",
        "Unknown. In the toy model a change of this kind needs a push, and the push can be counted exactly: "
        "twelve units at the paper's main setting of the knob (λ = 1.25), the same for every size of tube "
        "tested."),
    5: ("What is a metastable state, or false vacuum?",
        "A state that is stable for now: it lasts until chance hands it enough energy to leave. This chapter "
        "predicts how long the toy's version waits, and checks the prediction."),
    6: ("Can space change phase, the way water freezes?",
        "In the toy model it can: a patch of the new arrangement appears and grows while the old one is still "
        "there beside it. This chapter watches that happen and says what the pictures do and do not prove."),
    7: ("Where did the energy of the Big Bang come from?",
        "In the author's hypothesis the change itself released it, the way freezing water gives off heat. In "
        "the toy model that release, the burp, can be counted exactly and followed when nothing is allowed to "
        "leave."),
    8: ("Is anything left over from before the Big Bang?",
        "In the toy model something is: about one small scrap of the old arrangement survives each change. "
        "Whether anything like it exists in reality is not something a toy can say."),
    9: ("How do you test an idea about the universe with a simulation?",
        "By turning one knob at a time with the rules written down first, and publishing every setting, "
        "including the ones that failed. This chapter is that map."),
    10: ("Can a computer simulate the beginning of the universe?",
         "Not the real one. This chapter lists exactly how far these simulations go, where each stops, and what "
         "lies past each edge."),
    11: ("Is this a theory of where the universe came from?",
         "It is a hypothesis, with one mechanism tested in a toy model and no physicist's review yet. This "
         "chapter says what was learned and what would have to come next."),
}

BIG_QUESTIONS = [
    ("What was there before the Big Bang?",
     "Nobody knows, and this work does not settle it. It tests one hypothesis, the author's: that space is one "
     "settled arrangement of something deeper, and that before the change there was a different, specific "
     "arrangement, curled up and stable for now. A toy model shows that such a change can happen in a network of "
     "dots and links, with a countable push and a countable release. That is a possibility shown in a toy, not "
     "evidence about the real universe."),
    ("Where did the Big Bang come from?",
     "One hypothesis, tested here only in a toy model: the hot early universe is the energy released when an "
     "earlier arrangement gave way and space opened out, the way water gives off heat when it freezes. In the toy "
     "the release can be counted exactly and grows with the size of the system, while the push that starts it "
     "stays small and fixed at every size tested."),
    ("What was there before time?",
     "This paper cannot say. The toy model has no time in it: its clock counts attempted moves, not seconds. In "
     "the author's wider hypothesis, which this paper does not test, what came before space had order but not "
     "time as we experience it."),
    ("Is space made of something?",
     "Possibly. In the published model this work builds on, space is a network of dots and links with no "
     "positions at all, and flat space is one arrangement of that network. Whether real space is like that is an "
     "open research question."),
    ("Is this an accepted theory?",
     "No. It is a hobbyist's hypothesis, tested on a toy model with the predictions written down first, written "
     "with AI assistance and not yet reviewed by a physicist. The paper says exactly what was and was not shown."),
]

FAQ = [
    ("What is “The curled torus burps” about?",
     "It is a plain-language edition of a computational physics paper by Emily Smith. It asks what a sharp change "
     "from one specific arrangement into flat space would look like, and tests each part of that picture in a toy "
     "model made of dots and links: what it costs to start, how long the wait is, what takes shape, where the "
     "released energy goes, and what remains."),
    ("What is combinatorial quantum gravity, and is this it?",
     "Combinatorial quantum gravity is a published model, built by Carlo Trugenberger, Christy Kelly and Fabio "
     "Biancalana, in which space is a network with no positions at all and the energy is a count of squares that "
     "acts as a curvature. This paper's toy is a close cousin of that model, not that model itself: it turns one knob, "
     "the price of a surplus square (λ), above the published value of 1."),
    ("What is a curled torus?",
     "A torus is a grid that wraps around in both directions, and every shape in the paper is one: flat (the "
     "sheet), curled (the tube) or knot. Curl one direction of the flat one until it is only four steps "
     "around and you have a tube. In the toy the tube has one large direction where the flat sheet has two, and "
     "it sits 4(λ − 1) units of energy per dot above the flat sheet: one unit per dot at λ = 1.25."),
    ("What is the burp?",
     "The burp is the energy given off when the tube opens into the flat sheet. For a clean change it is exactly "
     "4(λ − 1) per dot, so it grows with the size of the tube, while the push needed to start it does not."),
    ("How much energy does it take to start the change?",
     "Twelve units at λ = 1.25: the cost of the cheapest partner swap out of a perfect tube, counted exactly, the "
     "same at every size from 48 to 288 dots. In 320 sealed runs, no tube left with a budget below 12 and every "
     "tube left with 12 or more."),
    ("How long does the tube wait before it starts?",
     "Count the exits a sweep offers, multiply by the chance each is taken, and you predict the mean wait with "
     "nothing fitted. Across twelve conditions the measured mean wait divided by the predicted one averaged 0.98. "
     "The waiting is memoryless, like rolling a die until a six comes up."),
    ("What is left behind after the change?",
     "About one four-dot scrap of the old arrangement per sheet, holding 14 units, whatever the size of the tube, "
     "in the sealed runs with the most room. What the scrap does afterwards is the subject of the next paper."),
    ("Does this show how the universe began?",
     "No. A toy can show that a mechanism is possible or impossible within a class of models; that is the whole "
     "claim. The clock in the simulation is a sampling rule, not physical time, and no physicist has reviewed the "
     "work."),
    ("Was AI used to write this?",
     "Yes. The author used Claude (Anthropic) and ChatGPT/Codex (OpenAI) to assist with code, analysis and "
     "writing, and is responsible for the result. The predictions for the main tests were written down before the "
     "runs."),
]

KEY_TERMS = ["what came before the Big Bang", "emergent spacetime", "combinatorial quantum gravity",
             "graph model of space", "curled torus", "metastable state", "false vacuum decay", "activation energy",
             "first exit time", "memoryless waiting time", "nucleation and front", "sealed system (microcanonical)",
             "Creutz reservoir", "relic defect", "pre-registration", "Markov chain Monte Carlo",
             "decompactification"]


def cite_block(url, title, note):
    bib = ("@misc{smith2026curledtorus,\n  author = {Smith, Emily},\n  title  = {%s},\n  year   = {2026},\n"
           "  month  = oct,\n  note   = {%s},\n  url    = {%s}\n}" % (title, note, url))
    return ('<section class="cite-box" id="how-to-cite"><h2>How to cite this page</h2>'
            '<p>Emily Smith, <i>%s</i> (%s), 10 October 2026. <a href="%s">%s</a></p>'
            '<pre>%s</pre></section>' % (html.escape(title), html.escape(note), url, url, html.escape(bib)))


def json_ld(kind, url, headline, description, extra=None, faq=None, terms=None):
    article = {
        "@type": "ScholarlyArticle", "@id": url + "#article", "headline": headline, "description": description,
        "url": url, "mainEntityOfPage": url, "inLanguage": "en", "datePublished": PUBLISHED,
        "dateModified": PUBLISHED,
        "author": {"@type": "Person", "name": "Emily Smith", "affiliation": "Independent researcher",
                   "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": "Side Nerd Apps", "url": SITE + "/"},
        "isPartOf": {"@type": "Blog", "name": "The Side Nerd Blog", "url": SITE + BLOG},
        "keywords": ", ".join(KEY_TERMS), "image": SITE + ASSETS + "og-image.png",
        "isAccessibleForFree": True, "sameAs": [PAPER_DIR],
        "about": [{"@type": "Thing", "name": t} for t in KEY_TERMS[:9]],
    }
    article.update(extra or {})
    graph = [article, {
        "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Side Nerd Apps", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "The Side Nerd Blog", "item": SITE + BLOG},
            {"@type": "ListItem", "position": 3,
             "name": TITLE + (" (technical edition)" if kind == "technical" else " (plain-language edition)"),
             "item": url}]}]
    if faq:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    if terms:
        graph.append({"@type": "DefinedTermSet", "@id": url + "#translations",
                      "name": "Terms used in The curled torus burps",
                      "hasDefinedTerm": [{"@type": "DefinedTerm", "name": n, "description": d,
                                          "inDefinedTermSet": url + "#translations"} for n, d in terms]})
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1))


def head(title, description, url, ld, mathjax, pdf, paper=True):
    """`paper=False` is for pages that are not a paper (the front page, the placeholder): no citation tags."""
    parts = [
        '<!DOCTYPE html>', '<html lang="en">', '<head>', '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<title>%s | Side Nerd Apps</title>' % html.escape(title),
        '<meta name="description" content="%s">' % html.escape(description),
        '<meta name="author" content="Emily Smith">',
        '<meta name="robots" content="index, follow, max-image-preview:large">',
        '<link rel="canonical" href="%s">' % url,
        '<meta property="og:type" content="article">', '<meta property="og:url" content="%s">' % url,
        '<meta property="og:title" content="%s">' % html.escape(title),
        '<meta property="og:description" content="%s">' % html.escape(description),
        '<meta property="og:image" content="%s">' % (SITE + ASSETS + "og-image.png"),
        '<meta property="og:site_name" content="Side Nerd Apps">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % html.escape(title),
        '<meta name="twitter:description" content="%s">' % html.escape(description),
        '<meta name="twitter:image" content="%s">' % (SITE + ASSETS + "og-image.png"),
        '<meta name="theme-color" content="#34b1e8">',
        '<meta name="citation_title" content="%s">' % html.escape(title),
        '<meta name="citation_author" content="Smith, Emily">',
        '<meta name="citation_publication_date" content="2026/10/10">',
        '<meta name="citation_pdf_url" content="%s">' % (SITE + pdf),
        '<link rel="icon" type="image/png" href="https://sidenerd-marketing-assets.s3.us-east-1.amazonaws.com/'
        'sidenerdapps/sidenerd-icon.png">',
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Space+Mono:wght@400;700'
        '&display=swap" rel="stylesheet">',
        '<link rel="stylesheet" href="%s%s">' % (SHARED, STYLESHEET),
        ld,
    ]
    if not paper:
        parts = [p for p in parts if 'name="citation_' not in p]
    if mathjax:
        parts.append("<script>window.MathJax={tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']],"
                     "tags:'none'},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};"
                     "</script>")
        parts.append('<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js"></script>')
    parts.append('</head>')
    return "\n".join(parts)


def masthead(edition, other_label, other_href, other_target, answers="#quick-answers", guestbook="#guestbook"):
    return '''
<div class="ticker" aria-hidden="true"><div class="ticker-run">%(ticker)s %(ticker)s</div></div>
<header class="masthead">
 <div class="mast-text">
  <p class="welcome">~ Welcome to <a href="%(blog)s">the Side Nerd Blog</a>, Main Nerd ~</p>
  <h1>%(title)s</h1>
  <p class="subtitle">%(subtitle)s</p>
  <p class="byline">Post No. 01 · 10 October 2026 · by <b>Emily Smith</b>, independent researcher · filed under Physics · %(edition)s</p>
  <p class="jump"><a class="bevel" href="%(other_href)s" target="%(other_target)s">%(other_label)s</a>
   <a class="bevel" href="%(answers)s">Quick answers</a> <a class="bevel" href="%(guestbook)s">Sign the guestbook</a>
   <a class="bevel" href="#how-to-cite">Cite</a></p>
  <p class="sponsor">Sponsored by <a href="%(sponsor)s">Side Nerd Apps</a></p>
 </div>
 <figure class="mascot">
  <img src="%(assets)ssleepy-cow.gif" width="208" height="254" alt="A line drawing of a shaggy cow curled up asleep; in the next frame it stretches both front legs and lets out a small burp.">
  <figcaption>Fig. 0. A curled arrangement, stable for now, gives way and burps. Round cow not available, artist's impression. Not a torus.</figcaption>
 </figure>
</header>''' % dict(ticker=html.escape(TICKER), title=TITLE, subtitle=SUBTITLE, edition=edition,
                    other_href=other_href, other_label=other_label, other_target=other_target, assets=ASSETS,
                    answers=answers, guestbook=guestbook, sponsor=html.escape(utm("masthead-sponsor")),
                    blog=BLOG)


def badges():
    return '''
<div class="badges" aria-hidden="true">
 <span class="badge">Best viewed with<br><b>Netscape Navigator 3.0</b></span>
 <span class="badge">800 × 600<br><b>256 colors</b></span>
 <span class="badge">Made with<br><b>Notepad</b></span>
 <span class="badge">Y2K<br><b>compliant</b></span>
</div>'''


GUESTBOOK_SCRIPT = r'''<script>
document.getElementById('gb-form').addEventListener('submit', function (e) {
  e.preventDefault();
  var f = e.target;
  function v(n) { return (f.elements[n].value || '').trim(); }
  var body = 'Name: ' + v('name') + '\nE-mail: ' + v('email') + '\nSurfing in from: ' + v('from') +
    '\nTell me when the next paper is posted: ' + (f.elements.updates.checked ? 'yes' : 'no') + '\n\n' + v('entry');
  window.location.href = 'mailto:ADDRESS?subject=' + encodeURIComponent('Guestbook: The curled torus burps') +
    '&body=' + encodeURIComponent(body);
});
</script>'''


def guestbook():
    return ('''
<section class="guestbook" id="guestbook"><h2>Sign the guestbook</h2>
<p>Leave a note, a question or a correction. The guestbook runs on e-mail, as in 1996: the button opens your mail
program with your entry filled in, and you press send.</p>
<form class="gb" id="gb-form" action="%(mailto)s" method="get">
 <label>Name <input name="name" autocomplete="name"></label>
 <label>E-mail <input name="email" type="email" autocomplete="email"></label>
 <label>Surfing in from <input name="from" placeholder="city, planet or lab"></label>
 <label class="wide">Your entry <textarea name="entry" rows="4"></textarea></label>
 <label class="check"><input type="checkbox" name="updates" value="yes"> E-mail me when the next paper is posted</label>
 <button class="bevel" type="submit">Sign it!</button>
</form>
<p class="small-ink">Your address is used only to reply to you and, if you tick the box, to tell you about the next
paper. Or skip the form and write to <a href="%(mailto)s">%(address)s</a>.</p>
''' % dict(mailto=html.escape(mailto("Guestbook: The curled torus burps")), address=AUTHOR_EMAIL)
            + GUESTBOOK_SCRIPT.replace("ADDRESS", AUTHOR_EMAIL) + "\n</section>")


# Navigation between posts, in the footer. A post links on to the next one; while that is not up, to the
# placeholder. When a second post is published, put its address here in place of SOON.
NEXT_POST = SOON


def post_nav(kind):
    links = ['<a href="%s">all posts</a>' % BLOG]
    if kind in ("plain", "technical"):
        links.append('<a href="%s">next post »</a>' % NEXT_POST)
    elif kind == "soon":
        links.insert(0, '<a href="%s">« previous post</a>' % BASE)
    else:                                              # the front page is the list of posts
        return ""
    return '<div class="postnav">%s</div>' % " | ".join(links)


def footer(kind):
    return '''
<footer class="foot">
 %(nav)s
 <p class="sponsor-foot"><a href="%(sponsor)s"><img src="%(logo)s" alt="" width="44" height="44" loading="lazy">
  Sponsored by Side Nerd Apps</a></p>
 <p><a class="bevel" href="%(base)s#guestbook">Sign the guestbook</a>
  <a href="%(repo)s/issues">report a mistake</a> ·
  <a href="%(paper)s">source, data and supplement</a> ·
  <a href="%(side)s">Side Nerd</a>, which hosts this blog and has no opinion on quantum gravity</p>
 %(badges)s
 <p class="small">Text and figures © 2026 Emily Smith. No physicist has reviewed this work. A toy model shows what is
  possible within a class of models, nothing about the real universe. The advertisements are real.</p>
</footer>''' % dict(base=BASE, tech=TECH, repo=REPO, paper=PAPER_DIR, side=html.escape(utm("footer-text-" + kind)),
                    sponsor=html.escape(utm("footer-sponsor-" + kind)), logo=LOGO, badges=badges(),
                    nav=post_nav(kind))


# ------------------------------------------------------------------ the plain-language page
def page_plain(plain, technical, chapter_to_section):
    url = SITE + BASE
    description = ("What came before space? A plain-language physics paper tests one hypothesis in a toy model: a "
                   "curled-up arrangement opens into flat space for a push of 12 units, releases a burp of energy "
                   "and leaves a scrap behind.")
    terms = _terms(plain["back"])
    ld = json_ld("plain", url, TITLE + ": " + SUBTITLE, description,
                 extra={"alternativeHeadline": "Plain-language edition",
                        "isBasedOn": SITE + TECH, "hasPart": [
                            {"@type": "WebPageElement", "name": c["title_text"], "url": url + "#ch%d" % c["num"]}
                            for c in _with_text(plain["chapters"])]},
                 faq=BIG_QUESTIONS + FAQ, terms=terms)
    nav = ['<nav class="side" aria-label="Chapters"><p class="side-head">THIS POST</p><ol>']
    for c in plain["chapters"]:
        nav.append('<li><a href="#ch%d">%s</a></li>' % (c["num"], _title_case(c["kicker"])))
    nav.append('</ol><p class="side-head">ELSEWHERE</p><ul>'
               '<li><a href="%s" target="mn-technical">Technical edition</a></li>'
               '<li><a href="%s">Turn the knobs (interactive)</a></li>'
               '<li><a href="%s">This edition as a PDF</a></li>'
               '<li><a href="#big-questions">The big questions</a></li>'
               '<li><a href="#translations">Glossary</a></li>'
               '<li><a href="#sources-head">Sources</a></li>'
               '<li><a href="#guestbook">Guestbook</a></li></ul>' % (TECH, LADDER, PDF_PLAIN))
    nav.append(AD_SIDE)
    nav.append('</nav>')

    body = [head(TITLE + ": what came before space? A hypothesis tested in a toy model, in plain language",
                 description, url, ld, plain["mathjax"], PDF_PLAIN),
            '<body class="plain">', '<a class="skip" href="#ch1">Skip to the paper</a>',
            masthead("plain-language edition", "Read the technical edition »", TECH, "mn-technical"),
            AD_TOP, '<div class="frame">', "\n".join(nav), '<main class="paper">',
            '<section class="opening">', SUMMARY, plain["opening"], '</section>']
    for c in plain["chapters"]:
        sec = chapter_to_section[c["num"]]
        question, bridge = CHAPTER_QUESTIONS[c["num"]]
        body.append('<section class="chapter" id="ch%d">' % c["num"])
        body.append('<p class="kicker">CHAPTER %d · %s</p><h2>%s</h2>' % (c["num"], c["kicker"], c["title"]))
        body.append('<div class="ask"><h3 id="ch%d-question">%s</h3><p>%s</p></div>'
                    % (c["num"], html.escape(question), html.escape(bridge)))
        body.append('<p class="xlink">Side by side: <a href="%s#%s" target="mn-technical">the same ground in the '
                    'technical edition, %s »</a></p>' % (TECH, sec, _section_label(technical, sec)))
        body.append(c["html"])
        body.append('</section>')
        if c["num"] == 4:
            body.append(AD_MID)
    body.append(AD_READER)
    body.append('<section class="back">%s</section>' % plain["back"])
    if plain["notes"]:
        body.append('<section class="notes" id="notes"><h2>Notes</h2><ol>%s</ol></section>' % plain["notes"])
    body.append('<section class="faq" id="big-questions"><h2>The big questions, and what this work can honestly '
                'say</h2>')
    for q, a in BIG_QUESTIONS:
        body.append('<h3>%s</h3><p>%s</p>' % (html.escape(q), html.escape(a)))
    body.append('</section>')
    body.append('<section class="faq" id="quick-answers"><h2>Quick answers</h2>')
    for q, a in FAQ:
        body.append('<h3>%s</h3><p>%s</p>' % (html.escape(q), html.escape(a)))
    body.append('</section>')
    body.append('<section class="terms" id="key-terms"><h2>What this page is about</h2><p>%s.</p></section>'
                % ", ".join(KEY_TERMS))
    body.append(guestbook())
    body.append(cite_block(url, TITLE + ": " + SUBTITLE, "plain-language edition"))
    body.append('</main></div>')
    body.append(AD_FOOT)
    body.append(footer("plain"))
    body.append('</body></html>')
    return ("\n".join(body) + "\n").replace(ARTIFACT, KNOBS)      # the blog's own copy of the companion


def _with_text(chapters):
    return [dict(c, title_text=re.sub(r"<[^>]+>", "", c["title"])) for c in chapters]


def _title_case(kicker):
    text = re.sub(r"<[^>]+>", "", kicker).lower()
    return text[:1].upper() + text[1:]


def _section_label(technical, sec):
    s = next(x for x in technical["sections"] if x["id"] == sec)
    name = re.sub(r"<[^>]+>", "", s["title"])
    return ("Sec. %s, %s" % (s["roman"], name)) if s["roman"] else name


def _terms(back_html):
    """(term, definition) pairs from the translations table of the plain edition, as plain text."""
    m = re.search(r'<table id="translations".*?</table>', back_html, flags=re.S)
    out = []
    if m:
        for row in re.findall(r"<tr><td>(.*?)</td><td>(.*?)</td></tr>", m.group(0), flags=re.S):
            clean = [html.unescape(re.sub(r"<[^>]+>", "", x)).replace("\\(", "").replace("\\)", "").strip()
                     for x in row]
            out.append((clean[0], clean[1]))
    return out


# ------------------------------------------------------------------ the technical page
def page_technical(technical, plain, section_to_chapters):
    url = SITE + TECH
    meta = technical["meta"]
    description = ("Technical edition: activated escape and conversion of a curled torus in four-regular bipartite "
                   "graph energies next to combinatorial quantum gravity. Exact barrier of 12 units, first-exit "
                   "times from counted moves, sealed-reservoir runs and relics.")
    abstract_text = html.unescape(re.sub(r"<[^>]+>", "", technical["abstract"]))
    ld = json_ld("technical", url, re.sub(r"<[^>]+>", "", meta["title"]), description,
                 extra={"abstract": abstract_text, "alternativeHeadline": "Technical edition",
                        "hasPart": [{"@type": "WebPageElement", "name": re.sub(r"<[^>]+>", "", s["title"]),
                                     "url": url + "#" + s["id"]} for s in technical["sections"]]})
    kickers = {c["num"]: _title_case(c["kicker"]) for c in plain["chapters"]}
    nav = ['<nav class="side" aria-label="Sections"><p class="side-head">THIS POST</p><ol class="roman">']
    for s in technical["sections"]:
        nav.append('<li><a href="#%s">%s%s</a></li>' % (s["id"], (s["roman"] + ". ") if s["roman"] else "",
                                                       re.sub(r"<[^>]+>", "", s["title"])))
    nav.append('</ol><p class="side-head">ELSEWHERE</p><ul>'
               '<li><a href="%s" target="mn-plain">Plain-language edition</a></li>'
               '<li><a href="%s">Turn the knobs (interactive)</a></li>'
               '<li><a href="%s">This paper as a PDF</a></li>'
               '<li><a href="%s">Supplement, data and code</a></li>'
               '<li><a href="#references-head">References</a></li>'
               '<li><a href="%s#guestbook" target="mn-plain">Guestbook</a></li></ul></nav>'
               % (BASE, LADDER, PDF_TECH, PAPER_DIR, BASE))

    body = [head(re.sub(r"<[^>]+>", "", meta["title"]) + " (technical edition)", description, url, ld,
                 technical["mathjax"], PDF_TECH), '<body class="technical">',
            '<a class="skip" href="#sec-intro">Skip to the paper</a>',
            masthead("technical edition", "« Read the plain-language edition", BASE, "mn-plain",
                     answers=BASE + "#quick-answers", guestbook=BASE + "#guestbook"),
            AD_READER,
            '<div class="frame">', "\n".join(nav), '<main class="paper">',
            '<section class="abstract" id="abstract"><h2 class="full-title">%s</h2>'
            '<p class="affil">%s · %s · %s</p><p><b>Abstract.</b> %s</p></section>'
            % (meta["title"], meta["author"], meta["affiliation"], meta["date"], technical["abstract"])]
    for s in technical["sections"]:
        body.append('<section class="chapter" id="%s">' % s["id"])
        body.append('<h2>%s%s</h2>' % ((s["roman"] + ". ") if s["roman"] else "", s["title"]))
        chapters = section_to_chapters.get(s["id"], [])
        if chapters:
            links = " and ".join('<a href="%s#ch%d" target="mn-plain">Chapter %d, %s</a>'
                                 % (BASE, n, n, html.escape(kickers[n])) for n in chapters)
            body.append('<p class="xlink">Side by side: in the plain-language edition this is %s »</p>' % links)
        body.append(s["html"])
        body.append('</section>')
    body.append(cite_block(url, re.sub(r"<[^>]+>", "", meta["title"]), "technical edition"))
    body.append('</main></div>')
    body.append(AD_TECH)
    body.append(footer("technical"))
    body.append('</body></html>')
    return ("\n".join(body) + "\n").replace(ARTIFACT, KNOBS)      # the blog's own copy of the companion


# ------------------------------------------------------------------ the blog's front page
def page_index():
    url = SITE + BLOG
    description = ("The Side Nerd Blog: physics papers by Emily Smith, each in a plain-language edition and a "
                   "technical edition, hosted by Side Nerd Apps.")
    ld = ('<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "Blog", "@id": url + "#blog", "name": "The Side Nerd Blog",
        "url": url, "description": description, "inLanguage": "en",
        "publisher": {"@type": "Organization", "name": "Side Nerd Apps", "url": SITE + "/"},
        "author": {"@type": "Person", "name": "Emily Smith"},
        "blogPost": [{"@type": "BlogPosting", "headline": TITLE + ": " + SUBTITLE, "url": SITE + BASE,
                      "datePublished": PUBLISHED, "author": {"@type": "Person", "name": "Emily Smith"}},
                     {"@type": "BlogPosting", "headline": TITLE + " (technical edition)", "url": SITE + TECH,
                      "datePublished": PUBLISHED, "author": {"@type": "Person", "name": "Emily Smith"}}],
    }, ensure_ascii=False, indent=1))
    body = [head("The Side Nerd Blog", description, url, ld, False, PDF_PLAIN, paper=False), '<body class="index">',
            '''
<div class="ticker" aria-hidden="true"><div class="ticker-run">%(ticker)s %(ticker)s</div></div>
<header class="masthead">
 <div class="mast-text">
  <p class="welcome">~ Welcome, Main Nerd ~</p>
  <h1>The Side Nerd Blog</h1>
  <p class="subtitle">Recreational physics, in plain language and in full</p>
  <p class="sponsor">Sponsored by <a href="%(sponsor)s">Side Nerd Apps</a></p>
 </div>
</header>''' % dict(ticker=html.escape(TICKER), sponsor=html.escape(utm("index-sponsor"))),
            AD_TOP, '<div class="frame index-frame"><main class="paper">',
            '<h2>Posts</h2>',
            '<article class="post-card"><p class="kicker">POST No. 01 · 10 OCTOBER 2026 · PHYSICS</p>'
            '<h3><a href="%s">%s</a></h3><p><i>%s.</i> By Emily Smith.</p>%s'
            '<p class="jump"><a class="bevel" href="%s">Read it in plain language »</a> '
            '<a class="bevel" href="%s">Read the technical edition »</a> '
            '<a class="bevel" href="%s">Plain PDF</a> <a class="bevel" href="%s">Technical PDF</a></p></article>'
            % (BASE, TITLE, SUBTITLE, SUMMARY.replace("<b>In one paragraph.</b> ", ""), BASE, TECH, PDF_PLAIN,
               PDF_TECH),
            AD_READER, '</main></div>', footer("index"), '</body></html>']
    return "\n".join(body) + "\n"


# ------------------------------------------------------------------ the placeholder for a post that is not up yet
def page_coming_soon():
    """Where "next post" lands while the next post does not exist. Kept out of search results; when a second post
    is published, put its address in NEXT_POST in place of SOON."""
    url = SITE + SOON
    description = "The next post on the Side Nerd Blog is not up yet."
    top = head("The next post is not up yet", description, url, "", False, PDF_PLAIN, paper=False)
    top = top.replace("index, follow, max-image-preview:large", "noindex, follow")
    body = [top, '<body class="index">',
            '''
<div class="ticker" aria-hidden="true"><div class="ticker-run">%(ticker)s %(ticker)s</div></div>
<header class="masthead">
 <div class="mast-text">
  <p class="welcome">~ <a href="%(blog)s">The Side Nerd Blog</a>, Main Nerd ~</p>
  <h1>Not up yet</h1>
  <p class="subtitle">The next post is still curled up</p>
  <p class="sponsor">Sponsored by <a href="%(sponsor)s">Side Nerd Apps</a></p>
 </div>
 <figure class="mascot">
  <img src="%(assets)ssleepy-cow.gif" width="208" height="254" alt="A line drawing of a shaggy cow curled up asleep; in the next frame it stretches both front legs and lets out a small burp.">
  <figcaption>Stable for now.</figcaption>
 </figure>
</header>''' % dict(ticker=html.escape(TICKER), assets=ASSETS, blog=BLOG,
                    sponsor=html.escape(utm("comingsoon-sponsor"))),
            '<div class="frame index-frame"><main class="paper">',
            '<h2>This post is not up yet</h2>'
            '<p>You have reached the end of what has been posted. The next post is being written; '
            'there is nothing to read here yet.</p>'
            '<p class="jump"><a class="bevel" href="%s">Post No. 01 in plain language »</a> '
            '<a class="bevel" href="%s">Post No. 01, technical edition »</a> '
            '<a class="bevel" href="%s#guestbook">Sign the guestbook to hear when it is up</a></p>'
            % (BASE, TECH, BASE),
            '</main></div>', footer("soon"), '</body></html>']
    return "\n".join(body) + "\n"


# ------------------------------------------------------------------ the interactive companion
# The blog's bar above and below the companion. The companion keeps its own style sheet, which styles bare elements
# (body, header, h1, p, table), so the bar is made only of div, span, a and img under one prefix, and the two
# leave each other alone.
KNOBS_BAR_CSS = """
html{-webkit-text-size-adjust:100%}body{margin:0}img{max-width:100%}[hidden]{display:none!important}
.mnb{margin:0 -16px;padding:10px 16px;background:#192933;color:#e2e8f0;border:4px ridge #34b1e8;text-align:center;
  font-family:"DM Sans",Arial,Helvetica,sans-serif;font-size:14px;line-height:1.6}
.mnb a{color:#5bc4f0}
.mnb-name{display:block;font-family:"Comic Sans MS","Comic Sans",cursive;font-size:17px;color:#5bc4f0}
.mnb-what{display:block;margin:2px 0 6px;color:#cbd5e1}
.mnb .mnb-btn{display:inline-block;margin:3px;padding:3px 12px;background:#c9d3da;color:#0d1419;font-weight:700;
  font-size:13.5px;text-decoration:none;border:3px outset #f1f5f9}
.mnb .mnb-btn:active{border-style:inset}
.mnb-sponsor{display:block;margin-top:6px;font-family:"Space Mono","Courier New",monospace;font-size:12.5px;
  letter-spacing:.06em;color:#cbd5e1}
.mnb-small{display:block;margin-top:8px;font-size:12.5px;color:#cbd5e1}
.mnb-foot{margin-top:28px}
@media print{.mnb{display:none}}
"""


def page_knobs(source):
    """The companion as a page of the blog. `source` is the text of docs/public/curling_ladder_tube.html: a title,
    font links, a style sheet, the markup and one script, written as an artifact's body. Its parts are moved to
    where a whole document wants them and nothing in them is changed."""
    title = re.search(r"<title>(.*?)</title>", source, flags=re.S)
    links = re.findall(r"<link\b[^>]*>", source)
    style = re.search(r"<style>.*?</style>", source, flags=re.S)
    assert title and style and source.count("<style>") == 1 and source.count("<script>") == 1
    body = source[style.end():].strip()
    assert "<link" not in body and "<title" not in body and body.rstrip().endswith("</script>")
    name = html.unescape(title.group(1))
    url = SITE + KNOBS
    description = ("Turn the toy model's knobs yourself: an interactive companion to \"The curled torus burps\". Exact "
                   "numbers at every setting; measured results only where the simulations ran.")
    top = head(name + ": turn the knobs", description, url, "", False, PDF_PLAIN, paper=False)
    top = top.replace('<link rel="stylesheet" href="%s%s">\n' % (SHARED, STYLESHEET), "")   # not the blog's style sheet
    top = top.replace("</head>", "\n".join(links) + "\n<style>" + KNOBS_BAR_CSS + "</style>\n" + style.group(0)
                      + "\n</head>")
    bar = ('<div class="mnb">'
           '<span class="mnb-name">~ <a href="%(blog)s">The Side Nerd Blog</a>, Main Nerd ~</span>'
           '<span class="mnb-what">The interactive companion to Post No. 01, <i>%(paper)s</i></span>'
           '<a class="mnb-btn" href="%(base)s">« Read it in plain language</a>'
           '<a class="mnb-btn" href="%(tech)s">Read the technical edition</a>'
           '<span class="mnb-sponsor">Sponsored by <a href="%(sponsor)s">Side Nerd Apps</a></span></div>'
           % dict(blog=BLOG, paper=TITLE, base=BASE, tech=TECH, sponsor=html.escape(utm("knobs-sponsor"))))
    foot = ('<div class="mnb mnb-foot">'
            '<a class="mnb-btn" href="%(base)s">« Back to the post</a>'
            '<a class="mnb-btn" href="%(blog)s">All posts</a>'
            '<a class="mnb-btn" href="%(base)s#guestbook">Sign the guestbook</a>'
            '<span class="mnb-sponsor">Sponsored by <a href="%(sponsor)s">Side Nerd Apps</a></span>'
            '<span class="mnb-small">Text and figures © 2026 Emily Smith. No physicist has reviewed this work. A toy '
            'model shows what is possible within a class of models, nothing about the real universe. '
            '<a href="%(repo)s/issues">Report a mistake</a>.</span></div>'
            % dict(blog=BLOG, base=BASE, repo=REPO, sponsor=html.escape(utm("knobs-footer-sponsor"))))
    cut = body.index("<script>")
    return "\n".join([top, "<body>", bar, body[:cut].rstrip(), foot, body[cut:], "</body></html>"]) + "\n"


# ------------------------------------------------------------------ the stylesheet
CSS = r'''
/* The Side Nerd Blog (sidenerdapps.com/mainnerd): a 1996 home page in Side Nerd's colors. One stylesheet. */
:root{
  --midnight:#0d1419; --navy:#192933; --slate:#2d3748; --aqua:#34b1e8; --aqua-light:#5bc4f0; --aqua-ink:#0b6795;
  --paper:#ffffff; --canvas:#f6f7f8; --ink:#16181d; --muted:#6b7280; --rule:#d8dadf; --text-on-dark:#e2e8f0;
  --exact:#176b70; --meas:#2f5f9e; --pub:#5a5a5a; --ours:#9a5b00; --claim:#8a2d5a;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;color:var(--text-on-dark);font-family:"Times New Roman",Times,serif;font-size:18px;line-height:1.55;
  background-color:var(--midnight);
  background-image:radial-gradient(1px 1px at 12px 18px,#5bc4f0 50%,transparent 51%),
    radial-gradient(1px 1px at 70px 96px,#e2e8f0 50%,transparent 51%),
    radial-gradient(1.5px 1.5px at 140px 40px,#94a3b8 50%,transparent 51%),
    radial-gradient(1px 1px at 190px 150px,#34b1e8 50%,transparent 51%),
    radial-gradient(1px 1px at 40px 170px,#e2e8f0 50%,transparent 51%);
  background-size:220px 200px}
a{color:var(--aqua-ink)}
.masthead a,.foot a,.side a{color:var(--aqua-light)}
a:visited{color:#5a4a9a}
.side a:visited,.foot a:visited{color:#b9a6ee}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;color:#000;padding:6px;z-index:9}

/* ticker: the marquee, done politely */
.ticker{overflow:hidden;white-space:nowrap;background:var(--navy);border-bottom:2px ridge var(--aqua);
  font-family:"Space Mono","Courier New",monospace;font-size:13px;color:var(--aqua-light);padding:4px 0}
.ticker-run{display:inline-block;padding-left:100%;animation:run 60s linear infinite}
.ticker:hover .ticker-run{animation-play-state:paused}
@keyframes run{to{transform:translateX(-100%)}}
@media (prefers-reduced-motion:reduce){.ticker-run{animation:none;padding-left:8px}}

.masthead{max-width:1180px;margin:18px auto 10px;padding:14px 18px;display:flex;gap:22px;align-items:center;
  border:4px ridge var(--aqua);background:var(--navy)}
.mast-text{flex:1;min-width:0;text-align:center}
.welcome{margin:0;font-family:"Comic Sans MS","Comic Sans",cursive;color:var(--aqua-light);font-size:17px}
.masthead h1{margin:6px 0 4px;font-size:clamp(34px,6vw,62px);line-height:1.05;color:#fff;letter-spacing:.5px;
  text-shadow:3px 3px 0 var(--aqua-ink),-1px -1px 0 var(--aqua)}
.subtitle{margin:0 0 8px;font-style:italic;font-size:21px;color:var(--text-on-dark)}
.byline{margin:0 0 10px;font-size:16px;color:#cbd5e1}
.jump{margin:0}
.bevel{display:inline-block;margin:3px;padding:3px 12px;background:#c9d3da;color:#0d1419 !important;
  border:2px outset #f1f5f9;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;text-decoration:none;cursor:pointer}
.bevel:active{border-style:inset}
.mascot{margin:0;flex:0 0 170px;text-align:center}
.mascot img{width:170px;height:auto;background:#fff;border:3px inset #c9d3da}
.mascot figcaption{font-size:12px;line-height:1.3;color:#cbd5e1;margin-top:4px}

.frame{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:230px minmax(0,1fr);gap:16px;padding:0 10px}
.index-frame{grid-template-columns:minmax(0,1fr);max-width:900px}
.post-card{border:3px ridge var(--aqua);background:var(--canvas);padding:14px 18px;margin:1em 0}
.post-card h3{margin:.2em 0;font-size:28px}
.side{align-self:start;position:sticky;top:8px;max-height:calc(100vh - 16px);overflow:auto;
  background:var(--navy);border:3px ridge var(--aqua);padding:10px 12px;font-family:Arial,Helvetica,sans-serif;font-size:14px}
.side-head{margin:8px 0 4px;font-family:"Space Mono","Courier New",monospace;font-size:12px;letter-spacing:.08em;color:var(--aqua)}
.side ol,.side ul{margin:0 0 8px;padding-left:22px}
.side ol.roman{list-style:none;padding-left:4px}
.side li{margin:3px 0;line-height:1.3}

.paper{background:var(--paper);color:var(--ink);border:4px ridge #c9d3da;padding:26px clamp(16px,4vw,46px) 34px;min-width:0}
.paper h2{font-family:Arial,Helvetica,sans-serif;font-size:30px;line-height:1.15;margin:.3em 0 .5em;color:#0d1419}
.paper h3{font-family:Arial,Helvetica,sans-serif;font-size:21px;margin:1.5em 0 .3em;color:#0d1419}
.paper p{margin:.7em 0}
.chapter{border-top:6px double var(--aqua);margin-top:2.6em;padding-top:1.1em}
.kicker{margin:0;font-family:"Space Mono","Courier New",monospace;font-size:13px;letter-spacing:.08em;color:var(--aqua-ink);font-weight:bold}
.ask{margin:.2em 0 .9em;padding:8px 14px;background:var(--canvas);border-left:6px solid var(--aqua-ink)}
.ask h3{margin:0;font-size:18px;font-style:italic;color:var(--aqua-ink)}
.ask h3::before{content:"People ask: ";font-style:normal;font-weight:normal;color:var(--muted);font-size:14px}
.ask p{margin:.25em 0 0;font-size:16.5px}
.xlink{font-family:Arial,Helvetica,sans-serif;font-size:14px;background:var(--canvas);border:1px dashed var(--aqua-ink);padding:5px 10px}
.takeaway{background:#e8f6fc;border-left:6px solid var(--aqua);padding:10px 14px;margin:1.3em 0}
.why{font-size:16px;color:#374151;border-left:3px dotted var(--aqua-ink);padding-left:12px}
.pull{text-align:center;font-family:Arial,Helvetica,sans-serif;font-weight:bold;font-size:25px;line-height:1.25;margin:1.2em 0;color:#0d1419}
.m{white-space:nowrap}
.m i,.paper i.v{font-family:"Times New Roman",Times,serif}
.tag{display:inline-block;font-family:Arial,Helvetica,sans-serif;font-size:10.5px;font-weight:bold;letter-spacing:.04em;
  color:#fff;padding:1px 5px;vertical-align:1px;white-space:nowrap}
.tag-exact{background:var(--exact)}.tag-meas{background:var(--meas)}.tag-pub{background:var(--pub)}
.tag-ours{background:var(--ours)}.tag-claim{background:var(--claim)}
.fig{margin:1.5em 0;text-align:center}
.fig img{max-width:100%;height:auto;background:#fff}
.fig figcaption{font-size:15.5px;line-height:1.4;text-align:left;color:#374151;margin-top:6px}
.tablewrap{overflow-x:auto;margin:1.2em 0}
table{border-collapse:collapse;margin:0 auto;min-width:min(100%,560px);font-family:Arial,Helvetica,sans-serif;font-size:14.5px;line-height:1.35}
caption{caption-side:top;text-align:left;font-family:"Times New Roman",Times,serif;font-size:15.5px;color:#374151;padding-bottom:6px}
th,td{border:1px solid var(--rule);padding:5px 9px;text-align:left;vertical-align:top}
th{background:#dbeef8}
tr:nth-child(even) td{background:var(--canvas)}
table.glossary td:first-child{font-weight:bold;white-space:nowrap}
.eq{display:block;overflow-x:auto;margin:.4em 0}
.runin{font-style:italic;font-weight:bold}
.cite{text-decoration:none}
sup.fn a{text-decoration:none}
.sources,.notes ol{font-size:16px}
.sources li{margin:.45em 0}
.abstract .full-title{font-size:27px}
.affil{font-family:Arial,Helvetica,sans-serif;font-size:14px;color:var(--muted)}
.faq h3{margin-top:1.1em}
.cite-box pre{background:var(--canvas);border:2px inset #c9d3da;padding:10px;overflow-x:auto;font-size:13px}
.terms p{font-size:16px;color:#374151}

/* the guestbook */
.guestbook{margin-top:2.4em;padding:14px 18px 18px;border:4px ridge var(--aqua);background:var(--canvas)}
.guestbook h2{margin-top:0}
.gb{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px 14px;align-items:end}
.gb label{display:block;font-family:Arial,Helvetica,sans-serif;font-size:13px;font-weight:bold}
.gb input:not([type=checkbox]),.gb textarea{display:block;width:100%;margin-top:3px;padding:5px 6px;border:2px inset #c9d3da;
  background:#fff;font-family:"Courier New",monospace;font-size:15px;color:var(--ink)}
.gb .wide,.gb .check{grid-column:1/-1}
.gb .check{font-weight:normal;font-size:14px}
.gb button{justify-self:start;font-size:15px;padding:5px 18px}
.small-ink{font-size:13.5px;color:var(--muted)}

/* the advertisements: few, labelled, and the only thing here set in the brand's own type */
.ad{font-family:"DM Sans",Arial,sans-serif;margin:16px auto;max-width:728px;text-align:center}
.ad-label{display:block;font-family:"Space Mono","Courier New",monospace;font-size:10.5px;letter-spacing:.12em;color:#94a3b8;margin-bottom:3px}
.paper .ad-label{color:var(--muted)}
.ad a{display:flex;align-items:center;gap:14px;text-decoration:none;color:#0d1419;background:var(--aqua);
  border:4px outset var(--aqua-light);padding:9px 14px;text-align:left}
.ad a:hover{border-style:inset}
.ad-logo{flex:0 0 auto;width:72px;height:72px;background:#fff;border:2px inset #c9d3da;padding:2px}
/* One phone cut out of the three-phone Ither picture (1000 x 500) and stood upright. Measured in that picture: each
   phone is 231 x 467 and leans 32 degrees to the left; the conversation's center is at (506, 249), the report's
   at (788, 249). The box is the phone's own outline; the picture is scaled, shifted and turned behind it. */
.ad-phone{flex:0 1 auto;display:block;position:relative;overflow:hidden;aspect-ratio:231/467;min-width:0;max-width:100%}
.ad-phone img{position:absolute;display:block;max-width:none;height:auto}
.ad-phone.talk img{width:432.3%;left:-168.7%;top:-3.2%;transform-origin:50.59% 49.72%;transform:rotate(31.62deg)}
.ad-phone.report img{width:432%;left:-290.4%;top:-3.1%;transform-origin:78.81% 49.72%;transform:rotate(32.2deg)}
.ad-tower .ad-phone{width:100%;max-width:176px}
.ad-pair{flex:0 1 auto;display:flex;align-items:center;justify-content:center;gap:6px;min-width:0;max-width:100%}
.ad-pair .ad-phone{width:118px}
.ad-arrow{flex:0 0 auto;font-weight:700;font-size:22px}
/* where the two phones and the words do not fit side by side, the words go underneath */
.ad-box a{flex-wrap:wrap;justify-content:center}
.ad-box .ad-copy{flex:1 1 200px}
.ad-copy{flex:1;min-width:0}
.ad-head{display:block;font-weight:700;font-size:20px;letter-spacing:.02em;line-height:1.2}
.ad-body{display:block;font-size:14.5px;line-height:1.35;margin:3px 0 6px}
.ad-btn{display:inline-block;background:#0d1419;color:#fff;font-weight:700;font-size:13px;padding:3px 12px;border:2px outset #94a3b8}
.ad-banner .ad-head{animation:blink 1.6s steps(2,start) 4}
@keyframes blink{50%{opacity:.25}}
@media (prefers-reduced-motion:reduce){.ad-banner .ad-head{animation:none}}
.ad-tower{margin:14px 0 4px}
.ad-tower a{flex-direction:column;text-align:center;padding:12px 8px;gap:8px}
.ad-tower .ad-head{font-size:17px}
.ad-box{max-width:560px;margin:2.2em auto}
.ad-wanted a{background:#fffbe6;border:4px dashed var(--aqua-ink);color:var(--ink);text-align:center}
.ad-wanted .ad-head{font-family:"Courier New",monospace;font-size:19px}
.ad-wanted .ad-btn{background:var(--aqua-ink)}
.paper .ad-wanted{margin:2.4em auto}

.foot{max-width:1180px;margin:20px auto 40px;padding:14px 18px;text-align:center;font-family:Arial,Helvetica,sans-serif;font-size:14px;
  border:4px ridge var(--aqua);background:var(--navy)}
.postnav{border:2px groove #94a3b8;padding:6px;margin-bottom:10px}
.sponsor{margin:8px 0 0;font-family:"Space Mono","Courier New",monospace;font-size:12.5px;letter-spacing:.06em;color:#cbd5e1}
.sponsor-foot{margin:4px 0 12px}
.sponsor-foot a{display:inline-flex;align-items:center;gap:10px;font-family:"DM Sans",Arial,sans-serif;font-weight:700;font-size:16px;
  color:#fff !important;text-decoration:none}
.sponsor-foot img{background:#fff;border:2px inset #c9d3da;padding:2px}
.small{font-size:12.5px;color:#cbd5e1}
.badges{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:12px 0}
.badge{font-size:10.5px;line-height:1.25;padding:4px 8px;border:2px outset #94a3b8;background:#c9d3da;color:#0d1419;min-width:88px}

@media (max-width:900px){
  body{font-size:17px}
  .frame{grid-template-columns:minmax(0,1fr)}
  .side{position:static;max-height:none}
  .side ol{columns:2}
  .masthead{flex-direction:column}
  .ad-tower{display:none}
  .gb{grid-template-columns:minmax(0,1fr)}
}
@media (max-width:520px){.ad a{flex-direction:column;text-align:center}}
@media print{
  body{background:#fff;color:#000}.ticker,.ad,.side,.foot,.mascot,.jump,.xlink,.guestbook{display:none}
  .frame{display:block}.paper{border:0;padding:0}
}
'''
