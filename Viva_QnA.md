# 🎤 Viva Questions & Answers
### Docker · Jenkins · Nagios · Kubernetes · AWS EC2
#### KMIT Lab Internal II — Software Engineering

---

## 🐳 DOCKER

---

**Q1. What is Docker?**
> Docker is an open-source containerization platform that packages an application and all its dependencies into a lightweight unit called a container, so it runs consistently across any environment.

---

**Q2. What is the difference between a Docker Image and a Docker Container?**
> - **Image** → A read-only blueprint/template (like a class in OOP). Built from a Dockerfile.
> - **Container** → A running instance of an image (like an object). Can be started, stopped, and deleted.

---

**Q3. What is a Dockerfile?**
> A Dockerfile is a text file with a set of instructions that Docker reads to automatically build an image. Each instruction (FROM, RUN, COPY, CMD, etc.) creates a layer in the image.

---

**Q4. Explain the difference between Docker and a Virtual Machine (VM).**
> | | Docker | VM |
> |---|---|---|
> | Virtualizes | OS (uses host kernel) | Hardware |
> | Size | MBs | GBs |
> | Startup | Seconds | Minutes |
> | Isolation | Process-level | Full OS-level |
>
> Docker is lighter and faster because containers share the host OS kernel.

---

**Q5. What is Docker Hub?**
> Docker Hub is a public cloud-based registry where Docker images are stored and shared. You can `docker pull` images from it and `docker push` your own images to it. URL: hub.docker.com

---

**Q6. What is Docker Compose?**
> Docker Compose is a tool that lets you define and run multi-container Docker applications using a single YAML file (`docker-compose.yml`). You define all services, networks, and volumes in one file and start everything with `docker compose up`.

---

**Q7. What is the difference between `docker compose stop` and `docker compose down`?**
> - `docker compose stop` → Pauses containers but does **not** delete them. Data and networks are preserved. Use `docker compose start` to resume.
> - `docker compose down` → Stops **and deletes** containers and networks. Data in volumes is preserved unless you add `-v`.
> - `docker compose down -v` → Also deletes volumes (all data lost).

---

**Q8. What is a Docker Volume? Why is it used?**
> A Docker Volume is a persistent storage mechanism that exists outside the container's filesystem. Even if the container is deleted, the data in the volume survives. It is used to persist database data (like MySQL files) across container restarts.

---

**Q9. What does `depends_on` do in docker-compose.yml?**
> `depends_on` tells Docker Compose to start one service before another. For example, if `app` depends on `db`, Docker starts `db` first. It does NOT wait for `db` to be fully ready, only for the container to start.

---

**Q10. What is a Docker Network? Why do containers need a custom network?**
> A Docker Network allows containers to communicate with each other using their service names instead of IP addresses. A custom network provides isolation — only containers on the same network can talk to each other. By default, containers on different networks are isolated.

---

**Q11. What is the difference between `COPY` and `ADD` in a Dockerfile?**
> - `COPY` → Copies files/directories from host to container. Simple, recommended.
> - `ADD` → Does everything COPY does, plus it can extract `.tar` files and fetch URLs. Use COPY unless you specifically need ADD's extra features.

---

**Q12. What is the difference between `CMD` and `ENTRYPOINT` in a Dockerfile?**
> - `CMD` → Provides default command to run. Can be overridden when running the container.
> - `ENTRYPOINT` → Sets the main process that always runs. CMD becomes its arguments.
> - If both are set: `ENTRYPOINT` runs and `CMD` is passed as arguments to it.

---

**Q13. What is the purpose of `EXPOSE` in a Dockerfile?**
> `EXPOSE` documents which port the container listens on. It does NOT actually publish the port to the host — that's done with `-p` in `docker run` or `ports:` in docker-compose.yml. It's informational/documentation.

---

**Q14. What happens when a MySQL container crashes while the app is still running?**
> The app container loses its database connection and throws connection errors. The app itself keeps running but cannot serve DB-dependent requests. To fix: restart the MySQL container with `docker compose start db` or `docker restart <container>`.

---

**Q15. How do you check logs of a running container?**
> ```bash
> docker logs <container_name>        # one-time log dump
> docker logs -f <container_name>     # follow live logs (Ctrl+C to stop)
> docker compose logs app             # logs of a compose service
> ```

---

**Q16. What is the `build: .` instruction in docker-compose.yml?**
> It tells Docker Compose to build a custom image using the `Dockerfile` found in the current directory (`.`). Used when deploying your own Java/Python app instead of a pre-built image like nginx.

---

**Q17. How does container-to-container communication work in Docker Compose?**
> When services are on the same Docker network, they can reach each other using their **service name** as the hostname. For example, if the app needs to connect to MySQL, it uses `db` as the host (the service name), not `localhost` or an IP address.

---

**Q18. What command rebuilds the Docker image and restarts containers?**
> ```bash
> docker compose up --build -d
> ```
> `--build` forces a fresh image build from the Dockerfile even if an image already exists.

---

**Q19. What is the difference between `docker ps` and `docker ps -a`?**
> - `docker ps` → Lists only **running** containers.
> - `docker ps -a` → Lists **all** containers including stopped/exited ones.

---

**Q20. What is the port mapping `9090:8080` in Docker?**
> `hostPort:containerPort` — requests to your machine's port 9090 are forwarded to the container's internal port 8080. The app inside always runs on 8080; you access it from outside on 9090.

---
---

## 🔧 JENKINS

---

**Q1. What is Jenkins?**
> Jenkins is an open-source automation server used for Continuous Integration (CI) and Continuous Delivery (CD). It automates the process of building, testing, and deploying software whenever developers push code changes.

---

**Q2. What is Continuous Integration (CI)?**
> CI is the practice of automatically building and testing code every time a developer commits changes to a shared repository. The goal is to detect errors quickly. Jenkins automates this — it triggers a build on every commit.

---

**Q3. What is the difference between CI and CD?**
> - **CI (Continuous Integration)** → Auto build + test on every code push.
> - **CD (Continuous Delivery)** → After CI passes, automatically package and prepare for deployment.
> - **CD (Continuous Deployment)** → Goes one step further — automatically deploys to production.

---

**Q4. What is a Jenkins Pipeline?**
> A Pipeline is a series of automated steps defined as code (Groovy script) that Jenkins executes: checkout → build → test → package → deploy. It is stored in a file called `Jenkinsfile`.

---

**Q5. What is the difference between a Scripted Pipeline and a Declarative Pipeline?**
> | | Scripted | Declarative |
> |---|---|---|
> | Syntax | `node { stage() {} }` | `pipeline { stages { stage() {} } }` |
> | Flexibility | High (full Groovy) | Structured/opinionated |
> | Error handling | `try-catch` | `post { failure {} }` |
> | Complexity | More complex | Easier to read |

---

**Q6. What is a Jenkinsfile?**
> A Jenkinsfile is a text file containing the Jenkins Pipeline definition written in Groovy. It is committed to the source code repository so the pipeline definition is versioned alongside the code — called "Pipeline as Code."

---

**Q7. What is a Build Trigger in Jenkins?**
> A Build Trigger defines when Jenkins should automatically start a build:
> - **GitHub Hook Trigger** → Triggered by a GitHub webhook when code is pushed.
> - **Poll SCM** → Jenkins polls the repo at intervals (e.g., every 5 mins).
> - **Build Periodically** → Cron-based schedule (e.g., every day at 6 PM).
> - **Build Now** → Manually triggered by a user.

---

**Q8. What is a GitHub Webhook and how does it work with Jenkins?**
> A webhook is a URL registered in GitHub that GitHub calls (HTTP POST) whenever an event occurs (like a push). Jenkins listens at `/github-webhook/`. When code is pushed → GitHub calls Jenkins → Jenkins starts the pipeline automatically.

---

**Q9. How do you securely store Docker Hub credentials in Jenkins?**
> Go to **Manage Jenkins → Credentials → Global → Add Credentials** → Kind: "Username with password" → Enter Docker Hub username & password → Set ID as `dockerhub-creds`. Then in the Jenkinsfile, use `withCredentials` block to access them without hardcoding.

---

**Q10. What is `withCredentials` in a Jenkinsfile?**
> `withCredentials` is a Groovy block that securely injects stored credentials as environment variables into a pipeline stage. The credentials are never printed in logs.
> ```groovy
> withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
>     usernameVariable: 'USER', passwordVariable: 'PASS')]) {
>     sh "docker login -u $USER -p $PASS"
> }
> ```

---

**Q11. What happens if a stage fails in a Scripted Pipeline?**
> By default, if any stage fails (throws an exception), subsequent stages are skipped and the pipeline is marked as FAILED. Using `try-catch`, you can handle failures gracefully — catch the error, send an email notification, and re-throw the exception so Jenkins marks the build as failed.

---

**Q12. What is the Stage View in Jenkins?**
> Stage View is a visual display on the Jenkins job page that shows each stage as a colored column — green for success, red for failure. It makes it easy to identify exactly which stage failed without reading the full console log.

---

**Q13. What is the purpose of `tool 'Maven'` in a Jenkinsfile?**
> It retrieves the path to the Maven installation configured in Jenkins (Manage Jenkins → Tools → Maven). The name must exactly match what was configured. This lets you use `mvn` commands in shell steps.

---

**Q14. What is `emailext` in Jenkins?**
> `emailext` is a Groovy command provided by the **Email Extension Plugin** that sends customizable email notifications from a pipeline. You can set subject, body, and recipient. Used to alert teams on build failures or successes.

---

**Q15. How do you schedule a Jenkins build to run every day at 6 PM?**
> In Job → Configure → Build Triggers → Build Periodically → enter cron:
> ```
> 0 18 * * *
> ```
> Format: `minute hour day month weekday`

---

**Q16. What is Maven and why is it used in Jenkins pipelines?**
> Maven is a build automation tool for Java projects. It manages dependencies (downloads JARs automatically from Maven Central), compiles code, runs tests, and packages the application into WAR/JAR files. Jenkins uses Maven via `mvn clean install` or `mvn package`.

---

**Q17. Developer pushes code but Jenkins pipeline doesn't trigger — what do you check?**
> 1. GitHub Webhook URL is correct (`http://jenkins-ip:8080/github-webhook/`)
> 2. Webhook is active in GitHub repo settings (green tick)
> 3. Jenkins job has "GitHub hook trigger for GITScm polling" enabled
> 4. Jenkins is reachable from the internet (not behind a firewall)
> 5. GitHub plugin is installed in Jenkins

---

**Q18. What is the difference between `mvn clean install` and `mvn clean package`?**
> - `mvn clean package` → Compiles + runs tests + creates the WAR/JAR in `target/`.
> - `mvn clean install` → Does everything `package` does + copies the artifact to the local Maven repository (`~/.m2`), making it available for other projects.

---

**Q19. What is a Jenkins Agent/Slave?**
> A Jenkins Agent (formerly called Slave) is a separate machine that Jenkins Master delegates jobs to. The Master handles scheduling; Agents run the actual build steps. This allows parallel builds and load distribution.

---

**Q20. What language are Jenkinsfiles written in?**
> Jenkinsfiles are written in **Groovy** (a JVM scripting language). The `node { }` structure is Scripted Pipeline; the `pipeline { }` structure is Declarative Pipeline.

---
---

## 📡 NAGIOS

---

**Q1. What is Nagios?**
> Nagios is an open-source IT infrastructure monitoring system. It monitors servers, networks, and applications, and sends alerts (email/SMS) to administrators when services fail or recover.

---

**Q2. What is the difference between a Host and a Service in Nagios?**
> - **Host** → A physical or virtual machine being monitored (e.g., a web server at 192.168.1.100).
> - **Service** → A specific check running on a host (e.g., HTTP check, CPU load check, disk usage check).
> One host can have multiple services.

---

**Q3. What are the four Nagios status states?**
> | State | Colour | Meaning |
> |-------|--------|---------|
> | OK | 🟢 Green | Everything is fine |
> | WARNING | 🟡 Yellow | Approaching threshold, needs attention |
> | CRITICAL | 🔴 Red | Severe problem, immediate action needed |
> | UNKNOWN | 🟠 Orange | Plugin couldn't determine status |

---

**Q4. What is a Nagios Plugin?**
> A plugin is an external script/program that Nagios runs to perform an actual check. Plugins output a status code (0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN) and a text message. Examples: `check_ping`, `check_http`, `check_disk`, `check_load`.

---

**Q5. What is the difference between WARNING and CRITICAL thresholds?**
> - **WARNING** → A soft alert — the value is approaching a problematic level (e.g., CPU > 80%). Nagios notifies but it may resolve itself.
> - **CRITICAL** → A hard alert — the value has crossed a severe threshold (e.g., CPU > 95%) or a service is completely down. Requires immediate action.

---

**Q6. What is NRPE in Nagios?**
> NRPE (Nagios Remote Plugin Executor) is an agent installed on remote hosts that allows Nagios to execute plugins on those remote machines. Without NRPE, Nagios can only run checks from its own server. NRPE listens on port **5666**.

---

**Q7. What is the difference between Active and Passive checks in Nagios?**
> - **Active checks** → Nagios initiates the check on a schedule (polls the host/service itself).
> - **Passive checks** → An external application or agent sends the result to Nagios. Useful for things Nagios can't reach directly.

---

**Q8. How does Nagios detect if a web application is down even if the server is running?**
> Nagios uses the `check_http` plugin to send an HTTP request to the application's URL/port. If Tomcat or the app is down, the HTTP request fails → Nagios marks the service as CRITICAL, even if the OS and server are still running fine.

---

**Q9. How would you identify whether downtime is caused by Tomcat, MySQL, or the network?**
> Each is monitored as a separate service:
> - `check_ping` → Network connectivity
> - `check_http` on app port → Tomcat/application
> - `check_mysql` → MySQL database
>
> Nagios shows which specific service is in CRITICAL state, pinpointing the exact cause.

---

**Q10. What happens if the Nagios monitoring server itself goes down?**
> All monitoring stops. No checks run, no alerts are sent. The solution is to set up a **redundant/secondary Nagios instance** or use a cloud-based monitoring backup that sends a "heartbeat" alert if it doesn't hear from the primary Nagios server.

---

**Q11. How do you run Nagios using Docker?**
> ```bash
> docker run -d -p 8090:80 --name nagios jasonrivers/nagios:latest
> # Access: http://localhost:8090/nagios
> # Login:  nagiosadmin / nagios
> ```

---

**Q12. What is the default check interval in Nagios?**
> The default check interval is **5 minutes**. This means Nagios re-runs each service check every 5 minutes. This can be customized in the service definition with `check_interval`.

---

**Q13. What is "Flapping" in Nagios?**
> Flapping occurs when a host or service rapidly changes state (e.g., OK → CRITICAL → OK → CRITICAL repeatedly). Nagios detects this and suppresses notifications to avoid alert fatigue, marking the service as "flapping" instead.

---

**Q14. What is Nagios XI vs Nagios Core?**
> - **Nagios Core** → Free, open-source version. Config done via text files. No advanced UI.
> - **Nagios XI** → Commercial version. Has a modern web UI, wizards, graphs, reports, and easier configuration.

---

**Q15. Where are Nagios config files stored?**
> Inside the Docker container (`jasonrivers/nagios`):
> - Main config → `/opt/nagios/etc/nagios.cfg`
> - Hosts → `/opt/nagios/etc/objects/hosts.cfg`
> - Services → `/opt/nagios/etc/objects/services.cfg`
> - Commands → `/opt/nagios/etc/objects/commands.cfg`

---
---

## ☸️ KUBERNETES

---

**Q1. What is Kubernetes?**
> Kubernetes (K8s) is an open-source container orchestration platform that automates deploying, scaling, and managing containerized applications. It was originally developed by Google and is now maintained by CNCF (Cloud Native Computing Foundation).

---

**Q2. Why is Kubernetes needed if Docker already exists?**
> Docker runs containers on a single machine. Kubernetes manages containers across multiple machines (a cluster). It provides:
> - **Auto-healing** → restarts crashed containers
> - **Auto-scaling** → adds/removes containers based on load
> - **Load balancing** → distributes traffic across containers
> - **Rolling updates** → deploys new versions with zero downtime

---

**Q3. What is a Pod in Kubernetes?**
> A Pod is the smallest deployable unit in Kubernetes. It wraps one or more containers that share the same network namespace and storage. All containers in a Pod run on the same node and can communicate via `localhost`.

---

**Q4. What is a Deployment in Kubernetes?**
> A Deployment is a Kubernetes resource that manages a desired state for Pods — it ensures a specified number of Pod replicas are always running. If a Pod crashes, the Deployment's ReplicaSet automatically creates a new one.

---

**Q5. What is a ReplicaSet?**
> A ReplicaSet ensures a specified number of identical Pod replicas are running at all times. If you request 4 replicas and one Pod dies, the ReplicaSet creates a new one. Deployments manage ReplicaSets automatically.

---

**Q6. What is the relationship between Deployment, ReplicaSet, and Pod?**
> ```
> Deployment  →  manages  →  ReplicaSet  →  manages  →  Pods
> ```
> You create a Deployment. It creates a ReplicaSet. The ReplicaSet creates and maintains the Pods.

---

**Q7. What is a Kubernetes Service? Why is it needed?**
> Pods have dynamic IPs that change when they restart. A Service provides a stable network endpoint (fixed IP + DNS name) to access Pods. It also load-balances traffic across all matching Pods.

---

**Q8. What are the types of Kubernetes Services?**
> | Type | Access | Use Case |
> |------|--------|----------|
> | ClusterIP | Internal only (default) | Service-to-service inside cluster |
> | NodePort | External via node IP + port | Dev/testing, lab exams |
> | LoadBalancer | External via cloud LB | Production on AWS/GCP/Azure |
> | ExternalName | Maps to external DNS | Access external services |

---

**Q9. What is Minikube?**
> Minikube is a tool that runs a single-node Kubernetes cluster locally on your laptop inside a VM or Docker. It is used for learning and development. Start it with `minikube start`.

---

**Q10. What is kubectl?**
> `kubectl` is the command-line tool used to interact with a Kubernetes cluster. It communicates with the Kubernetes API Server to create, read, update, and delete resources.

---

**Q11. How do you scale a deployment to 4 replicas?**
> ```bash
> kubectl scale deployment myapp --replicas=4
> ```
> Verify: `kubectl get pods` (should show 4 running pods) or `kubectl get deployments` (READY: 4/4)

---

**Q12. What happens when you delete a Pod manually?**
> Kubernetes automatically creates a new Pod to maintain the desired replica count defined in the Deployment. This is called **auto-healing** or **self-healing**.

---

**Q13. A Service shows `ENDPOINTS: <none>` — what does this mean?**
> It means the Service cannot find any matching Pods. The cause is a **label mismatch** — the `selector` in the Service doesn't match the `labels` on the Pods.
>
> Fix: Check `kubectl describe service myapp` (see Selector) and `kubectl get pods --show-labels` (see labels). Make them match exactly.

---

**Q14. What is the difference between `kubectl apply` and `kubectl create`?**
> - `kubectl create` → Creates a resource. Fails if it already exists.
> - `kubectl apply` → Creates the resource if it doesn't exist, or updates it if it does. Preferred for production — idempotent.

---

**Q15. How do you perform a rolling update and rollback?**
> ```bash
> # Update to new image
> kubectl set image deployment/myapp myapp=myimage:v2
>
> # Watch rollout progress
> kubectl rollout status deployment myapp
>
> # Rollback to previous version
> kubectl rollout undo deployment myapp
> ```

---

**Q16. What are the components of the Kubernetes Control Plane?**
> | Component | Role |
> |-----------|------|
> | API Server | Entry point for all commands; front door of the cluster |
> | etcd | Key-value store; holds all cluster state/data |
> | Scheduler | Decides which node a new Pod runs on |
> | Controller Manager | Runs controllers that maintain desired state |

---

**Q17. What is etcd in Kubernetes?**
> etcd is a distributed key-value store that stores all Kubernetes cluster data — configurations, state of all resources, secrets. It is the most critical component — if etcd is lost, the cluster state is lost.

---

**Q18. What is a Namespace in Kubernetes?**
> A Namespace is a virtual cluster inside a Kubernetes cluster. It provides isolation between teams or environments (dev, test, prod) on the same cluster. The default namespace is called `default`.

---

**Q19. What is a NodePort and what is its valid range?**
> NodePort is a Service type that exposes the app on a static port on every node. The valid port range is **30000–32767**. External users access the app via `NodeIP:NodePort`.

---

**Q20. How do you get the URL to access an app running in Minikube?**
> ```bash
> minikube service <service-name> --url
> # OR open directly in browser:
> minikube service <service-name>
> ```

---

**Q21. What is the difference between scaling up and scaling down?**
> - **Scaling up** → Increasing replicas (e.g., 2 → 4) to handle more traffic.
> - **Scaling down** → Decreasing replicas (e.g., 4 → 1) to save resources during low traffic.
> Both done with: `kubectl scale deployment myapp --replicas=N`

---

**Q22. How does Kubernetes distribute requests among multiple Pods?**
> Through the **Service** resource. A Kubernetes Service automatically load-balances incoming traffic across all healthy Pods that match its selector using round-robin by default (via `kube-proxy`).

---
---

## ☁️ AWS EC2

---

**Q1. What is AWS EC2?**
> Amazon Elastic Compute Cloud (EC2) is a web service that provides resizable virtual servers (called instances) in the AWS cloud. You choose the OS, CPU, RAM, and storage, and pay only for what you use.

---

**Q2. What is an AMI?**
> AMI (Amazon Machine Image) is a pre-configured template used to launch an EC2 instance. It includes the operating system, application server, and sometimes applications. Example: "Ubuntu Server 22.04 LTS" or "Amazon Linux 2023".

---

**Q3. What is a Security Group in AWS?**
> A Security Group acts as a virtual firewall for EC2 instances. It controls:
> - **Inbound rules** → what traffic is allowed IN (e.g., SSH on port 22, HTTP on port 80)
> - **Outbound rules** → what traffic is allowed OUT (default: all traffic allowed)

---

**Q4. What is the difference between Stop and Terminate for an EC2 instance?**
> | | Stop | Terminate |
> |---|---|---|
> | Instance | Paused | Permanently deleted |
> | EBS data | Preserved | Deleted (unless configured otherwise) |
> | Charges | No compute charge (EBS still charged) | No charges |
> | Reversible | Yes — can Start again | No — cannot undo |

---

**Q5. What is a Key Pair in AWS EC2?**
> A Key Pair consists of a public key (stored in AWS) and a private key (`.pem` file downloaded to your machine). It is used to securely SSH into Linux EC2 instances. You cannot recover a lost `.pem` file — keep it safe.

---

**Q6. What is an Elastic IP?**
> An Elastic IP is a static public IPv4 address that you allocate from AWS and associate with an EC2 instance. Unlike the regular public IP (which changes on stop/start), an Elastic IP stays the same permanently.

---

**Q7. Developer cannot connect to EC2 via SSH — what are the possible causes?**
> 1. **Security Group** — Port 22 (SSH) inbound rule is missing or restricted
> 2. **Key pair** — Wrong `.pem` file, or permissions not set correctly
> 3. **Wrong username** — Should be `ubuntu` for Ubuntu, `ec2-user` for Amazon Linux
> 4. **Instance state** — Instance is stopped or pending
> 5. **Wrong IP** — Using private IP instead of public IP
> 6. **Network** — Instance in a private subnet with no internet gateway

---

**Q8. App is running on EC2 port 8080 but not accessible from browser — why?**
> The Security Group does not have an inbound rule for port 8080. Fix: EC2 Console → Security Groups → Edit Inbound Rules → Add Rule → Custom TCP → Port 8080 → Source: 0.0.0.0/0.

---

**Q9. What is EBS and how is it different from instance store?**
> - **EBS (Elastic Block Store)** → Persistent network-attached storage. Data survives instance stop/start. Can be detached and re-attached.
> - **Instance Store** → Temporary local storage on the physical host. Data is lost when the instance stops or terminates.

---

**Q10. What is the Free Tier for EC2?**
> AWS Free Tier provides **750 hours/month** of `t2.micro` or `t3.micro` instance usage for 12 months after account creation. This is enough to run one instance 24/7 for a month.

---

**Q11. What is an EC2 instance type? Give examples.**
> Instance type defines the hardware specs (CPU, RAM, network). Format: `family.size`
> | Family | Optimized for | Example |
> |--------|--------------|---------|
> | t | General (burstable) | t2.micro, t3.small |
> | m | General balanced | m5.large |
> | c | Compute (CPU) | c5.xlarge |
> | r | Memory | r5.large |
> | p/g | GPU | p3.2xlarge |

---

**Q12. What is the default username for Ubuntu EC2 instances?**
> `ubuntu`
>
> Other common defaults:
> - Amazon Linux → `ec2-user`
> - CentOS → `centos`
> - RHEL → `ec2-user` or `root`

---

**Q13. What is the difference between Public IP and Private IP in EC2?**
> - **Public IP** → Accessible from the internet. Changes every time the instance stops/starts (unless Elastic IP).
> - **Private IP** → Accessible only within the VPC (internal AWS network). Stays the same while the instance exists.

---

**Q14. What is a VPC?**
> VPC (Virtual Private Cloud) is an isolated virtual network within AWS where you launch resources like EC2. It has its own IP range, subnets, route tables, and internet gateways. Your EC2 instances run inside a VPC.

---

**Q15. What EC2 pricing models are available?**
> | Model | Description | Best For |
> |-------|-------------|----------|
> | On-Demand | Pay per hour/second, no commitment | Short-term, unpredictable |
> | Reserved | 1–3 year commitment, up to 75% cheaper | Steady workloads |
> | Spot | Bid on unused capacity, cheapest | Fault-tolerant, flexible |
> | Dedicated Host | Physical server for you | Compliance requirements |

---

**Q16. How do you deploy a Docker app on an EC2 Ubuntu instance?**
> ```bash
> # SSH into instance
> ssh -i key.pem ubuntu@<public-ip>
>
> # Install Docker
> sudo apt-get update -y
> sudo apt-get install -y docker.io
> sudo systemctl start docker
>
> # Clone repo and deploy
> git clone https://github.com/user/repo.git
> cd repo
> docker build -t myapp .
> docker run -d -p 9090:8080 myapp
> ```

---

**Q17. How is data kept safe when an EC2 instance is stopped?**
> Use an **EBS (Elastic Block Store)** volume. EBS is a network-attached persistent disk — data remains intact when the instance is stopped. The root EBS volume is attached by default and persists unless "Delete on Termination" is set to true.

---

**Q18. What should you configure in the Security Group to allow HTTP but restrict SSH?**
> - **Port 80 (HTTP)** → Source: `0.0.0.0/0` (everyone can access the website)
> - **Port 22 (SSH)** → Source: `<admin-ip>/32` (only the admin's specific IP can SSH)

---

**Q19. What happens if Tomcat stops while the EC2 instance is still running?**
> The EC2 instance continues to run, but the web application becomes unreachable. The Security Group and instance are fine — the problem is the application layer. Fix: SSH into the instance and restart the Docker container: `docker restart <container>`.

---

**Q20. What is an Application Load Balancer (ALB) and why is it better than a single EC2?**
> An ALB distributes incoming HTTP/HTTPS traffic across multiple EC2 instances. Benefits over single EC2:
> - **High availability** — if one instance fails, others handle traffic
> - **Auto scaling** — add/remove instances based on load
> - **No downtime deployments** — update instances one at a time
> - **Health checks** — ALB stops sending traffic to unhealthy instances

---
---

## ⚡ RAPID FIRE — One-Liner Answers

| Question | Answer |
|----------|--------|
| Full form of K8s | Kubernetes (K + 8 letters + s) |
| Default Jenkins port | 8080 |
| Default Nagios login | nagiosadmin / nagios |
| Nagios NRPE port | 5666 |
| Docker Hub URL | hub.docker.com |
| Kubernetes CLI tool | kubectl |
| EC2 free tier instance | t2.micro |
| EC2 Ubuntu default user | ubuntu |
| EC2 Amazon Linux default user | ec2-user |
| File to define multi-container app | docker-compose.yml |
| File to define Jenkins pipeline | Jenkinsfile |
| Language of Jenkinsfile | Groovy |
| K8s cluster state store | etcd |
| K8s smallest deployable unit | Pod |
| NodePort valid range | 30000–32767 |
| Docker command to list running containers | `docker ps` |
| Docker command to enter container shell | `docker exec -it <name> bash` |
| K8s command to scale to 4 replicas | `kubectl scale deployment X --replicas=4` |
| Nagios plugin to check HTTP | `check_http` |
| AWS static public IP | Elastic IP |
| Docker persistent storage | Volume |
| K8s auto-healing — who does it? | ReplicaSet |
| K8s load balancing — who does it? | Service |
| AWS firewall for EC2 | Security Group |
| `docker compose stop` vs `down` | stop=pause, down=delete |
