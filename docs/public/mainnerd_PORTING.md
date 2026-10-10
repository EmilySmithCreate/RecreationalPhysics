# The Side Nerd Blog (`/mainnerd/`): porting the pages to sidenerdapps.com

Built here on 10 October 2026 for the Side Nerd marketing site. Nothing in this repository deploys them.

**Status, 10 October.** At the owner's instruction the folder was copied, file for file, to
`sites/sidenerdapps/mainnerd/` on a new branch of the SideNerdMarketing repository,
`feat/sidenerdapps-main-nerd-blog` (commit `4522930`, branched from that repository's up-to-date `main`),
with the four addresses added to the sitemap, and pushed. The owner merged that first copy into the
marketing repository's `main` the same day (pull request 56). The folder was then rebuilt here after a
correction to both editions (one long wait, not two) and copied to the same branch again as commit `17acde2`,
pushed after the merge; she merged that too (pull request 57) and deployed, so **the blog is live** with the
corrected text. Each later rebuild is copied to the same branch as a new commit and needs its own pull request
and deploy: the next is the wording of 10 October that every shape in the paper is a torus (flat, curled,
knot). As of 10 October sidenerdapps.com carries no analytics tag of its own (one compliance page carries
another site's), so visits to the blog and clicks on its advertisements are not counted; a measurement ID for
the site is the owner's to create. After any rebuild here, copy the folder again.

**The name.** The blog is "Main Nerd" (the owner's choice, 10 October: funnier beside "Side Nerd"). It was
built first at `/ownedmediaphysics/` and then as "Primary Nerd" at `/primarynerd/`, both the same day; nothing
was ported under either name. The address is the one constant `BLOG` in `scripts/main_nerd_site.py`.

## What is in `docs/public/mainnerd/`

| Path | What it is | URL once ported |
|---|---|---|
| `index.html` | The blog's front page: the list of posts (one so far, in two editions) | `https://sidenerdapps.com/mainnerd/` |
| `01thecurledtorusburpsPL/index.html` | Post 01, plain-language edition, eleven chapters | `https://sidenerdapps.com/mainnerd/01thecurledtorusburpsPL/` |
| `01thecurledtorusburps/index.html` | Post 01, technical edition, section by section | `https://sidenerdapps.com/mainnerd/01thecurledtorusburps/` |
| `01thecurledtorusburpsKnobs/index.html` | The interactive companion, "The Tube's Curling Ladder" (turn the knobs) | `https://sidenerdapps.com/mainnerd/01thecurledtorusburpsKnobs/` |
| `comingsoon/index.html` | The placeholder "next post" lands on while the next post is not up yet | `https://sidenerdapps.com/mainnerd/comingsoon/` |
| `assets/main-nerd.css` | The stylesheet, shared by every post | `/mainnerd/assets/main-nerd.css` |
| `assets/01thecurledtorusburps/` | This paper's 34 figures (SVG), both PDFs, the cow GIF, the share image | `/mainnerd/assets/01thecurledtorusburps/...` |

**The folder name is spelled "torus".** The owner's message of 10 October gave the addresses as
`.../01thecurledtourusburpsPL` and `.../01thecurledtourusburps`; the paper's title is "The curled torus burps", so
the pages were built with `torus` and the difference was put to her. **Her answer, the same day: spell it as
it is spelled in mathematics and the source papers.** That is "torus", so the addresses stand as built. (The
name is the one constant `SLUG` in `scripts/main_nerd_site.py`.)

Each chapter of the plain page links to the matching section of the technical page and each section links
back. The cross-links open in a second named window (`mn-technical`, `mn-plain`), so with both pages open a
click in one moves the other to the matching place.

The front page was not asked for. It is there because the posts' breadcrumbs and "all posts" links need
somewhere to land, and a missing page on this site silently shows the home page. Drop it if it is not wanted
(then remove the blog level from the structured data too).

## To port

1. In the SideNerdMarketing repository, branch from an up-to-date `origin/main`. (The local checkout was 95
   commits behind on 10 October and lacked the live `/physics` page; a deploy from it would delete that page.)
2. Copy the whole folder to `sites/sidenerdapps/mainnerd/`.
3. Add to `sites/sidenerdapps/sitemap.xml`:

   ```xml
   <url><loc>https://sidenerdapps.com/mainnerd/</loc><lastmod>2026-10-10</lastmod></url>
   <url><loc>https://sidenerdapps.com/mainnerd/01thecurledtorusburpsPL/</loc><lastmod>2026-10-10</lastmod></url>
   <url><loc>https://sidenerdapps.com/mainnerd/01thecurledtorusburps/</loc><lastmod>2026-10-10</lastmod></url>
   <url><loc>https://sidenerdapps.com/mainnerd/01thecurledtorusburpsKnobs/</loc><lastmod>2026-10-10</lastmod></url>
   ```

   The placeholder (`comingsoon/`) is marked `noindex` and stays out of the sitemap.

4. Merge, then run the Deploy Site Content workflow for `sidenerdapps` (dry run first).

No terraform change is needed: the site's rewrite rule serves a folder path, with or without the trailing
slash, from its `index.html`. Paths on that site are case-sensitive, so `...burpsPL` needs its capitals.

## What the frame adds around the papers (owner's notes of 10 October)

- **A blog.** The masthead reads "Welcome to the Side Nerd Blog, Main Nerd"; each paper is a numbered post.
  "Sponsored by Side Nerd Apps" stands in the masthead and the footer.
- **Question headings.** Every chapter of the plain page opens with one commonly searched question ("What was
  there before the Big Bang?") and two sentences that connect it to the chapter without claiming an answer. A
  section near the end, "The big questions, and what this work can honestly say", takes five of them head on,
  and they are in the page's structured data. One answer ("What was there before time?") states the author's
  wider hypothesis in a sentence, from the project record and not from this paper: hers to confirm or reword.
- **Navigation between posts.** Each edition's footer has "all posts | next post »". While there is no
  second post, "next post" lands on `/mainnerd/comingsoon/` ("This post is not up yet", with buttons back
  to both editions and to the guestbook). When a second post is published, put its address in `NEXT_POST` in
  `scripts/main_nerd_site.py` in place of `SOON` and rebuild. (A "web ring" line stood here first; the
  owner removed it.)
- **The interactive companion is hosted here too** (the owner, 10 October: "let's host this in the blog"). It
  was first published as a Claude artifact; the build now makes a page of the blog from the same source file,
  `docs/public/curling_ladder_tube.html`, with every part of it unchanged, and the two editions' "Turn the
  knobs" links go to that page. It keeps its own look (its style sheet restyles bare elements, so the blog's
  style sheet is left off that page) under a Main Nerd bar at the top and bottom. The papers' PDFs still link
  to the artifact; point them at the blog's copy once it is live.
- **The cow** is the torus paper's: it is in the masthead of both editions (and on the placeholder), not on
  the blog's front page.
- **Advertisements.** Labelled with the one word, and real: four for Side Nerd on the plain page and one on
  the technical page, in the manner of a 1990s banner. Three carry the logo. Two show Ither on a phone in
  the logo's place: the sidebar panel has the text conversation (a volunteer texts hours, Ither logs them),
  and the mid-article box has the conversation and the volunteer report side by side. The site has one
  Ither picture, the three tilted phones of `sidenerdapps/ither-3phones-hero.png` (on `/capture-work` and
  textither.com); the stylesheet cuts one phone out of it and stands it upright, so the picture is loaded
  from the marketing assets bucket like the logo and nothing was copied into this repository. If that
  picture is ever replaced by one with a different layout, the two cut-outs (`.ad-phone.talk`,
  `.ad-phone.report`) need new numbers; single upright screenshots would be simpler and sharper. The sidebar panel is hidden on narrow screens.
  One more advertisement calls for a physicist, mathematician or relevant scientist to volunteer as a reader, and
  opens an e-mail to the author.
- **A guestbook that runs on e-mail.** The form opens the visitor's mail program with the entry filled in, so
  entries arrive in the author's inbox and nothing has to be hosted. It promises that an address is used only
  to reply and, if the box is ticked, to announce the next paper. Entries are not shown on the page. A
  guestbook that stores entries needs a form endpoint (a form service, or a Side Nerd intake of its own).
- **No visitor counter.** A real one needs something that stores a number (a small endpoint of the site's own,
  or a counter service); a static page cannot count. The joke counter was removed.
- **The address** in the reader advertisement and the guestbook is `AUTHOR_EMAIL` in
  `scripts/main_nerd_site.py`, the one printed on the technical paper. A public address collects spam.

## Things to know

- **Links are root-absolute** (`/mainnerd/...`). The site serves a folder with and without the trailing
  slash and does not redirect, so relative links would break on the slashless form. To preview locally:
  `python -m http.server --directory docs/public` and open `http://localhost:8000/mainnerd/`. Opening a
  file directly will not find its stylesheet.
- **A missing file returns the home page with status 200** on that site, so after deploying check that a
  figure and the stylesheet actually load, not just that the request succeeds.
- **The UTMs are not recorded by anything yet.** Every link back to sidenerdapps.com carries
  `utm_source=mainnerd&utm_medium=owned-media&utm_campaign=physics-01-curled-torus-burps&utm_content=<slot>`
  (slots: `top-banner`, `mid-article`, `sidebar`, `footer-banner`, `technical-footer`, `masthead-sponsor`,
  `index-sponsor`, `comingsoon-sponsor`, `footer-sponsor-plain`, `footer-sponsor-technical`,
  `footer-sponsor-index`, `footer-sponsor-soon`, and
  `footer-text-...`), in the lowercase, hyphenated form of the one full example in the marketing repository.
  sidenerdapps.com carried no analytics snippet on 10 October, so the tags are decoration until one is added.
  Because the pages live on the same site they point to, an analytics tool will also read these as a new
  session source; a click event on the ads would count them more cleanly.
- **Outside requests:** Google Fonts (DM Sans and Space Mono, as on the rest of the site), MathJax from
  jsDelivr for the equations, and the favicon, the logo and the Ither picture in two advertisements from the
  marketing assets bucket.
- **Links to GitHub** (source, data and supplement; "report a mistake"; the sources' repository links) point
  at the `main` branch. On 10 October `main` still held the 25 September paper and no supplement, so those
  links show old or missing files until this branch is merged. The two PDF links do not depend on that: the
  PDFs are copied into the paper's assets folder by the build.
- **"Turn the knobs"** opens the blog's own copy of the companion. The link inside the two PDFs still opens
  the Claude artifact, which works for visitors only while that artifact is shared by link.
- **The share image** is `assets/01thecurledtorusburps/og-image.png`, made for these pages. The site-wide
  `og-image.png` the other pages point to did not exist on 10 October.
- **The existing `/physics` page** is not linked from these pages. Say if it should be.

## To rebuild

The pages are generated from the papers' LaTeX, so a change to either paper is one command away:

```sh
python scripts/build_main_nerd_pages.py --tectonic .tools/tectonic/tectonic.exe
python scripts/make_main_nerd_assets.py "path/to/the cow.gif"     # only if the GIF changes
```

`--skip-figures` reuses the SVG files. The script needs PyMuPDF (figures) and the second needs Pillow.
The frame (ticker, advertisements, question headings, quick answers, guestbook, footer) is in
`scripts/main_nerd_site.py`; the questions and answers restate the plain-language edition and must be
changed there first. A second paper would get its own `SLUG` and its own folder under `assets/`.
