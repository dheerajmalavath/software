# 🚀 DevOps Complete Cheat Sheet
### Docker · Jenkins · Nagios · Kubernetes · AWS EC2
#### KMIT Lab Internal II — Software Engineering (23CC501PC)

> **Format of every entry:**
> ```
> ─────────────────────────────────────────
> 📌 WHAT IT DOES  →  expected output
> $ actual command or file content
> ─────────────────────────────────────────
> ```

---

## 📋 TABLE OF CONTENTS

1. [Docker — Multi-Container from GitHub](#1-docker--multi-container-from-github)
2. [Jenkins — Scripted Pipeline CI/CD](#2-jenkins--scripted-pipeline-cicd)
3. [Nagios — Monitoring via Docker](#3-nagios--monitoring-via-docker)
4. [Kubernetes — Deploy & Scale with Minikube](#4-kubernetes--deploy--scale-with-minikube)
5. [AWS EC2 — Cloud Deployment](#5-aws-ec2--cloud-deployment)
6. [Scenario Q&A — All 9 Sets](#6-scenario-qa--all-9-sets)

---
---

# 1. DOCKER — Multi-Container from GitHub

> **Exam scenario:** Given a GitHub repo link. Deploy the app + MySQL using Docker Compose.

---

## 1.1 — Clone the Repository

```
─────────────────────────────────────────────────────────────────────
📌 Downloads the project from GitHub onto your machine
   Output: "Cloning into 'OLTRS'..." then folder created
─────────────────────────────────────────────────────────────────────
$ git clone https://github.com/archanareddyse/OLTRS.git
```

```
─────────────────────────────────────────────────────────────────────
📌 Enter the project folder — ALL remaining commands run from HERE
   Output: prompt changes to show OLTRS folder
─────────────────────────────────────────────────────────────────────
$ cd OLTRS
```

---

## 1.2 — Inspect the Project

```
─────────────────────────────────────────────────────────────────────
📌 List files to understand the project structure
   Output: src/  target/  pom.xml  Dockerfile  etc.
─────────────────────────────────────────────────────────────────────
$ dir                        # Windows CMD
$ Get-ChildItem              # Windows PowerShell
$ ls                         # Linux/Mac
```

```
─────────────────────────────────────────────────────────────────────
📌 Find the WAR filename from pom.xml (needed in Dockerfile)
   Output: <finalName>ticket-reservation</finalName>
─────────────────────────────────────────────────────────────────────
$ Select-String "finalName" pom.xml         # PowerShell
$ grep finalName pom.xml                    # Linux
```

```
─────────────────────────────────────────────────────────────────────
📌 Check if it's WAR (web app) or JAR (plain Java)
   Output: <packaging>war</packaging>
─────────────────────────────────────────────────────────────────────
$ Select-String "packaging" pom.xml         # PowerShell
$ grep packaging pom.xml                    # Linux
```

---

## 1.3 — Build the WAR File (Maven)

```
─────────────────────────────────────────────────────────────────────
📌 Compiles source code + creates deployable WAR file in target/
   Output: [INFO] BUILD SUCCESS
           target/ticket-reservation.war
─────────────────────────────────────────────────────────────────────
$ mvn clean package -DskipTests
```

```
─────────────────────────────────────────────────────────────────────
📌 Same as above but also runs test cases
   Output: [INFO] Tests run: X, Failures: 0
─────────────────────────────────────────────────────────────────────
$ mvn clean install
```

```
─────────────────────────────────────────────────────────────────────
📌 Verify the WAR file was created
   Output: ticket-reservation.war   (or similar name)
─────────────────────────────────────────────────────────────────────
$ dir target\*.war              # PowerShell
$ ls target/*.war               # Linux
```

```
─────────────────────────────────────────────────────────────────────
📌 If Maven not installed locally — build using Docker's Maven image
   Output: [INFO] BUILD SUCCESS  (WAR created in target/)
─────────────────────────────────────────────────────────────────────
$ docker run --rm -v "${PWD}:/app" -w /app maven:3.9-eclipse-temurin-17 mvn clean package -DskipTests
```

---

## 1.4 — Write the Dockerfile

> Save as `Dockerfile` (no extension) in the project root (same level as pom.xml)

```
─────────────────────────────────────────────────────────────────────
📌 Dockerfile for a WAR app — packages it into Tomcat
   Use this when pom.xml has <packaging>war</packaging>
─────────────────────────────────────────────────────────────────────
```

```dockerfile
FROM tomcat:9.0

RUN rm -rf /usr/local/tomcat/webapps/*

COPY target/ticket-reservation.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080

CMD ["catalina.sh", "run"]
```

> ⚠️ Replace `ticket-reservation.war` with your actual `<finalName>` from pom.xml

```
─────────────────────────────────────────────────────────────────────
📌 Create Dockerfile in one shot from PowerShell (fastest in exam)
   Output: File 'Dockerfile' created
─────────────────────────────────────────────────────────────────────
$ @"
FROM tomcat:9.0
RUN rm -rf /usr/local/tomcat/webapps/*
COPY target/ticket-reservation.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD ["catalina.sh", "run"]
"@ | Out-File -FilePath Dockerfile -Encoding utf8
```

---

## 1.5 — Write docker-compose.yml

> Save in the SAME folder as Dockerfile

### Case A: Java App + MySQL (most common in exam)

```
─────────────────────────────────────────────────────────────────────
📌 docker-compose.yml — Tomcat app + MySQL database
   app runs at localhost:9090 | MySQL at port 3307 (use 3307 if 3306 is taken)
─────────────────────────────────────────────────────────────────────
```

```yaml
services:

  app:
    build: .
    container_name: myapp
    ports:
      - "9090:8080"
    depends_on:
      - db
    networks:
      - appnet

  db:
    image: mysql:8.0
    container_name: myapp-db
    environment:
      MYSQL_ROOT_PASSWORD: root123
      MYSQL_DATABASE: appdb
      MYSQL_USER: appuser
      MYSQL_PASSWORD: apppass
    volumes:
      - dbdata:/var/lib/mysql
    ports:
      - "3307:3306"
    networks:
      - appnet

volumes:
  dbdata:

networks:
  appnet:
    driver: bridge
```

### Case B: WordPress + MySQL (SET 1, SET 6)

```yaml
services:

  wordpress:
    image: wordpress:latest
    container_name: wordpress-app
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wpdb
    depends_on:
      - db
    volumes:
      - wpfiles:/var/www/html

  db:
    image: mysql:5.7
    container_name: wordpress-db
    environment:
      MYSQL_DATABASE: wpdb
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
      MYSQL_ROOT_PASSWORD: root123
    volumes:
      - wpdata:/var/lib/mysql

volumes:
  wpfiles:
  wpdata:
```

### Case C: Flask + Nginx (SET 5)

```yaml
services:

  flask:
    image: python:3.9-slim
    container_name: flask-api
    ports:
      - "5000:5000"
    working_dir: /app
    volumes:
      - ./app:/app
    command: python app.py

  nginx:
    image: nginx:latest
    container_name: nginx-web
    ports:
      - "80:80"
```

### Case D: App + Nagios (SET 8)

```yaml
services:

  app:
    build: .
    container_name: myapp
    ports:
      - "9090:8080"

  nagios:
    image: jasonrivers/nagios:latest
    container_name: nagios
    ports:
      - "8090:80"
```

---

## 1.6 — Docker Compose Commands (Run from Project Folder)

```
─────────────────────────────────────────────────────────────────────
📌 Build custom image from Dockerfile + start ALL containers in background
   Output: Container myapp  Started  ✔
           Container myapp-db  Started  ✔
─────────────────────────────────────────────────────────────────────
$ docker compose up --build -d
```

```
─────────────────────────────────────────────────────────────────────
📌 Start containers WITHOUT rebuilding image (image already built)
   Output: Container myapp  Started  ✔
─────────────────────────────────────────────────────────────────────
$ docker compose up -d
```

```
─────────────────────────────────────────────────────────────────────
📌 List running containers with status and port mappings
   Output: NAME     IMAGE    STATUS        PORTS
           myapp    myapp    Up 2 minutes  0.0.0.0:9090->8080/tcp
─────────────────────────────────────────────────────────────────────
$ docker compose ps
```

```
─────────────────────────────────────────────────────────────────────
📌 PAUSE all containers — containers survive, data safe, networks kept
   Output: Container myapp  Stopped  ✔
─────────────────────────────────────────────────────────────────────
$ docker compose stop
```

```
─────────────────────────────────────────────────────────────────────
📌 Resume previously stopped containers WITHOUT recreating them
   Output: Container myapp  Started  ✔
─────────────────────────────────────────────────────────────────────
$ docker compose start
```

```
─────────────────────────────────────────────────────────────────────
📌 Stop ONE specific service, keep others running
   Output: Container myapp-db  Stopped  ✔
─────────────────────────────────────────────────────────────────────
$ docker compose stop db
```

```
─────────────────────────────────────────────────────────────────────
📌 Stop + DELETE containers and networks (volumes kept, data safe)
   Output: Container myapp  Removed  ✔   Network appnet  Removed  ✔
─────────────────────────────────────────────────────────────────────
$ docker compose down
```

```
─────────────────────────────────────────────────────────────────────
📌 Stop + DELETE containers, networks AND volumes (all data wiped)
   Output: Container myapp  Removed  ✔   Volume dbdata  Removed  ✔
─────────────────────────────────────────────────────────────────────
$ docker compose down -v
```

```
─────────────────────────────────────────────────────────────────────
📌 Apply new service added to docker-compose.yml and start it
   Output: Container new-service  Created  ✔  Started  ✔
─────────────────────────────────────────────────────────────────────
$ docker compose up -d
```

```
─────────────────────────────────────────────────────────────────────
📌 View logs from all services
   Output: myapp    | Tomcat started on port 8080
           myapp-db | MySQL ready for connections
─────────────────────────────────────────────────────────────────────
$ docker compose logs
```

```
─────────────────────────────────────────────────────────────────────
📌 Follow live logs of one service (Ctrl+C to stop)
   Output: myapp | real-time log stream...
─────────────────────────────────────────────────────────────────────
$ docker compose logs -f app
```

```
─────────────────────────────────────────────────────────────────────
📌 Open interactive shell inside a running container
   Output: root@abc123:/usr/local/tomcat#
─────────────────────────────────────────────────────────────────────
$ docker compose exec app bash
```

```
─────────────────────────────────────────────────────────────────────
📌 Validate docker-compose.yml for syntax errors
   Output: Prints resolved config OR error message
─────────────────────────────────────────────────────────────────────
$ docker compose config
```

---

## 1.7 — Standalone Docker Commands (without Compose)

```
─────────────────────────────────────────────────────────────────────
📌 Download an image from Docker Hub
   Output: latest: Pulling from library/nginx  ...  Status: Downloaded
─────────────────────────────────────────────────────────────────────
$ docker pull nginx
$ docker pull mysql:8.0
$ docker pull tomcat:9.0
$ docker pull jasonrivers/nagios
$ docker pull jenkins/jenkins:lts
```

```
─────────────────────────────────────────────────────────────────────
📌 List all locally available images
   Output: REPOSITORY   TAG      IMAGE ID       SIZE
           tomcat       9.0      abc123def456   400MB
─────────────────────────────────────────────────────────────────────
$ docker images
```

```
─────────────────────────────────────────────────────────────────────
📌 Build a Docker image from Dockerfile in current folder
   Output: Successfully built abc123  Successfully tagged myapp:latest
─────────────────────────────────────────────────────────────────────
$ docker build -t myapp:latest .
```

```
─────────────────────────────────────────────────────────────────────
📌 Run a container in background with port mapping
   Output: container ID printed (long hex string)
─────────────────────────────────────────────────────────────────────
$ docker run -d -p 9090:8080 --name myapp myapp:latest
```

```
─────────────────────────────────────────────────────────────────────
📌 List all RUNNING containers
   Output: CONTAINER ID  IMAGE  STATUS  PORTS  NAMES
─────────────────────────────────────────────────────────────────────
$ docker ps
```

```
─────────────────────────────────────────────────────────────────────
📌 List ALL containers including stopped ones
   Output: Same as above but includes Exited containers
─────────────────────────────────────────────────────────────────────
$ docker ps -a
```

```
─────────────────────────────────────────────────────────────────────
📌 Stop a running container
   Output: myapp (container name echoed back)
─────────────────────────────────────────────────────────────────────
$ docker stop myapp
```

```
─────────────────────────────────────────────────────────────────────
📌 Remove a stopped container
   Output: myapp
─────────────────────────────────────────────────────────────────────
$ docker rm myapp
```

```
─────────────────────────────────────────────────────────────────────
📌 View logs of a running container
   Output: Tomcat started... MySQL ready...
─────────────────────────────────────────────────────────────────────
$ docker logs myapp
$ docker logs -f myapp        # follow live logs
```

```
─────────────────────────────────────────────────────────────────────
📌 Enter an interactive shell inside a running container
   Output: root@containerid:/#
─────────────────────────────────────────────────────────────────────
$ docker exec -it myapp bash
```

```
─────────────────────────────────────────────────────────────────────
📌 Create a custom Docker network for container communication
   Output: network ID printed
─────────────────────────────────────────────────────────────────────
$ docker network create appnet
```

```
─────────────────────────────────────────────────────────────────────
📌 Login to Docker Hub (needed before push)
   Output: Login Succeeded
─────────────────────────────────────────────────────────────────────
$ docker login
```

```
─────────────────────────────────────────────────────────────────────
📌 Tag image with Docker Hub username before pushing
   Output: (no output = success)
─────────────────────────────────────────────────────────────────────
$ docker tag myapp:latest yourusername/myapp:latest
```

```
─────────────────────────────────────────────────────────────────────
📌 Push image to Docker Hub
   Output: latest: digest: sha256:... pushed
─────────────────────────────────────────────────────────────────────
$ docker push yourusername/myapp:latest
```

---

## 1.8 — Complete Exam Flow (End-to-End)

```bash
# STEP 1 — Clone repo
git clone https://github.com/archanareddyse/OLTRS.git
cd OLTRS

# STEP 2 — Check WAR name
Select-String "finalName" pom.xml     # Remember: ticket-reservation

# STEP 3 — Build WAR
mvn clean package -DskipTests
dir target\*.war                       # Verify: ticket-reservation.war exists

# STEP 4 — Write Dockerfile (paste into Notepad, save as Dockerfile no extension)
# FROM tomcat:9.0
# RUN rm -rf /usr/local/tomcat/webapps/*
# COPY target/ticket-reservation.war /usr/local/tomcat/webapps/ROOT.war
# EXPOSE 8080
# CMD ["catalina.sh", "run"]

# STEP 5 — Write docker-compose.yml (paste into Notepad, save as docker-compose.yml)
# (use Case A template from section 1.5 above)

# STEP 6 — Start everything
docker compose up --build -d

# STEP 7 — Verify
docker compose ps                      # STATUS should say "Up"

# STEP 8 — Open browser
# http://localhost:9090

# STEP 9 — Cleanup
docker compose down -v
```

---
---

# 2. JENKINS — Scripted Pipeline CI/CD

> **Exam scenario:** Given a GitHub repo. Automate build, test, Docker push using Jenkins Pipeline.

---

## 2.1 — Start Jenkins via Docker

```
─────────────────────────────────────────────────────────────────────
📌 Start Jenkins container (port 9080 — avoids conflict with apps on 8080)
   Output: Container started, Jenkins accessible at localhost:9080
─────────────────────────────────────────────────────────────────────
$ docker run -d \
    --name jenkins \
    -p 9080:8080 \
    -p 50000:50000 \
    -v jenkins_home:/var/jenkins_home \
    jenkins/jenkins:lts
```

```
─────────────────────────────────────────────────────────────────────
📌 Get the initial admin unlock password
   Output: a32-character hex string e.g. 74317dd4e3b84be88878a845d2a05286
─────────────────────────────────────────────────────────────────────
$ docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

```
─────────────────────────────────────────────────────────────────────
📌 Follow Jenkins startup logs (wait for "Jenkins is fully up and running")
   Output: ...Jenkins is fully up and running
─────────────────────────────────────────────────────────────────────
$ docker logs -f jenkins
```

```
─────────────────────────────────────────────────────────────────────
📌 Stop Jenkins (data saved in volume)
   Output: jenkins
─────────────────────────────────────────────────────────────────────
$ docker stop jenkins
```

```
─────────────────────────────────────────────────────────────────────
📌 Start Jenkins again (all jobs/configs preserved)
   Output: jenkins
─────────────────────────────────────────────────────────────────────
$ docker start jenkins
```

---

## 2.2 — Jenkins Initial Setup (in Browser at localhost:9080)

```
─────────────────────────────────────────────────────────────────────
Step 1 → Paste unlock password → Click Continue
Step 2 → Click "Install suggested plugins" → Wait 3-5 mins
Step 3 → Create Admin User:
         Username : admin
         Password : admin123
         Full name: Admin
         Email    : admin@test.com
Step 4 → Keep URL as http://localhost:9080/ → Save and Finish
─────────────────────────────────────────────────────────────────────
🌐 URL: http://localhost:9080
```

---

## 2.3 — Configure Tools in Jenkins

```
─────────────────────────────────────────────────────────────────────
📌 Add Maven tool so pipelines can use mvn commands
   Navigate: Manage Jenkins → Tools → Maven → Add Maven
   Name     : Maven         ← EXACT name used in Jenkinsfile
   Version  : 3.9.x (Install automatically ✔)
─────────────────────────────────────────────────────────────────────
🌐 Manage Jenkins → Tools → Maven installations → Add Maven
```

```
─────────────────────────────────────────────────────────────────────
📌 Add Docker Hub credentials so pipeline can push images securely
   Navigate: Manage Jenkins → Credentials → Global → Add Credentials
   Kind    : Username with password
   Username: your-dockerhub-username
   Password: your-dockerhub-password
   ID      : dockerhub-creds      ← EXACT ID used in Jenkinsfile
─────────────────────────────────────────────────────────────────────
🌐 Manage Jenkins → Credentials → System → Global credentials → Add
```

---

## 2.4 — Jenkinsfile Templates

### Template A — Basic Build + Test (Freestyle-style pipeline)

```groovy
node {
    def mvnHome = tool 'Maven'

    stage('Checkout') {
        git url: 'https://github.com/archanareddyse/OLTRS.git',
            branch: 'main'
    }

    stage('Build') {
        sh "${mvnHome}/bin/mvn clean install -DskipTests"
    }

    stage('Test') {
        sh "${mvnHome}/bin/mvn test"
    }

    stage('Package') {
        sh "${mvnHome}/bin/mvn package"
    }
}
```

### Template B — Build + Docker Build + Docker Push

```groovy
node {
    def mvnHome = tool 'Maven'

    stage('Checkout') {
        git url: 'https://github.com/archanareddyse/OLTRS.git',
            branch: 'main'
    }

    stage('Build') {
        sh "${mvnHome}/bin/mvn clean install -DskipTests"
    }

    stage('Test') {
        sh "${mvnHome}/bin/mvn test"
    }

    stage('Docker Build') {
        sh "docker build -t yourusername/oltrs:latest ."
    }

    stage('Docker Push') {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {
            sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
            sh "docker push ${DOCKER_USER}/oltrs:latest"
        }
    }
}
```

### Template C — With Email Notification on Failure

```groovy
node {
    def mvnHome = tool 'Maven'

    try {
        stage('Checkout') {
            git url: 'https://github.com/archanareddyse/OLTRS.git',
                branch: 'main'
        }

        stage('Build') {
            sh "${mvnHome}/bin/mvn clean install -DskipTests"
        }

        stage('Test') {
            sh "${mvnHome}/bin/mvn test"
        }

        stage('Docker Build') {
            sh "docker build -t yourusername/oltrs:latest ."
        }

        stage('Docker Push') {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )]) {
                sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                sh "docker push ${DOCKER_USER}/oltrs:latest"
            }
        }

        // Email on SUCCESS
        emailext(
            subject: "✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "Build passed! URL: ${env.BUILD_URL}",
            to: 'team@example.com'
        )

    } catch (e) {
        // Email ONLY on FAILURE
        emailext(
            subject: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "Build failed!\nError: ${e.getMessage()}\nLogs: ${env.BUILD_URL}console",
            to: 'team@example.com'
        )
        throw e
    }
}
```

### Template D — Intentional Failure (to test email alert)

```groovy
node {
    def mvnHome = tool 'Maven'

    try {
        stage('Checkout') {
            git url: 'https://github.com/archanareddyse/OLTRS.git'
        }
        stage('Build') {
            sh "${mvnHome}/bin/mvn clean install -DskipTests"
        }
        stage('Force Fail') {
            sh "this-command-does-not-exist"    // ← intentional failure
        }
    } catch (e) {
        emailext(
            subject: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "Error: ${e.getMessage()}",
            to: 'team@example.com'
        )
        throw e
    }
}
```

### Template E — Declarative Pipeline (alternative syntax)

```groovy
pipeline {
    agent any
    tools {
        maven 'Maven'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/archanareddyse/OLTRS.git'
            }
        }
        stage('Build') {
            steps { sh 'mvn clean install -DskipTests' }
        }
        stage('Test') {
            steps { sh 'mvn test' }
        }
        stage('Package') {
            steps { sh 'mvn package' }
        }
    }
    post {
        failure {
            emailext subject: "FAILED: ${env.JOB_NAME}",
                     body: "Build failed",
                     to: 'team@example.com'
        }
        success {
            echo 'Build successful!'
        }
    }
}
```

---

## 2.5 — Create Pipeline Job in Jenkins UI

```
─────────────────────────────────────────────────────────────────────
📌 Create a new Pipeline job in Jenkins
─────────────────────────────────────────────────────────────────────
Step 1 → Click "New Item" in sidebar
Step 2 → Enter name: OLTRS-Pipeline
Step 3 → Select "Pipeline" → Click OK
Step 4 → Build Triggers: tick "GitHub hook trigger for GITScm polling"
Step 5 → Pipeline section → Definition: "Pipeline script"
Step 6 → Paste Jenkinsfile from Template B or C above
Step 7 → Click Save
Step 8 → Click "Build Now"
Step 9 → Click build number → "Console Output" to see logs
```

---

## 2.6 — Scheduled Build Trigger (Cron)

```
─────────────────────────────────────────────────────────────────────
📌 Auto-run pipeline at a specific time (SET 6 asks 6 PM daily)
   Navigate: Job → Configure → Build Triggers → "Build periodically"
─────────────────────────────────────────────────────────────────────
Every day at 6:00 PM  →  0 18 * * *
Every day at 9:00 AM  →  0 9 * * *
Every 15 minutes      →  H/15 * * * *
Every weekday 9 AM    →  0 9 * * 1-5
```

---

## 2.7 — Useful Jenkins Navigation Cheat Sheet

```
─────────────────────────────────────────────────────────────────────
See which stage failed     →  Job → Build # → Stage View
See error details          →  Job → Build # → Console Output
Install plugins            →  Manage Jenkins → Plugins → Available
Add Maven tool             →  Manage Jenkins → Tools → Maven
Add credentials            →  Manage Jenkins → Credentials → Global
Configure email (SMTP)     →  Manage Jenkins → System → Email
Restart Jenkins            →  http://localhost:9080/restart
─────────────────────────────────────────────────────────────────────
```

---
---

# 3. NAGIOS — Monitoring via Docker

> **Exam scenario:** Monitor server/application availability, check CPU/memory/HTTP status.

---

## 3.1 — Start Nagios via Docker

```
─────────────────────────────────────────────────────────────────────
📌 Pull and run Nagios monitoring container
   Output: Container nagios Started ✔
─────────────────────────────────────────────────────────────────────
$ docker run -d \
    -p 8090:80 \
    --name nagios \
    jasonrivers/nagios:latest
```

```
─────────────────────────────────────────────────────────────────────
📌 Access Nagios web dashboard
   Username: nagiosadmin    Password: nagios
─────────────────────────────────────────────────────────────────────
🌐 URL: http://localhost:8090/nagios
```

```
─────────────────────────────────────────────────────────────────────
📌 Verify Nagios container is running
   Output: nagios   jasonrivers/nagios   Up 2 minutes   0.0.0.0:8090->80/tcp
─────────────────────────────────────────────────────────────────────
$ docker ps | findstr nagios
```

```
─────────────────────────────────────────────────────────────────────
📌 Enter Nagios container to edit config files
   Output: root@containerid:/opt/nagios#
─────────────────────────────────────────────────────────────────────
$ docker exec -it nagios bash
```

---

## 3.2 — Nagios Config Files (inside container)

```
─────────────────────────────────────────────────────────────────────
📌 Key config file locations inside the Nagios container
─────────────────────────────────────────────────────────────────────
Main config    →  /opt/nagios/etc/nagios.cfg
Hosts config   →  /opt/nagios/etc/objects/hosts.cfg
Services config→  /opt/nagios/etc/objects/services.cfg
Commands config→  /opt/nagios/etc/objects/commands.cfg
Contacts config→  /opt/nagios/etc/objects/contacts.cfg
```

---

## 3.3 — Sample Host Definition

```
─────────────────────────────────────────────────────────────────────
📌 Define a host to monitor (add inside container → hosts.cfg)
   This tells Nagios WHICH machine to watch
─────────────────────────────────────────────────────────────────────
```

```cfg
define host {
    use             linux-server
    host_name       webserver01
    alias           My Web Server
    address         192.168.1.100
    max_check_attempts  3
    check_period        24x7
    notification_period 24x7
}
```

---

## 3.4 — Sample Service Definition

```
─────────────────────────────────────────────────────────────────────
📌 Define a service check (add to services.cfg)
   This tells Nagios WHAT to check on the host
─────────────────────────────────────────────────────────────────────
```

```cfg
# Check if HTTP is responding
define service {
    use                 generic-service
    host_name           webserver01
    service_description HTTP Check
    check_command       check_http
    max_check_attempts  3
    check_interval      5
    notification_interval 60
}

# Check CPU load
define service {
    use                 generic-service
    host_name           webserver01
    service_description CPU Load
    check_command       check_load!5.0!4.0!3.0!10.0!6.0!4.0
    check_interval      5
}

# Check disk usage
define service {
    use                 generic-service
    host_name           webserver01
    service_description Disk Usage
    check_command       check_disk!20%!10%!/
    check_interval      5
}
```

---

## 3.5 — Nagios Status Reference

```
─────────────────────────────────────────────────────────────────────
OK       (Green)  → Everything normal
WARNING  (Yellow) → Approaching threshold (e.g. CPU > 80%)
CRITICAL (Red)    → Severe problem (e.g. service down, CPU > 95%)
UNKNOWN  (Orange) → Cannot determine status (check failed to run)
─────────────────────────────────────────────────────────────────────
```

---

## 3.6 — Common Nagios Plugins

```
─────────────────────────────────────────────────────────────────────
check_ping    →  Is host reachable?
check_http    →  Is web server (Tomcat/Nginx) responding?
check_disk    →  Is disk usage within limits?
check_load    →  Is CPU load acceptable?
check_procs   →  Are expected processes running?
check_mysql   →  Is MySQL responding?
check_smtp    →  Is mail server working?
─────────────────────────────────────────────────────────────────────
```

---

## 3.7 — Nagios via Docker Compose (with App — SET 8)

```yaml
services:

  app:
    build: .
    container_name: myapp
    ports:
      - "9090:8080"
    networks:
      - monnet

  nagios:
    image: jasonrivers/nagios:latest
    container_name: nagios
    ports:
      - "8090:80"
    networks:
      - monnet

networks:
  monnet:
    driver: bridge
```

```
─────────────────────────────────────────────────────────────────────
📌 Start both app and Nagios together
   App URL    → http://localhost:9090
   Nagios URL → http://localhost:8090/nagios
─────────────────────────────────────────────────────────────────────
$ docker compose up -d
```

---
---

# 4. KUBERNETES — Deploy & Scale with Minikube

> **Exam scenario:** Deploy app from Docker Hub image, expose as NodePort service, scale to 4 replicas.

---

## 4.1 — Start Minikube

```
─────────────────────────────────────────────────────────────────────
📌 Start a local single-node Kubernetes cluster
   Output: Done! kubectl is now configured to use "minikube" cluster
─────────────────────────────────────────────────────────────────────
$ minikube start
```

```
─────────────────────────────────────────────────────────────────────
📌 Check Minikube is running
   Output: minikube: Running   kubectl: Correctly Configured
─────────────────────────────────────────────────────────────────────
$ minikube status
```

```
─────────────────────────────────────────────────────────────────────
📌 Open Kubernetes web dashboard in browser
   Output: Browser opens with K8s dashboard
─────────────────────────────────────────────────────────────────────
$ minikube dashboard
```

```
─────────────────────────────────────────────────────────────────────
📌 Get Minikube's IP address (needed for NodePort access)
   Output: 192.168.49.2  (or similar)
─────────────────────────────────────────────────────────────────────
$ minikube ip
```

---

## 4.2 — kubectl Cluster Info

```
─────────────────────────────────────────────────────────────────────
📌 List all nodes in the cluster
   Output: NAME       STATUS   ROLES           AGE   VERSION
           minikube   Ready    control-plane   2m    v1.31.0
─────────────────────────────────────────────────────────────────────
$ kubectl get nodes
```

```
─────────────────────────────────────────────────────────────────────
📌 Show cluster API server address and services
   Output: Kubernetes control plane running at https://...
─────────────────────────────────────────────────────────────────────
$ kubectl cluster-info
```

---

## 4.3 — Create Deployment

```
─────────────────────────────────────────────────────────────────────
📌 Create a Deployment from a Docker Hub image
   Output: deployment.apps/myapp created
─────────────────────────────────────────────────────────────────────
$ kubectl create deployment myapp --image=yourusername/oltrs:latest
```

```
─────────────────────────────────────────────────────────────────────
📌 List all deployments
   Output: NAME    READY   UP-TO-DATE   AVAILABLE   AGE
           myapp   1/1     1            1           30s
─────────────────────────────────────────────────────────────────────
$ kubectl get deployments
```

```
─────────────────────────────────────────────────────────────────────
📌 Get detailed info about a deployment (use for troubleshooting)
   Output: Name, Namespace, Replicas, Conditions, Events
─────────────────────────────────────────────────────────────────────
$ kubectl describe deployment myapp
```

---

## 4.4 — Manage Pods

```
─────────────────────────────────────────────────────────────────────
📌 List all pods in default namespace
   Output: NAME                    READY   STATUS    RESTARTS   AGE
           myapp-abc123-xyz789     1/1     Running   0          45s
─────────────────────────────────────────────────────────────────────
$ kubectl get pods
```

```
─────────────────────────────────────────────────────────────────────
📌 List pods with node assignment info
   Output: Same + NODE column showing which node each pod runs on
─────────────────────────────────────────────────────────────────────
$ kubectl get pods -o wide
```

```
─────────────────────────────────────────────────────────────────────
📌 Detailed pod info — use when pod won't start (check Events section)
   Output: Status, Conditions, Volumes, Events (errors shown here)
─────────────────────────────────────────────────────────────────────
$ kubectl describe pod myapp-abc123-xyz789
```

```
─────────────────────────────────────────────────────────────────────
📌 View pod logs (stdout of the app running inside)
   Output: Tomcat started... application ready...
─────────────────────────────────────────────────────────────────────
$ kubectl logs myapp-abc123-xyz789
```

```
─────────────────────────────────────────────────────────────────────
📌 Delete a pod — Kubernetes AUTOMATICALLY creates a new one
   Output: pod "myapp-abc123" deleted  → new pod appears in kubectl get pods
─────────────────────────────────────────────────────────────────────
$ kubectl delete pod myapp-abc123-xyz789
```

```
─────────────────────────────────────────────────────────────────────
📌 Enter a running pod's shell
   Output: root@myapp-abc123:/#
─────────────────────────────────────────────────────────────────────
$ kubectl exec -it myapp-abc123-xyz789 -- bash
```

---

## 4.5 — Scale Deployment (EXAM FAVORITE — always 4 replicas)

```
─────────────────────────────────────────────────────────────────────
📌 Scale deployment to 4 replicas (asked in EVERY exam set)
   Output: deployment.apps/myapp scaled
─────────────────────────────────────────────────────────────────────
$ kubectl scale deployment myapp --replicas=4
```

```
─────────────────────────────────────────────────────────────────────
📌 Verify 4 pods are running
   Output: NAME            READY   STATUS    AGE
           myapp-xxx-1     1/1     Running   10s
           myapp-xxx-2     1/1     Running   10s
           myapp-xxx-3     1/1     Running   10s
           myapp-xxx-4     1/1     Running   10s
─────────────────────────────────────────────────────────────────────
$ kubectl get pods
```

```
─────────────────────────────────────────────────────────────────────
📌 Check deployment shows READY 4/4
   Output: NAME    READY   UP-TO-DATE   AVAILABLE
           myapp   4/4     4            4
─────────────────────────────────────────────────────────────────────
$ kubectl get deployments
```

---

## 4.6 — Create Service (Expose App to Browser)

```
─────────────────────────────────────────────────────────────────────
📌 Expose deployment as NodePort service (accessible from browser)
   Output: service/myapp exposed
─────────────────────────────────────────────────────────────────────
$ kubectl expose deployment myapp \
    --type=NodePort \
    --port=80 \
    --target-port=8080
```

```
─────────────────────────────────────────────────────────────────────
📌 List services
   Output: NAME    TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)
           myapp   NodePort   10.96.xxx.xxx  <none>        80:30080/TCP
─────────────────────────────────────────────────────────────────────
$ kubectl get services
```

```
─────────────────────────────────────────────────────────────────────
📌 Get the full service details (check ENDPOINTS — if <none>, labels mismatch)
   Output: Name, Selector, Endpoints, Port mappings
─────────────────────────────────────────────────────────────────────
$ kubectl describe service myapp
```

```
─────────────────────────────────────────────────────────────────────
📌 Get the browser URL to access the app through Minikube
   Output: http://192.168.49.2:30080  (open this in browser)
─────────────────────────────────────────────────────────────────────
$ minikube service myapp --url
```

```
─────────────────────────────────────────────────────────────────────
📌 Open the app directly in browser (Minikube does it automatically)
   Output: Browser opens with the app
─────────────────────────────────────────────────────────────────────
$ minikube service myapp
```

---

## 4.7 — Rolling Update and Rollback

```
─────────────────────────────────────────────────────────────────────
📌 Update the app to a new image version
   Output: deployment.apps/myapp image updated
─────────────────────────────────────────────────────────────────────
$ kubectl set image deployment/myapp myapp=yourusername/oltrs:v2
```

```
─────────────────────────────────────────────────────────────────────
📌 Watch the rolling update progress
   Output: Waiting for deployment... deployment "myapp" successfully rolled out
─────────────────────────────────────────────────────────────────────
$ kubectl rollout status deployment myapp
```

```
─────────────────────────────────────────────────────────────────────
📌 Rollback to previous working version
   Output: deployment.apps/myapp rolled back
─────────────────────────────────────────────────────────────────────
$ kubectl rollout undo deployment myapp
```

---

## 4.8 — Delete Resources

```
─────────────────────────────────────────────────────────────────────
📌 Delete a deployment (also deletes its ReplicaSet and Pods)
   Output: deployment.apps "myapp" deleted
─────────────────────────────────────────────────────────────────────
$ kubectl delete deployment myapp
```

```
─────────────────────────────────────────────────────────────────────
📌 Delete a service
   Output: service "myapp" deleted
─────────────────────────────────────────────────────────────────────
$ kubectl delete service myapp
```

```
─────────────────────────────────────────────────────────────────────
📌 Verify everything was deleted
   Output: No resources found in default namespace.
─────────────────────────────────────────────────────────────────────
$ kubectl get pods
$ kubectl get services
$ kubectl get deployments
```

---

## 4.9 — List Everything at Once

```
─────────────────────────────────────────────────────────────────────
📌 Show all resources in default namespace
   Output: pods, services, deployments, replicasets all listed
─────────────────────────────────────────────────────────────────────
$ kubectl get all
```

---

## 4.10 — YAML Deployment File (alternative to kubectl create)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 4
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp              # ← MUST match selector.matchLabels
    spec:
      containers:
      - name: myapp
        image: yourusername/oltrs:latest
        ports:
        - containerPort: 8080
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp                  # ← MUST match pod labels above
  type: NodePort
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080             # Range: 30000–32767
```

```
─────────────────────────────────────────────────────────────────────
📌 Apply YAML files to create/update resources
   Output: deployment.apps/myapp created   service/myapp-service created
─────────────────────────────────────────────────────────────────────
$ kubectl apply -f deployment.yaml
$ kubectl apply -f service.yaml
```

---

## 4.11 — Complete Exam Flow (End-to-End)

```bash
# 1. Start cluster
minikube start
minikube status

# 2. Create deployment from your Docker Hub image
kubectl create deployment myapp --image=yourusername/oltrs:latest

# 3. Verify pod is running
kubectl get pods

# 4. Scale to 4 replicas
kubectl scale deployment myapp --replicas=4
kubectl get pods          # all 4 should show Running

# 5. Expose as NodePort service
kubectl expose deployment myapp --type=NodePort --port=80 --target-port=8080

# 6. Get browser URL
minikube service myapp --url

# 7. Open that URL in browser ✅

# 8. Demonstrate pod auto-recovery
kubectl delete pod <any-pod-name>
kubectl get pods          # new pod appears automatically

# 9. Rollback if needed
kubectl rollout undo deployment myapp

# 10. Cleanup
kubectl delete deployment myapp
kubectl delete service myapp
kubectl get all           # verify empty
```

---
---

# 5. AWS EC2 — Cloud Deployment

> **Exam scenario:** Launch EC2 instance, deploy Docker app, make it accessible via public IP.

---

## 5.1 — Launch EC2 Instance (AWS Console in Browser)

```
─────────────────────────────────────────────────────────────────────
📌 Launch a free-tier EC2 instance step by step
─────────────────────────────────────────────────────────────────────
Step 1 → Login: https://console.aws.amazon.com
Step 2 → Search "EC2" in top bar → Click EC2
Step 3 → Click "Launch Instance" (orange button)

Configure:
  Name           : my-app-server
  AMI            : Ubuntu Server 22.04 LTS (Free tier eligible)
  Instance type  : t2.micro (Free tier eligible)
  Key pair       : Create new → name it "mykey" → Download .pem file
                   ⚠️ SAVE THIS FILE — you cannot download again!
  Security group : Create new → Add rules:
                   SSH    Port 22   Source: Anywhere (0.0.0.0/0)
                   HTTP   Port 80   Source: Anywhere (0.0.0.0/0)
                   Custom Port 8080 Source: Anywhere (0.0.0.0/0)
                   Custom Port 9090 Source: Anywhere (0.0.0.0/0)
  Storage        : 8 GB gp3 (default, free tier)

Step 4 → Click "Launch Instance"
Step 5 → Wait 1–2 minutes for status to show "Running"
Step 6 → Note the PUBLIC IPv4 address (shown in instance details)
```

---

## 5.2 — Connect to EC2 via SSH

```
─────────────────────────────────────────────────────────────────────
📌 Connect from Windows PowerShell using the .pem key file
   Output: Welcome to Ubuntu 22.04... ubuntu@ip-xxx:~$
─────────────────────────────────────────────────────────────────────
$ cd C:\Users\YourName\Downloads       # go to where .pem was saved
$ ssh -i "mykey.pem" ubuntu@<EC2-PUBLIC-IP>
```

```
─────────────────────────────────────────────────────────────────────
📌 If you get permission error on .pem file (Windows fix)
   Output: Permissions fixed
─────────────────────────────────────────────────────────────────────
$ icacls "mykey.pem" /inheritance:r /grant:r "%USERNAME%":"(R)"
$ ssh -i "mykey.pem" ubuntu@<EC2-PUBLIC-IP>
```

```
─────────────────────────────────────────────────────────────────────
📌 Alternative: Connect via Browser (no .pem needed)
   AWS Console → EC2 → Instances → Select instance → Connect
   → Choose "EC2 Instance Connect" → Click Connect
   Output: Browser terminal opens ✅
─────────────────────────────────────────────────────────────────────
🌐 AWS Console → EC2 → Instances → Connect → EC2 Instance Connect
```

---

## 5.3 — Setup EC2 After Connecting (run inside EC2 terminal)

```
─────────────────────────────────────────────────────────────────────
📌 Update package list (always do this first)
   Output: ...Reading package lists... Done
─────────────────────────────────────────────────────────────────────
$ sudo apt-get update -y
```

```
─────────────────────────────────────────────────────────────────────
📌 Install Docker on Ubuntu EC2
   Output: ...Setting up docker.io... done
─────────────────────────────────────────────────────────────────────
$ sudo apt-get install -y docker.io
```

```
─────────────────────────────────────────────────────────────────────
📌 Start Docker service and enable auto-start on reboot
   Output: (no output = success)
─────────────────────────────────────────────────────────────────────
$ sudo systemctl start docker
$ sudo systemctl enable docker
```

```
─────────────────────────────────────────────────────────────────────
📌 Add ubuntu user to docker group (run docker without sudo)
   Output: (logout and login again to apply)
─────────────────────────────────────────────────────────────────────
$ sudo usermod -aG docker ubuntu
$ exit
$ ssh -i "mykey.pem" ubuntu@<EC2-PUBLIC-IP>    # reconnect
```

```
─────────────────────────────────────────────────────────────────────
📌 Install git (to clone GitHub repos)
   Output: ...Setting up git... done
─────────────────────────────────────────────────────────────────────
$ sudo apt-get install -y git
```

```
─────────────────────────────────────────────────────────────────────
📌 Install Maven (to build WAR files)
   Output: ...Setting up maven... done
─────────────────────────────────────────────────────────────────────
$ sudo apt-get install -y maven
```

---

## 5.4 — Deploy App on EC2

```
─────────────────────────────────────────────────────────────────────
📌 Clone GitHub repo onto EC2
   Output: Cloning into 'OLTRS'...
─────────────────────────────────────────────────────────────────────
$ git clone https://github.com/archanareddyse/OLTRS.git
$ cd OLTRS
```

```
─────────────────────────────────────────────────────────────────────
📌 Build the WAR file
   Output: [INFO] BUILD SUCCESS
─────────────────────────────────────────────────────────────────────
$ mvn clean package -DskipTests
```

```
─────────────────────────────────────────────────────────────────────
📌 Build Docker image
   Output: Successfully built abc123  Successfully tagged oltrs:latest
─────────────────────────────────────────────────────────────────────
$ docker build -t oltrs:latest .
```

```
─────────────────────────────────────────────────────────────────────
📌 Run the container on port 9090
   Output: container ID printed
─────────────────────────────────────────────────────────────────────
$ docker run -d -p 9090:8080 --name myapp oltrs:latest
```

```
─────────────────────────────────────────────────────────────────────
📌 Verify container is running
   Output: CONTAINER ID  IMAGE  STATUS  PORTS
─────────────────────────────────────────────────────────────────────
$ docker ps
```

```
─────────────────────────────────────────────────────────────────────
📌 Access app in browser
   Replace <EC2-PUBLIC-IP> with the IPv4 shown in AWS Console
─────────────────────────────────────────────────────────────────────
🌐 http://<EC2-PUBLIC-IP>:9090
```

---

## 5.5 — Deploy index.html with Nginx (Simple Website — SET 4, 5, 6)

```
─────────────────────────────────────────────────────────────────────
📌 Create a simple HTML file and serve it with Nginx
   Access: http://<EC2-PUBLIC-IP>  (port 80)
─────────────────────────────────────────────────────────────────────
$ echo "<h1>Hello from EC2!</h1>" > index.html
$ docker run -d -p 80:80 \
    -v $(pwd)/index.html:/usr/share/nginx/html/index.html \
    --name webserver nginx
```

---

## 5.6 — Deploy from GitHub with Custom Dockerfile

```bash
# Clone repo that has only HTML/static files + create Dockerfile
git clone https://github.com/Kumbhambhargavi75/HospitalManagementSystem
cd HospitalManagementSystem

# Create Dockerfile for Nginx static site
cat > Dockerfile << 'EOF'
FROM nginx:latest
COPY . /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
EOF

# Build and run
docker build -t hospital-site .
docker run -d -p 80:80 --name hospital hospital-site

# Access: http://<EC2-PUBLIC-IP>
```

---

## 5.7 — EC2 Security Group Rules (Fix Access Issues)

```
─────────────────────────────────────────────────────────────────────
📌 Add inbound rule to allow traffic on a specific port
   Navigate: EC2 → Instances → Click instance → Security tab
           → Click Security Group → Edit Inbound Rules → Add Rule
─────────────────────────────────────────────────────────────────────
SSH access (port 22)  → Type: SSH,         Source: 0.0.0.0/0
HTTP (port 80)        → Type: HTTP,        Source: 0.0.0.0/0
App port 8080         → Type: Custom TCP,  Port: 8080, Source: 0.0.0.0/0
App port 9090         → Type: Custom TCP,  Port: 9090, Source: 0.0.0.0/0
MySQL port 3306       → Type: MySQL/Aurora,Source: 0.0.0.0/0
```

---

## 5.8 — EC2 Cleanup

```
─────────────────────────────────────────────────────────────────────
📌 Stop the Docker container on EC2 (run inside EC2 terminal)
   Output: myapp
─────────────────────────────────────────────────────────────────────
$ docker stop myapp
$ docker rm myapp
```

```
─────────────────────────────────────────────────────────────────────
📌 Terminate EC2 instance (AWS Console — PERMANENT, cannot undo)
   EC2 → Instances → Select → Instance State → Terminate
─────────────────────────────────────────────────────────────────────
🌐 AWS Console → EC2 → Instances → Select → Instance State → Terminate
```

---
---

# 6. SCENARIO Q&A — All 9 Sets

> These exact scenario questions appear in every paper (5 marks each). Know these cold.

---

## Docker Compose Scenarios

| Q | Answer |
|---|--------|
| Stop all services without removing containers? | `docker compose stop` |
| Start stopped containers without recreating? | `docker compose start` |
| Remove containers + network after testing? | `docker compose down` |
| New service added — apply and start? | `docker compose up -d` |
| Stop only backend, keep others running? | `docker compose stop backend` |
| WordPress starts before MySQL and crashes? | Add `depends_on: - db` to wordpress service |
| Protect DB data when MySQL container stops? | Use named volume: `dbdata:/var/lib/mysql` |
| MySQL crashes while app is running? | App loses DB connection → restart MySQL to recover |
| Run web service with 3 replicas? | `docker compose up --scale web=3 -d` |

---

## Jenkins Pipeline Scenarios

| Q | Answer |
|---|--------|
| Developer pushes but Jenkins doesn't trigger? | Check: webhook URL set in GitHub, "GitHub hook trigger" enabled in job, Jenkins reachable from internet |
| Maven fails — skip Docker stages? | `try-catch`: exception in Build stage skips all stages after it |
| Docker Hub push fails (auth error)? | Credentials not added in Jenkins. Go to: Manage Jenkins → Credentials → add with ID `dockerhub-creds` |
| Which stage failed — how to find? | Jenkins Job → Build # → Stage View (red = failed stage) |
| Error details of a failed stage? | Jenkins Job → Build # → Console Output |
| Email only on failure, not success? | Put `emailext` only inside `catch(e)` block |
| Email on both success and failure? | Put success `emailext` after try block, failure `emailext` in catch block |
| Run pipeline at 6 PM daily? | Build Triggers → Build Periodically → `0 18 * * *` |
| Intentionally fail to test email? | Add `sh "invalid-command"` as a stage |

---

## Kubernetes Scenarios

| Q | Answer |
|---|--------|
| Scale from 2 to 4 replicas? | `kubectl scale deployment myapp --replicas=4` |
| Verify 4 replicas running? | `kubectl get pods` (4 rows) OR `kubectl get deployments` (READY: 4/4) |
| Pods running but can't access from browser? | NodePort Service missing → `kubectl expose deployment myapp --type=NodePort --port=80 --target-port=8080` |
| 4 replicas set but only 2 running — why? | `kubectl describe deployment myapp` → check Events. `kubectl describe pod <pending-pod>` → check image pull errors |
| Service created but ENDPOINTS = `<none>`? | Label mismatch! Service `selector` doesn't match pod `labels`. Check: `kubectl describe service myapp` vs `kubectl get pods --show-labels` |
| Delete deployment and service? | `kubectl delete deployment myapp` + `kubectl delete service myapp` |
| Verify resources deleted? | `kubectl get all` → should show nothing |
| One pod crashes — what happens? | ReplicaSet automatically creates a new pod to maintain desired count |
| Demonstrate auto-recovery? | `kubectl delete pod <name>` → `kubectl get pods` → new pod appears |
| Rollback failed update? | `kubectl rollout undo deployment myapp` |

---

## AWS EC2 Scenarios

| Q | Answer |
|---|--------|
| Can't SSH into EC2? | Check: (1) Port 22 inbound rule in Security Group (2) `.pem` permissions `icacls key.pem /inheritance:r` (3) Correct user: `ubuntu` for Ubuntu AMI (4) Instance is Running state |
| App on port 8080 not accessible via public IP? | Add Custom TCP inbound rule for port 8080 in Security Group |
| EC2 has no public IP? | Assign an **Elastic IP** to the instance from EC2 console |
| Data must survive EC2 stop/start? | Use **EBS volume** (default root volume persists when stopped) |
| Allow HTTP but restrict SSH to admins only? | Port 80: Source `0.0.0.0/0` (open) · Port 22: Source admin's specific IP e.g. `203.x.x.x/32` |
| Tomcat stops while EC2 is running? | App unreachable, but instance is up. SSH in and restart: `docker restart myapp` |
| Terminate instance — cleanup? | `docker stop myapp` + `docker rm myapp` → AWS Console → Terminate instance |

---
---

# QUICK REFERENCE — Exam Repo URLs

| Set | Repo | App Name |
|-----|------|----------|
| SET 1 | `github.com/deepthisagar7/library-management` | Library Management |
| SET 2 | `github.com/deepthisagar7/metro-reservation` | Metro Reservation |
| SET 3 | `github.com/deepthisagar7/AI-OLMS` | AI Online Learning |
| SET 4, 5 | `github.com/Kumbhambhargavi75/HospitalManagementSystem` | Hospital Mgmt |
| SET 5 (Q1) | `github.com/Kumbhambhargavi75/FoodSystem` | Food Management |
| SET 6 | `github.com/Kumbhambhargavi75/CEMS` | Campus Event Mgmt |
| SET 7, 8, 9 | `github.com/archanareddyse/OLTRS` | Online Ticket Reservation |

---

# QUICK REFERENCE — Port Numbers

| Service | Container Port | Host Port |
|---------|---------------|-----------|
| Tomcat/App | 8080 | 9090 (use 9090 to avoid conflicts) |
| Nginx | 80 | 80 or 8080 |
| MySQL | 3306 | 3307 (use 3307 if 3306 is taken locally) |
| Jenkins | 8080 | 9080 (use 9080 to avoid conflicts) |
| Nagios | 80 | 8090 |
| Flask | 5000 | 5000 |
| K8s NodePort | any | 30000–32767 |

---

# QUICK REFERENCE — Default Credentials

| Tool | Username | Password |
|------|----------|----------|
| Nagios | `nagiosadmin` | `nagios` |
| Jenkins (first setup) | see `initialAdminPassword` | - |
| MySQL (in compose) | `root` | `root123` |
| WordPress | set during first browser setup | - |
| AWS Console | your email | your password |
| EC2 SSH (Ubuntu) | `ubuntu` | (use .pem key) |
| EC2 SSH (Amazon Linux) | `ec2-user` | (use .pem key) |
