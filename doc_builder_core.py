"""
Complete Word Document (.docx) Generator for DevOps & SE Lab Cheat Sheet.
Tailored exclusively for Ubuntu (Linux) environments with strict explanation -> code -> verification alignment.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_cell_borders(cell, left_color="2563EB", left_sz="24", border_color="CBD5E1", border_sz="4"):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{border_sz}" w:space="0" w:color="{border_color}"/>'
        f'<w:left w:val="single" w:sz="{left_sz}" w:space="0" w:color="{left_color}"/>'
        f'<w:bottom w:val="single" w:sz="{border_sz}" w:space="0" w:color="{border_color}"/>'
        f'<w:right w:val="single" w:sz="{border_sz}" w:space="0" w:color="{border_color}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

class CheatsheetDocBuilder:
    def __init__(self):
        self.doc = docx.Document()
        self._setup_page_margins()
        self._setup_base_styles()

    def _setup_page_margins(self):
        for section in self.doc.sections:
            section.top_margin = Inches(0.8)
            section.bottom_margin = Inches(0.8)
            section.left_margin = Inches(0.8)
            section.right_margin = Inches(0.8)

    def _setup_base_styles(self):
        normal_style = self.doc.styles['Normal']
        normal_style.font.name = 'Calibri'
        normal_style.font.size = Pt(10)
        normal_style.font.color.rgb = RGBColor(30, 41, 59) # Slate 800
        normal_style.paragraph_format.line_spacing = 1.15
        normal_style.paragraph_format.space_after = Pt(4)

    def add_cover(self, title, subtitle, author, metadata_items):
        p_title = self.doc.add_paragraph()
        p_title.paragraph_format.space_before = Pt(18)
        p_title.paragraph_format.space_after = Pt(6)
        r_title = p_title.add_run(title)
        r_title.font.name = 'Arial'
        r_title.font.size = Pt(24)
        r_title.font.bold = True
        r_title.font.color.rgb = RGBColor(27, 54, 93) # Deep Navy

        p_sub = self.doc.add_paragraph()
        p_sub.paragraph_format.space_after = Pt(14)
        r_sub = p_sub.add_run(subtitle)
        r_sub.font.name = 'Calibri'
        r_sub.font.size = Pt(13)
        r_sub.font.color.rgb = RGBColor(71, 85, 105) # Slate 600

        tbl = self.doc.add_table(rows=len(metadata_items), cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(2.2)
        tbl.columns[1].width = Inches(4.7)

        for i, (k, v) in enumerate(metadata_items):
            c0 = tbl.cell(i, 0)
            c1 = tbl.cell(i, 1)
            set_cell_background(c0, "F8FAFC")
            set_cell_background(c1, "F8FAFC")
            set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
            set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
            set_cell_borders(c0, left_color="1B365D", left_sz="12", border_color="E2E8F0", border_sz="4")
            set_cell_borders(c1, left_color="E2E8F0", left_sz="4", border_color="E2E8F0", border_sz="4")

            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_after = Pt(0)
            r0 = p0.add_run(k)
            r0.font.bold = True
            r0.font.size = Pt(9.5)
            r0.font.color.rgb = RGBColor(27, 54, 93)

            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_after = Pt(0)
            r1 = p1.add_run(v)
            r1.font.size = Pt(9.5)
            r1.font.color.rgb = RGBColor(15, 23, 42)

        self.doc.add_paragraph().paragraph_format.space_after = Pt(12)

    def add_h1(self, text):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = RGBColor(27, 54, 93) # Navy

    def add_h2(self, text):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = RGBColor(2, 132, 199) # Blue 600

    def add_h3(self, text):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = RGBColor(51, 65, 85) # Slate 700

    def add_paragraph(self, text, bold_prefix=None, italic=False):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix + " ")
            r_pre.font.bold = True
            r_pre.font.color.rgb = RGBColor(15, 23, 42)
        run = p.add_run(text)
        run.font.italic = italic
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(30, 41, 59)
        return p

    def add_callout(self, title, text, callout_type="info"):
        tbl = self.doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.9)

        cell = tbl.cell(0, 0)
        if callout_type == "warning":
            fill = "FFFBEB" # Amber 50
            border_left = "D97706" # Amber 600
            title_color = RGBColor(180, 83, 9)
        elif callout_type == "success":
            fill = "F0FDF4" # Green 50
            border_left = "16A34A" # Green 600
            title_color = RGBColor(21, 128, 61)
        else: # info
            fill = "EFF6FF" # Blue 50
            border_left = "2563EB" # Blue 600
            title_color = RGBColor(29, 78, 216)

        set_cell_background(cell, fill)
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        set_cell_borders(cell, left_color=border_left, left_sz="24", border_color="E2E8F0", border_sz="4")

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        r_title = p.add_run(f"📌 {title}: ")
        r_title.font.bold = True
        r_title.font.size = Pt(9.5)
        r_title.font.color.rgb = title_color

        r_text = p.add_run(text)
        r_text.font.size = Pt(9.5)
        r_text.font.color.rgb = RGBColor(15, 23, 42)

        p_spacer = self.doc.add_paragraph()
        p_spacer.paragraph_format.space_before = Pt(0)
        p_spacer.paragraph_format.space_after = Pt(4)

    def add_step(self, task_explanation, code_content, verification_output=None, note=None):
        """
        Adds a perfectly aligned DevOps step:
        1. Task / Explanation
        2. Ubuntu Command / Code
        3. Verification / Expected Output
        """
        # 1. Task / Explanation
        p_task = self.doc.add_paragraph()
        p_task.paragraph_format.space_before = Pt(6)
        p_task.paragraph_format.space_after = Pt(3)
        p_task.paragraph_format.keep_with_next = True
        r_label = p_task.add_run("■ Task / Explanation: ")
        r_label.font.bold = True
        r_label.font.size = Pt(10)
        r_label.font.color.rgb = RGBColor(27, 54, 93)

        r_exp = p_task.add_run(task_explanation)
        r_exp.font.size = Pt(10)
        r_exp.font.color.rgb = RGBColor(30, 41, 59)

        # 2. Ubuntu Command / Code Block
        tbl = self.doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.9)

        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F8FAFC") # Light Slate 50
        set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
        set_cell_borders(cell, left_color="2563EB", left_sz="20", border_color="CBD5E1", border_sz="4")

        p_code = cell.paragraphs[0]
        p_code.paragraph_format.space_before = Pt(0)
        p_code.paragraph_format.space_after = Pt(0)
        p_code.paragraph_format.line_spacing = 1.05

        r_code = p_code.add_run(code_content.strip())
        r_code.font.name = 'Consolas'
        r_code.font.size = Pt(9.0)
        r_code.font.color.rgb = RGBColor(15, 23, 42)

        # 3. Verification / Expected Output
        if verification_output:
            p_ver = self.doc.add_paragraph()
            p_ver.paragraph_format.space_before = Pt(3)
            p_ver.paragraph_format.space_after = Pt(6)
            r_vlabel = p_ver.add_run("✔ Expected Output / Verification: ")
            r_vlabel.font.bold = True
            r_vlabel.font.size = Pt(9.5)
            r_vlabel.font.color.rgb = RGBColor(22, 101, 52) # Green 800

            r_vtext = p_ver.add_run(verification_output)
            r_vtext.font.size = Pt(9.5)
            r_vtext.font.italic = True
            r_vtext.font.color.rgb = RGBColor(51, 65, 85)

        if note:
            self.add_callout("Ubuntu Note", note, "info")

    def add_table(self, headers, data, col_widths=None):
        tbl = self.doc.add_table(rows=len(data) + 1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False

        if col_widths and len(col_widths) == len(headers):
            for col_idx, width in enumerate(col_widths):
                tbl.columns[col_idx].width = Inches(width)

        # Header Row
        hdr_cells = tbl.rows[0].cells
        for col_idx, heading in enumerate(headers):
            c = hdr_cells[col_idx]
            set_cell_background(c, "1B365D") # Deep Navy
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            set_cell_borders(c, left_color="CBD5E1", left_sz="4", border_color="CBD5E1", border_sz="4")
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(heading)
            run.font.bold = True
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(255, 255, 255)

        # Data Rows
        for row_idx, row_data in enumerate(data):
            row_cells = tbl.rows[row_idx + 1].cells
            bg_color = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
            for col_idx, cell_value in enumerate(row_data):
                c = row_cells[col_idx]
                set_cell_background(c, bg_color)
                set_cell_margins(c, top=60, bottom=60, left=100, right=100)
                set_cell_borders(c, left_color="E2E8F0", left_sz="4", border_color="E2E8F0", border_sz="4")
                p = c.paragraphs[0]
                p.paragraph_format.space_after = Pt(0)
                run = p.add_run(str(cell_value))
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(15, 23, 42)

        p_spacer = self.doc.add_paragraph()
        p_spacer.paragraph_format.space_after = Pt(8)

    def add_page_break(self):
        self.doc.add_page_break()

    def save(self, filepath):
        self.doc.save(filepath)
        print(f"Document saved successfully at: {filepath}")

if __name__ == '__main__':
    print("CheatsheetDocBuilder module compiled successfully.")
