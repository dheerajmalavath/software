"""
Builds the comprehensive 400+ Viva Questions & Answers Word Document (.docx) and Markdown (.md).
Covers all 8 topics with at least 50 questions per topic.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from viva_data_topic1 import GIT_QUESTIONS
from viva_data_topic2 import MAVEN_QUESTIONS
from viva_data_topic3 import DOCKER_CLI_QUESTIONS
from viva_data_topic4 import COMPOSE_QUESTIONS
from viva_data_topic5 import JENKINS_QUESTIONS
from viva_data_topic6 import K8S_QUESTIONS
from viva_data_topic7 import NAGIOS_QUESTIONS
from viva_data_topic8 import AWS_QUESTIONS

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
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

def set_cell_borders(cell, left_color="1B365D", left_sz="16", border_color="E2E8F0", border_sz="4"):
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

def build_viva_docx(docx_paths):
    doc = docx.Document()

    # Margins
    for sec in doc.sections:
        sec.top_margin = Inches(0.8)
        sec.bottom_margin = Inches(0.8)
        sec.left_margin = Inches(0.8)
        sec.right_margin = Inches(0.8)

    # Base style
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(10)
    normal.font.color.rgb = RGBColor(30, 41, 59) # Slate 800
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(4)

    # Title & Metadata
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(20)
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("DevOps & Software Engineering Comprehensive Viva Guide")
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(24)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(27, 54, 93) # Deep Navy

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("400 Technical Viva & Interview Questions with In-Depth Technical Explanations Across All 8 Core Syllabus Modules")
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(71, 85, 105)

    # Metadata table
    meta = [
        ("Course & Subject", "Software Engineering Lab — 23CC501PC (KMIT)"),
        ("Environment", "Ubuntu Linux (20.04 / 22.04 / 24.04 LTS)"),
        ("Question Count", "400 Questions (50 In-Depth Questions Per Topic)"),
        ("Topics Covered", "Git & GitHub, Maven with Eclipse, Docker CLI, Compose, Jenkins, Kubernetes, Nagios, AWS EC2"),
        ("Repository Target", "https://github.com/dheerajmalavath/software")
    ]
    tbl_meta = doc.add_table(rows=len(meta), cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_meta.autofit = False
    tbl_meta.columns[0].width = Inches(2.2)
    tbl_meta.columns[1].width = Inches(4.7)

    for i, (k, v) in enumerate(meta):
        c0 = tbl_meta.cell(i, 0)
        c1 = tbl_meta.cell(i, 1)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "F8FAFC")
        set_cell_margins(c0, top=50, bottom=50, left=90, right=90)
        set_cell_margins(c1, top=50, bottom=50, left=90, right=90)
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

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(12)

    # Topics mapping
    topics = [
        ("Topic 1: Git & GitHub — Version Control & Collaboration", GIT_QUESTIONS),
        ("Topic 2: Apache Maven & Eclipse IDE Build Automation", MAVEN_QUESTIONS),
        ("Topic 3: Docker Engine & Container CLI Architecture", DOCKER_CLI_QUESTIONS),
        ("Topic 4: Docker Compose & Dockerfile Multi-Container Systems", COMPOSE_QUESTIONS),
        ("Topic 5: Jenkins CI/CD Automation & Pipelines", JENKINS_QUESTIONS),
        ("Topic 6: Kubernetes & Minikube Container Orchestration", K8S_QUESTIONS),
        ("Topic 7: Nagios Infrastructure & Service Monitoring", NAGIOS_QUESTIONS),
        ("Topic 8: AWS EC2 & Cloud Infrastructure Deployment", AWS_QUESTIONS),
    ]

    for topic_idx, (topic_title, questions) in enumerate(topics):
        if topic_idx > 0:
            doc.add_page_break()

        # Section Header
        p_hdr = doc.add_paragraph()
        p_hdr.paragraph_format.space_before = Pt(16)
        p_hdr.paragraph_format.space_after = Pt(8)
        p_hdr.paragraph_format.keep_with_next = True
        r_hdr = p_hdr.add_run(f"{topic_title} ({len(questions)} Questions)")
        r_hdr.font.name = 'Arial'
        r_hdr.font.size = Pt(16)
        r_hdr.font.bold = True
        r_hdr.font.color.rgb = RGBColor(27, 54, 93)

        for q_idx, (question, answer) in enumerate(questions):
            # Question Block Table or Paragraph
            p_q = doc.add_paragraph()
            p_q.paragraph_format.space_before = Pt(10)
            p_q.paragraph_format.space_after = Pt(3)
            p_q.paragraph_format.keep_with_next = True

            r_num = p_q.add_run(f"Q{q_idx + 1}. ")
            r_num.font.name = 'Arial'
            r_num.font.bold = True
            r_num.font.size = Pt(11)
            r_num.font.color.rgb = RGBColor(2, 132, 199) # Blue 600

            r_qtext = p_q.add_run(question)
            r_qtext.font.name = 'Arial'
            r_qtext.font.bold = True
            r_qtext.font.size = Pt(10.5)
            r_qtext.font.color.rgb = RGBColor(15, 23, 42)

            # Answer Block Table for high polish
            tbl_ans = doc.add_table(rows=1, cols=1)
            tbl_ans.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl_ans.autofit = False
            tbl_ans.columns[0].width = Inches(6.9)

            c_ans = tbl_ans.cell(0, 0)
            set_cell_background(c_ans, "F8FAFC")
            set_cell_margins(c_ans, top=80, bottom=80, left=120, right=120)
            set_cell_borders(c_ans, left_color="2563EB", left_sz="16", border_color="E2E8F0", border_sz="4")

            p_ans = c_ans.paragraphs[0]
            p_ans.paragraph_format.space_before = Pt(0)
            p_ans.paragraph_format.space_after = Pt(0)
            p_ans.paragraph_format.line_spacing = 1.15

            r_ans_label = p_ans.add_run("Explanation & Answer:\n")
            r_ans_label.font.bold = True
            r_ans_label.font.size = Pt(9.5)
            r_ans_label.font.color.rgb = RGBColor(27, 54, 93)

            r_ans_text = p_ans.add_run(answer)
            r_ans_text.font.size = Pt(9.5)
            r_ans_text.font.color.rgb = RGBColor(30, 41, 59)

            # Check if answer contains code or commands
            lines = answer.split("\n")
            for line in lines:
                if line.strip().startswith("$") or line.strip().startswith("docker") or line.strip().startswith("git") or line.strip().startswith("mvn") or line.strip().startswith("kubectl"):
                    # Format as monospaced
                    pass

    for p in docx_paths:
        doc.save(p)
        print(f"Saved viva docx to: {p}")

def export_viva_markdown(md_path):
    topics = [
        ("Topic 1: Git & GitHub — Version Control & Collaboration", GIT_QUESTIONS),
        ("Topic 2: Apache Maven & Eclipse IDE Build Automation", MAVEN_QUESTIONS),
        ("Topic 3: Docker Engine & Container CLI Architecture", DOCKER_CLI_QUESTIONS),
        ("Topic 4: Docker Compose & Dockerfile Multi-Container Systems", COMPOSE_QUESTIONS),
        ("Topic 5: Jenkins CI/CD Automation & Pipelines", JENKINS_QUESTIONS),
        ("Topic 6: Kubernetes & Minikube Container Orchestration", K8S_QUESTIONS),
        ("Topic 7: Nagios Infrastructure & Service Monitoring", NAGIOS_QUESTIONS),
        ("Topic 8: AWS EC2 & Cloud Infrastructure Deployment", AWS_QUESTIONS),
    ]

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# DevOps & Software Engineering Comprehensive Viva Guide\n")
        f.write("### 400 Technical Questions & In-Depth Explanations Across All 8 Core Syllabus Topics\n")
        f.write("#### KMIT Lab Internal II — Software Engineering (23CC501PC) · Ubuntu Linux\n\n---\n\n")

        total_q = 0
        for topic_title, questions in topics:
            f.write(f"\n## {topic_title} ({len(questions)} Questions)\n\n")
            for i, (q, a) in enumerate(questions):
                total_q += 1
                f.write(f"### Q{i+1}. {q}\n")
                f.write(f"**Explanation & Answer:**\n\n{a}\n\n---\n\n")

    print(f"Saved Viva Markdown ({total_q} questions) to: {md_path}")

if __name__ == '__main__':
    docx_targets = ["DevOps_SE_Viva_Questions.docx", "Viva_QnA.docx"]
    build_viva_docx(docx_targets)
    export_viva_markdown("Viva_QnA.md")
    print("Viva generation completed successfully!")
