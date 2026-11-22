"""
Viva Question and Answer Data Store for Topic 4: Docker Compose & Dockerfile (50 questions).
"""

COMPOSE_QUESTIONS = [
    (
        "What is Docker Compose?",
        "Docker Compose is an orchestration tool used to define, configure, and execute multi-container Docker applications. "
        "Through a single declarative YAML file ('docker-compose.yml'), it provisions multiple interdependent services, "
        "inter-container bridge networks, environment variables, and persistent storage volumes in a single execution."
    ),
    (
        "What is the difference between Dockerfile and Docker Compose?",
        "• Dockerfile: A blueprint script containing instructions ('FROM', 'COPY', 'RUN') used to build a SINGLE Docker image.\n"
        "• Docker Compose: A configuration tool used to coordinate and run MULTIPLE containers simultaneously, managing their startup dependencies, network communication, port forwarding, and persistent volume mounts."
    ),
    (
        "What is the structure of a Dockerfile?",
        "A Dockerfile is an ordered text file starting with a base image ('FROM') followed by environment setup ('WORKDIR', 'ENV'), "
        "layer additions ('COPY', 'RUN'), metadata ('EXPOSE', 'LABEL'), and an execution command ('CMD' or 'ENTRYPOINT')."
    ),
    (
        "What is the 'FROM' instruction in a Dockerfile?",
        "The 'FROM' instruction specifies the parent base image from which the new image is constructed (e.g. 'FROM tomcat:9.0' or 'FROM openjdk:17-jdk'). "
        "It must be the first non-comment instruction in any standard Dockerfile."
    ),
    (
        "What is the difference between 'RUN', 'CMD', and 'ENTRYPOINT' in a Dockerfile?",
        "• 'RUN': Executes commands at IMAGE BUILD time and commits the result as a new image layer (e.g. 'RUN apt-get update && apt-get install -y curl').\n"
        "• 'CMD': Specifies the DEFAULT command and parameters executed when the container STARTS at runtime. Can be overridden easily by command line arguments.\n"
        "• 'ENTRYPOINT': Defines the immutable fixed executable run on container startup that is NOT overridden by command line arguments (arguments appended to entrypoint)."
    ),
    (
        "When should you use 'ENTRYPOINT' vs 'CMD'?",
        "Use 'ENTRYPOINT' when the container is intended to act as a dedicated executable binary (e.g. 'ENTRYPOINT [\"java\", \"-jar\", \"app.jar\"]'). "
        "Use 'CMD' to provide default parameters to 'ENTRYPOINT' that users can easily override, or when a default shell command is sufficient."
    ),
    (
        "What is the 'COPY' instruction, and how does it differ from 'ADD'?",
        "• 'COPY': Copies local files or directories from the host build context into the container filesystem. It is transparent and preferred.\n"
        "• 'ADD': Performs everything 'COPY' does, but also automatically unpacks local tar archives (tar.gz) and can download files directly from remote URLs (not recommended for simple copies)."
    ),
    (
        "What is the 'WORKDIR' instruction in a Dockerfile?",
        "'WORKDIR /path' sets the working directory inside the container for all subsequent 'RUN', 'CMD', 'ENTRYPOINT', and 'COPY' instructions, "
        "automatically creating the directory if it does not already exist (avoiding multiple 'cd' commands)."
    ),
    (
        "What is the 'EXPOSE' instruction, and does it publish the port to the host?",
        "'EXPOSE <port>' acts as internal documentation indicating which network port the application listens on inside the container. "
        "It does NOT actually publish or forward the port to the host system. Publishing to the host requires passing '-p <host_port>:<container_port>' at runtime."
    ),
    (
        "What is the 'ENV' instruction in a Dockerfile?",
        "'ENV KEY=VALUE' sets environment variables that persist both during image build steps and inside the running container at runtime. "
        "Used for configuring database connection parameters, Java options ('JAVA_OPTS'), and system paths."
    ),
    (
        "What is multi-stage Docker build, and why is it used?",
        "A multi-stage build uses multiple 'FROM' statements in a single Dockerfile. Early stages compile the code using full SDKs/compilers (e.g. Maven/JDK), "
        "and subsequent final stages copy ONLY the compiled artifact (.war/.jar) into a minimal lightweight JRE runtime image. "
        "This drastically reduces final image sizes from 800MB+ down to ~150MB and eliminates compiler security vulnerabilities from production."
    ),
    (
        "Write a minimal Dockerfile for deploying a WAR file to Apache Tomcat.",
        "FROM tomcat:9.0-jdk11-openjdk-slim\n"
        "RUN rm -rf /usr/local/tomcat/webapps/*\n"
        "COPY target/*.war /usr/local/tomcat/webapps/ROOT.war\n"
        "EXPOSE 8080\n"
        "CMD [\"catalina.sh\", \"run\"]"
    ),
    (
        "Write a minimal Dockerfile for running a Spring Boot JAR file.",
        "FROM eclipse-temurin:17-jdk-alpine\n"
        "WORKDIR /app\n"
        "COPY target/*.jar app.jar\n"
        "EXPOSE 8080\n"
        "ENTRYPOINT [\"java\", \"-jar\", \"app.jar\"]"
    ),
    (
        "What are Docker image layers, and how does layer caching improve build performance?",
        "Every instruction in a Dockerfile ('RUN', 'COPY') creates an immutable read-only filesystem layer. "
        "Docker caches these layers. When re-building an image, Docker reuses unchanged cached layers instead of re-executing steps, "
        "reducing subsequent build times from minutes down to seconds."
    ),
    (
        "What is a .dockerignore file, and what should be included in it?",
        "'.dockerignore' prevents unwanted files and large directories on the host from being sent to the Docker daemon during build context evaluation. "
        "Typically includes: '.git/', 'target/classes/', 'node_modules/', '*.log', and sensitive '.env' files."
    ),
    (
        "What is docker-compose.yml, and what file format does it use?",
        "'docker-compose.yml' is a YAML (YAML Ain't Markup Language) configuration file. "
        "It uses strict 2-space indentation (tabs are strictly prohibited) to define services, volumes, networks, and environment variables."
    ),
    (
        "What are the top-level keys in a docker-compose.yml file?",
        "The standard top-level keys are:\n"
        "• 'version': Specifies compose file format specification (e.g. '3.8').\n"
        "• 'services': Defines the containers to be created and managed.\n"
        "• 'networks': Declares custom networks shared across services.\n"
        "• 'volumes': Declares persistent named volumes shared across services."
    ),
    (
        "What is a 'service' in Docker Compose?",
        "A service in Docker Compose represents an individual containerized application component (e.g. 'app', 'db', 'web', 'redis'). "
        "Each service specifies an image or build context, port mappings, environment variables, and runtime dependencies."
    ),
    (
        "What is the 'build:' directive in Docker Compose?",
        "'build:' tells Docker Compose to build an image from a Dockerfile on the local filesystem rather than pulling a pre-built image from Docker Hub. "
        "Example: 'build: .' builds the Dockerfile located in the current project root directory."
    ),
    (
        "What is the 'image:' directive in Docker Compose?",
        "'image:' specifies the pre-built Docker image to pull and run from a registry (e.g. 'image: mysql:8.0' or 'image: wordpress:latest')."
    ),
    (
        "What happens if both 'build:' and 'image:' are specified in a Compose service?",
        "If both are present, Compose builds the image using the local 'build:' context and tags the resulting image with the name supplied in 'image:'."
    ),
    (
        "What does 'container_name:' do in Docker Compose?",
        "By default, Compose assigns container names following the pattern '<project>_<service>_<index>'. "
        "'container_name: oltrs-app' forces Docker Compose to assign a custom static name, making CLI inspection and log querying straightforward."
    ),
    (
        "What is the 'ports:' directive in Docker Compose?",
        "Maps host ports to container ports ('HostPort:ContainerPort'). "
        "Example:\n"
        "ports:\n"
        "  - \"9090:8080\"\n"
        "Forwards incoming traffic on Ubuntu host port 9090 to container port 8080."
    ),
    (
        "What is the 'environment:' directive, and how can environment variables be passed from a .env file?",
        "'environment:' sets runtime environment variables inside the container (e.g. DB_HOST, DB_NAME, MYSQL_ROOT_PASSWORD). "
        "Compose automatically loads key-value pairs from a local '.env' file in the same directory and substitutes them via '${VARIABLE_NAME}' syntax."
    ),
    (
        "What is the 'depends_on:' directive in Docker Compose?",
        "'depends_on:' controls container startup and shutdown order. "
        "Example: 'depends_on: - db' ensures the database container starts BEFORE the application container is launched."
    ),
    (
        "Does 'depends_on' guarantee that the database inside the container is fully ready to accept connections?",
        "No. 'depends_on' only waits until the dependency container process STARTS running, not until the internal database daemon has completed initialization and is ready to accept client connections."
    ),
    (
        "How do you solve the race condition where an app container crashes before MySQL finishes initialization?",
        "1. In docker-compose.yml: Add 'restart: always' so Docker continuously restarts the crashed app container until MySQL is ready.\n"
        "2. Use health checks with 'condition: service_healthy' in depends_on.\n"
        "3. Implement retry connection logic inside the application code (e.g. JDBC connection pool)."
    ),
    (
        "What is the 'volumes:' directive in Compose, and how do you define a named volume?",
        "Under the service block, specify: '- dbdata:/var/lib/mysql'. "
        "At the bottom of 'docker-compose.yml', define the volume globally:\n"
        "volumes:\n"
        "  dbdata:\n"
        "This tells Compose to allocate a persistent named volume that outlives the database container."
    ),
    (
        "What is the 'networks:' directive in Compose, and how do services talk to each other?",
        "Services attached to the same declared network communicate with each other over an isolated software bridge. "
        "Docker's embedded DNS automatically resolves service names (e.g. 'db', 'app') to their respective container IP addresses."
    ),
    (
        "In a Compose network, what hostname does an application container use to connect to MySQL?",
        "The application uses the SERVICE NAME (e.g. 'db' or 'mysql'), NOT 'localhost' or '127.0.0.1'. "
        "Inside container network namespaces, 'localhost' refers strictly to the application container itself, whereas 'db' resolves via Docker DNS to the database container."
    ),
    (
        "What is the 'restart: always' or 'restart: unless-stopped' policy?",
        "• 'restart: always': Automatically restarts the container if it exits, crashes, or if the Docker daemon reboots, regardless of exit code.\n"
        "• 'restart: unless-stopped': Restarts the container on crashes or daemon reboot, unless the user explicitly ran 'docker stop'."
    ),
    (
        "What command starts all services defined in docker-compose.yml in the background?",
        "Run: $ docker compose up -d\n"
        "Creates networks, volumes, pulls/builds images, and starts all containers in detached mode."
    ),
    (
        "What is the difference between 'docker compose up' and 'docker compose up -d'?",
        "• 'docker compose up': Runs in foreground mode, interleaving console logs from all containers in the terminal. Closing the terminal stops all containers.\n"
        "• 'docker compose up -d': Runs containers as background daemons and releases the terminal."
    ),
    (
        "When should you use 'docker compose up --build -d'?",
        "Use '--build' whenever source code or Dockerfile changes have been made. "
        "Without '--build', Compose reuses existing cached local images and ignores your recent code changes."
    ),
    (
        "What does 'docker compose ps' show?",
        "'docker compose ps' displays the status of all containers belonging specifically to the current compose project, showing service names, container states (Up/Exited), and mapped ports."
    ),
    (
        "How do you view logs of all services vs a single service in Docker Compose?",
        "• All services: $ docker compose logs -f\n"
        "• Specific service: $ docker compose logs -f <service-name> (e.g. 'docker compose logs -f app')."
    ),
    (
        "What does 'docker compose stop' do?",
        "'docker compose stop' sends SIGTERM to stop all running service containers without removing the containers, networks, or volume data."
    ),
    (
        "What does 'docker compose start' do?",
        "'docker compose start' restarts previously stopped containers without re-reading the compose configuration or regenerating container IDs."
    ),
    (
        "What does 'docker compose restart' do?",
        "'docker compose restart' stops and immediately re-executes all running services, useful for picking up configuration tweaks."
    ),
    (
        "How do you stop and remove only one specific service while keeping others running?",
        "Run: $ docker compose stop <service_name>\n"
        "Followed by: $ docker compose rm -f <service_name>\n"
        "Leaves all other services (like the database) active and untouched."
    ),
    (
        "What is the difference between 'docker compose down' and 'docker compose down -v'?",
        "• 'docker compose down': Stops and removes containers and networks, but PRESERVES persistent volumes on disk.\n"
        "• 'docker compose down -v': Stops and removes containers, networks, AND permanently deletes all named volumes, wiping all database data."
    ),
    (
        "What happens to MySQL database records when 'docker compose down' is executed without -v?",
        "All database tables and records remain completely safe and intact inside the persistent Docker volume. "
        "When 'docker compose up -d' is run next time, the database container mounts the existing volume and reloads all records."
    ),
    (
        "How do you scale a service in Docker Compose? (--scale web=3)",
        "Run: $ docker compose up --scale <service_name>=<count> -d\n"
        "Example: '$ docker compose up --scale web=3 -d' launches 3 identical, parallel container instances of the 'web' service."
    ),
    (
        "Why does scaling a service fail if a fixed host port mapping (e.g. 8080:8080) is used?",
        "Because two containers cannot bind to the exact same physical host port (8080) simultaneously on Ubuntu, causing a 'port is already allocated' bind collision error."
    ),
    (
        "How do you scale a web service behind an Nginx reverse proxy load balancer?",
        "Remove host port mappings from the web service (expose only container port internally), and place an Nginx container in front that binds to host port 80/8080 and load-balances traffic across the scaled service instances."
    ),
    (
        "How do you execute commands inside a Compose service container? (docker compose exec app ...)",
        "Run: $ docker compose exec <service_name> <command>\n"
        "Example: '$ docker compose exec app env' or '$ docker compose exec db mysql -u root -p'."
    ),
    (
        "Explain the architecture of a multi-container Java + MySQL application in Docker Compose.",
        "Consists of: (1) App container running Tomcat/Spring Boot on custom network, (2) DB container running MySQL 8.0 on same network, "
        "(3) Persistent named volume mounted at '/var/lib/mysql', and (4) Environment variables linking App to DB hostname 'db'."
    ),
    (
        "Explain the architecture of a WordPress + MySQL application in Docker Compose.",
        "Consists of: (1) Official WordPress image exposing port 80/9090, (2) MySQL 5.7/8.0 database image, "
        "(3) Shared bridge network, and (4) Environment variables 'WORDPRESS_DB_HOST: db:3306', 'WORDPRESS_DB_USER', and 'WORDPRESS_DB_PASSWORD'."
    ),
    (
        "What is the difference between 'docker-compose' (v1 with hyphen) and 'docker compose' (v2 with space)?",
        "• 'docker-compose' (v1): A legacy standalone Python script that is deprecated and discontinued.\n"
        "• 'docker compose' (v2): A modern Go-based plugin compiled directly into the official Docker CLI, offering faster execution, resource sharing, and improved command syntax."
    ),
    (
        "How do you validate the syntax of a docker-compose.yml file without running it? (docker compose config)",
        "Run: $ docker compose config\n"
        "This parses the YAML file, validates syntax rules, resolves environment variable substitutions, and prints the fully resolved configuration. If syntax is invalid, it reports exact line errors."
    )
]

print(f"Docker Compose questions compiled: {len(COMPOSE_QUESTIONS)}")
