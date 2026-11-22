"""
Viva Question and Answer Data Store for Topic 3: Docker & Docker CLI (50 questions).
"""

DOCKER_CLI_QUESTIONS = [
    (
        "What is Docker, and what problem does it solve in modern software development?",
        "Docker is an open-source platform that automates the deployment of applications inside lightweight, portable containers. "
        "It solves the classic 'it works on my machine' problem by packaging the application code along with its exact runtime, libraries, environment variables, "
        "and system dependencies, ensuring 100% consistent execution across development, testing, and cloud production environments."
    ),
    (
        "What is containerization, and how does it differ from virtualization (Virtual Machines)?",
        "• Virtualization (VMs): Each Virtual Machine runs a complete guest operating system on top of a hypervisor (like VMware/VirtualBox), requiring dedicated kernel memory, slow boot times (minutes), and gigabytes of disk space.\n"
        "• Containerization (Docker): Containers share the host operating system's Linux kernel and isolate processes using kernel namespaces and cgroups. They boot in milliseconds, consume megabytes of RAM, and are extremely lightweight."
    ),
    (
        "What is the role of the Linux kernel (cgroups and namespaces) in Docker?",
        "Docker containers rely directly on two core Linux kernel primitives:\n"
        "1. Namespaces: Provide isolation between containers (PID for process IDs, NET for network interfaces/routes, MNT for filesystem mount points, IPC for inter-process communication, and UTS for hostnames).\n"
        "2. Control Groups (cgroups): Meter, restrict, and enforce resource limits (CPU quotas, memory caps, block I/O bandwidth, network priority) on container process trees."
    ),
    (
        "What is a Docker Image?",
        "A Docker Image is an immutable, read-only executable template containing everything needed to run an application—code, runtime, libraries, environment variables, "
        "and configuration files. Images are built from layers defined in a Dockerfile and stored in registries like Docker Hub."
    ),
    (
        "What is a Docker Container?",
        "A Docker Container is a runnable, isolated instance of a Docker Image. When an image is run, Docker adds a thin read-write layer on top of the immutable image layers, "
        "allowing the application to execute, read, and write files in an isolated user space."
    ),
    (
        "What is Docker Hub?",
        "Docker Hub (hub.docker.com) is the default cloud-hosted public and private container image registry. "
        "It provides official base images (e.g. ubuntu, openjdk, mysql, tomcat, redis) and allows developers to publish, share, and pull versioned images globally."
    ),
    (
        "What is the Docker Daemon (dockerd), and how does it interact with the Docker CLI?",
        "The Docker Daemon ('dockerd') is a background service running on the host OS that manages containers, images, networks, storage volumes, and kernel cgroups. "
        "The Docker CLI ('docker') acts as a REST client that communicates with the daemon over a local Unix domain socket ('/var/run/docker.sock') or network API."
    ),
    (
        "How do you start, stop, and verify the Docker daemon on Ubuntu using systemctl?",
        "• Start daemon: $ sudo systemctl start docker\n"
        "• Stop daemon: $ sudo systemctl stop docker\n"
        "• Restart daemon: $ sudo systemctl restart docker\n"
        "• Verify status: $ sudo systemctl status docker\n"
        "Status should show 'Active: active (running)'."
    ),
    (
        "How do you run Docker commands without sudo on Ubuntu?",
        "Add the current non-root user to the 'docker' system group and refresh the shell session:\n"
        "$ sudo usermod -aG docker $USER\n"
        "$ newgrp docker\n"
        "This grants permission to communicate with the Unix socket '/var/run/docker.sock' without root elevation."
    ),
    (
        "What does 'docker pull' do?",
        "'docker pull <image>:<tag>' downloads the specified container image layers from a registry (Docker Hub) to the local Docker engine cache. "
        "If no tag is specified, it defaults to pulling the ':latest' tag."
    ),
    (
        "What does 'docker images' or 'docker image ls' display?",
        "It lists all locally stored images, displaying:\n"
        "• REPOSITORY (e.g. mysql, redis)\n"
        "• TAG (e.g. 8.0, latest)\n"
        "• IMAGE ID (unique truncated hexadecimal identifier)\n"
        "• CREATED (time elapsed since creation)\n"
        "• SIZE (disk space consumed on host filesystem)."
    ),
    (
        "What is an image tag, and what does 'latest' mean?",
        "A tag is a human-readable alias or version identifier attached to an image (e.g. 'mysql:8.0' or 'openjdk:17-jdk'). "
        "'latest' is simply a default convention tag applied when no explicit tag is passed during build or pull; it does NOT guarantee the newest version if an older build was tagged as latest."
    ),
    (
        "How do you remove a Docker image using 'docker rmi'?",
        "Run: $ docker rmi <image-id-or-name>\n"
        "If a stopped container is still referencing the image, Docker prevents removal. Force removal using '$ docker rmi -f <image>' or delete the referencing container first."
    ),
    (
        "What is a dangling image, and how do you prune unused images?",
        "A dangling image is an untagged image layer displayed as '<none>:<none>' created when a new image is built with the same tag as an existing image. "
        "Prune all dangling and unused images on Ubuntu by running:\n"
        "$ docker image prune -a -f"
    ),
    (
        "What does 'docker run' do? Explain the combination of 'create' and 'start'.",
        "'docker run' performs three operations sequentially in one command:\n"
        "1. Pulls the image from Docker Hub if not present locally.\n"
        "2. Executes 'docker create' to allocate container filesystem layers, network endpoints, and namespace settings.\n"
        "3. Executes 'docker start' to launch the container's entrypoint process."
    ),
    (
        "What is the purpose of the '-d' (detached) flag in 'docker run'?",
        "The '-d' (detached mode) flag runs the container as a background daemon process, immediately returning control of the terminal shell to the user and printing the container ID hash. "
        "Without '-d', the container runs in foreground mode, attaching its standard output/error directly to the terminal."
    ),
    (
        "What is port forwarding / port mapping in Docker? What does '-p 9090:8080' mean?",
        "Containers run in isolated network namespaces with private IP addresses. Port forwarding routes host traffic to the container.\n"
        "Syntax: '-p <HostPort>:<ContainerPort>'.\n"
        "'-p 9090:8080' binds port 9090 on the Ubuntu host machine to port 8080 inside the container. External requests to http://localhost:9090 are forwarded to container port 8080."
    ),
    (
        "What is the difference between host port and container port?",
        "• Host Port: The physical network port exposed on the host operating system (Ubuntu), accessed by external clients and web browsers.\n"
        "• Container Port: The internal private port that the application inside the container listens on (e.g. 8080 for Tomcat, 3306 for MySQL, 5000 for Flask)."
    ),
    (
        "How do you name a container using '--name', and why is it recommended?",
        "Pass the '--name' flag during container launch: '$ docker run -d --name oltrs-app -p 9090:8080 myimage'.\n"
        "Naming containers is recommended because it provides human-readable aliases for commands ('docker logs oltrs-app', 'docker stop oltrs-app') "
        "and enables inter-container DNS communication on custom networks."
    ),
    (
        "What is the difference between 'docker ps' and 'docker ps -a'?",
        "• 'docker ps': Lists only currently running active containers.\n"
        "• 'docker ps -a': Lists ALL containers on the system, including running, paused, exited (crashed or stopped), and dead containers."
    ),
    (
        "What information is shown in 'docker ps' output?",
        "Columns displayed: (1) CONTAINER ID, (2) IMAGE used, (3) COMMAND executed on startup, (4) CREATED timestamp, "
        "(5) STATUS (e.g. Up 2 hours, Exited (0)), (6) PORTS mapping, and (7) NAMES assigned to the container."
    ),
    (
        "What does 'docker stop' do, and how does it differ from 'docker kill'? (SIGTERM vs SIGKILL)",
        "• 'docker stop': Sends a graceful POSIX SIGTERM signal to the container's PID 1 process, allowing it to flush buffers, finish active transactions, and shut down cleanly. If it doesn't terminate within 10 seconds, it sends SIGKILL.\n"
        "• 'docker kill': Sends an immediate, abrupt SIGKILL signal, terminating the process instantly without graceful cleanup."
    ),
    (
        "What does 'docker start' do, and how does it differ from 'docker run'?",
        "'docker run' initializes and creates a brand-new container from an image. "
        "'docker start <container-name>' resumes execution of an existing, stopped container, preserving all data and filesystem modifications made in its read-write layer."
    ),
    (
        "What does 'docker restart' do?",
        "'docker restart <container-name>' stops the running container (via SIGTERM) and immediately starts it back up, reloading process configurations and refreshing network sockets."
    ),
    (
        "How do you view container logs using 'docker logs'?",
        "Run: $ docker logs <container-name-or-id>\n"
        "This outputs all standard output (stdout) and standard error (stderr) streams generated by the container's PID 1 process since startup."
    ),
    (
        "How do you stream live container logs using 'docker logs -f'?",
        "Run: $ docker logs -f --tail 100 <container-name>\n"
        "The '-f' (follow) flag keeps the terminal connection open to stream new log entries in real-time (similar to 'tail -f' in Linux), while '--tail 100' displays only the latest 100 lines."
    ),
    (
        "What does 'docker exec' do?",
        "'docker exec' runs a new command inside an already running container within its existing namespaces, without restarting or modifying the container."
    ),
    (
        "How do you open an interactive terminal shell inside a running container using 'docker exec -it'?",
        "Run: $ docker exec -it <container-name> /bin/bash\n"
        "(Or '/bin/sh' if the image is minimal/Alpine).\n"
        "• '-i' (interactive): Keeps standard input (stdin) open.\n"
        "• '-t' (tty): Allocates a pseudo-terminal, giving the user an interactive shell prompt inside the container."
    ),
    (
        "What is the difference between '/bin/bash' and '/bin/sh' in 'docker exec'?",
        "• '/bin/bash': The full Bourne Again Shell featuring tab completion, history, and rich scripting. Available in standard Ubuntu/Debian images.\n"
        "• '/bin/sh': The minimal POSIX Bourne shell. Present in ultra-lightweight distributions like Alpine Linux that lack bash by default."
    ),
    (
        "How do you remove a stopped container using 'docker rm'?",
        "Run: $ docker rm <container-name-or-id>\n"
        "This deletes the container's writable layer and metadata from disk."
    ),
    (
        "How do you forcefully remove a running container using 'docker rm -f'?",
        "Run: $ docker rm -f <container-name>\n"
        "The '-f' flag issues a SIGKILL signal to the running container process and deletes the container immediately in a single step."
    ),
    (
        "How do you remove all stopped containers in one command?",
        "Run either of the following commands in Ubuntu:\n"
        "$ docker container prune -f\n"
        "$ docker rm $(docker ps -a -q -f status=exited)"
    ),
    (
        "What is 'docker inspect', and what type of information does it return?",
        "'docker inspect <container-or-image>' returns a detailed JSON array describing the low-level configuration of the target. "
        "It includes IP addresses, MAC address, gateway, mounted volumes, environment variables, health status, and state flags."
    ),
    (
        "How do you filter 'docker inspect' output using grep or --format?",
        "• Using grep: $ docker inspect my-redis | grep IPAddress\n"
        "• Using Go template '--format': $ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-redis\n"
        "This outputs only the container's private IP address."
    ),
    (
        "What is container storage ephemerality, and why do containers lose data on removal?",
        "Containers use an ephemeral, copy-on-write storage driver. When a container is deleted ('docker rm'), its top writable layer is wiped permanently. "
        "Any files created inside the container (such as MySQL databases) are lost unless saved to an external persistent Docker Volume."
    ),
    (
        "What is a Docker Volume, and why is it preferred for database storage?",
        "A Docker Volume is a directory managed directly by Docker outside the container's storage driver, stored on the host filesystem. "
        "Volumes are preferred because: (1) data persists even when containers are deleted, (2) volumes have higher I/O performance than copy-on-write layers, and (3) volumes can be safely shared across multiple containers."
    ),
    (
        "How do you create, list, and inspect Docker volumes on Ubuntu?",
        "• Create volume: $ docker volume create mydata\n"
        "• List volumes: $ docker volume ls\n"
        "• Inspect volume: $ docker volume inspect mydata"
    ),
    (
        "Where are Docker volumes physically stored on the Ubuntu filesystem?",
        "On Ubuntu Linux, Docker volumes are physically stored under root storage at:\n"
        "'/var/lib/docker/volumes/<volume-name>/_data/'."
    ),
    (
        "What is the difference between a named volume and a bind mount?",
        "• Named Volume ('-v mydata:/var/lib/mysql'): Completely managed by Docker inside '/var/lib/docker/volumes/'. Recommended for production data and databases.\n"
        "• Bind Mount ('-v /home/ubuntu/app:/usr/share/nginx/html'): Mounts any arbitrary physical directory or file from the host filesystem directly into the container. Recommended for local source code development."
    ),
    (
        "How do you mount a volume to a container using the '-v' flag?",
        "Syntax: '-v <VolumeName>:<ContainerMountPath>'.\n"
        "Example:\n"
        "$ docker run -d --name db -v mysql_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 mysql:8.0\n"
        "MySQL will store all table schemas and records into 'mysql_data'."
    ),
    (
        "What is Docker networking, and what is the default network driver? (bridge)",
        "Docker networking provides isolated communication channels between containers and external hosts. "
        "The default driver is 'bridge', which creates a virtual Linux software bridge interface ('docker0') assigning private IP addresses (typically 172.17.0.0/16) to containers."
    ),
    (
        "What are the built-in network drivers in Docker? (bridge, host, none, overlay)",
        "• bridge: Default isolated network for standalone containers on a single host.\n"
        "• host: Removes network isolation; container shares host network stack directly (e.g. port 80 binds directly to host port 80).\n"
        "• none: Disables all networking; container has only a loopback interface.\n"
        "• overlay: Enables multi-host container-to-container networking across Swarm or Kubernetes clusters."
    ),
    (
        "What is a custom bridge network, and why is it better than the default bridge network?",
        "A custom bridge network ('docker network create my-net') provides automatic DNS resolution between containers by container name, "
        "better security isolation (only attached containers can communicate), and runtime configurability without stopping containers."
    ),
    (
        "How does Docker provide automatic DNS service discovery on custom networks?",
        "Docker runs an embedded DNS server at 127.0.0.11 inside each container connected to a custom network. "
        "When an app connects to 'db:3306', Docker's internal DNS automatically resolves the service/container name 'db' to its current internal container IP."
    ),
    (
        "How do you create and connect containers to a custom bridge network?",
        "1. Create network: $ docker network create app-net\n"
        "2. Run container on network: $ docker run -d --name db --network app-net mysql:8.0\n"
        "3. Attach existing container: $ docker network connect app-net web"
    ),
    (
        "How do you push a local Docker image to Docker Hub?",
        "1. Login: $ docker login\n"
        "2. Tag image: $ docker tag myapp:latest dheerajmalavath/myapp:v1\n"
        "3. Push: $ docker push dheerajmalavath/myapp:v1"
    ),
    (
        "What is 'docker tag', and why must the image name include the Docker Hub username?",
        "'docker tag' creates an alias for an existing image ID. "
        "The image name must be prefixed with your Docker Hub username ('<username>/<repo>:<tag>') so that the Docker CLI knows which registry account namespace to upload the image layers to during 'docker push'."
    ),
    (
        "What is 'docker login', and where are credentials stored?",
        "'docker login' authenticates against Docker Hub or a private registry. "
        "On Ubuntu Linux, authentication tokens and credentials are encrypted and stored in '~/.docker/config.json'."
    ),
    (
        "What is 'docker stats', and what system metrics does it report?",
        "'docker stats' provides a live streaming dashboard of container resource utilization, reporting:\n"
        "• CPU % usage\n"
        "• Memory usage vs limit (and Memory %)\n"
        "• Network I/O (bytes sent/received)\n"
        "• Block I/O (disk read/written)\n"
        "• PIDs (total active thread count)."
    ),
    (
        "What is 'docker system prune', and what resources does it clean up?",
        "Run: $ docker system prune -a --volumes -f\n"
        "This completely purges: (1) all stopped containers, (2) all unused networks, (3) all dangling and unused images, (4) all build cache layers, and (5) all unattached volumes, freeing gigabytes of host disk space."
    )
]

print(f"Docker CLI questions compiled: {len(DOCKER_CLI_QUESTIONS)}")
