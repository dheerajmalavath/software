"""
Generates a comprehensive Word document (.docx) containing 4 files:
1. Dockerfile for JAR (Spring Boot / Java App)
2. Dockerfile for WAR (Tomcat Web App)
3. docker-compose.yml for JAR (App + MySQL Database)
4. docker-compose.yml for WAR (Tomcat Web App + MySQL Database)
With line-by-line comments detailing WHAT and WHERE content must be modified.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

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

def set_cell_borders(cell, left_color="2563EB", left_sz="20", border_color="CBD5E1", border_sz="4"):
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

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.9)

    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F8FAFC") # Light slate 50
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    set_cell_borders(cell, left_color="2563EB", left_sz="24", border_color="CBD5E1", border_sz="4")

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05

    run = p.add_run(code_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(9.0)
    run.font.color.rgb = RGBColor(15, 23, 42)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(6)

def add_callout(doc, title, text, callout_type="info"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.9)

    cell = tbl.cell(0, 0)
    if callout_type == "warning":
        fill = "FFFBEB"
        border_left = "D97706"
        title_color = RGBColor(180, 83, 9)
    else:
        fill = "EFF6FF"
        border_left = "2563EB"
        title_color = RGBColor(29, 78, 216)

    set_cell_background(cell, fill)
    set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
    set_cell_borders(cell, left_color=border_left, left_sz="20", border_color="E2E8F0", border_sz="4")

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

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(6)

def build_document():
    doc = docx.Document()

    for sec in doc.sections:
        sec.top_margin = Inches(0.8)
        sec.bottom_margin = Inches(0.8)
        sec.left_margin = Inches(0.8)
        sec.right_margin = Inches(0.8)

    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(10)
    normal.font.color.rgb = RGBColor(30, 41, 59)
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(4)

    # Document Cover / Header
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(20)
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("Docker & Docker Compose Blueprint Guide")
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(24)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(27, 54, 93)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("Complete Reference for JAR & WAR Deployments with Annotated In-File Modification Guides")
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(71, 85, 105)

    # Metadata Table
    meta = [
        ("Course & Subject", "Software Engineering Lab — 23CC501PC (DevOps Practicals)"),
        ("Target System", "Ubuntu Linux (or Git Bash on Windows)"),
        ("Files Included", "2 Dockerfiles (JAR, WAR) & 2 docker-compose.yml files (JAR, WAR)"),
        ("Key Feature", "Comprehensive inline comments detailing WHAT to change & WHERE to find values")
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

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(10)

    add_callout(
        doc,
        "HOW TO USE THIS BLUEPRINT",
        "Before copying any file, check your project's 'pom.xml' file: "
        "if '<packaging>war</packaging>' is present, use the WAR templates; "
        "if '<packaging>jar</packaging>' is present (or packaging is omitted), use the JAR templates. "
        "Each template contains detailed comment headers pointing directly to the file and line number in your repository where the correct value resides.",
        "info"
    )

    # =========================================================================
    # QUICK REFERENCE TABLE: WHERE TO LOOK IN YOUR REPOSITORY
    # =========================================================================
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(14)
    p_h1.paragraph_format.space_after = Pt(4)
    p_h1.paragraph_format.keep_with_next = True
    r_h1 = p_h1.add_run("Quick Reference: Where to Find Values in Your Repository")
    r_h1.font.name = 'Arial'
    r_h1.font.size = Pt(14)
    r_h1.font.bold = True
    r_h1.font.color.rgb = RGBColor(27, 54, 93)

    ref_headers = ["Parameter / Value", "Where to Look in Repo", "Command to Inspect (Ubuntu/Bash)", "Example Found Value"]
    ref_data = [
        ["Packaging Type (WAR vs JAR)", "pom.xml (<packaging> tag)", "cat pom.xml | grep '<packaging>'", "<packaging>war</packaging>"],
        ["Artifact File Name", "target/ directory after build", "ls -la target/*.war target/*.jar", "target/ticket-reservation.war"],
        ["Java Runtime Version", "pom.xml (<java.version> / compiler plugin)", "cat pom.xml | grep -E 'source|target|java.version'", "<target>17</target> → use JDK 17"],
        ["App Internal Port", "application.properties or server default", "cat src/main/resources/application.properties", "server.port=8080 (Tomcat default: 8080)"],
        ["Database Name", "application.properties (datasource URL)", "grep -i 'jdbc:mysql' src/main/resources/*", "jdbc:mysql://localhost:3306/oltrsdb"],
        ["Database Username", "application.properties (datasource username)", "grep -i 'username' src/main/resources/*", "spring.datasource.username=root"],
        ["Database Password", "application.properties (datasource password)", "grep -i 'password' src/main/resources/*", "spring.datasource.password=root123"],
        ["External Host Port", "Question Paper", "Check assigned question text", "9090 (or 8080)"]
    ]

    tbl_ref = doc.add_table(rows=len(ref_data) + 1, cols=4)
    tbl_ref.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ref.autofit = False
    col_widths = [1.6, 2.0, 2.0, 1.3]
    for c_i, w in enumerate(col_widths):
        tbl_ref.columns[c_i].width = Inches(w)

    for c_i, h in enumerate(ref_headers):
        c = tbl_ref.rows[0].cells[c_i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=60, bottom=60, left=80, right=80)
        set_cell_borders(c, left_color="CBD5E1", left_sz="4", border_color="CBD5E1", border_sz="4")
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    for r_i, row in enumerate(ref_data):
        bg = "F8FAFC" if r_i % 2 == 1 else "FFFFFF"
        for c_i, val in enumerate(row):
            c = tbl_ref.rows[r_i + 1].cells[c_i]
            set_cell_background(c, bg)
            set_cell_margins(c, top=50, bottom=50, left=80, right=80)
            set_cell_borders(c, left_color="E2E8F0", left_sz="4", border_color="E2E8F0", border_sz="4")
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGBColor(15, 23, 42)

    p_sp2 = doc.add_paragraph()
    p_sp2.paragraph_format.space_after = Pt(12)

    # =========================================================================
    # FILE 1: DOCKERFILE FOR JAR (JAVA / SPRING BOOT)
    # =========================================================================
    doc.add_page_break()

    p_f1 = doc.add_paragraph()
    p_f1.paragraph_format.space_before = Pt(12)
    p_f1.paragraph_format.space_after = Pt(4)
    p_f1.paragraph_format.keep_with_next = True
    r_f1 = p_f1.add_run("File 1: Dockerfile for JAR (Spring Boot / Standalone Java App)")
    r_f1.font.name = 'Arial'
    r_f1.font.size = Pt(15)
    r_f1.font.bold = True
    r_f1.font.color.rgb = RGBColor(27, 54, 93)

    p_f1_desc = doc.add_paragraph()
    p_f1_desc.paragraph_format.space_after = Pt(4)
    p_f1_desc.add_run(
        "Use this Dockerfile when your project's pom.xml has <packaging>jar</packaging> or has no packaging declared. "
        "It uses a lightweight OpenJDK Alpine runtime, sets up an isolated working directory, copies the compiled JAR package, "
        "and defines the container entrypoint."
    )

    dockerfile_jar_code = """# =============================================================================
# FILE: Dockerfile (FOR JAR / SPRING BOOT APPLICATIONS)
# =============================================================================

# -----------------------------------------------------------------------------
# LINE 1: BASE IMAGE
# -----------------------------------------------------------------------------
# WHAT TO CHANGE: Match the Java version specified in your project's pom.xml.
# WHERE TO LOOK : In pom.xml, look for:
#                 <properties><java.version>17</java.version></properties>
#                 or <maven-compiler-plugin><source>17</source></maven-compiler-plugin>
# CHOICES       : 
#   - For Java 17: FROM eclipse-temurin:17-jdk-alpine  (or openjdk:17-jdk-slim)
#   - For Java 11: FROM eclipse-temurin:11-jdk-alpine
#   - For Java 8 : FROM openjdk:8-jdk-alpine
FROM eclipse-temurin:17-jdk-alpine

# -----------------------------------------------------------------------------
# LINE 2: WORKING DIRECTORY
# -----------------------------------------------------------------------------
# WHAT IT DOES  : Creates and sets '/app' as the current directory inside container.
# NOTE          : Usually no change needed. Standard convention is /app.
WORKDIR /app

# -----------------------------------------------------------------------------
# LINE 3: COPY JAR ARTIFACT INTO CONTAINER
# -----------------------------------------------------------------------------
# WHAT TO CHANGE: Path to the built JAR file.
# WHERE TO LOOK : Run 'mvn clean package -DskipTests' first, then run 'ls target/*.jar'.
# PRO-TIP       : Using wildcard 'target/*.jar app.jar' guarantees you NEVER get a
#                 filename error if the version or artifactId changes!
# SYNTAX        : COPY <host-path> <container-path>
COPY target/*.jar app.jar

# -----------------------------------------------------------------------------
# LINE 4: EXPOSED PORT
# -----------------------------------------------------------------------------
# WHAT TO CHANGE: The port your Spring Boot app listens on internally.
# WHERE TO LOOK : In 'src/main/resources/application.properties':
#                 look for 'server.port=8080'. If not specified, default is 8080.
# NOTE          : For Spring Boot default is 8080; for Python Flask use 5000.
EXPOSE 8080

# -----------------------------------------------------------------------------
# LINE 5: STARTUP COMMAND (ENTRYPOINT)
# -----------------------------------------------------------------------------
# WHAT IT DOES  : Executes the JAR file using the Java Virtual Machine on startup.
# NOTE          : No change needed if you renamed the target to 'app.jar' in COPY line.
ENTRYPOINT ["java", "-jar", "app.jar"]
"""
    add_code_block(doc, dockerfile_jar_code)

    p_f1_cli = doc.add_paragraph()
    p_f1_cli.paragraph_format.space_before = Pt(4)
    p_f1_cli.paragraph_format.space_after = Pt(2)
    r_cli1 = p_f1_cli.add_run("Ubuntu Terminal Execution Commands for File 1:")
    r_cli1.font.bold = True
    r_cli1.font.color.rgb = RGBColor(2, 132, 199)

    add_code_block(doc, """# Step 1: Create the Dockerfile using nano in project root
nano Dockerfile
# (Paste the content above. Save: Ctrl+O, Enter, Ctrl+X)

# Step 2: Build the JAR package with Maven
mvn clean package -DskipTests

# Step 3: Build the Docker image
docker build -t my-jar-app:latest .

# Step 4: Run the standalone container on port 9090
docker run -d --name my-jar-container -p 9090:8080 my-jar-app:latest

# Step 5: Verify container is running and test in browser
docker ps
curl -I http://localhost:9090""")

    # =========================================================================
    # FILE 2: DOCKERFILE FOR WAR (TOMCAT WEB APPLICATION)
    # =========================================================================
    doc.add_page_break()

    p_f2 = doc.add_paragraph()
    p_f2.paragraph_format.space_before = Pt(12)
    p_f2.paragraph_format.space_after = Pt(4)
    p_f2.paragraph_format.keep_with_next = True
    r_f2 = p_f2.add_run("File 2: Dockerfile for WAR (Tomcat Web Application)")
    r_f2.font.name = 'Arial'
    r_f2.font.size = Pt(15)
    r_f2.font.bold = True
    r_f2.font.color.rgb = RGBColor(27, 54, 93)

    p_f2_desc = doc.add_paragraph()
    p_f2_desc.paragraph_format.space_after = Pt(4)
    p_f2_desc.add_run(
        "Use this Dockerfile when your project's pom.xml has <packaging>war</packaging>. "
        "It uses Apache Tomcat 9, purges default sample applications, deploys your WAR file as ROOT.war "
        "(so the application loads at the website root / without typing a subpath), and starts catalina server."
    )

    dockerfile_war_code = """# =============================================================================
# FILE: Dockerfile (FOR WAR / APACHE TOMCAT WEB APPLICATIONS)
# =============================================================================

# -----------------------------------------------------------------------------
# LINE 1: BASE IMAGE
# -----------------------------------------------------------------------------
# WHAT TO CHANGE: Apache Tomcat base image version.
# WHERE TO LOOK : In pom.xml, verify: <packaging>war</packaging>.
# CHOICES       : 
#   - For standard exam labs: FROM tomcat:9.0-jdk11-openjdk-slim
#   - Or simple tag         : FROM tomcat:9.0
#   - For modern Jakarta EE : FROM tomcat:10.1-jdk17
FROM tomcat:9.0-jdk11-openjdk-slim

# -----------------------------------------------------------------------------
# LINE 2: MAINTAINER LABEL (OPTIONAL)
# -----------------------------------------------------------------------------
# WHAT TO CHANGE: Set to your name or student ID.
LABEL maintainer="dheerajmalavath"

# -----------------------------------------------------------------------------
# LINE 3: REMOVE DEFAULT TOMCAT SAMPLE APPS
# -----------------------------------------------------------------------------
# WHAT IT DOES  : Deletes default manager, docs, and ROOT folders from webapps.
# WHY IT MATTERS: Prevents default Tomcat welcome page from conflicting with your app.
# NOTE          : Keep this line unchanged.
RUN rm -rf /usr/local/tomcat/webapps/*

# -----------------------------------------------------------------------------
# LINE 4: COPY WAR ARTIFACT INTO TOMCAT WEBAPPS
# -----------------------------------------------------------------------------
# WHAT TO CHANGE: Path to the built WAR file.
# WHERE TO LOOK : Run 'mvn clean package -DskipTests' first, then 'ls target/*.war'.
# PRO-TIP       : Always copy as 'ROOT.war'!
#                 When named 'ROOT.war', Tomcat automatically deploys your app to
#                 the root URL: 'http://localhost:9090/' (no subpath needed!).
#                 Using wildcard 'target/*.war' prevents any filename typos.
COPY target/*.war /usr/local/tomcat/webapps/ROOT.war

# -----------------------------------------------------------------------------
# LINE 5: EXPOSED PORT
# -----------------------------------------------------------------------------
# WHAT IT DOES  : Documents internal port Tomcat listens on.
# NOTE          : Always 8080 for Apache Tomcat. Do NOT change this line.
EXPOSE 8080

# -----------------------------------------------------------------------------
# LINE 6: STARTUP COMMAND
# -----------------------------------------------------------------------------
# WHAT IT DOES  : Starts Tomcat catalina servlet engine in the foreground.
# NOTE          : Keep this line unchanged.
CMD ["catalina.sh", "run"]
"""
    add_code_block(doc, dockerfile_war_code)

    p_f2_cli = doc.add_paragraph()
    p_f2_cli.paragraph_format.space_before = Pt(4)
    p_f2_cli.paragraph_format.space_after = Pt(2)
    r_cli2 = p_f2_cli.add_run("Ubuntu Terminal Execution Commands for File 2:")
    r_cli2.font.bold = True
    r_cli2.font.color.rgb = RGBColor(2, 132, 199)

    add_code_block(doc, """# Step 1: Create the Dockerfile using nano in project root
nano Dockerfile
# (Paste the content above. Save: Ctrl+O, Enter, Ctrl+X)

# Step 2: Build the WAR package with Maven
mvn clean package -DskipTests

# Step 3: Verify the WAR file exists inside target/
ls -la target/*.war

# Step 4: Build the Docker image
docker build -t my-war-app:latest .

# Step 5: Run the standalone container mapping host port 9090 to Tomcat 8080
docker run -d --name my-war-container -p 9090:8080 my-war-app:latest

# Step 6: Verify container is running and check logs
docker ps
docker logs -f my-war-container""")

    # =========================================================================
    # FILE 3: DOCKER-COMPOSE.YML FOR JAR (APP + MYSQL DATABASE)
    # =========================================================================
    doc.add_page_break()

    p_f3 = doc.add_paragraph()
    p_f3.paragraph_format.space_before = Pt(12)
    p_f3.paragraph_format.space_after = Pt(4)
    p_f3.paragraph_format.keep_with_next = True
    r_f3 = p_f3.add_run("File 3: docker-compose.yml for JAR (Spring Boot App + MySQL)")
    r_f3.font.name = 'Arial'
    r_f3.font.size = Pt(15)
    r_f3.font.bold = True
    r_f3.font.color.rgb = RGBColor(27, 54, 93)

    p_f3_desc = doc.add_paragraph()
    p_f3_desc.paragraph_format.space_after = Pt(4)
    p_f3_desc.add_run(
        "Use this docker-compose.yml when running a Spring Boot JAR application alongside a MySQL database. "
        "It sets up automatic container building, connects both services to an isolated bridge network, "
        "configures Spring Datasource environment variables, and creates a persistent volume for database schemas."
    )

    compose_jar_code = """# =============================================================================
# FILE: docker-compose.yml (FOR JAR / SPRING BOOT + MYSQL DATABASE)
# =============================================================================

version: '3.8'

services:
  # ===========================================================================
  # SERVICE 1: SPRING BOOT APPLICATION CONTAINER
  # ===========================================================================
  app:
    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: 'build: .' uses the Dockerfile in the current directory.
    # NOTE          : Keep as '.' unless your Dockerfile is in a subdirectory.
    # -------------------------------------------------------------------------
    build: .

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Container name for easier CLI querying.
    # WHERE TO LOOK : Set to your project name (e.g. library-app, ticket-app).
    # -------------------------------------------------------------------------
    container_name: spring-boot-app

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Port mapping "HostPort:ContainerPort"
    # WHERE TO LOOK : 
    #   - HostPort      : Given in question paper (e.g. 9090 or 8080).
    #   - ContainerPort : Set in application.properties (server.port=8080).
    # -------------------------------------------------------------------------
    ports:
      - "9090:8080"

    # -------------------------------------------------------------------------
    # WHAT IT DOES  : Ensures the database container starts BEFORE the app container.
    # -------------------------------------------------------------------------
    depends_on:
      - db

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Database connection credentials injected into Spring Boot.
    # WHERE TO LOOK : In 'src/main/resources/application.properties':
    #                 look for spring.datasource.url, username, password.
    # CRITICAL RULE : In the URL 'jdbc:mysql://db:3306/...', the host MUST be 'db'
    #                 (matching the database service name below, NOT localhost!).
    # -------------------------------------------------------------------------
    environment:
      # Database connection URL: db is the service name, 3306 is MySQL internal port, appdb is DB name
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/appdb?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC
      # Database username: MUST match MYSQL_USER or root below
      SPRING_DATASOURCE_USERNAME: root
      # Database password: MUST match MYSQL_ROOT_PASSWORD below
      SPRING_DATASOURCE_PASSWORD: root123
      # JPA / Hibernate auto table generation (optional but helpful in lab exams)
      SPRING_JPA_HIBERNATE_DDL_AUTO: update

    # -------------------------------------------------------------------------
    # RESTART POLICY: Restarts container if it crashes (e.g. if DB takes time to boot).
    # -------------------------------------------------------------------------
    restart: always

    networks:
      - app-net

  # ===========================================================================
  # SERVICE 2: MYSQL DATABASE CONTAINER
  # ===========================================================================
  db:
    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: MySQL image version (usually mysql:8.0 or mysql:5.7).
    # -------------------------------------------------------------------------
    image: mysql:8.0

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Container name for database.
    # -------------------------------------------------------------------------
    container_name: spring-boot-db

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: MySQL initialization environment variables.
    # WHERE TO LOOK : In 'src/main/resources/application.properties'.
    # -------------------------------------------------------------------------
    environment:
      # Root superuser password
      MYSQL_ROOT_PASSWORD: root123
      # Initial database schema to automatically create on first startup
      MYSQL_DATABASE: appdb
      # Optional standard user credentials
      MYSQL_USER: appuser
      MYSQL_PASSWORD: apppass

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: External host port for accessing MySQL from host (e.g. DBeaver).
    # PRO-TIP       : Map host port to 3307 ("3307:3306") so it never conflicts
    #                 if MySQL is already running natively on Ubuntu host port 3306!
    # -------------------------------------------------------------------------
    ports:
      - "3307:3306"

    # -------------------------------------------------------------------------
    # WHAT IT DOES  : Named volume to persist database records on disk.
    # NOTE          : Keep '/var/lib/mysql' unchanged (MySQL's internal data directory).
    # -------------------------------------------------------------------------
    volumes:
      - db-data:/var/lib/mysql

    restart: always

    networks:
      - app-net

# =============================================================================
# VOLUMES: PERSISTENT STORAGE DECLARATION
# =============================================================================
volumes:
  # Named volume created on host filesystem (/var/lib/docker/volumes/...)
  db-data:

# =============================================================================
# NETWORKS: INTER-CONTAINER BRIDGE NETWORK
# =============================================================================
networks:
  app-net:
    driver: bridge
"""
    add_code_block(doc, compose_jar_code)

    p_f3_cli = doc.add_paragraph()
    p_f3_cli.paragraph_format.space_before = Pt(4)
    p_f3_cli.paragraph_format.space_after = Pt(2)
    r_cli3 = p_f3_cli.add_run("Ubuntu Terminal Execution Commands for File 3:")
    r_cli3.font.bold = True
    r_cli3.font.color.rgb = RGBColor(2, 132, 199)

    add_code_block(doc, """# Step 1: Create docker-compose.yml using nano in project root
nano docker-compose.yml
# (Paste the content above. Save: Ctrl+O, Enter, Ctrl+X)

# Step 2: Build images and start all containers in detached background mode
docker compose up --build -d

# Step 3: Check status of all running services
docker compose ps

# Step 4: Follow live logs of the app service to verify DB connection
docker compose logs -f app

# Step 5: Tear down containers and networks (preserving DB volume data)
docker compose down

# Step 6: Tear down containers, networks, AND purge DB volume completely
docker compose down -v""")

    # =========================================================================
    # FILE 4: DOCKER-COMPOSE.YML FOR WAR (TOMCAT WEB APP + MYSQL)
    # =========================================================================
    doc.add_page_break()

    p_f4 = doc.add_paragraph()
    p_f4.paragraph_format.space_before = Pt(12)
    p_f4.paragraph_format.space_after = Pt(4)
    p_f4.paragraph_format.keep_with_next = True
    r_f4 = p_f4.add_run("File 4: docker-compose.yml for WAR (Tomcat Web App + MySQL)")
    r_f4.font.name = 'Arial'
    r_f4.font.size = Pt(15)
    r_f4.font.bold = True
    r_f4.font.color.rgb = RGBColor(27, 54, 93)

    p_f4_desc = doc.add_paragraph()
    p_f4_desc.paragraph_format.space_after = Pt(4)
    p_f4_desc.add_run(
        "Use this docker-compose.yml when deploying a Java Web Application (WAR) on Apache Tomcat alongside a MySQL database. "
        "This configuration matches the majority of Lab Exam Sets (SET 2, 3, 4, 7, 8, 9) and passes DB_HOST, DB_NAME, DB_USER, "
        "and DB_PASS environment variables directly into the Tomcat runtime."
    )

    compose_war_code = """# =============================================================================
# FILE: docker-compose.yml (FOR WAR / TOMCAT WEB APP + MYSQL DATABASE)
# =============================================================================

version: '3.8'

services:
  # ===========================================================================
  # SERVICE 1: TOMCAT WEB APPLICATION CONTAINER
  # ===========================================================================
  app:
    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: 'build: .' builds the Dockerfile located in current folder.
    # NOTE          : Ensure the WAR Dockerfile (File 2) exists in this directory.
    # -------------------------------------------------------------------------
    build: .

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Name of the app container.
    # WHERE TO LOOK : Set to the project name (e.g. oltrs-app, hospital-app, cems-app).
    # -------------------------------------------------------------------------
    container_name: oltrs-web-app

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Port mapping "HostPort:ContainerPort"
    # WHERE TO LOOK : 
    #   - HostPort      : Port specified in the question paper (e.g. 9090 or 8080).
    #   - ContainerPort : Internal Tomcat port (always 8080).
    # -------------------------------------------------------------------------
    ports:
      - "9090:8080"

    # -------------------------------------------------------------------------
    # WHAT IT DOES  : Starts the database before launching Tomcat.
    # -------------------------------------------------------------------------
    depends_on:
      - db

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Environment variables consumed by DB connection pool / servlets.
    # WHERE TO LOOK : In 'src/main/resources/application.properties' or DB class:
    #   - DB_HOST : MUST match the MySQL service name declared below ('db').
    #   - DB_NAME : Database name (e.g. oltrsdb, hospitaldb, cemsdb).
    #   - DB_USER : User name (root or appuser).
    #   - DB_PASS : User password (root123 or apppass).
    # -------------------------------------------------------------------------
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_NAME: oltrsdb
      DB_USER: root
      DB_PASS: root123

    # -------------------------------------------------------------------------
    # RESTART POLICY: Auto-restarts if Tomcat starts before MySQL finishes booting.
    # -------------------------------------------------------------------------
    restart: always

    networks:
      - oltrs-network

  # ===========================================================================
  # SERVICE 2: MYSQL DATABASE CONTAINER
  # ===========================================================================
  db:
    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: MySQL image version (mysql:8.0 is standard for all 9 sets).
    # -------------------------------------------------------------------------
    image: mysql:8.0

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Container name for database.
    # -------------------------------------------------------------------------
    container_name: oltrs-mysql-db

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: MySQL root password and database name.
    # WHERE TO LOOK : Check DB configuration in src/main/resources/.
    # -------------------------------------------------------------------------
    environment:
      # Root superuser password
      MYSQL_ROOT_PASSWORD: root123
      # Schema name automatically created on initial launch
      MYSQL_DATABASE: oltrsdb
      # Optional non-root user and password
      MYSQL_USER: appuser
      MYSQL_PASSWORD: apppass

    # -------------------------------------------------------------------------
    # WHAT TO CHANGE: Host port mapping for external database client inspection.
    # PRO-TIP       : Map to host port 3307 to avoid collisions with native MySQL.
    # -------------------------------------------------------------------------
    ports:
      - "3307:3306"

    # -------------------------------------------------------------------------
    # WHAT IT DOES  : Named volume preserving database tables on host disk.
    # -------------------------------------------------------------------------
    volumes:
      - oltrs-dbdata:/var/lib/mysql

    restart: always

    networks:
      - oltrs-network

# =============================================================================
# VOLUMES: PERSISTENT STORAGE DECLARATION
# =============================================================================
volumes:
  oltrs-dbdata:

# =============================================================================
# NETWORKS: INTER-CONTAINER BRIDGE NETWORK
# =============================================================================
networks:
  oltrs-network:
    driver: bridge
"""
    add_code_block(doc, compose_war_code)

    p_f4_cli = doc.add_paragraph()
    p_f4_cli.paragraph_format.space_before = Pt(4)
    p_f4_cli.paragraph_format.space_after = Pt(2)
    r_cli4 = p_f4_cli.add_run("Ubuntu Terminal Execution Commands for File 4:")
    r_cli4.font.bold = True
    r_cli4.font.color.rgb = RGBColor(2, 132, 199)

    add_code_block(doc, """# Step 1: Ensure WAR Dockerfile exists and create docker-compose.yml
nano docker-compose.yml
# (Paste the content above. Save: Ctrl+O, Enter, Ctrl+X)

# Step 2: Build WAR package
mvn clean package -DskipTests

# Step 3: Launch multi-container services with build
docker compose up --build -d

# Step 4: Verify both containers are running (Status: Up)
docker compose ps

# Step 5: Test web application in browser
# Open: http://localhost:9090/
curl -I http://localhost:9090/

# Step 6: View logs of application container
docker compose logs -f app

# Step 7: Stop services without deleting containers
docker compose stop

# Step 8: Clean teardown (preserving database volume)
docker compose down""")

    # Output paths
    output_filename = "Docker_Templates_JAR_WAR.docx"
    doc.save(output_filename)
    print(f"Document saved successfully as: {output_filename}")

    # Also copy to gh_software_tmp for pushing to git
    return output_filename

if __name__ == '__main__':
    build_document()
