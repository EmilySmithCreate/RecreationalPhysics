"""A small Markdown-to-.docx writer with no dependencies (a .docx is a zip of XML), for the outreach package of
22 October 2026. Handles: # and ## headings, paragraphs (lines joined until a blank line), '- ' bullets with wrapped
continuation lines, numbered '1. ' items, **bold**, *italic*, `code` (rendered as plain text), and embedded PNG figures
given as a list of (path, caption). Everything before the first line starting with '# ' is skipped (the draft's status
header for the owner).

Usage: python3 sandbox/md_to_docx.py IN.md OUT.docx [FIG.png "caption"]...
"""
import re
import struct
import sys
import zipfile
from xml.sax.saxutils import escape

EMU_PER_INCH = 914400
PAGE_WIDTH_IN = 6.3


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", path
    w, h = struct.unpack(">II", head[16:24])
    return w, h


def runs(text):
    """Inline markdown -> w:r elements."""
    text = text.replace("`", "")
    out = []
    pos = 0
    pattern = re.compile(r"(\*\*(.+?)\*\*|\*(.+?)\*)")
    for m in pattern.finditer(text):
        if m.start() > pos:
            out.append(run(text[pos:m.start()]))
        if m.group(2) is not None:
            out.append(run(m.group(2), bold=True))
        else:
            out.append(run(m.group(3), italic=True))
        pos = m.end()
    if pos < len(text):
        out.append(run(text[pos:]))
    return "".join(out)


def run(text, bold=False, italic=False):
    props = ""
    if bold or italic:
        props = "<w:rPr>%s%s</w:rPr>" % ("<w:b/>" if bold else "", "<w:i/>" if italic else "")
    return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (props, escape(text))


def para(text, style=None, numbered=False, bullet=False):
    ppr = ""
    if style:
        ppr = '<w:pPr><w:pStyle w:val="%s"/></w:pPr>' % style
    elif bullet:
        ppr = '<w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr></w:pPr>'
    elif numbered:
        ppr = '<w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr></w:pPr>'
    return "<w:p>%s%s</w:p>" % (ppr, runs(text))


def figure(rid, w, h, index):
    width_emu = int(PAGE_WIDTH_IN * EMU_PER_INCH)
    height_emu = int(width_emu * h / w)
    return ('<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
            '<wp:extent cx="%d" cy="%d"/><wp:docPr id="%d" name="Figure %d"/>'
            '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="%d" name="figure%d.png"/><pic:cNvPicPr/></pic:nvPicPr>'
            '<pic:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
            '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
            % (width_emu, height_emu, index, index, index, index, rid, width_emu, height_emu))


def table(rows):
    """A markdown table (list of lists of cell strings) -> w:tbl with a header row in bold."""
    cells = []
    for i, row in enumerate(rows):
        tcs = "".join('<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/></w:tcPr><w:p><w:pPr><w:spacing w:after="0"/></w:pPr>%s</w:p></w:tc>'
                      % (run(c, bold=(i == 0)) if i == 0 else runs(c)) for c in row)
        cells.append("<w:tr>%s</w:tr>" % tcs)
    borders = "".join('<w:%s w:val="single" w:sz="4" w:space="0" w:color="888888"/>' % b
                      for b in ("top", "left", "bottom", "right", "insideH", "insideV"))
    return ('<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/><w:tblBorders>%s</w:tblBorders>'
            '<w:tblCellMar><w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr>%s</w:tbl>'
            '<w:p/>' % (borders, "".join(cells)))


def body_from_markdown(md):
    lines = md.splitlines()
    # the document starts at the LAST line beginning "# " before the first "## " (the drafts carry a status
    # header under a first "# " line, then the letter's own title)
    starts = [i for i, l in enumerate(lines) if l.startswith("# ")]
    first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    start = max([i for i in starts if i < first_h2], default=0)
    lines = lines[start:]
    out = []
    buf = []
    mode = None            # None, "bullet", "number"
    tbl = []

    def flush():
        nonlocal buf, mode, tbl
        if tbl:
            out.append(table(tbl))
            tbl = []
        if buf:
            text = " ".join(s.strip() for s in buf)
            out.append(para(text, bullet=(mode == "bullet"), numbered=(mode == "number")))
        buf, mode = [], None

    for l in lines:
        if l.startswith("|"):
            if buf:
                flush()
            cells_ = [c.strip() for c in l.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", c) for c in cells_):
                continue
            tbl.append(cells_)
            continue
        elif tbl:
            flush()
        if not l.strip():
            flush()
            continue
        if l.startswith("# "):
            flush(); out.append(para(l[2:], style="Title")); continue
        if l.startswith("## "):
            flush(); out.append(para(l[3:], style="Heading1")); continue
        if l.startswith("### "):
            flush(); out.append(para(l[4:], style="Heading2")); continue
        if l.strip() == "---":
            flush(); continue
        if l.startswith("- "):
            flush(); mode = "bullet"; buf = [l[2:]]; continue
        m = re.match(r"^(\d+)\. (.*)", l)
        if m:
            flush(); mode = "number"; buf = [m.group(2)]; continue
        if l.startswith("  ") and buf and mode in ("bullet", "number"):
            buf.append(l); continue
        if buf and mode is None:
            buf.append(l); continue
        if buf and mode in ("bullet", "number") and not l.startswith(" "):
            flush()
        buf.append(l)
    flush()
    return out


STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="264" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="200"/></w:pPr><w:rPr><w:b/><w:sz w:val="32"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="280" w:after="120"/></w:pPr><w:rPr><w:b/><w:sz w:val="26"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="200" w:after="80"/></w:pPr><w:rPr><w:b/><w:sz w:val="23"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Caption"><w:name w:val="caption"/><w:basedOn w:val="Normal"/><w:rPr><w:i/><w:sz w:val="20"/></w:rPr></w:style>
</w:styles>"""

NUMBERING = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:abstractNum w:abstractNumId="0"><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="&#8226;"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="540" w:hanging="270"/></w:pPr></w:lvl></w:abstractNum>
<w:abstractNum w:abstractNumId="1"><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:lvlText w:val="%1."/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="540" w:hanging="270"/></w:pPr></w:lvl></w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num><w:num w:numId="2"><w:abstractNumId w:val="1"/></w:num>
</w:numbering>"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Default Extension="png" ContentType="image/png"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>"""

ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""


def write_docx(md_path, out_path, figures):
    md = open(md_path, encoding="utf-8").read()
    body = body_from_markdown(md)
    # drop the trailing "*Figure 1.*" caption lines of the draft (figures are embedded with their own captions)
    body = [b for b in body if "Figure 1." not in b and "Figure 2." not in b and "Table 1." not in b]
    rels = ['<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>',
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>']
    media = []
    for i, (path, caption) in enumerate(figures, start=1):
        rid = "rId%d" % (10 + i)
        w, h = png_size(path)
        rels.append('<Relationship Id="%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/figure%d.png"/>' % (rid, i))
        media.append(("word/media/figure%d.png" % i, open(path, "rb").read()))
        body.append(figure(rid, w, h, i))
        body.append(para("Figure %d. %s" % (i, caption), style="Caption"))
    document = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
                'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
                'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">'
                '<w:body>%s<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1200" w:right="1200" w:bottom="1200" w:left="1200" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr></w:body></w:document>'
                % "".join(body))
    doc_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">%s</Relationships>' % "".join(rels))
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", ROOT_RELS)
        z.writestr("word/document.xml", document)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/numbering.xml", NUMBERING)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
        for name, data in media:
            z.writestr(name, data)


if __name__ == "__main__":
    args = sys.argv[1:]
    md_path, out_path = args[0], args[1]
    figs = [(args[i], args[i + 1]) for i in range(2, len(args) - 1, 2)]
    write_docx(md_path, out_path, figs)
    print("wrote", out_path)
