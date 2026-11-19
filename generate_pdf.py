"""
Clean PDF generator for CHEATSHEET.md  —  dark-themed, properly structured.
Correctly skips heading/separator detection inside fenced code blocks.
"""

import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Preformatted,
    Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER

# ── Palette ───────────────────────────────────────────────────────────────────
BG       = colors.HexColor("#11111b")
BG_CODE  = colors.HexColor("#1e1e2e")
BG_CODE2 = colors.HexColor("#13131f")
FG       = colors.HexColor("#cdd6f4")
BLUE     = colors.HexColor("#89b4fa")
GREEN    = colors.HexColor("#a6e3a1")
RED      = colors.HexColor("#f38ba8")
YELLOW   = colors.HexColor("#f9e2af")
TEAL     = colors.HexColor("#89dceb")
MUTED    = colors.HexColor("#7f849c")
BORDER   = colors.HexColor("#45475a")
TBL_HD   = colors.HexColor("#313244")
TBL_ALT  = colors.HexColor("#24273a")
NOTE_BG  = colors.HexColor("#1e3a2f")
WARN_BG  = colors.HexColor("#3b2a1a")

PAGE_W, PAGE_H = A4
M = 1.8 * cm
CW = PAGE_W - 2 * M          # usable content width


# ── Page background + footer ──────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.4)
    canvas.line(M, 1.1 * cm, PAGE_W - M, 1.1 * cm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7)
    canvas.drawCentredString(PAGE_W / 2, 0.65 * cm,
                             f"DevOps Cheat Sheet  ·  Page {doc.page}  ·  "
                             "Docker · Jenkins · Nagios · Kubernetes · AWS EC2")
    canvas.restoreState()


# ── Styles ────────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

STYLES = {
    "h1":   S("H1",  fontSize=20, leading=26, textColor=BLUE,   fontName="Helvetica-Bold",
               spaceBefore=14, spaceAfter=4),
    "h2":   S("H2",  fontSize=13, leading=18, textColor=GREEN,  fontName="Helvetica-Bold",
               spaceBefore=10, spaceAfter=3),
    "h3":   S("H3",  fontSize=10, leading=14, textColor=RED,    fontName="Helvetica-Bold",
               spaceBefore=7,  spaceAfter=2),
    "h4":   S("H4",  fontSize=9,  leading=12, textColor=YELLOW, fontName="Helvetica-Bold",
               spaceBefore=5,  spaceAfter=1),
    "body": S("body",fontSize=8.5,leading=12, textColor=FG,     fontName="Helvetica",
               spaceBefore=1,  spaceAfter=1),
    "bull": S("bull",fontSize=8.5,leading=12, textColor=FG,     fontName="Helvetica",
               spaceBefore=1,  spaceAfter=1, leftIndent=14),
    "note": S("note",fontSize=8,  leading=11, textColor=GREEN,  fontName="Helvetica-Oblique",
               leftIndent=10),
    "warn": S("warn",fontSize=8,  leading=11, textColor=YELLOW, fontName="Helvetica-Oblique",
               leftIndent=10),
    "cov_t":S("covt",fontSize=30, leading=38, textColor=BLUE,   fontName="Helvetica-Bold",
               alignment=TA_CENTER),
    "cov_s":S("covs",fontSize=13, leading=18, textColor=GREEN,  fontName="Helvetica",
               alignment=TA_CENTER, spaceAfter=3),
    "cov_m":S("covm",fontSize=8,  leading=12, textColor=MUTED,  fontName="Helvetica",
               alignment=TA_CENTER, spaceAfter=2),
}


def safe_p(txt, style):
    """Paragraph with inline markdown (bold, italic, backtick) safely converted."""
    txt = str(txt)
    txt = re.sub(r'`([^`]+)`',
                 r'<font name="Courier" color="#f9e2af">\1</font>', txt)
    txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', txt)
    txt = re.sub(r'\*(.+?)\*',    r'<i>\1</i>', txt)
    txt = txt.replace("&", "&amp;").replace("<b>", "\x00b").replace("</b>", "\x01b") \
             .replace("<i>", "\x00i").replace("</i>", "\x01i") \
             .replace("<font", "\x00f").replace("</font>", "\x01f")
    # restore tags
    txt = txt.replace("\x00b", "<b>").replace("\x01b", "</b>") \
             .replace("\x00i", "<i>").replace("\x01i", "</i>") \
             .replace("\x00f", "<font").replace("\x01f", "</font>")
    try:
        return Paragraph(txt, style)
    except Exception:
        clean = re.sub(r'<[^>]+>', '', txt)
        return Paragraph(clean, style)


def code_blk(lines_list, lang=""):
    """Dark styled code block table."""
    text = "\n".join(lines_list)
    # wrap very long lines
    wrapped = []
    for ln in text.split("\n"):
        while len(ln) > 92:
            wrapped.append(ln[:92])
            ln = "    " + ln[92:]
        wrapped.append(ln)

    label = Paragraph(lang.upper() or "CODE",
                      ParagraphStyle("lbl", fontName="Helvetica-Bold",
                                     fontSize=6, textColor=MUTED, leftIndent=4))
    pre   = Preformatted("\n".join(wrapped),
                         ParagraphStyle("pre", fontName="Courier", fontSize=7,
                                        leading=10, textColor=FG,
                                        leftIndent=4, rightIndent=4))
    tbl = Table([[label], [pre]], colWidths=[CW - 0.2 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BG_CODE),
        ("BACKGROUND",    (0, 0), (-1,  0), BG_CODE2),
        ("LINEBEFORE",    (0, 0), (-1, -1), 2.5, BLUE),
        ("LINEABOVE",     (0, 0), (-1,  0), 0.5, BLUE),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
    ]))
    return tbl


def md_tbl(rows):
    """Render a markdown table as a styled ReportLab Table."""
    cs  = ParagraphStyle("tc", fontName="Helvetica",      fontSize=7.5,
                          leading=10, textColor=FG)
    hs  = ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=7.5,
                          leading=10, textColor=BLUE)
    data = []
    for ri, row in enumerate(rows):
        st = hs if ri == 0 else cs
        data.append([Paragraph(c.strip(), st) for c in row])

    ncols = max(len(r) for r in data)
    cw    = (CW - 0.2 * cm) / ncols
    tbl   = Table(data, colWidths=[cw] * ncols, repeatRows=1)
    ts    = [
        ("BACKGROUND",    (0, 0), (-1, 0),  TBL_HD),
        ("LINEBELOW",     (0, 0), (-1, 0),  1,   BLUE),
        ("GRID",          (0, 0), (-1, -1), 0.3, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]
    for ri in range(1, len(data)):
        if ri % 2 == 0:
            ts.append(("BACKGROUND", (0, ri), (-1, ri), TBL_ALT))
    tbl.setStyle(TableStyle(ts))
    return tbl


def note_box(text, kind="NOTE"):
    is_warn = kind in ("WARNING", "CAUTION", "IMPORTANT")
    bg      = WARN_BG if is_warn else NOTE_BG
    border  = YELLOW  if is_warn else GREEN
    icon    = {"NOTE": "📝", "TIP": "💡", "IMPORTANT": "⚠️",
               "WARNING": "⚠️", "CAUTION": "🚨"}.get(kind, "ℹ️")
    style   = STYLES["warn"] if is_warn else STYLES["note"]
    p = Paragraph(f"<b>{icon} {kind}:</b> {text}", style)
    tbl = Table([[p]], colWidths=[CW - 0.2 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), bg),
        ("LINEBEFORE",    (0, 0), (-1, -1), 2.5, border),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
    ]))
    return tbl


# ── Main parser ───────────────────────────────────────────────────────────────
def parse(md_text):
    flowables = []
    lines = md_text.split("\n")
    i = 0

    sp  = lambda h=0.12: flowables.append(Spacer(1, h * cm))
    hr  = lambda: (
        flowables.append(Spacer(1, 0.15 * cm)),
        flowables.append(HRFlowable(width="100%", thickness=0.4,
                                    color=BORDER, spaceAfter=3)),
        flowables.append(Spacer(1, 0.15 * cm))
    )

    while i < len(lines):
        line = lines[i]

        # ── Fenced code block — consume everything inside ──────────────────
        if line.startswith("```"):
            lang = line[3:].strip()
            body = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1   # skip closing ```
            if body:
                sp(0.1)
                flowables.append(code_blk(body, lang))
                sp(0.1)
            continue

        # ── Horizontal rule ────────────────────────────────────────────────
        if re.match(r'^-{3,}$', line.strip()):
            hr(); i += 1; continue

        # ── H1 ────────────────────────────────────────────────────────────
        if re.match(r'^# [^#]', line):
            flowables.append(PageBreak())
            flowables.append(safe_p(line[2:], STYLES["h1"]))
            flowables.append(HRFlowable(width="100%", thickness=1.5,
                                        color=BLUE, spaceAfter=5))
            i += 1; continue

        # ── H2 ────────────────────────────────────────────────────────────
        if re.match(r'^## [^#]', line):
            sp(0.25)
            flowables.append(safe_p(line[3:], STYLES["h2"]))
            flowables.append(HRFlowable(width="35%", thickness=0.7,
                                        color=GREEN, spaceAfter=3, hAlign="LEFT"))
            i += 1; continue

        # ── H3 ────────────────────────────────────────────────────────────
        if re.match(r'^### [^#]', line):
            sp(0.15)
            flowables.append(safe_p(line[4:], STYLES["h3"]))
            i += 1; continue

        # ── H4 ────────────────────────────────────────────────────────────
        if re.match(r'^#### [^#]', line):
            flowables.append(safe_p(line[5:], STYLES["h4"]))
            i += 1; continue

        # ── Markdown table ─────────────────────────────────────────────────
        if line.strip().startswith("|") and "|" in line:
            rows = []
            while i < len(lines) and "|" in lines[i]:
                r = lines[i].strip().strip("|")
                if re.match(r'^[-| :]+$', r):   # separator row
                    i += 1; continue
                rows.append([c.strip() for c in r.split("|")])
                i += 1
            if rows:
                sp(0.08)
                flowables.append(md_tbl(rows))
                sp(0.08)
            continue

        # ── Blockquote note/warning ────────────────────────────────────────
        if re.match(r'^> \[!', line):
            m    = re.match(r'^> \[!(\w+)\](.*)', line)
            kind = m.group(1).upper() if m else "NOTE"
            bits = [m.group(2).strip()] if m else []
            i += 1
            while i < len(lines) and lines[i].startswith("> "):
                bits.append(lines[i][2:].strip())
                i += 1
            flowables.append(note_box(" ".join(bits), kind))
            sp(0.08)
            continue

        if line.startswith("> "):
            flowables.append(safe_p(line[2:], STYLES["note"]))
            i += 1; continue

        # ── Bullet / numbered list ─────────────────────────────────────────
        if re.match(r'^[\-\*] ', line):
            flowables.append(safe_p("• " + line[2:], STYLES["bull"]))
            i += 1; continue

        if re.match(r'^\d+\. ', line):
            num  = re.match(r'^(\d+)\. ', line).group(1)
            rest = line[len(num) + 2:]
            flowables.append(safe_p(f"{num}. {rest}", STYLES["bull"]))
            i += 1; continue

        # ── Blank line ─────────────────────────────────────────────────────
        if not line.strip():
            sp(0.06); i += 1; continue

        # ── Default body ───────────────────────────────────────────────────
        flowables.append(safe_p(line, STYLES["body"]))
        i += 1

    return flowables


# ── Cover page ────────────────────────────────────────────────────────────────
def cover():
    items = [Spacer(1, 3.5 * cm)]
    items.append(Paragraph("🚀 DevOps", STYLES["cov_t"]))
    items.append(Paragraph("Complete Cheat Sheet", STYLES["cov_t"]))
    items.append(Spacer(1, 0.4 * cm))
    items.append(HRFlowable(width="55%", thickness=1.5, color=BLUE, hAlign="CENTER"))
    items.append(Spacer(1, 0.4 * cm))
    for t in ["🐳 Docker  ·  Multi-Container Compose",
              "🔧 Jenkins  ·  Scripted Pipeline CI/CD",
              "📡 Nagios  ·  Infrastructure Monitoring",
              "☸️  Kubernetes  ·  Deploy & Scale",
              "☁️  AWS EC2  ·  Cloud Deployment"]:
        items.append(Paragraph(t, STYLES["cov_s"]))
    items.append(Spacer(1, 1.2 * cm))
    items.append(HRFlowable(width="35%", thickness=0.5, color=BORDER, hAlign="CENTER"))
    items.append(Spacer(1, 0.4 * cm))
    for t in ["KMIT Lab Internal II  ·  Software Engineering (23CC501PC)",
              "III Year / I Semester  ·  A.Y 2026–2027",
              "Covers all 9 exam sets — SET 1 through SET 9"]:
        items.append(Paragraph(t, STYLES["cov_m"]))
    items.append(PageBreak())
    return items


# ── Entry point ───────────────────────────────────────────────────────────────
def main():
    src = r"d:\notes\SE\lab\int 2\software-repo\CHEATSHEET.md"
    out = r"d:\notes\SE\lab\int 2\software-repo\CHEATSHEET.pdf"

    with open(src, encoding="utf-8") as f:
        md = f.read()

    doc = SimpleDocTemplate(
        out, pagesize=A4,
        leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=1.8 * cm,
        title="DevOps Cheat Sheet",
        author="dheerajmalavath",
        subject="Docker · Jenkins · Nagios · Kubernetes · AWS EC2",
    )
    story = cover() + parse(md)
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"✅ PDF generated → {out}")

    # Quick sanity check
    with open(out, "rb") as f:
        data = f.read()
    pages = len(re.findall(rb'/Type\s*/Page[^s]', data))
    print(f"   Pages : ~{pages}")
    print(f"   Size  : {len(data)/1024:.1f} KB")


if __name__ == "__main__":
    main()
