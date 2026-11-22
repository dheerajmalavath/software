"""
Main generator script for creating the comprehensive Ubuntu DevOps Cheatsheet Word Document.
"""

from doc_builder_core import CheatsheetDocBuilder

def build_complete_document():
    b = CheatsheetDocBuilder()

    # COVER / HEADER
    b.add_cover(
        title="DevOps & Software Engineering Lab Manual & Cheat Sheet",
        subtitle="Complete Ubuntu (Linux) Practical Reference Guide — Git, Maven, Docker, Jenkins, Kubernetes, Nagios & AWS EC2",
        author="dheerajmalavath",
        metadata_items=[
            ("Subject & Code", "Software Engineering Lab — 23CC501PC (KMIT)"),
            ("Target OS", "Ubuntu Linux (20.04 / 22.04 / 24.04 LTS)"),
            ("Core Focus", "Git/GitHub, Maven with Eclipse, Docker CLI, Compose, Jenkins, Kubernetes, Nagios, AWS EC2"),
            ("Coverage", "Laboratory Internal II Syllabus, Weeks 2 to 8, and Exam Sets 1 through 9"),
            ("Text Editor Used", "nano (Ubuntu terminal standard: Ctrl+O Save, Enter, Ctrl+X Exit)"),
            ("Repository Destination", "https://github.com/dheerajmalavath/software")
        ]
    )

    b.add_callout(
        "CRITICAL UBUNTU LINUX ENVIRONMENT DIRECTIVE",
        "All instructions, paths, environment variables, and commands in this manual are strictly engineered for Ubuntu (Linux). "
        "Do NOT use Windows commands such as 'notepad', 'dir', 'icacls', or backslashes. "
        "In Ubuntu, use 'nano' or 'vim' for file editing, 'ls -la' for listing files, 'chmod 400' for key permissions, "
        "and standard Linux forward slashes (/) for all directory paths.",
        "warning"
    )

    # =========================================================================
    # MODULE 0: MASTER BLUEPRINT — WHAT TO MODIFY & WHERE TO FIND NAMES
    # =========================================================================
    b.add_h1("0. Master Blueprint — Configuration Customization & Value Discovery")
    b.add_paragraph(
        "In the practical laboratory exam and real-world DevOps workflows, every question paper provides a specific application repository "
        "and port requirement. This section details the 3 golden places where parameters are identified and explains exactly which configuration "
        "lines must be modified across Dockerfile, docker-compose.yml, Jenkinsfile, and Kubernetes YAML files."
    )

    b.add_h2("0.1 The 3 Golden Places to Find Your Values in Ubuntu")
    b.add_step(
        "Step 1: Inspect the Project Root Directory and pom.xml to identify packaging type (WAR vs JAR), output artifact name, and dependencies.",
        "cd ~/projects/my-app\n"
        "cat pom.xml | grep -E '<packaging>|<artifactId>|<version>|<finalName>'\n"
        "ls -la src/main/resources/application.properties 2>/dev/null || ls -la src/main/resources/",
        "Output displays: <packaging>war</packaging>, artifactId, and MySQL connection credentials (username, password, DB name) inside application.properties.",
        "If <packaging> is omitted in pom.xml, Maven defaults to jar packaging. If it says war, Tomcat base image is required."
    )

    b.add_step(
        "Step 2: Read the Question Paper for specific GitHub URLs and Host Port numbers.",
        "# Identify given parameters from question paper:\n"
        "# Example Repo URL: https://github.com/archanareddyse/OLTRS.git\n"
        "# Assigned Host Port: 9090 (or 8080)\n"
        "# Database Name: oltrsdb, User: root, Password: root123",
        "Parameters mapped: HostPort=9090, ContainerPort=8080 (for Tomcat) or 5000 (for Flask)."
    )

    b.add_step(
        "Step 3: Check Local Machine Ports in Ubuntu to prevent 'port already allocated' bind errors.",
        "sudo netstat -tuln | grep -E '8080|9090|3306|3307|9080|8090'\n"
        "# Alternative using ss:\n"
        "ss -tulpn | grep 9090",
        "If a port is already occupied by a background process, pick an alternative (e.g. 9090 instead of 8080, 3307 instead of 3306) or kill the offending process using: sudo kill -9 <PID>."
    )

    b.add_h2("0.2 File-by-File Modification Rules")
    b.add_paragraph("Summary of exact lines to update when adapting templates to your assigned exam set:")
    b.add_table(
        headers=["File Name", "Target Line / Parameter", "How to Determine Value in Ubuntu"],
        data=[
            ["Dockerfile", "FROM <base-image>", "Look at <packaging> in pom.xml: if 'war' use tomcat:9.0; if 'jar' use eclipse-temurin:17-jdk."],
            ["Dockerfile", "COPY target/*.war ...", "Use wildcard '*.war' so you never encounter exact filename mismatch errors."],
            ["Dockerfile", "EXPOSE <port>", "8080 for Tomcat / Spring Boot, 5000 for Python Flask, 80 for Nginx."],
            ["docker-compose.yml", "container_name: <name>", "Set to project name (e.g. oltrs-app, library-app)."],
            ["docker-compose.yml", "ports: - 'HostPort:ContainerPort'", "Map host port from question paper (e.g. '9090:8080')."],
            ["docker-compose.yml", "environment: DB_HOST: db", "MUST match database service name declared under 'services:'."],
            ["Jenkinsfile", "git url: '...', branch: 'main'", "Copy exact GitHub repository URL and default branch ('main' or 'master')."],
            ["Jenkinsfile", "def mvnHome = tool 'Maven'", "Must match tool name defined in Jenkins → Manage Jenkins → Tools → Maven."],
            ["Jenkinsfile", "docker build -t <user>/<repo>:latest .", "Use your personal Docker Hub username for tagging."],
            ["deployment.yaml", "image: <username>/<image>:tag", "Provide public Docker Hub image pushed from your Jenkins or local build."],
            ["deployment.yaml", "replicas: 4", "Exam standard requires 4 replicas for high availability and auto-healing."],
            ["service.yaml", "type: NodePort", "Exposes pod to host browser within port range 30000–32767."]
        ],
        col_widths=[1.5, 2.2, 3.2]
    )

    # =========================================================================
    # MODULE 1: GIT & GITHUB (UBUNTU LINUX)
    # =========================================================================
    b.add_h1("1. Git & GitHub — Version Control & Collaboration in Ubuntu")
    b.add_paragraph(
        "Git is a distributed version control system that tracks changes in source code across development teams. "
        "GitHub provides cloud-hosted remote repositories, collaboration tools, pull requests, issue tracking, and webhooks."
    )

    b.add_h2("1.1 Installing and Configuring Git on Ubuntu")
    b.add_step(
        "Update the Ubuntu package index and install Git CLI.",
        "sudo apt update && sudo apt install -y git",
        "git version 2.34.1 (or higher installed successfully)."
    )
    b.add_step(
        "Configure your global Git author identity (Name and Email) and set default branch to main.",
        "git config --global user.name \"dheerajmalavath\"\n"
        "git config --global user.email \"dheerajmalavath@gmail.com\"\n"
        "git config --global init.defaultBranch main\n"
        "git config --list --show-origin",
        "Displays global configuration with author name, email, and defaultBranch=main."
    )

    b.add_h2("1.2 Setting Up SSH Key Authentication for GitHub on Ubuntu")
    b.add_paragraph(
        "GitHub deprecated password authentication for Git operations. Setting up an SSH key allows secure, frictionless "
        "cloning, pushing, and pulling without typing credentials repeatedly."
    )
    b.add_step(
        "Generate an ED25519 SSH Key Pair and display public key in Ubuntu terminal.",
        "ssh-keygen -t ed25519 -C \"dheerajmalavath@gmail.com\" -f ~/.ssh/id_ed25519 -N \"\"\n"
        "cat ~/.ssh/id_ed25519.pub",
        "Public key starting with 'ssh-ed25519 AAAAC3NzaC1...' is output to terminal. Copy this key string."
    )
    b.add_step(
        "Add key to GitHub and test SSH connection.",
        "# Step 1: Open GitHub in browser -> Settings -> SSH and GPG keys -> New SSH key\n"
        "# Step 2: Paste the copied key and click 'Add SSH key'\n"
        "# Step 3: Test connection from Ubuntu terminal:\n"
        "ssh -T git@github.com",
        "Hi dheerajmalavath! You've successfully authenticated, but GitHub does not provide shell access."
    )

    b.add_h2("1.3 Local Repository Lifecycle: Init, Staging, Committing, and History")
    b.add_step(
        "Initialize a new Git repository in a project directory.",
        "mkdir -p ~/projects/devops-lab && cd ~/projects/devops-lab\n"
        "git init",
        "Initialized empty Git repository in /home/user/projects/devops-lab/.git/"
    )
    b.add_step(
        "Create sample project files using Ubuntu nano editor.",
        "nano README.md\n"
        "# Type: # DevOps Practice Project\n"
        "# Save in nano: Press Ctrl+O, hit Enter, then Ctrl+X to exit.\n"
        "nano app.py\n"
        "# Type: print('DevOps Pipeline Active')\n"
        "# Save in nano: Ctrl+O, Enter, Ctrl+X",
        "Files README.md and app.py created on disk."
    )
    b.add_step(
        "Check status and stage changes into index.",
        "git status\n"
        "git add README.md app.py\n"
        "# Or stage all files in current directory:\n"
        "git add .",
        "Changes to be committed: new file: README.md, new file: app.py (shown in green)."
    )
    b.add_step(
        "Commit staged changes with a descriptive message.",
        "git commit -m \"feat: initial project structure with README and app entrypoint\"",
        "[main (root-commit) 4a8b1c2] feat: initial project structure with README and app entrypoint\n 2 files changed, 2 insertions(+)"
    )
    b.add_step(
        "Inspect commit history in concise one-line graph view.",
        "git log --oneline --graph --decorate",
        "* 4a8b1c2 (HEAD -> main) feat: initial project structure with README and app entrypoint"
    )

    b.add_h2("1.4 Undoing Changes, Restoring Files, and Resetting")
    b.add_step(
        "Discard uncommitted changes in the working tree (before staging).",
        "# Suppose you edited app.py and made a mistake:\n"
        "git restore app.py",
        "Working directory cleaned; app.py restored to state of last commit."
    )
    b.add_step(
        "Unstage a file that was accidentally staged with git add.",
        "git add app.py\n"
        "git restore --staged app.py",
        "app.py is removed from staging area while keeping modifications in working tree."
    )
    b.add_step(
        "Amend the most recent commit message or include forgotten files.",
        "git commit --amend -m \"feat: initial project setup with updated documentation\"",
        "The previous commit hash is replaced with the new updated commit message."
    )
    b.add_step(
        "Stash working changes temporarily when switching branches.",
        "git stash\n"
        "git stash list\n"
        "# Restore stashed changes later:\n"
        "git stash pop",
        "Saved working directory and index state WIP on main; restored cleanly with pop."
    )

    b.add_h2("1.5 Remote Repository Management: Remote, Push, Pull, and Fetch")
    b.add_step(
        "Connect local Ubuntu repository to a remote GitHub repository.",
        "git remote add origin https://github.com/dheerajmalavath/software.git\n"
        "git remote -v",
        "origin  https://github.com/dheerajmalavath/software.git (fetch)\norigin  https://github.com/dheerajmalavath/software.git (push)"
    )
    b.add_step(
        "Push local branch to remote repository with upstream tracking.",
        "git branch -M main\n"
        "git push -u origin main",
        "Branch 'main' set up to track remote branch 'main' from 'origin'. Everything up-to-date."
    )
    b.add_step(
        "Fetch remote updates and inspect remote tracking branches without merging.",
        "git fetch origin\n"
        "git branch -r\n"
        "git remote show origin",
        "Lists remote branches: origin/main, origin/dev. Shows HEAD branch and push/pull URLs."
    )
    b.add_step(
        "Pull remote updates (fetches and merges into current branch).",
        "git pull origin main",
        "Fast-forward merge or Already up to date."
    )

    b.add_h2("1.6 Branching, Merging, and Conflict Resolution")
    b.add_step(
        "Create and switch to a new feature branch in Ubuntu.",
        "git checkout -b feature-login\n"
        "# Or using modern switch command:\n"
        "# git switch -c feature-login\n"
        "git branch",
        "Lists branches with asterisk on current: * feature-login, main."
    )
    b.add_step(
        "Simulate work on feature branch and commit.",
        "echo \"def login(): return True\" >> app.py\n"
        "git commit -am \"feat: implement login authentication function\"",
        "[feature-login 8f2d3a1] feat: implement login authentication function\n 1 file changed, 1 insertion(+)"
    )
    b.add_step(
        "Switch back to main and merge feature branch.",
        "git switch main\n"
        "git merge feature-login",
        "Updating 4a8b1c2..8f2d3a1\nFast-forward\n app.py | 1 +\n 1 file changed, 1 insertion(+)"
    )
    b.add_step(
        "Resolving Merge Conflicts step-by-step in Ubuntu.",
        "# When both branches modify the same line:\n"
        "# 1. Attempt merge: git merge feature-branch\n"
        "# Output: CONFLICT (content): Merge conflict in app.py. Automatic merge failed.\n"
        "# 2. Open conflicting file with nano:\n"
        "nano app.py\n"
        "# You will see conflict markers:\n"
        "# <<<<<<< HEAD\n"
        "# print('Main Version')\n"
        "# =======\n"
        "# print('Feature Version')\n"
        "# >>>>>>> feature-branch\n"
        "# 3. Manually edit file to keep the desired code and delete markers.\n"
        "# 4. Save file: Ctrl+O, Enter, Ctrl+X.\n"
        "# 5. Stage resolved file and finalize commit:\n"
        "git add app.py\n"
        "git commit -m \"fix: resolve merge conflict between main and feature-branch\"",
        "[main b3c2a10] fix: resolve merge conflict between main and feature-branch"
    )

    b.add_h2("1.7 Collaborative Coding, Patches, and Organizations")
    b.add_step(
        "Generate a Git Patch for code review or offline sharing.",
        "git format-patch -1 HEAD\n"
        "ls -la *.patch",
        "Outputs patch file: 0001-fix-resolve-merge-conflict.patch containing full diff and metadata."
    )
    b.add_step(
        "Apply a Git Patch cleanly on another Ubuntu system.",
        "git apply --check 0001-fix-resolve-merge-conflict.patch\n"
        "git apply 0001-fix-resolve-merge-conflict.patch",
        "Checks for syntax conflicts first (--check); applies cleanly without error."
    )
    b.add_step(
        "Create standard .gitignore file for Ubuntu Java/Maven projects.",
        "nano .gitignore\n"
        "# Paste following lines:\n"
        "target/\n"
        "*.class\n"
        ".project\n"
        ".classpath\n"
        ".settings/\n"
        "*.log\n"
        ".DS_Store\n"
        "# Save: Ctrl+O, Enter, Ctrl+X\n"
        "git add .gitignore && git commit -m \"chore: add standard maven gitignore\"",
        "Build artifacts and IDE temporary files ignored by Git."
    )

    # =========================================================================
    # MODULE 2: MAVEN USING ECLIPSE & UBUNTU CLI
    # =========================================================================
    b.add_page_break()
    b.add_h1("2. Maven Build Automation with Eclipse IDE & Ubuntu CLI")
    b.add_paragraph(
        "Apache Maven is a software project management and comprehension tool based on the Project Object Model (POM). "
        "It standardizes project directory structures, manages external dependencies, compiles source code, runs automated tests, "
        "and packages applications into deployable JAR (Java Archive) or WAR (Web Archive) files."
    )

    b.add_h2("2.1 Maven Standard Directory Architecture")
    b.add_paragraph(
        "Maven enforces a standard folder structure across all Java projects:\n"
        "• src/main/java — Production Java source code (.java files).\n"
        "• src/main/resources — Application properties, XML configs, DB connection settings.\n"
        "• src/main/webapp — Web application root (WEB-INF/web.xml, JSP, HTML, CSS) for WAR projects.\n"
        "• src/test/java — Unit test source code (JUnit test cases).\n"
        "• target/ — Output directory containing compiled .class files, test reports, and final .jar/.war packages.\n"
        "• pom.xml — Root XML configuration declaring GroupId, ArtifactId, Version (GAV), dependencies, and build plugins."
    )

    b.add_h2("2.2 Installing Maven and JDK 17 on Ubuntu")
    b.add_step(
        "Install OpenJDK 17 and Maven via apt.",
        "sudo apt update && sudo apt install -y openjdk-17-jdk maven",
        "Installed openjdk-17 and maven."
    )
    b.add_step(
        "Verify Java compiler and Maven versions.",
        "java -version\n"
        "mvn -version",
        "Apache Maven 3.6.3 (or 3.8.x), Java version: 17.0.x, OS name: Linux, Ubuntu."
    )

    b.add_h2("2.3 Creating Maven Java Project in Eclipse IDE (Step-by-Step UI)")
    b.add_paragraph("Follow these exact steps inside Eclipse IDE on Ubuntu:")
    b.add_table(
        headers=["Step #", "Action in Eclipse IDE UI", "Details / Input Value"],
        data=[
            ["Step 1", "Launch Eclipse IDE", "Select default workspace directory (/home/ubuntu/eclipse-workspace). Click Launch."],
            ["Step 2", "File → New → Other...", "Expand the 'Maven' folder, select 'Maven Project', and click 'Next'."],
            ["Step 3", "Select Project Location", "Leave 'Use default Workspace location' checked. Click 'Next'."],
            ["Step 4", "Choose Archetype", "In Filter box, type 'quickstart'. Select 'org.apache.maven.archetypes : maven-archetype-quickstart (1.4)'. Click 'Next'."],
            ["Step 5", "Specify Project Metadata", "Group Id: 'com.example' | Artifact Id: 'my-java-app' | Version: '1.0-SNAPSHOT' | Package: 'com.example'. Click 'Finish'."],
            ["Step 6", "Confirm Archetype Prompt", "If prompted in Console view with Y/N: type 'Y' and press Enter to confirm archetype generation."],
            ["Step 7", "Verify Project Layout", "Project Explorer displays: src/main/java (with App.java), src/test/java (with AppTest.java), and pom.xml."]
        ],
        col_widths=[1.0, 2.7, 3.2]
    )

    b.add_h2("2.4 Creating Maven Web Project in Eclipse IDE (Webapp Archetype)")
    b.add_paragraph("For web applications deploying to Apache Tomcat (generating WAR files):")
    b.add_table(
        headers=["Step #", "Action in Eclipse IDE UI", "Details / Input Value"],
        data=[
            ["Step 1", "File → New → Other...", "Expand 'Maven' folder, choose 'Maven Project', click 'Next'."],
            ["Step 2", "Select Archetype", "In Filter, type 'webapp'. Select 'org.apache.maven.archetypes : maven-archetype-webapp (1.4)'. Click 'Next'."],
            ["Step 3", "Project Metadata", "Group Id: 'com.example' | Artifact Id: 'my-web-app' | Packaging: 'war'. Click 'Finish'."],
            ["Step 4", "Web Structure Created", "Includes: src/main/webapp/WEB-INF/web.xml and src/main/webapp/index.jsp."]
        ],
        col_widths=[1.0, 2.7, 3.2]
    )

    b.add_h2("2.5 Configuring pom.xml: Dependencies and Compiler Plugins")
    b.add_step(
        "Open pom.xml in Eclipse or Ubuntu nano and add Servlet, MySQL, and Compiler plugin configs.",
        "nano pom.xml\n"
        "# Paste dependencies and build plugins inside <project> tag:\n"
        "<dependencies>\n"
        "  <!-- Java Servlet API for Web Applications -->\n"
        "  <dependency>\n"
        "    <groupId>javax.servlet</groupId>\n"
        "    <artifactId>javax.servlet-api</artifactId>\n"
        "    <version>4.0.1</version>\n"
        "    <scope>provided</scope>\n"
        "  </dependency>\n"
        "  <!-- MySQL Connector/J -->\n"
        "  <dependency>\n"
        "    <groupId>mysql</groupId>\n"
        "    <artifactId>mysql-connector-java</artifactId>\n"
        "    <version>8.0.33</version>\n"
        "  </dependency>\n"
        "  <!-- JUnit 5 Testing -->\n"
        "  <dependency>\n"
        "    <groupId>org.junit.jupiter</groupId>\n"
        "    <artifactId>junit-jupiter-api</artifactId>\n"
        "    <version>5.9.3</version>\n"
        "    <scope>test</scope>\n"
        "  </dependency>\n"
        "</dependencies>\n"
        "\n"
        "<build>\n"
        "  <finalName>my-web-app</finalName>\n"
        "  <plugins>\n"
        "    <!-- Java 17 Compiler Plugin -->\n"
        "    <plugin>\n"
        "      <groupId>org.apache.maven.plugins</groupId>\n"
        "      <artifactId>maven-compiler-plugin</artifactId>\n"
        "      <version>3.11.0</version>\n"
        "      <configuration>\n"
        "        <source>17</source>\n"
        "        <target>17</target>\n"
        "      </configuration>\n"
        "    </plugin>\n"
        "  </plugins>\n"
        "</build>",
        "File saved. In Eclipse: Right-click project → Maven → Update Project (Alt+F5) to force dependency download."
    )

    b.add_h2("2.6 Building and Running Inside Eclipse IDE")
    b.add_paragraph("Eclipse provides built-in run configurations for Maven lifecycles:")
    b.add_table(
        headers=["Build Goal", "How to Trigger in Eclipse UI", "Expected Result"],
        data=[
            ["Maven Clean", "Right-click project/pom.xml → Run As → Maven Clean", "Deletes target/ directory to clear stale artifacts."],
            ["Maven Install", "Right-click project/pom.xml → Run As → Maven Install", "Compiles code, runs tests, packages .war/.jar, copies to ~/.m2/repository."],
            ["Maven Test", "Right-click project/pom.xml → Run As → Maven Test", "Executes all unit tests under src/test/java and prints test reports."],
            ["Custom Maven Build", "Right-click project → Run As → Maven Build... → Enter Goals: 'clean install -DskipTests' → Click Run", "Performs full clean package without failing on test timeouts."],
            ["Run Java App", "Right-click App.java → Run As → Java Application", "Console prints 'Hello World!' or application output."]
        ],
        col_widths=[1.5, 3.2, 2.2]
    )

    b.add_h2("2.7 Maven CLI Operations on Ubuntu Terminal")
    b.add_step(
        "Compile source code and verify target classes.",
        "cd ~/projects/my-web-app\n"
        "mvn compile\n"
        "ls -la target/classes",
        "[INFO] BUILD SUCCESS. Target classes directory populated with .class binaries."
    )
    b.add_step(
        "Build deployable WAR package skipping unit tests for fast exam builds.",
        "mvn clean package -DskipTests\n"
        "ls -la target/*.war",
        "-rw-r--r-- 1 ubuntu ubuntu 15420192 Nov 23 04:30 target/my-web-app.war\n[INFO] BUILD SUCCESS"
    )
    b.add_step(
        "Debug Maven build failures using the -X verbose debug switch.",
        "mvn clean compile -X",
        "Prints full stack trace showing exact dependency resolution and plugin configuration errors."
    )
    b.add_step(
        "Run only a specific failed test case from Ubuntu terminal.",
        "mvn test -Dtest=AppTest#testSpecificMethod",
        "[INFO] Running com.example.AppTest\n[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0"
    )

    # =========================================================================
    # MODULE 3: DOCKER & DOCKER CLI (UBUNTU LINUX)
    # =========================================================================
    b.add_page_break()
    b.add_h1("3. Docker & Docker CLI — Container Management on Ubuntu")
    b.add_paragraph(
        "Docker packages applications and their dependencies into portable containers that execute consistently across all environments. "
        "A Docker Image is an immutable blueprint; a Docker Container is an active, running instance of an image."
    )

    b.add_h2("3.1 Installing Docker Engine and Service Control in Ubuntu")
    b.add_step(
        "Install Docker Engine and grant current user non-root socket permissions.",
        "sudo apt update && sudo apt install -y docker.io\n"
        "sudo systemctl enable docker\n"
        "sudo systemctl start docker\n"
        "sudo usermod -aG docker $USER\n"
        "newgrp docker",
        "Docker daemon started and enabled on boot; docker commands can now run without sudo."
    )
    b.add_step(
        "Verify Docker service status and CLI version in Ubuntu.",
        "sudo systemctl status docker --no-pager\n"
        "docker --version",
        "Active: active (running). Docker version 24.x or 20.x on x86_64 Linux."
    )

    b.add_h2("3.2 Image Management: Pulling, Listing, Inspecting, and Removing")
    b.add_step(
        "Pull standard images from Docker Hub.",
        "docker pull redis:latest\n"
        "docker pull nginx:alpine\n"
        "docker pull mysql:8.0\n"
        "docker pull tomcat:9.0-jdk11-openjdk-slim",
        "Status: Downloaded newer image for redis:latest."
    )
    b.add_step(
        "List all downloaded images with repository, tag, image ID, and size.",
        "docker images",
        "REPOSITORY   TAG       IMAGE ID       CREATED        SIZE\nredis        latest    7f8e9d0a1b2c   2 days ago     117MB\nnginx        alpine    3b4c5d6e7f8a   1 week ago     41MB"
    )
    b.add_step(
        "Inspect low-level image metadata (environment variables, entrypoint, ports).",
        "docker image inspect redis:latest | grep -E '\"ExposedPorts\"|\"Cmd\"'",
        "Displays exposed port 6379/tcp and default command [\"redis-server\"]."
    )
    b.add_step(
        "Remove unused or dangling images to reclaim disk space.",
        "docker rmi redis:latest\n"
        "# Prune all unused images:\n"
        "docker image prune -a -f",
        "Total reclaimed space: 500MB+."
    )

    b.add_h2("3.3 Container Lifecycle: Run, Logs, Exec, Stop, Start, and Kill")
    b.add_step(
        "Run container in detached mode with custom name and port forwarding (HostPort:ContainerPort).",
        "docker run -d --name my-redis -p 6379:6379 redis:latest",
        "Outputs 64-character container ID hash."
    )
    b.add_step(
        "List active running containers vs all containers (including stopped).",
        "docker ps\n"
        "# List all including stopped containers:\n"
        "docker ps -a",
        "CONTAINER ID   IMAGE   COMMAND                  CREATED         STATUS         PORTS                    NAMES\ne1d2c3b4a5f6   redis   \"docker-entrypoint.s…\"   5 seconds ago   Up 4 seconds   0.0.0.0:6379->6379/tcp   my-redis"
    )
    b.add_step(
        "Inspect real-time container log output.",
        "docker logs my-redis\n"
        "# Stream live logs with timestamp and tail:\n"
        "docker logs -f --tail 50 my-redis",
        "1:M 23 Nov 04:35:12.123 * Ready to accept connections tcp"
    )
    b.add_step(
        "Open an interactive terminal shell inside a running Ubuntu container.",
        "docker exec -it my-redis /bin/sh\n"
        "# Inside container:\n"
        "# redis-cli ping\n"
        "# PONG\n"
        "# exit",
        "Returns interactive shell prompt root@e1d2c3b4a5f6:/data#."
    )
    b.add_step(
        "Stop, start, and restart container.",
        "docker stop my-redis\n"
        "docker start my-redis\n"
        "docker restart my-redis",
        "my-redis output confirms state transitions."
    )
    b.add_step(
        "Forcefully remove single or all stopped containers.",
        "docker rm -f my-redis\n"
        "# Remove all stopped containers at once:\n"
        "docker container prune -f",
        "Container removed."
    )

    b.add_h2("3.4 Persistent Storage with Docker Volumes")
    b.add_step(
        "Create and inspect a managed Docker volume on Ubuntu.",
        "docker volume create mysql_data\n"
        "docker volume ls\n"
        "docker volume inspect mysql_data",
        "Mountpoint: /var/lib/docker/volumes/mysql_data/_data on host Ubuntu filesystem."
    )
    b.add_step(
        "Run MySQL container with named volume persistence.",
        "docker run -d --name lab-mysql \\\n"
        "  -p 3306:3306 \\\n"
        "  -e MYSQL_ROOT_PASSWORD=root123 \\\n"
        "  -e MYSQL_DATABASE=labdb \\\n"
        "  -v mysql_data:/var/lib/mysql \\\n"
        "  mysql:8.0",
        "Even if container is deleted (docker rm -f lab-mysql), data persists inside mysql_data volume."
    )

    b.add_h2("3.5 Custom Bridge Networking")
    b.add_step(
        "Create custom user-defined bridge network for inter-container DNS communication.",
        "docker network create app-network\n"
        "docker network ls",
        "NETWORK ID     NAME          DRIVER    SCOPE\n4d5e6f7a8b9c   app-network   bridge    local"
    )
    b.add_step(
        "Connect containers to network and demonstrate name-based DNS resolution.",
        "docker run -d --name redis-server --network app-network redis:latest\n"
        "docker run --rm --network app-network alpine ping -c 2 redis-server",
        "64 bytes from redis-server (172.19.0.2): seq=1 ttl=64 time=0.082 ms. DNS resolves container name!"
    )

    b.add_h2("3.6 Pushing and Pulling from Docker Hub")
    b.add_step(
        "Log in to Docker Hub from Ubuntu terminal.",
        "docker login -u dheerajmalavath",
        "Enter password / personal access token: Login Succeeded."
    )
    b.add_step(
        "Tag local image with Docker Hub repository name and push.",
        "docker tag redis:latest dheerajmalavath/custom-redis:v1\n"
        "docker push dheerajmalavath/custom-redis:v1",
        "The push refers to repository [docker.io/dheerajmalavath/custom-redis]\nv1: digest: sha256:... size: 1572"
    )

    # =========================================================================
    # MODULE 4: DOCKER COMPOSE & MULTI-CONTAINER SERVICES
    # =========================================================================
    b.add_page_break()
    b.add_h1("4. Docker Compose & Dockerfile — Multi-Container Interdependent Services")
    b.add_paragraph(
        "Docker Compose is an orchestration tool used to define and run multi-container Docker applications via a single "
        "declarative YAML configuration file (docker-compose.yml). It manages interconnected services, shared networks, and persistent volumes."
    )

    b.add_h2("4.1 Writing the Dockerfile in Ubuntu")
    b.add_step(
        "Create Dockerfile for Java Tomcat Web Application using nano in Ubuntu.",
        "nano Dockerfile\n"
        "# Paste the following content:\n"
        "FROM tomcat:9.0-jdk11-openjdk-slim\n"
        "LABEL maintainer=\"dheerajmalavath\"\n"
        "RUN rm -rf /usr/local/tomcat/webapps/*\n"
        "COPY target/*.war /usr/local/tomcat/webapps/ROOT.war\n"
        "EXPOSE 8080\n"
        "CMD [\"catalina.sh\", \"run\"]\n"
        "# Save in nano: Ctrl+O, Enter, Ctrl+X",
        "Dockerfile created in project root directory."
    )

    b.add_h2("4.2 Production Multi-Container Compose Templates for Exam Sets")
    b.add_step(
        "Case A: Java Web Application + MySQL Database (SET 2, 3, 4, 7, 8, 9).",
        "nano docker-compose.yml\n"
        "# Paste following content:\n"
        "version: '3.8'\n"
        "\n"
        "services:\n"
        "  app:\n"
        "    build: .\n"
        "    container_name: oltrs-app\n"
        "    ports:\n"
        "      - \"9090:8080\"\n"
        "    depends_on:\n"
        "      - db\n"
        "    environment:\n"
        "      DB_HOST: db\n"
        "      DB_NAME: oltrsdb\n"
        "      DB_USER: appuser\n"
        "      DB_PASS: apppass\n"
        "    networks:\n"
        "      - appnet\n"
        "    restart: always\n"
        "\n"
        "  db:\n"
        "    image: mysql:8.0\n"
        "    container_name: oltrs-db\n"
        "    environment:\n"
        "      MYSQL_ROOT_PASSWORD: root123\n"
        "      MYSQL_DATABASE: oltrsdb\n"
        "      MYSQL_USER: appuser\n"
        "      MYSQL_PASSWORD: apppass\n"
        "    ports:\n"
        "      - \"3307:3306\"\n"
        "    volumes:\n"
        "      - dbdata:/var/lib/mysql\n"
        "    networks:\n"
        "      - appnet\n"
        "    restart: always\n"
        "\n"
        "volumes:\n"
        "  dbdata:\n"
        "\n"
        "networks:\n"
        "  appnet:\n"
        "    driver: bridge\n"
        "# Save: Ctrl+O, Enter, Ctrl+X",
        "docker-compose.yml ready for multi-container deployment."
    )

    b.add_step(
        "Case B: WordPress + MySQL Interdependent Setup (SET 1, SET 6).",
        "nano docker-compose.yml\n"
        "# Paste:\n"
        "version: '3.8'\n"
        "\n"
        "services:\n"
        "  wordpress:\n"
        "    image: wordpress:latest\n"
        "    container_name: wordpress-app\n"
        "    ports:\n"
        "      - \"9090:80\"\n"
        "    depends_on:\n"
        "      - db\n"
        "    environment:\n"
        "      WORDPRESS_DB_HOST: db:3306\n"
        "      WORDPRESS_DB_USER: wpuser\n"
        "      WORDPRESS_DB_PASSWORD: wppassword\n"
        "      WORDPRESS_DB_NAME: wordpress\n"
        "    networks:\n"
        "      - wpnet\n"
        "\n"
        "  db:\n"
        "    image: mysql:5.7\n"
        "    container_name: wordpress-db\n"
        "    environment:\n"
        "      MYSQL_ROOT_PASSWORD: rootpassword\n"
        "      MYSQL_DATABASE: wordpress\n"
        "      MYSQL_USER: wpuser\n"
        "      MYSQL_PASSWORD: wppassword\n"
        "    volumes:\n"
        "      - wpdata:/var/lib/mysql\n"
        "    networks:\n"
        "      - wpnet\n"
        "\n"
        "volumes:\n"
        "  wpdata:\n"
        "networks:\n"
        "  wpnet:",
        "WordPress multi-container compose configuration created."
    )

    b.add_h2("4.3 Docker Compose CLI Execution Commands")
    b.add_step(
        "Start all services in detached background mode with image build.",
        "docker compose up --build -d",
        "[+] Running 4/4\n ✔ Network appnet     Created\n ✔ Volume dbdata      Created\n ✔ Container oltrs-db Started\n ✔ Container oltrs-app Started"
    )
    b.add_step(
        "Check status of compose services and verify mapped ports.",
        "docker compose ps",
        "NAME        IMAGE       COMMAND                  SERVICE   CREATED         STATUS         PORTS\noltrs-app   oltrs_app   \"catalina.sh run\"        app       2 minutes ago   Up 2 minutes   0.0.0.0:9090->8080/tcp\noltrs-db    mysql:8.0   \"docker-entrypoint.s…\"   db        2 minutes ago   Up 2 minutes   0.0.0.0:3307->3306/tcp"
    )
    b.add_step(
        "View streaming logs for specific service (troubleshoot DB connection).",
        "docker compose logs -f app",
        "Shows Tomcat deployment logs and DB connection establishment."
    )
    b.add_step(
        "Stop only one service while keeping others active.",
        "docker compose stop app\n"
        "# Resume without recreating:\n"
        "docker compose start app",
        "Stopped oltrs-app; DB remains running with data intact."
    )
    b.add_step(
        "Tear down multi-container application cleanly.",
        "# Down without deleting volume (preserves DB records):\n"
        "docker compose down\n"
        "# Down AND delete persistent volumes:\n"
        "docker compose down -v",
        "[+] Running 3/3\n ✔ Container oltrs-app Removed\n ✔ Container oltrs-db  Removed\n ✔ Network appnet      Removed"
    )

    # =========================================================================
    # MODULE 5: JENKINS CI/CD AUTOMATION
    # =========================================================================
    b.add_page_break()
    b.add_h1("5. Jenkins — CI/CD Pipeline Automation in Ubuntu")
    b.add_paragraph(
        "Jenkins is an extensible open-source automation server supporting Continuous Integration (CI) and Continuous Delivery (CD). "
        "It automates code checkout, Maven compilation, testing, Docker image building, and automated deployment."
    )

    b.add_h2("5.1 Running Jenkins Container on Ubuntu")
    b.add_step(
        "Run Jenkins LTS container with persistent home directory and exposed ports in Ubuntu.",
        "docker run -d \\\n"
        "  --name jenkins \\\n"
        "  --restart=always \\\n"
        "  -p 9080:8080 \\\n"
        "  -p 50000:50000 \\\n"
        "  -v jenkins_home:/var/jenkins_home \\\n"
        "  jenkins/jenkins:lts",
        "Outputs container hash. Jenkins will be accessible at http://localhost:9080."
    )
    b.add_step(
        "Retrieve initial administrator unlock password from container volume.",
        "docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword",
        "Outputs a 32-character hexadecimal key (e.g. 4a8e2b9c7d1f0e3a5b6c8d7e9f0a1b2c). Copy this key."
    )

    b.add_h2("5.2 First-Time Unlock & UI Configuration in Browser")
    b.add_table(
        headers=["Step #", "Action in Jenkins Browser UI", "Explanation / Input"],
        data=[
            ["Step 1", "Navigate to http://localhost:9080", "Opens 'Unlock Jenkins' welcome screen."],
            ["Step 2", "Paste Administrator Password", "Paste the 32-character key retrieved from terminal. Click 'Continue'."],
            ["Step 3", "Install Suggested Plugins", "Click 'Install suggested plugins' box. Wait for automated download of Git, Pipeline, etc."],
            ["Step 4", "Create First Admin User", "Username: 'admin' | Password: 'password123' | Full Name: 'Lab Admin' | Email: 'admin@example.com'. Click 'Save and Continue'."],
            ["Step 5", "Instance Configuration", "Confirm Jenkins URL: 'http://localhost:9080/'. Click 'Save and Finish' → 'Start using Jenkins'."]
        ],
        col_widths=[1.0, 3.0, 2.9]
    )

    b.add_h2("5.3 Installing Plugins: Maven & Docker Pipeline")
    b.add_step(
        "Install required Maven and Docker plugins in Jenkins UI.",
        "# 1. Click 'Manage Jenkins' on the left sidebar.\n"
        "# 2. Click 'Plugins' -> Select 'Available plugins' tab.\n"
        "# 3. In search bar, type: 'Maven Integration' and 'Docker Pipeline'.\n"
        "# 4. Check the checkboxes next to both plugins.\n"
        "# 5. Click 'Install without restart' button at bottom.",
        "Status changes to 'Success' for all downloaded plugins."
    )
    b.add_step(
        "Configure Global Tools (Maven & JDK) in Jenkins UI.",
        "# 1. Manage Jenkins -> 'Tools'.\n"
        "# 2. Scroll to 'Maven installations' -> Click 'Add Maven'.\n"
        "# 3. Set Name: 'Maven' (CRITICAL: exact case; matches Jenkinsfile def mvnHome = tool 'Maven').\n"
        "# 4. Check 'Install automatically' -> Version: '3.9.6'. Click 'Save'.",
        "Tool 'Maven' configured globally for all Freestyle and Pipeline jobs."
    )

    b.add_h2("5.4 Freestyle Project Configuration (SET 1, 2, 3 Exam Questions)")
    b.add_table(
        headers=["UI Section", "Field Name", "Value to Configure"],
        data=[
            ["Job Creation", "Item Name", "Enter 'oltrs-freestyle-ci', select 'Freestyle project', click 'OK'."],
            ["Source Code Mgmt", "Git Repository URL", "Enter assigned repo: 'https://github.com/archanareddyse/OLTRS.git'."],
            ["Source Code Mgmt", "Branches to build", "Change '*/master' to '*/main' (check GitHub default branch)."],
            ["Build Environment", "Delete workspace before build starts", "Check this box to ensure clean pristine builds."],
            ["Build Steps", "Add build step", "Select 'Invoke top-level Maven targets'."],
            ["Build Steps", "Maven Version & Goals", "Select Maven Version: 'Maven' | Goals: 'clean package -DskipTests'."],
            ["Post-build Actions", "Archive the artifacts", "Files to archive: 'target/*.war' (or target/*.jar)."],
            ["Execution", "Build Now", "Click 'Build Now' on left sidebar. Click build #1 → 'Console Output' to observe build."]
        ],
        col_widths=[1.6, 2.2, 3.1]
    )

    b.add_h2("5.5 Complete Scripted Pipeline Templates (Groovy Syntax for Script Box)")
    b.add_step(
        "Template A: Full CI/CD Scripted Pipeline with Maven Build, Test, and Docker Push.",
        "node {\n"
        "    def mvnHome = tool 'Maven'\n"
        "    \n"
        "    stage('Checkout') {\n"
        "        echo 'Cloning repository from GitHub...'\n"
        "        git url: 'https://github.com/archanareddyse/OLTRS.git', branch: 'main'\n"
        "    }\n"
        "    \n"
        "    stage('Build') {\n"
        "        echo 'Compiling and Packaging WAR file...'\n"
        "        sh \"${mvnHome}/bin/mvn clean package -DskipTests\"\n"
        "    }\n"
        "    \n"
        "    stage('Test') {\n"
        "        echo 'Executing Automated Unit Tests...'\n"
        "        sh \"${mvnHome}/bin/mvn test\"\n"
        "    }\n"
        "    \n"
        "    stage('Docker Build & Push') {\n"
        "        echo 'Building Docker Image and Pushing to Docker Hub...'\n"
        "        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {\n"
        "            sh '''\n"
        "                docker build -t dheerajmalavath/oltrs:latest .\n"
        "                echo $DH_PASS | docker login -u $DH_USER --password-stdin\n"
        "                docker push dheerajmalavath/oltrs:latest\n"
        "            '''\n"
        "        }\n"
        "    }\n"
        "}",
        "Console Output displays: Finished: SUCCESS. Docker image visible on hub.docker.com."
    )

    b.add_step(
        "Template B: Intentional Failure Stage for Email Notification Testing (SET 4 Q2c).",
        "node {\n"
        "    try {\n"
        "        stage('Checkout') {\n"
        "            git url: 'https://github.com/Kumbhambhargavi75/HospitalManagementSystem.git', branch: 'main'\n"
        "        }\n"
        "        stage('Intentional Failure Test') {\n"
        "            echo 'Simulating failed test suite to verify alert notification...'\n"
        "            sh 'exit 1' // Forces build error\n"
        "        }\n"
        "    } catch (err) {\n"
        "        stage('Notification') {\n"
        "            echo \"Build failed with error: ${err}\"\n"
        "            mail to: 'student@example.com',\n"
        "                 subject: \"FAILURE: Jenkins Build #${env.BUILD_NUMBER} Failed\",\n"
        "                 body: \"The CI build failed during unit testing. Check ${env.BUILD_URL}\"\n"
        "        }\n"
        "        error('Terminating pipeline with failure status')\n"
        "    }\n"
        "}",
        "Stage 'Intentional Failure Test' turns RED. Notification block triggers and pipeline marks failure."
    )

    b.add_h2("5.6 Build Triggers: Webhooks & Cron Schedules")
    b.add_step(
        "Configure GitHub Webhook in GitHub Repository Settings.",
        "# In GitHub repo -> Settings -> Webhooks -> Add webhook:\n"
        "# Payload URL: http://<your-public-ip>:9080/github-webhook/\n"
        "# Content type: application/json\n"
        "# Which events: 'Just the push event'\n"
        "# Active: Checked -> Click 'Add webhook'",
        "Green checkmark next to webhook URL confirms 200 OK delivery on every git push."
    )
    b.add_step(
        "Configure Scheduled Builds with Cron Syntax (SET 6 Question: Run at 6:00 PM daily).",
        "# In Jenkins Job Configuration -> 'Build Triggers' -> Check 'Build periodically':\n"
        "# Syntax: MINUTE HOUR DOM MONTH DOW\n"
        "0 18 * * *       # Triggers every day at 6:00 PM (18:00)\n"
        "H/15 * * * *     # Triggers every 15 minutes\n"
        "0 9 * * 1-5      # Triggers Monday through Friday at 9:00 AM",
        "Jenkins schedules next run at specified time."
    )

    # =========================================================================
    # MODULE 6: KUBERNETES DEPLOYMENT & SCALING
    # =========================================================================
    b.add_page_break()
    b.add_h1("6. Kubernetes — Container Orchestration & Scaling with Minikube")
    b.add_paragraph(
        "Kubernetes (K8s) is an open-source container orchestration system for automating application deployment, scaling, and management. "
        "Minikube creates a single-node local Kubernetes cluster inside Ubuntu using the Docker driver."
    )

    b.add_h2("6.1 Installing Minikube and kubectl on Ubuntu")
    b.add_step(
        "Download and install Minikube binary on Ubuntu.",
        "curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64\n"
        "sudo install minikube-linux-amd64 /usr/local/bin/minikube\n"
        "minikube version",
        "minikube version: v1.32.0 (or latest installed)."
    )
    b.add_step(
        "Download and install kubectl CLI on Ubuntu.",
        "curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"\n"
        "sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl\n"
        "kubectl version --client",
        "Client Version: v1.28.x."
    )

    b.add_h2("6.2 Starting Minikube Cluster and Inspecting Nodes")
    b.add_step(
        "Start Minikube cluster using Docker driver in Ubuntu.",
        "minikube start --driver=docker",
        "🏄  Done! kubectl is now configured to use \"minikube\" cluster and \"default\" namespace by default."
    )
    b.add_step(
        "Inspect cluster components and worker node status.",
        "kubectl cluster-info\n"
        "kubectl get nodes -o wide",
        "NAME       STATUS   ROLES           AGE   VERSION   INTERNAL-IP    OS-IMAGE\nminikube   Ready    control-plane   2m    v1.28.3   192.168.49.2   Ubuntu 22.04 LTS"
    )

    b.add_h2("6.3 Deployments, Scaling, and Self-Healing Demonstration")
    b.add_step(
        "Create a Deployment from Docker Hub image.",
        "kubectl create deployment my-app --image=dheerajmalavath/oltrs:latest",
        "deployment.apps/my-app created."
    )
    b.add_step(
        "Scale the Deployment to 4 Replicas (Exam Required Task).",
        "kubectl scale deployment my-app --replicas=4\n"
        "kubectl get deployments",
        "NAME     READY   UP-TO-DATE   AVAILABLE   AGE\nmy-app   4/4     4            4           45s"
    )
    b.add_step(
        "Verify all 4 Pods are in Running state.",
        "kubectl get pods -o wide",
        "NAME                      READY   STATUS    RESTARTS   AGE   IP           NODE\nmy-app-6d8b9c-a1b2c       1/1     Running   0          50s   10.244.0.5   minikube\nmy-app-6d8b9c-d4e5f       1/1     Running   0          50s   10.244.0.6   minikube\nmy-app-6d8b9c-g7h8i       1/1     Running   0          50s   10.244.0.7   minikube\nmy-app-6d8b9c-j1k2l       1/1     Running   0          50s   10.244.0.8   minikube"
    )
    b.add_step(
        "Demonstrate Kubernetes Self-Healing (Pod Auto-Recovery) to Examiner.",
        "# 1. Delete one active running pod:\n"
        "kubectl delete pod my-app-6d8b9c-a1b2c\n"
        "# 2. Immediately inspect pods:\n"
        "kubectl get pods",
        "Pod my-app-6d8b9c-a1b2c is Terminating; ReplicaSet instantly spawned a brand new Pod my-app-6d8b9c-z9y8x with AGE 2s in ContainerCreating/Running status! Total desired count (4/4) is maintained automatically."
    )

    b.add_h2("6.4 Exposing Deployment via Service (NodePort) and Browser Access")
    b.add_step(
        "Expose Deployment through NodePort Service to route external traffic.",
        "kubectl expose deployment my-app --type=NodePort --port=8080 --target-port=8080\n"
        "kubectl get services",
        "NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE\nkubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          10m\nmy-app       NodePort    10.105.12.34    <none>        8080:31254/TCP   15s\nNodePort assigned in the 30000–32767 range (e.g. 31254)."
    )
    b.add_step(
        "Retrieve the accessible browser URL using Minikube CLI.",
        "minikube service my-app --url\n"
        "# Test HTTP response in terminal:\n"
        "curl -I $(minikube service my-app --url)",
        "Outputs accessible URL: http://192.168.49.2:31254\nHTTP/1.1 200 OK (Application accessible in browser)."
    )

    b.add_h2("6.5 Rolling Updates and Rollback")
    b.add_step(
        "Perform zero-downtime Rolling Update to a new version.",
        "kubectl set image deployment/my-app oltrs=dheerajmalavath/oltrs:v2\n"
        "kubectl rollout status deployment/my-app",
        "Waiting for deployment \"my-app\" rollout to finish: 2 out of 4 new replicas have been updated...\ndeployment \"my-app\" successfully rolled out."
    )
    b.add_step(
        "Roll back failed update to previous revision.",
        "kubectl rollout history deployment/my-app\n"
        "kubectl rollout undo deployment/my-app\n"
        "kubectl rollout status deployment/my-app",
        "deployment.apps/my-app rolled back. Replicas restored to previous stable image."
    )

    b.add_h2("6.6 Declarative YAML Manifests (deployment.yaml & service.yaml)")
    b.add_step(
        "Create deployment.yaml using nano in Ubuntu.",
        "nano deployment.yaml\n"
        "# Paste:\n"
        "apiVersion: apps/v1\n"
        "kind: Deployment\n"
        "metadata:\n"
        "  name: my-web-app\n"
        "spec:\n"
        "  replicas: 4\n"
        "  selector:\n"
        "    matchLabels:\n"
        "      app: web\n"
        "  template:\n"
        "    metadata:\n"
        "      labels:\n"
        "        app: web\n"
        "    spec:\n"
        "      containers:\n"
        "      - name: web\n"
        "        image: dheerajmalavath/oltrs:latest\n"
        "        ports:\n"
        "        - containerPort: 8080\n"
        "# Save: Ctrl+O, Enter, Ctrl+X\n"
        "kubectl apply -f deployment.yaml",
        "deployment.apps/my-web-app created."
    )
    b.add_step(
        "Create service.yaml using nano in Ubuntu.",
        "nano service.yaml\n"
        "# Paste:\n"
        "apiVersion: v1\n"
        "kind: Service\n"
        "metadata:\n"
        "  name: my-web-service\n"
        "spec:\n"
        "  type: NodePort\n"
        "  selector:\n"
        "    app: web\n"
        "  ports:\n"
        "  - port: 8080\n"
        "    targetPort: 8080\n"
        "    nodePort: 30080\n"
        "# Save: Ctrl+O, Enter, Ctrl+X\n"
        "kubectl apply -f service.yaml",
        "service/my-web-service created."
    )

    # =========================================================================
    # MODULE 7: NAGIOS MONITORING
    # =========================================================================
    b.add_page_break()
    b.add_h1("7. Nagios — Infrastructure & Application Monitoring in Ubuntu")
    b.add_paragraph(
        "Nagios is an enterprise-grade IT infrastructure monitoring tool that monitors servers, containers, switches, and network services. "
        "It alerts administrators when outages occur and sends recovery notifications when services return to health."
    )

    b.add_h2("7.1 Starting Nagios Server via Docker on Ubuntu")
    b.add_step(
        "Run Nagios Docker container on Ubuntu host port 8090.",
        "docker run -d \\\n"
        "  --name nagios \\\n"
        "  --restart=always \\\n"
        "  -p 8090:80 \\\n"
        "  jasonrivers/nagios:latest",
        "Outputs container ID hash. Accessible at http://localhost:8090."
    )
    b.add_step(
        "Verify Nagios container is running and healthy.",
        "docker ps | grep nagios",
        "Up X minutes (healthy)  0.0.0.0:8090->80/tcp  nagios"
    )

    b.add_h2("7.2 Nagios Web Dashboard UI Navigation (What to Show Examiner)")
    b.add_paragraph("Open browser and navigate to: http://localhost:8090. Default Login: Username: 'nagiosadmin' | Password: 'nagios'.")
    b.add_table(
        headers=["UI Section on Left Bar", "What It Displays", "What to Demonstrate to Examiner"],
        data=[
            ["Tactical Overview", "Overall monitoring health matrix across all hosts and services.", "Point out: 0 Hosts Down, 0 Critical Services, all green gauges."],
            ["Hosts", "List of all monitored host machines / containers.", "Shows 'localhost' with Status UP, Duration, and Last Check timestamp."],
            ["Services", "Detailed list of all service checks running against monitored hosts.", "Shows HTTP, PING, SSH, Root Partition, Current Load, and Total Processes."],
            ["Service Problems", "Filtered view displaying only services in WARNING or CRITICAL state.", "Demonstrates alerting filter when a container crashes or is stopped."],
            ["Event Log", "Chronological audit log of all state transitions, check executions, and alerts.", "Shows exact timestamp when an alert was triggered or resolved."]
        ],
        col_widths=[1.8, 2.6, 2.5]
    )

    b.add_h2("7.3 Nagios Configuration Files Architecture (Inside Container)")
    b.add_paragraph(
        "All Nagios configuration files reside inside the container at /opt/nagios/etc/. "
        "Key files include nagios.cfg (main config), objects/hosts.cfg (host definitions), objects/services.cfg (service definitions), "
        "and objects/commands.cfg (plugin execution commands)."
    )
    b.add_step(
        "Inspect Nagios configuration files and run pre-flight syntax check.",
        "docker exec -it nagios /opt/nagios/bin/nagios -v /opt/nagios/etc/nagios.cfg",
        "Total Warnings: 0, Total Errors: 0. Things look okay - No serious problems were detected during the pre-flight check."
    )

    b.add_h2("7.4 Sample Host and Service Definitions")
    b.add_step(
        "Sample Host Definition for App Server inside /opt/nagios/etc/objects/hosts.cfg.",
        "define host {\n"
        "    use                     linux-server\n"
        "    host_name               oltrs-web-app\n"
        "    alias                   Online Ticket Reservation System\n"
        "    address                 172.17.0.1  # Docker host IP\n"
        "    max_check_attempts      3\n"
        "    check_period            24x7\n"
        "    notification_interval   30\n"
        "    notification_period     24x7\n"
        "}",
        "Host definition registered."
    )
    b.add_step(
        "Sample Service Definition to Monitor Web App HTTP Port 9090.",
        "define service {\n"
        "    use                     generic-service\n"
        "    host_name               oltrs-web-app\n"
        "    service_description     HTTP Port 9090 Status\n"
        "    check_command           check_http!-p 9090 -u /ROOT/\n"
        "    check_interval          1\n"
        "    retry_interval          1\n"
        "    max_check_attempts      2\n"
        "    notification_period     24x7\n"
        "}",
        "Nagios polls http://172.17.0.1:9090/ROOT/ every minute."
    )

    b.add_h2("7.5 Nagios Status Codes Reference")
    b.add_table(
        headers=["Exit Code", "Status Label", "Dashboard Color", "Meaning / Condition"],
        data=[
            ["0", "OK", "Green", "Service is responding normally within acceptable thresholds."],
            ["1", "WARNING", "Yellow", "Service is functional but exceeding warning thresholds (e.g. disk 85% full, latency high)."],
            ["2", "CRITICAL", "Red", "Service has crashed, port is unreachable, or threshold exceeded (e.g. HTTP 500 error, host DOWN)."],
            ["3", "UNKNOWN", "Orange", "Check plugin syntax error or plugin could not determine state."]
        ],
        col_widths=[1.0, 1.5, 1.5, 2.9]
    )

    # =========================================================================
    # MODULE 8: AWS EC2 CLOUD DEPLOYMENT
    # =========================================================================
    b.add_page_break()
    b.add_h1("8. AWS EC2 — Cloud Deployment on Ubuntu Instance")
    b.add_paragraph(
        "Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS cloud. "
        "In this module, you launch an Ubuntu Server 22.04 LTS instance, configure SSH security permissions, "
        "set up the runtime environment, and deploy containerized applications accessible via Public IPv4."
    )

    b.add_h2("8.1 Step-by-Step EC2 Instance Launch Guide (AWS Management Console)")
    b.add_table(
        headers=["Launch Wizard Step", "Field / Parameter", "Value to Select in AWS Console"],
        data=[
            ["Step 1: Name", "Instance Name", "Enter 'devops-ubuntu-server'."],
            ["Step 2: OS Image (AMI)", "Application and OS Images", "Select 'Ubuntu' → Choose 'Ubuntu Server 22.04 LTS (HVM), SSD Volume Type' (Free tier eligible)."],
            ["Step 3: Architecture", "Architecture", "Select '64-bit (x86)'."],
            ["Step 4: Instance Type", "Instance type", "Select 't2.micro' (1 vCPU, 1 GiB Memory, Free tier eligible)."],
            ["Step 5: Key Pair", "Key pair (login)", "Click 'Create new key pair' → Name: 'devops-key' → Type: 'RSA' → Format: '.pem' → Download to ~/Downloads/."],
            ["Step 6: Network Settings", "Firewall (Security Groups)", "Select 'Create security group'. Check 'Allow SSH traffic from Anywhere (0.0.0.0/0)' and 'Allow HTTP traffic from the internet'."],
            ["Step 7: Storage", "Configure storage", "Leave default: 1x 8 GiB gp3 root volume."],
            ["Step 8: Launch", "Launch Instance", "Click orange 'Launch instance' button on right summary panel. Click 'View all instances'."]
        ],
        col_widths=[1.5, 2.2, 3.2]
    )

    b.add_h2("8.2 Connecting to EC2 via SSH from Ubuntu Terminal (Setting Permissions)")
    b.add_paragraph(
        "In Ubuntu Linux, the SSH client enforces strict file permission checks on private key files. "
        "If the key permissions are too open, SSH rejects the connection with: 'UNPROTECTED PRIVATE KEY FILE! Permissions 0644 for devops-key.pem are too open'."
    )
    b.add_step(
        "Move key to ~/.ssh directory and set secure chmod 400 permissions in Ubuntu.",
        "mkdir -p ~/.ssh\n"
        "mv ~/Downloads/devops-key.pem ~/.ssh/\n"
        "chmod 400 ~/.ssh/devops-key.pem\n"
        "# Verify permissions:\n"
        "ls -l ~/.ssh/devops-key.pem",
        "-r-------- 1 ubuntu ubuntu 1674 Nov 23 04:40 /home/ubuntu/.ssh/devops-key.pem (Read-only by owner)."
    )
    b.add_step(
        "Connect to your Ubuntu EC2 instance using SSH.",
        "# Replace <EC2-PUBLIC-IP> with the Public IPv4 address from AWS EC2 Console:\n"
        "ssh -i ~/.ssh/devops-key.pem ubuntu@54.210.123.45\n"
        "# When prompted: 'Are you sure you want to continue connecting (yes/no/[fingerprint])?'\n"
        "# Type: yes and hit Enter.",
        "Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.15.0-aws x86_64)\nubuntu@ip-172-31-45-67:~$ (Connected!)."
    )

    b.add_h2("8.3 Configuring Ubuntu EC2 Terminal & Deploying Application")
    b.add_step(
        "Update OS packages and install Docker, Git, Java, and Maven inside EC2 instance shell.",
        "sudo apt update && sudo apt upgrade -y\n"
        "sudo apt install -y docker.io git openjdk-17-jdk maven\n"
        "sudo systemctl enable docker && sudo systemctl start docker\n"
        "sudo usermod -aG docker ubuntu\n"
        "newgrp docker",
        "Development environment ready on EC2 cloud instance."
    )
    b.add_step(
        "Clone repository, build WAR, and run Docker container on port 9090 inside EC2.",
        "git clone https://github.com/archanareddyse/OLTRS.git\n"
        "cd OLTRS\n"
        "mvn clean package -DskipTests\n"
        "\n"
        "# Create Dockerfile using nano:\n"
        "nano Dockerfile\n"
        "# Paste:\n"
        "# FROM tomcat:9.0\n"
        "# RUN rm -rf /usr/local/tomcat/webapps/*\n"
        "# COPY target/*.war /usr/local/tomcat/webapps/ROOT.war\n"
        "# EXPOSE 8080\n"
        "# CMD [\"catalina.sh\", \"run\"]\n"
        "# Save: Ctrl+O, Enter, Ctrl+X\n"
        "\n"
        "# Build and Run container:\n"
        "docker build -t oltrs-app:latest .\n"
        "docker run -d --name my-app -p 9090:8080 oltrs-app:latest\n"
        "docker ps",
        "Container active: 0.0.0.0:9090->8080/tcp."
    )

    b.add_h2("8.4 Unblocking Application Port in AWS Security Group (Custom TCP Inbound Rule)")
    b.add_paragraph(
        "By default, AWS Security Groups block port 9090 and 8080. If you try opening http://<EC2-PUBLIC-IP>:9090 "
        "in your browser, the page will time out with 'ERR_CONNECTION_TIMED_OUT'. You must add an inbound rule in AWS Console:"
    )
    b.add_table(
        headers=["Step #", "Action in AWS Management Console", "Setting Value"],
        data=[
            ["Step 1", "Navigate to Security Groups", "In EC2 Console left sidebar → Under 'Network & Security', click 'Security Groups'."],
            ["Step 2", "Select Instance Security Group", "Click the Security Group associated with your instance (e.g. 'launch-wizard-1')."],
            ["Step 3", "Open Inbound Rules Editor", "In lower panel, click the 'Inbound rules' tab → Click 'Edit inbound rules' button."],
            ["Step 4", "Add Custom TCP Rule", "Click 'Add rule' button at bottom: Type: 'Custom TCP' | Port range: '9090' (or 8080) | Source: 'Anywhere-IPv4' (0.0.0.0/0)."],
            ["Step 5", "Save Rules", "Click orange 'Save rules' button at bottom right."],
            ["Step 6", "Verify in Browser", "Open browser: http://<EC2-PUBLIC-IP>:9090. Application loads immediately without timeout!"]
        ],
        col_widths=[1.0, 2.7, 3.2]
    )

    b.add_h2("8.5 Assigning an Elastic IP (When Instance Has No Public IPv4 Address)")
    b.add_paragraph("Scenario: Your EC2 instance only has a private IP address, but must be reachable over the internet.")
    b.add_step(
        "Allocate and associate Elastic IP in AWS Console.",
        "# 1. In EC2 Console left sidebar -> Under 'Network & Security', click 'Elastic IPs'.\n"
        "# 2. Click 'Allocate Elastic IP address' -> Click 'Allocate' (default Amazon pool).\n"
        "# 3. Select the allocated IP -> Click 'Actions' dropdown -> Click 'Associate Elastic IP address'.\n"
        "# 4. Resource type: 'Instance' -> Choose your running EC2 instance -> Click 'Associate'.",
        "Instance now possesses a permanent, static Public IPv4 address that does not change when stopped and restarted."
    )

    b.add_h2("8.6 Proper Cleanup and Instance Termination")
    b.add_step(
        "Terminate EC2 instance to prevent billing after lab session.",
        "# 1. Navigate to EC2 Console -> 'Instances'.\n"
        "# 2. Select your instance -> Click 'Instance state' dropdown -> Click 'Terminate instance'.\n"
        "# 3. Confirm termination. Instance status changes to 'Shutting-down' then 'Terminated'.\n"
        "# 4. Under 'Elastic IPs', select any allocated IP -> Click 'Actions' -> 'Release Elastic IP address'.",
        "All cloud resources de-provisioned; billing completely halted."
    )

    # =========================================================================
    # MODULE 9: SCENARIO-BASED QUESTIONS & ANSWERS (ALL 9 SETS)
    # =========================================================================
    b.add_page_break()
    b.add_h1("9. Scenario-Based Questions & Solutions (All 9 Exam Sets)")
    b.add_paragraph(
        "These exact scenario-based troubleshooting questions appear across all 9 practical exam sets (carrying 5 marks each). "
        "Review these solutions to guarantee maximum marks."
    )

    b.add_h2("9.1 Docker Compose Scenarios")
    b.add_table(
        headers=["Exam Scenario Question", "Correct Ubuntu CLI Solution / Configuration", "Explanation"],
        data=[
            [
                "How do you stop all services without removing containers and networks?",
                "docker compose stop",
                "Halts container execution while preserving container states, IP assignments, and network configurations."
            ],
            [
                "How do you resume stopped containers without recreating them?",
                "docker compose start",
                "Starts existing stopped containers instantly without re-reading the compose YAML or regenerating IDs."
            ],
            [
                "How do you remove containers, networks, and persistent volumes completely after testing?",
                "docker compose down -v",
                "The '-v' flag deletes declared named volumes alongside containers and networks."
            ],
            [
                "A new microservice was added to docker-compose.yml. How do you apply changes without interrupting running services?",
                "docker compose up -d",
                "Compose detects changes in YAML, creates only the new service, and leaves unchanged services untouched."
            ],
            [
                "WordPress container starts before MySQL container is ready and crashes with DB connection error. How do you fix it?",
                "Add 'depends_on: - db' under wordpress service in docker-compose.yml.",
                "Enforces startup order so database container initializes before the application container starts."
            ],
            [
                "How do you run a web service with 3 load-balanced replica containers?",
                "docker compose up --scale web=3 -d",
                "Scales the 'web' service to 3 independent running container instances on the bridge network."
            ],
            [
                "MySQL container crashes while web app is running. How do you recover?",
                "docker compose restart db",
                "Restarts the database service; application reconnects automatically or upon page refresh."
            ]
        ],
        col_widths=[2.4, 2.3, 2.2]
    )

    b.add_h2("9.2 Jenkins Pipeline Scenarios")
    b.add_table(
        headers=["Exam Scenario Question", "Correct Jenkins Solution", "Explanation"],
        data=[
            [
                "Developer pushes code to GitHub, but Jenkins does not trigger automatically. How do you troubleshoot?",
                "1. Verify Webhook payload URL: http://<ip>:9080/github-webhook/\n2. Ensure 'GitHub hook trigger for GITScm polling' is checked in Jenkins job.\n3. Check GitHub Webhook delivery history for HTTP 200 OK.",
                "Common failures include wrong port, firewall blocking incoming GitHub POST requests, or missing trailing slash in webhook URL."
            ],
            [
                "Build fails with 'mvn: command not found' in Jenkins console.",
                "Ensure 'def mvnHome = tool \"Maven\"' is defined in Jenkinsfile and matches exact name in Jenkins -> Tools -> Maven.",
                "Pipelines require binding the Maven executable path from Jenkins tool installations."
            ],
            [
                "How do you securely push a Docker image to Docker Hub from Jenkins without hardcoding passwords in Jenkinsfile?",
                "Use Jenkins Credential Binding:\nwithCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'U', passwordVariable: 'P')]) {\n  sh 'echo $P | docker login -u $U --password-stdin'\n}",
                "Injects encrypted secrets as runtime environment variables and masks passwords from console logs (displays ****)."
            ],
            [
                "SET 6 Question: Configure pipeline to run every weekday at 6:00 PM automatically.",
                "In Build Triggers -> Check 'Build periodically' -> Enter cron expression: 0 18 * * 1-5",
                "Fields: Minute (0), Hour 18 (6 PM), Day of Month (*), Month (*), Day of Week (1-5 = Monday through Friday)."
            ]
        ],
        col_widths=[2.3, 2.5, 2.1]
    )

    b.add_h2("9.3 Kubernetes Scenarios")
    b.add_table(
        headers=["Exam Scenario Question", "Correct kubectl Solution", "Explanation"],
        data=[
            [
                "One pod in a deployment crashes. What does Kubernetes do?",
                "ReplicaSet detects current count (3) < desired count (4) and immediately schedules a new replacement pod.",
                "Demonstrates Kubernetes self-healing and desired state reconciliation."
            ],
            [
                "Deployment was scaled to 4 replicas, but 'kubectl get pods' only shows 2 running and 2 pending. Why?",
                "1. Insufficient cluster memory/CPU.\n2. Node is out of resources.\nCheck cause with: kubectl describe pod <pending-pod-name>.",
                "Events section in describe output explains whether failure is due to Insufficient cpu or FailedScheduling."
            ],
            [
                "You updated deployment to a bad image tag that crashes on boot (CrashLoopBackOff). How do you roll back instantly?",
                "kubectl rollout undo deployment/my-app",
                "Reverts the pod template to the previous working ReplicaSet revision with zero downtime."
            ],
            [
                "How do you verify whether all pods and services were deleted completely?",
                "kubectl get all",
                "Should display only the default 'service/kubernetes' ClusterIP."
            ]
        ],
        col_widths=[2.3, 2.4, 2.2]
    )

    b.add_h2("9.4 AWS EC2 Scenarios")
    b.add_table(
        headers=["Exam Scenario Question", "Correct AWS / Ubuntu Solution", "Explanation"],
        data=[
            [
                "SSH connection to EC2 fails with 'Permission denied (publickey)'. What do you check?",
                "1. Check key permissions in Ubuntu: chmod 400 ~/.ssh/devops-key.pem\n2. Verify username: 'ubuntu' for Ubuntu AMI ('ec2-user' for Amazon Linux).\n3. Ensure Port 22 is open in Security Group.",
                "Wrong username or permissive key permissions (0644/0777) cause immediate SSH client rejection."
            ],
            [
                "Application is running inside EC2 on port 9090, but browser shows ERR_CONNECTION_TIMED_OUT on http://<Public-IP>:9090.",
                "Add Inbound Rule in EC2 Security Group: Type: Custom TCP | Port: 9090 | Source: 0.0.0.0/0.",
                "AWS security groups are stateful firewalls that drop all unlisted incoming port traffic by default."
            ],
            [
                "How do you ensure application database data survives if the EC2 instance is stopped and restarted?",
                "Attach an Amazon EBS (Elastic Block Store) volume and store database data on it.",
                "EBS root and attached storage volumes persist data across instance stop/start cycles."
            ]
        ],
        col_widths=[2.3, 2.4, 2.2]
    )

    # =========================================================================
    # MODULE 10: MASTER LOOKUP & QUICK REFERENCE TABLES
    # =========================================================================
    b.add_page_break()
    b.add_h1("10. Master Lookup & Quick Reference Tables")

    b.add_h2("10.1 Exam Repository URLs for All 9 Sets")
    b.add_table(
        headers=["Exam Set", "Application Name", "Official GitHub Repository URL", "Packaging"],
        data=[
            ["SET 1", "Library Management System", "https://github.com/deepthisagar7/library-management.git", "WAR (Tomcat)"],
            ["SET 2", "Metro Rail Reservation", "https://github.com/deepthisagar7/metro-reservation.git", "WAR (Tomcat)"],
            ["SET 3", "AI Online Learning System (AI-OLMS)", "https://github.com/deepthisagar7/AI-OLMS.git", "WAR (Tomcat)"],
            ["SET 4", "Hospital Management System", "https://github.com/Kumbhambhargavi75/HospitalManagementSystem.git", "WAR (Tomcat)"],
            ["SET 5", "Food Management System / Flask", "https://github.com/Kumbhambhargavi75/FoodSystem.git", "Python / Flask"],
            ["SET 6", "Campus Event Management System (CEMS)", "https://github.com/Kumbhambhargavi75/CEMS.git", "WAR (Tomcat)"],
            ["SET 7", "Online Ticket Reservation System (OLTRS)", "https://github.com/archanareddyse/OLTRS.git", "WAR (Tomcat)"],
            ["SET 8", "Online Ticket Reservation + Nagios", "https://github.com/archanareddyse/OLTRS.git", "WAR (Tomcat)"],
            ["SET 9", "Online Ticket Reservation Full CI/CD", "https://github.com/archanareddyse/OLTRS.git", "WAR (Tomcat)"]
        ],
        col_widths=[1.0, 2.3, 2.6, 1.0]
    )

    b.add_h2("10.2 Default Ports Reference Table")
    b.add_table(
        headers=["Service / Technology", "Default Container Port", "Recommended Ubuntu Host Port", "Reason / Notes"],
        data=[
            ["Apache Tomcat (Web App)", "8080", "9090", "Avoids collision with Jenkins default port 8080."],
            ["Jenkins Automation Server", "8080", "9080", "Mapped to 9080 so Tomcat can run on 8080 or 9090."],
            ["MySQL Database Engine", "3306", "3307", "Prevents conflict if MySQL is running natively on Ubuntu host."],
            ["Nagios Monitoring Server", "80", "8090", "Standard HTTP port 80 inside container mapped to 8090."],
            ["Nginx Reverse Proxy", "80", "80 or 8080", "Front-end routing container."],
            ["Python Flask Application", "5000", "5000", "Default Flask development / WSGI port."],
            ["Kubernetes NodePort Range", "Variable", "30000–32767", "Kubernetes assigned external port range."]
        ],
        col_widths=[1.8, 1.5, 1.7, 1.9]
    )

    b.add_h2("10.3 Default Credentials Reference Table")
    b.add_table(
        headers=["Tool / Service", "Default Username", "Default Password / Secret", "Location / Retrieval Command"],
        data=[
            ["Nagios Core Web UI", "nagiosadmin", "nagios", "Configured in container htpasswd file."],
            ["Jenkins Initial Unlock", "admin", "Hexadecimal string", "docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword"],
            ["MySQL Container (Compose)", "root / appuser", "root123 / apppass", "Set via MYSQL_ROOT_PASSWORD environment variable."],
            ["WordPress Web Admin", "admin (or user defined)", "Chosen in browser", "Configured during step 1 of WordPress web installation."],
            ["Ubuntu EC2 Cloud SSH", "ubuntu", "SSH Private Key (.pem)", "ssh -i ~/.ssh/devops-key.pem ubuntu@<IP>"],
            ["Amazon Linux EC2 SSH", "ec2-user", "SSH Private Key (.pem)", "ssh -i ~/.ssh/devops-key.pem ec2-user@<IP>"]
        ],
        col_widths=[1.8, 1.6, 1.7, 1.8]
    )

    # Save to both file names
    b.save("CHEATSHEET.docx")
    b.save("DevOps_Ubuntu_Cheatsheet.docx")
    print("Both CHEATSHEET.docx and DevOps_Ubuntu_Cheatsheet.docx created successfully!")

if __name__ == '__main__':
    build_complete_document()
