"""
Viva Question and Answer Data Store for Topic 5: Jenkins CI/CD Automation (50 questions).
"""

JENKINS_QUESTIONS = [
    (
        "What is Continuous Integration (CI) and Continuous Delivery/Deployment (CD)?",
        "• Continuous Integration (CI): The practice of frequently committing code to a shared repository (multiple times daily) where automated builds and unit tests execute immediately to detect regressions early.\n"
        "• Continuous Delivery (CD): Automatically packaging and preparing tested code for release to staging/production with a single manual approval click.\n"
        "• Continuous Deployment: Fully automated pipeline where every passing commit automatically deploys directly to production with zero manual intervention."
    ),
    (
        "What role does Jenkins play in a DevOps lifecycle?",
        "Jenkins serves as the central automation orchestrator. It listens for code pushes from Git, checks out code, invokes Maven to compile and run tests, "
        "builds Docker container images, scans for security flaws, pushes images to Docker Hub, and triggers deployments to Kubernetes or AWS."
    ),
    (
        "How is Jenkins deployed inside a Docker container on Ubuntu?",
        "Run the following command:\n"
        "$ docker run -d --name jenkins --restart=always -p 9080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts\n"
        "Exposes port 9080 for web dashboard and mounts volume 'jenkins_home' to persist configurations."
    ),
    (
        "What ports does Jenkins expose by default, and what are their purposes? (8080 and 50000)",
        "• Port 8080 (mapped to 9080): HTTP web interface port used by administrators and developers to access the Jenkins dashboard.\n"
        "• Port 50000: JNLP (Java Network Launch Protocol) agent connection port used by distributed Jenkins worker/agent nodes to communicate with the controller."
    ),
    (
        "Why is '-v jenkins_home:/var/jenkins_home' critical when running Jenkins in Docker?",
        "All Jenkins job configurations, build histories, plugins, user credentials, and secrets reside inside '/var/jenkins_home'. "
        "Mounting a persistent volume ensures that when the Jenkins container is stopped, updated, or recreated, all jobs, credentials, and settings remain completely intact."
    ),
    (
        "How do you retrieve the initial admin password to unlock Jenkins on Ubuntu?",
        "Run inside the container volume:\n"
        "$ docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword\n"
        "Outputs a 32-character hexadecimal key to paste into the browser unlock screen at http://localhost:9080."
    ),
    (
        "What are suggested plugins during initial Jenkins setup?",
        "Suggested plugins include Git, Pipeline, Folders, OWASP Markup Formatter, Credentials Binding, Timestamper, Workspace Cleanup, "
        "Ant, Gradle, Mailer, and SSH Slaves. They provide the fundamental baseline for version control and pipeline orchestration."
    ),
    (
        "How do you manage and install new plugins in Jenkins?",
        "1. In Jenkins dashboard, click 'Manage Jenkins' on the left sidebar.\n"
        "2. Click 'Plugins' → Select the 'Available plugins' tab.\n"
        "3. Search for plugin names (e.g. 'Maven Integration', 'Docker Pipeline').\n"
        "4. Check the desired checkboxes and click 'Install without restart'."
    ),
    (
        "What plugins are essential for a Java/DevOps CI/CD pipeline in Jenkins? (Git, Pipeline, Maven, Docker)",
        "• Git Plugin: Pulls source code from GitHub repositories.\n"
        "• Pipeline Plugin: Enables writing Jenkinsfile Pipeline-as-Code.\n"
        "• Maven Integration Plugin: Integrates Maven tools, automated test parsing, and goals.\n"
        "• Docker Pipeline & Docker Plugin: Enables building, running, and pushing Docker images within pipeline stages."
    ),
    (
        "What is a Freestyle project in Jenkins?",
        "A Freestyle project is a legacy, UI-driven job configuration model in Jenkins. "
        "Users configure repository URLs, build steps, and post-build actions through dropdowns, text boxes, and checkboxes in the Jenkins web browser interface."
    ),
    (
        "How do you configure a Git repository in a Freestyle project?",
        "Under the 'Source Code Management' section in the job configuration:\n"
        "1. Select 'Git'.\n"
        "2. In 'Repository URL', enter: 'https://github.com/archanareddyse/OLTRS.git'.\n"
        "3. Provide credentials if private, or leave 'None' if public."
    ),
    (
        "How do you specify the build branch (e.g. '*/main') in Jenkins?",
        "In the 'Branches to build' field, enter '*/main' (or '*/master'). "
        "Always verify on GitHub whether the repository's default branch is 'main' or 'master' to avoid 'Couldn't find any revision to build' errors."
    ),
    (
        "How do you invoke Maven targets in a Freestyle project?",
        "Under the 'Build Steps' section:\n"
        "1. Click 'Add build step' dropdown → Select 'Invoke top-level Maven targets'.\n"
        "2. In 'Maven Version', select configured tool (e.g. 'Maven').\n"
        "3. In 'Goals', type: 'clean package -DskipTests'."
    ),
    (
        "What are Post-build Actions in a Freestyle project?",
        "Post-build actions execute after build steps complete. Examples include: (1) Archiving build artifacts (e.g. 'target/*.war'), "
        "(2) Publishing JUnit test result reports, (3) Sending email failure notifications, and (4) Triggering downstream build jobs."
    ),
    (
        "What is an Artifact in Jenkins, and how is it archived?",
        "An artifact is a binary file produced by a build (e.g. 'ticket-reservation.war' or JAR file). "
        "Under Post-build Actions, select 'Archive the artifacts' and enter 'target/*.war'. "
        "Jenkins stores this file on the controller, displaying a clickable download link on the job summary page."
    ),
    (
        "What is a Jenkins Pipeline?",
        "A Jenkins Pipeline is a suite of plugins that supports implementing and integrating continuous delivery pipelines into Jenkins. "
        "It models an entire software delivery workflow from version control to production as code."
    ),
    (
        "What is a Jenkinsfile, and why is Pipeline-as-Code superior to Freestyle jobs?",
        "A 'Jenkinsfile' is a text file checked directly into the root of a Git repository containing the pipeline definition. "
        "Advantages over Freestyle: (1) Version controlled alongside application code, (2) Code reviewed via Pull Requests, (3) Disaster recovery is instant, and (4) Complex multi-branch logic is easily expressed."
    ),
    (
        "What are the two types of Jenkins Pipeline syntax? (Declarative vs Scripted)",
        "• Declarative Pipeline: A structured, opinionated syntax enclosed in 'pipeline { ... }' with strict predefined sections ('agent', 'stages', 'steps', 'post'). Easier to read and recommended for most standard CI/CD pipelines.\n"
        "• Scripted Pipeline: A flexible, code-centric Groovy-based syntax enclosed in 'node { ... }'. Provides maximum programmatic power, loops, conditional logic, and exception handling."
    ),
    (
        "What is the fundamental structure of a Scripted Pipeline? (node { ... })",
        "node {\n"
        "    stage('Checkout') { git url: '...' }\n"
        "    stage('Build') { sh 'mvn clean compile' }\n"
        "    stage('Test') { sh 'mvn test' }\n"
        "    stage('Deploy') { sh 'docker run ...' }\n"
        "}"
    ),
    (
        "What is the fundamental structure of a Declarative Pipeline? (pipeline { agent any ... })",
        "pipeline {\n"
        "    agent any\n"
        "    stages {\n"
        "        stage('Build') {\n"
        "            steps { sh 'mvn clean compile' }\n"
        "        }\n"
        "    }\n"
        "    post {\n"
        "        always { cleanWs() }\n"
        "    }\n"
        "}"
    ),
    (
        "What is a 'stage' in a Jenkins Pipeline?",
        "A 'stage' represents a major logical phase of the CI/CD pipeline (e.g. 'Checkout', 'Build', 'Test', 'Docker Build', 'Deploy'). "
        "Jenkins Stage View UI renders each stage as a distinct graphical column displaying execution time and status (green/red)."
    ),
    (
        "What is a 'step' in a Jenkins Pipeline?",
        "A 'step' is a single basic task that tells Jenkins what action to perform within a stage (e.g. 'sh', 'git', 'echo', 'mail', 'tool', 'archiveArtifacts')."
    ),
    (
        "What is an 'agent' in Declarative Pipeline?",
        "The 'agent' directive specifies WHERE the pipeline or a specific stage will execute. "
        "'agent any' runs on any available agent node; 'agent { docker { image 'maven:3.8-openjdk-17' } }' executes inside an isolated container."
    ),
    (
        "How do you configure the Maven tool in Jenkins Global Tool Configuration?",
        "1. Manage Jenkins → 'Tools'.\n"
        "2. Scroll down to 'Maven installations' → Click 'Add Maven'.\n"
        "3. Enter Name: 'Maven' (matches 'tool \"Maven\"' in Jenkinsfile).\n"
        "4. Check 'Install automatically' → Select version 3.9.x → Click 'Save'."
    ),
    (
        "How do you reference the configured Maven tool inside a Scripted Pipeline? (def mvnHome = tool 'Maven')",
        "In Groovy script box:\n"
        "def mvnHome = tool 'Maven'\n"
        "This resolves the absolute installation path of the Maven executable on disk, allowing commands to be executed via: 'sh \"${mvnHome}/bin/mvn clean package\"'."
    ),
    (
        "What does 'sh \"${mvnHome}/bin/mvn clean package\"' do inside a Jenkins pipeline on Ubuntu?",
        "It invokes the Linux shell ('sh') step to run the Maven executable on Ubuntu, compiling the code, running tests, and generating the packaged artifact (.war/.jar) inside the workspace."
    ),
    (
        "How does Jenkins handle credentials securely? (Credentials Store)",
        "Jenkins provides a centralized encrypted Credentials Store. Credentials are encrypted using master encryption keys and stored at 'credentials.xml'. "
        "Pipelines reference credentials safely by an assigned ID (e.g. 'dockerhub-creds') without exposing plaintext secrets in code."
    ),
    (
        "What credential types are supported in Jenkins?",
        "• Secret text: API tokens, GitHub Personal Access Tokens (PAT).\n"
        "• Username with password: For Docker Hub, database logins, basic auth.\n"
        "• SSH Username with private key: For SSH access to remote deployment servers (AWS EC2).\n"
        "• Secret file: For SSL certificates, Kubernetes kubeconfig files."
    ),
    (
        "How do you bind credentials in a Scripted Pipeline? (withCredentials([usernamePassword(...)])",
        "withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {\n"
        "    sh 'echo $DH_PASS | docker login -u $DH_USER --password-stdin'\n"
        "}"
    ),
    (
        "Why does Jenkins mask credentials in console output with ****?",
        "Jenkins has a built-in credential masking filter that intercepts console output. If an environment variable injected by 'withCredentials' "
        "is echoed to stdout, Jenkins automatically masks the plaintext password with '****' to prevent security leaks in build logs."
    ),
    (
        "How do you build and push a Docker image to Docker Hub inside a Jenkins pipeline?",
        "stage('Docker Build & Push') {\n"
        "    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {\n"
        "        sh '''\n"
        "            docker build -t dheerajmalavath/oltrs:latest .\n"
        "            echo $DH_PASS | docker login -u $DH_USER --password-stdin\n"
        "            docker push dheerajmalavath/oltrs:latest\n"
        "        '''\n"
        "    }\n"
        "}"
    ),
    (
        "What is the purpose of Docker Pipeline plugin in Jenkins?",
        "It allows Jenkins pipelines to run build steps dynamically inside temporary Docker containers (e.g. 'docker.image(\"maven:3.8\").inside { ... }') "
        "without needing tool compilers pre-installed on the host system."
    ),
    (
        "How do you handle pipeline build failures using try-catch in Groovy?",
        "try {\n"
        "    stage('Build') { sh 'mvn clean compile' }\n"
        "    stage('Test') { sh 'mvn test' }\n"
        "} catch (Exception e) {\n"
        "    stage('Alert') {\n"
        "        mail to: 'admin@example.com', subject: 'BUILD FAILED', body: e.getMessage()\n"
        "    }\n"
        "    error('Build failed due to test errors.')\n"
        "}"
    ),
    (
        "How do you configure email notifications on build failure in Jenkins?",
        "1. In Manage Jenkins → System → Configure 'E-mail Notification' (SMTP server, port, credentials).\n"
        "2. In pipeline script, add 'mail to: \"...\", subject: \"...\", body: \"...\"' in failure blocks or Declarative 'post { failure { ... } }'."
    ),
    (
        "How can you intentionally simulate a build failure to test notification alerting? (SET 4 Q2c)",
        "Insert an intentional failure shell step inside a pipeline stage:\n"
        "stage('Intentional Failure Test') {\n"
        "    sh 'exit 1'\n"
        "}\n"
        "An exit code of 1 forces Jenkins to immediately fail the stage and trigger the exception handling or failure notification block."
    ),
    (
        "What is a Build Trigger in Jenkins?",
        "A Build Trigger is a condition or event that automatically initiates job execution. "
        "Common triggers include: (1) GitHub Webhook (Push events), (2) Poll SCM (Periodic repo checking), (3) Build periodically (Cron), and (4) Trigger after other projects build."
    ),
    (
        "What is 'Poll SCM' in Jenkins?",
        "'Poll SCM' configures Jenkins to periodically connect to the remote Git repository on a schedule (e.g. every 5 minutes) and query for new commits. "
        "If new commits are detected, it triggers a build."
    ),
    (
        "What is the difference between 'Poll SCM' and a GitHub Webhook?",
        "• Poll SCM (Pull mechanism): Jenkins periodically pesters GitHub every few minutes asking 'Are there new commits?'. Wastes network bandwidth and causes delay.\n"
        "• GitHub Webhook (Push mechanism): Real-time event-driven. The millisecond a developer pushes code, GitHub immediately notifies Jenkins via an HTTP POST request, triggering builds instantly."
    ),
    (
        "What is a GitHub Webhook, and what payload URL does Jenkins expect?",
        "In GitHub Repo → Settings → Webhooks → Add webhook:\n"
        "Payload URL: 'http://<jenkins-server-ip>:9080/github-webhook/'\n"
        "Content type: 'application/json'\n"
        "The trailing slash ('/') is mandatory."
    ),
    (
        "What is 'Build periodically' in Jenkins?",
        "A scheduled trigger that runs a build at specific recurring clock times based on a standard cron syntax expression, independent of whether source code changes were made."
    ),
    (
        "Explain the 5 fields of Jenkins cron syntax: MINUTE HOUR DOM MONTH DOW.",
        "1. MINUTE: 0–59\n"
        "2. HOUR: 0–23 (military time)\n"
        "3. DOM (Day of Month): 1–31\n"
        "4. MONTH: 1–12\n"
        "5. DOW (Day of Week): 0–7 (0 and 7 = Sunday, 1 = Monday, 5 = Friday)."
    ),
    (
        "Write the cron expression to run a build every day at 6:00 PM. (0 18 * * *)",
        "0 18 * * *\n"
        "(Minute 0, Hour 18 = 6 PM, every day of month, every month, every day of week)."
    ),
    (
        "Write the cron expression to run a build every 15 minutes. (H/15 * * * *)",
        "H/15 * * * *\n"
        "(Runs approximately every 15 minutes, using Jenkins Hash function to distribute load)."
    ),
    (
        "What does the 'H' (Hash) symbol mean in Jenkins cron expressions?",
        "The 'H' (Hash) symbol tells Jenkins to choose an arbitrary, consistent minute offset based on a hash of the project name. "
        "This prevents multiple jobs configured with '0 * * * *' from firing simultaneously at the top of the hour and overwhelming system CPU."
    ),
    (
        "What is a Jenkins Master (Controller) and Agent (Node) architecture?",
        "Jenkins uses a distributed master-agent architecture:\n"
        "• Controller (Master): Hosts the web GUI, parses Jenkinsfiles, manages plugin configurations, and schedules jobs.\n"
        "• Agents (Nodes): Lightweight worker daemons that execute the physical build scripts, compile code, and run tests, reporting results back to the controller."
    ),
    (
        "Why should heavy builds not run on the Jenkins Controller?",
        "Running heavy compilation or Docker builds on the controller can exhaust CPU, memory, or disk space, causing the Jenkins web interface to freeze, drop webhooks, and disconnect all connected agents."
    ),
    (
        "What is a multi-branch pipeline in Jenkins?",
        "A multi-branch pipeline automatically discovers branches in a GitHub repository containing a 'Jenkinsfile' and automatically creates individual, isolated pipeline jobs for each branch (e.g. main, feature-auth, dev)."
    ),
    (
        "How do you view the console output of a running or completed build in Jenkins?",
        "Click on the job name → Click on the specific build number (e.g. '#1') in the build history on the left → Click 'Console Output' to view streaming terminal logs."
    ),
    (
        "What does blue/green, yellow, and red status mean in Jenkins job dashboard?",
        "• Blue / Green: SUCCESS — Build completed cleanly and all tests passed.\n"
        "• Yellow: UNSTABLE — Build succeeded, but unit tests failed or compiler warnings occurred.\n"
        "• Red: FAILURE — Build failed during execution (compilation error, syntax error, or aborted step)."
    ),
    (
        "What is Jenkins Blue Ocean, and what advantages does it offer?",
        "Blue Ocean is a modern, visual user interface replacement for the classic Jenkins dashboard. "
        "It provides visual pipeline progression graphs, visual stage logs, branch tracking, and an intuitive visual Jenkinsfile editor."
    )
]

print(f"Jenkins questions compiled: {len(JENKINS_QUESTIONS)}")
