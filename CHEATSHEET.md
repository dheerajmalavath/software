# DevOps Complete Cheat Sheet & Practical Manual
### Ubuntu Linux Edition · Git · Maven · Docker · Jenkins · Nagios · Kubernetes · AWS EC2
#### KMIT Lab Internal II — Software Engineering (23CC501PC)

---

> 📌 **CRITICAL UBUNTU LINUX DIRECTIVE:** All commands and file editing in this guide are engineered for Ubuntu (Linux). Use `nano` or `vim` for editing (Ctrl+O to save, Enter, Ctrl+X to exit), `chmod 400` for EC2 keys, `ls -la` for directory listings, and standard Linux forward slashes (`/`). Do not use Windows commands like `notepad`, `dir`, or `icacls`.

---

## TABLE OF CONTENTS
- [0. Master Blueprint — Parameter Discovery & Configuration Customization](#0-master-blueprint)
- [1. Git & GitHub — Version Control & Collaboration in Ubuntu](#1-git--github)
- [2. Maven Build Automation with Eclipse IDE & Ubuntu CLI](#2-maven-with-eclipse--cli)
- [3. Docker & Docker CLI — Container Management on Ubuntu](#3-docker--docker-cli)
- [4. Docker Compose & Dockerfile — Multi-Container Interdependent Services](#4-docker-compose--dockerfile)
- [5. Jenkins — CI/CD Pipeline Automation in Ubuntu](#5-jenkins-cicd)
- [6. Kubernetes — Container Orchestration & Scaling with Minikube](#6-kubernetes-with-minikube)
- [7. Nagios — Infrastructure & Application Monitoring in Ubuntu](#7-nagios-monitoring)
- [8. AWS EC2 — Cloud Deployment on Ubuntu Instance](#8-aws-ec2-deployment)
- [9. Scenario-Based Questions & Solutions (All 9 Exam Sets)](#9-scenario-qa)
- [10. Master Lookup & Quick Reference Tables](#10-quick-reference-tables)

---

# 0. Master Blueprint

## 0.1 Parameter Discovery in Ubuntu
Before writing any Dockerfile, docker-compose.yml, Jenkinsfile, or Kubernetes YAML, extract values from the project files:

**■ Task / Explanation:** Inspect `pom.xml` to determine whether the app generates a WAR or JAR file and find the output package name.
```bash
cat pom.xml | grep -E '<packaging>|<artifactId>|<version>|<finalName>'
```
*✔ Expected Output / Verification:* Output displays packaging type (`<packaging>war</packaging>`) and artifact details. If packaging is omitted, it defaults to JAR.

**■ Task / Explanation:** Check database credentials in application properties.
```bash
cat src/main/resources/application.properties 2>/dev/null || cat src/main/resources/config.properties
```
*✔ Expected Output / Verification:* Displays `spring.datasource.url`, database name, username, and password.

**■ Task / Explanation:** Inspect local Ubuntu ports to prevent port conflicts before running containers.
```bash
sudo netstat -tuln | grep -E '8080|9090|3306|3307|9080|8090'
```
*✔ Expected Output / Verification:* Lists listening ports. If a port is busy, choose an alternate host port mapping.

---

# 1. Git & GitHub

## 1.1 Installing and Configuring Git on Ubuntu

**■ Task / Explanation:** Update Ubuntu package repositories and install Git CLI.
```bash
sudo apt update && sudo apt install -y git
git --version
```
*✔ Expected Output / Verification:* `git version 2.34.1` (or latest).

**■ Task / Explanation:** Configure author name, email, and standard main branch.
```bash
git config --global user.name "dheerajmalavath"
git config --global user.email "dheerajmalavath@gmail.com"
git config --global init.defaultBranch main
git config --list
```
*✔ Expected Output / Verification:* Lists configured user parameters and global settings.

## 1.2 SSH Key Pair Generation for GitHub Authentication

**■ Task / Explanation:** Generate an ED25519 SSH key pair on Ubuntu and display the public key to paste into GitHub Settings.
```bash
ssh-keygen -t ed25519 -C "dheerajmalavath@gmail.com" -f ~/.ssh/id_ed25519 -N ""
cat ~/.ssh/id_ed25519.pub
```
*✔ Expected Output / Verification:* Prints public key `ssh-ed25519 AAAAC3...`. Copy and paste into GitHub → Settings → SSH and GPG keys.

**■ Task / Explanation:** Verify SSH authentication with GitHub servers from Ubuntu terminal.
```bash
ssh -T git@github.com
```
*✔ Expected Output / Verification:* `Hi dheerajmalavath! You've successfully authenticated, but GitHub does not provide shell access.`

## 1.3 Local Repository Lifecycle & History

**■ Task / Explanation:** Initialize repository, create files with nano, stage, and commit.
```bash
mkdir -p ~/projects/lab-demo && cd ~/projects/lab-demo
git init
nano README.md
# Enter: # DevOps Project (Save: Ctrl+O, Enter, Ctrl+X)
git add .
git commit -m "feat: initial commit with project readme"
git log --oneline --graph --decorate
```
*✔ Expected Output / Verification:* `[main (root-commit) 5b2a1c0] feat: initial commit with project readme`.

## 1.4 Undoing & Stashing Changes

**■ Task / Explanation:** Discard unstaged working modifications or unstage a staged file.
```bash
# Revert unstaged changes in a file:
git restore app.py
# Unstage a file from the index:
git restore --staged app.py
# Temporarily stash uncommitted changes:
git stash
git stash list
git stash pop
```
*✔ Expected Output / Verification:* Restores pristine state or applies stashed changes back cleanly.

## 1.5 Remote Management, Branching & Merge Conflicts

**■ Task / Explanation:** Link remote repository and push upstream to GitHub.
```bash
git remote add origin https://github.com/dheerajmalavath/software.git
git remote -v
git branch -M main
git push -u origin main
```
*✔ Expected Output / Verification:* `Branch 'main' set up to track remote branch 'main' from 'origin'.`

**■ Task / Explanation:** Create a feature branch, commit, and merge into main.
```bash
git checkout -b feature-auth
echo "auth_token = True" >> auth.py
git add auth.py && git commit -m "feat: implement authentication"
git switch main
git merge feature-auth
```
*✔ Expected Output / Verification:* Fast-forward merge updating main branch.

**■ Task / Explanation:** Step-by-Step Merge Conflict Resolution in Ubuntu.
```bash
# If git merge produces: CONFLICT (content): Merge conflict in file.txt
# Step 1: Open conflicting file with nano:
nano file.txt
# Step 2: Locate <<<<<<< HEAD, =======, >>>>>>> markers and edit desired content.
# Step 3: Save file: Ctrl+O, Enter, Ctrl+X
# Step 4: Finalize merge:
git add file.txt
git commit -m "fix: resolve merge conflict between main and feature-auth"
```
*✔ Expected Output / Verification:* `Merge made by the 'ort' strategy.`

---

# 2. Maven with Eclipse & CLI

## 2.1 Standard Maven Architecture
- `src/main/java`: Application source code (.java)
- `src/main/resources`: Configuration properties and DB credentials
- `src/main/webapp`: Web application root (`WEB-INF/web.xml`, JSP files for WAR packages)
- `src/test/java`: Automated JUnit unit test cases
- `target/`: Build outputs (.class, .jar, .war)
- `pom.xml`: Project Object Model dependencies and build plugins

## 2.2 Installing Maven and JDK 17 on Ubuntu
```bash
sudo apt update && sudo apt install -y openjdk-17-jdk maven
mvn -version
```
*✔ Expected Output / Verification:* `Apache Maven 3.6.3 / 3.8.x`, `Java version: 17.0.x`.

## 2.3 Creating Maven Projects in Eclipse IDE (Step-by-Step UI)

| Project Type | Eclipse Navigation | Archetype Selection | Metadata Values |
| :--- | :--- | :--- | :--- |
| **Java Application** | File → New → Other... → Maven Project | `org.apache.maven.archetypes : maven-archetype-quickstart (1.4)` | GroupId: `com.example`, ArtifactId: `my-java-app` |
| **Web Application (WAR)** | File → New → Other... → Maven Project | `org.apache.maven.archetypes : maven-archetype-webapp (1.4)` | GroupId: `com.example`, ArtifactId: `my-web-app` |

## 2.4 Configuring pom.xml & Eclipse Builds

**■ Task / Explanation:** Add Java 17 compiler plugin and build project.
```xml
<build>
  <finalName>my-web-app</finalName>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>3.11.0</version>
      <configuration>
        <source>17</source>
        <target>17</target>
      </configuration>
    </plugin>
  </plugins>
</build>
```

**■ Task / Explanation:** Build WAR package from Ubuntu CLI terminal.
```bash
cd ~/projects/my-web-app
mvn clean package -DskipTests
ls -la target/*.war
```
*✔ Expected Output / Verification:* `[INFO] BUILD SUCCESS` and `target/my-web-app.war` generated.

---

# 3. Docker & Docker CLI

## 3.1 Docker Installation and Daemon Status on Ubuntu
```bash
sudo apt update && sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER && newgrp docker
docker --version
```
*✔ Expected Output / Verification:* `Docker version 24.x.x, build ...` and active (running) daemon status.

## 3.2 Container Lifecycle CLI Operations

**■ Task / Explanation:** Pull standard images and run Redis container in background with port forwarding.
```bash
docker pull redis:latest
docker run -d --name my-redis -p 6379:6379 redis:latest
docker ps
```
*✔ Expected Output / Verification:* Container listed with status `Up` and port mapping `0.0.0.0:6379->6379/tcp`.

**■ Task / Explanation:** Inspect live logs and launch interactive shell inside container.
```bash
docker logs --tail 20 my-redis
docker exec -it my-redis /bin/sh
```
*✔ Expected Output / Verification:* Gives root shell inside container prompt (`#`). Type `exit` to return.

**■ Task / Explanation:** Manage persistent volumes and custom bridge networks.
```bash
# Create volume:
docker volume create dbdata
# Create network:
docker network create my-net
# Run MySQL with volume & network:
docker run -d --name mysql-db --network my-net -v dbdata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 mysql:8.0
```
*✔ Expected Output / Verification:* Data persists inside `dbdata` volume even if container is destroyed.

---

# 4. Docker Compose & Dockerfile

## 4.1 Writing the Dockerfile for Tomcat Web Apps in Ubuntu
```bash
nano Dockerfile
```
```dockerfile
FROM tomcat:9.0-jdk11-openjdk-slim
RUN rm -rf /usr/local/tomcat/webapps/*
COPY target/*.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD ["catalina.sh", "run"]
```

## 4.2 Multi-Container docker-compose.yml Templates

### Case A: Java Web Application + MySQL Database (SET 2, 3, 4, 7, 8, 9)
```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: oltrs-app
    ports:
      - "9090:8080"
    depends_on:
      - db
    environment:
      DB_HOST: db
      DB_NAME: oltrsdb
      DB_USER: appuser
      DB_PASS: apppass
    networks:
      - appnet
    restart: always

  db:
    image: mysql:8.0
    container_name: oltrs-db
    environment:
      MYSQL_ROOT_PASSWORD: root123
      MYSQL_DATABASE: oltrsdb
      MYSQL_USER: appuser
      MYSQL_PASSWORD: apppass
    ports:
      - "3307:3306"
    volumes:
      - dbdata:/var/lib/mysql
    networks:
      - appnet
    restart: always

volumes:
  dbdata:

networks:
  appnet:
    driver: bridge
```

## 4.3 Docker Compose CLI Commands
```bash
# Build and start services in background:
docker compose up --build -d

# Check status of compose services:
docker compose ps

# View real-time logs of app service:
docker compose logs -f app

# Stop services without deleting containers:
docker compose stop

# Resume services:
docker compose start

# Delete containers and networks (keeping volumes):
docker compose down

# Delete containers, networks, AND persistent volumes:
docker compose down -v
```

---

# 5. Jenkins CI/CD

## 5.1 Starting Jenkins in Docker on Ubuntu
```bash
docker run -d \
  --name jenkins \
  --restart=always \
  -p 9080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

# Retrieve initial admin unlock password:
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
*✔ Expected Output / Verification:* Outputs 32-character hexadecimal key. Open `http://localhost:9080` to unlock.

## 5.2 Jenkins Pipeline Groovy Script (Scripted Pipeline Box)
```groovy
node {
    def mvnHome = tool 'Maven'
    
    stage('Checkout') {
        echo 'Cloning repository from GitHub...'
        git url: 'https://github.com/archanareddyse/OLTRS.git', branch: 'main'
    }
    
    stage('Build') {
        echo 'Compiling and Packaging WAR file...'
        sh "${mvnHome}/bin/mvn clean package -DskipTests"
    }
    
    stage('Test') {
        echo 'Executing Automated Unit Tests...'
        sh "${mvnHome}/bin/mvn test"
    }
    
    stage('Docker Build & Push') {
        echo 'Building Docker image...'
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
            sh '''
                docker build -t dheerajmalavath/oltrs:latest .
                echo $DH_PASS | docker login -u $DH_USER --password-stdin
                docker push dheerajmalavath/oltrs:latest
            '''
        }
    }
}
```

## 5.3 Scheduled Triggers & Webhooks
- **GitHub Webhook:** In repo Settings → Webhooks → Payload URL: `http://<ip>:9080/github-webhook/`, Content type: `application/json`.
- **Cron Scheduled Build:** Under Build Triggers → Build periodically:
  - `0 18 * * *` — Every day at 6:00 PM.
  - `H/15 * * * *` — Every 15 minutes.

---

# 6. Kubernetes with Minikube

## 6.1 Minikube & kubectl Setup in Ubuntu
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
minikube start --driver=docker
kubectl cluster-info
```

## 6.2 Deployment, Scaling to 4 Replicas & Self-Healing Demo
```bash
# 1. Create deployment:
kubectl create deployment my-app --image=dheerajmalavath/oltrs:latest

# 2. Scale to 4 replicas (Exam Favorite):
kubectl scale deployment my-app --replicas=4
kubectl get pods -o wide

# 3. Expose as NodePort service:
kubectl expose deployment my-app --type=NodePort --port=8080 --target-port=8080
minikube service my-app --url

# 4. Demonstrate Self-Healing:
kubectl delete pod <pod-name>
# Observe ReplicaSet immediately creates replacement pod to maintain 4/4 count:
kubectl get pods
```

## 6.3 Rolling Update and Rollback
```bash
# Update image:
kubectl set image deployment/my-app oltrs=dheerajmalavath/oltrs:v2
kubectl rollout status deployment/my-app

# Rollback failed deployment:
kubectl rollout undo deployment/my-app
```

---

# 7. Nagios Monitoring

## 7.1 Running Nagios in Docker
```bash
docker run -d --name nagios --restart=always -p 8090:80 jasonrivers/nagios:latest
docker ps | grep nagios
```
*✔ Expected Output / Verification:* Web UI accessible at `http://localhost:8090`. Default login: `nagiosadmin` / `nagios`.

## 7.2 Nagios UI Navigation
- **Tactical Overview:** Global bird's-eye view of network health.
- **Hosts:** Monitored servers with status UP/DOWN.
- **Services:** HTTP, PING, SSH, and disk monitoring checks.
- **Service Problems:** Filtered alert list showing only WARNING and CRITICAL issues.
- **Event Log:** Chronological log of alerts and recovery actions.

## 7.3 Status Codes
- `0`: **OK** (Green) — Healthy.
- `1`: **WARNING** (Yellow) — Threshold reached.
- `2`: **CRITICAL** (Red) — Service down / port unresponsive.
- `3`: **UNKNOWN** (Orange) — Check error.

---

# 8. AWS EC2 Deployment

## 8.1 Launching Ubuntu Server on EC2
1. Console → EC2 → Launch Instance.
2. Name: `devops-ubuntu-server`.
3. AMI: **Ubuntu Server 22.04 LTS (HVM)**, 64-bit (x86).
4. Instance Type: `t2.micro` (Free tier).
5. Key Pair: RSA, `.pem` format (e.g. `devops-key.pem`).
6. Security Group: Allow SSH (Port 22) and HTTP (Port 80).

## 8.2 SSH Connection from Ubuntu Terminal (Setting Key Permissions)
```bash
# Crucial in Ubuntu: Set read-only 400 permissions on key file
mkdir -p ~/.ssh
mv ~/Downloads/devops-key.pem ~/.ssh/
chmod 400 ~/.ssh/devops-key.pem

# Connect to EC2 instance:
ssh -i ~/.ssh/devops-key.pem ubuntu@<EC2-PUBLIC-IP>
```
*✔ Expected Output / Verification:* `Welcome to Ubuntu 22.04 LTS`.

## 8.3 Unblocking Port 9090 in AWS Security Group
1. EC2 Console → Security Groups → Click your Security Group.
2. Inbound rules tab → Click **Edit inbound rules**.
3. Add rule: Type: `Custom TCP` | Port range: `9090` | Source: `Anywhere-IPv4 (0.0.0.0/0)`.
4. Click **Save rules**. Port is reachable immediately on `http://<EC2-PUBLIC-IP>:9090`.

---

# 9. Scenario Q&A

| Category | Question | Solution |
| :--- | :--- | :--- |
| **Compose** | Stop all services without deleting containers? | `docker compose stop` |
| **Compose** | Remove containers + volumes completely? | `docker compose down -v` |
| **Compose** | App crashes before DB is ready? | Add `depends_on: - db` in `docker-compose.yml` |
| **Jenkins** | Developer pushes code but Jenkins doesn't trigger? | Check webhook URL `http://<ip>:9080/github-webhook/` and push event. |
| **Jenkins** | Hide Docker Hub password in Jenkinsfile? | Use `withCredentials([usernamePassword(...)])`. |
| **K8s** | Pod crashes in deployment? | ReplicaSet automatically schedules a replacement pod. |
| **K8s** | Rollback bad image update? | `kubectl rollout undo deployment/<name>` |
| **AWS** | SSH fails with "Permission denied (publickey)"? | Run `chmod 400 key.pem` and verify user is `ubuntu`. |
| **AWS** | App running on port 9090 unreachable over internet? | Add Inbound Rule for Custom TCP port 9090 in Security Group. |

---

# 10. Quick Reference Tables

### Exam Repositories (Sets 1 to 9)
| Set | App Name | GitHub Repository URL | Packaging |
| :--- | :--- | :--- | :--- |
| **SET 1** | Library Management | `github.com/deepthisagar7/library-management` | WAR |
| **SET 2** | Metro Reservation | `github.com/deepthisagar7/metro-reservation` | WAR |
| **SET 3** | AI Online Learning | `github.com/deepthisagar7/AI-OLMS` | WAR |
| **SET 4, 5** | Hospital Management | `github.com/Kumbhambhargavi75/HospitalManagementSystem` | WAR |
| **SET 5 (Q1)**| Food System / Flask | `github.com/Kumbhambhargavi75/FoodSystem` | Python |
| **SET 6** | Campus Events (CEMS) | `github.com/Kumbhambhargavi75/CEMS` | WAR |
| **SET 7, 8, 9**| Online Ticket Reservation | `github.com/archanareddyse/OLTRS` | WAR |

### Default Ports
| Service | Container Port | Host Port |
| :--- | :--- | :--- |
| Tomcat Web App | 8080 | 9090 |
| Jenkins CI | 8080 | 9080 |
| MySQL Database | 3306 | 3307 |
| Nagios Core | 80 | 8090 |
| Flask App | 5000 | 5000 |
| Kubernetes NodePort | Variable | 30000–32767 |

### Default Credentials
| Tool | Username | Password |
| :--- | :--- | :--- |
| Nagios | `nagiosadmin` | `nagios` |
| Jenkins | `admin` | See `initialAdminPassword` |
| MySQL | `root` | `root123` |
| EC2 Ubuntu | `ubuntu` | `.pem` private key |
