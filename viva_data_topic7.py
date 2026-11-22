"""
Viva Question and Answer Data Store for Topic 7: Nagios Monitoring (50 questions).
"""

NAGIOS_QUESTIONS = [
    (
        "What is Nagios, and what is its role in DevOps infrastructure management?",
        "Nagios is an industry-standard open-source IT infrastructure monitoring and alerting engine. "
        "It monitors mission-critical servers, switches, applications, containers, and network protocols, proactively alerting system administrators via email/SMS when failures occur and when services recover."
    ),
    (
        "What are the main benefits of using Nagios for IT infrastructure monitoring?",
        "• Proactive Outage Detection: Detects hardware, server, or container downtime before end-users notice.\n"
        "• Root-Cause Analysis: Distinguishes between network path failure and actual host failure (network topology mapping).\n"
        "• SLA & Availability Reporting: Generates uptime and compliance reports.\n"
        "• Extensible Plugin Architecture: Any script returning standard exit codes (0, 1, 2, 3) can act as a custom Nagios monitoring plugin."
    ),
    (
        "How is Nagios deployed in a containerized environment using Docker on Ubuntu?",
        "Run the following terminal command:\n"
        "$ docker run -d --name nagios --restart=always -p 8090:80 jasonrivers/nagios:latest\n"
        "Runs Nagios Core web server on host port 8090."
    ),
    (
        "What host port is typically mapped to Nagios container port 80? (8090:80)",
        "Host port 8090 is mapped to container port 80 ('-p 8090:80') to avoid port collisions with host Apache/Nginx web servers or default port 80."
    ),
    (
        "What are the default login credentials for the Nagios Core web interface?",
        "• Username: 'nagiosadmin'\n"
        "• Password: 'nagios'\n"
        "Configured in the container's '/etc/nagios/htpasswd.users' Apache basic authentication file."
    ),
    (
        "What is the URL to access Nagios dashboard locally? (http://localhost:8090)",
        "Open any web browser on Ubuntu and navigate to: 'http://localhost:8090' (or 'http://<server-ip>:8090')."
    ),
    (
        "What is the Tactical Overview in the Nagios web console?",
        "Tactical Overview is the main executive dashboard screen. It summarizes the overall health of the monitored environment in a grid of gauges, "
        "displaying total host and service counts grouped by status (Up, Down, Unreachable, OK, Warning, Critical, Unknown)."
    ),
    (
        "What information is displayed in the 'Hosts' view in Nagios?",
        "Lists all monitored host machines/devices, showing: Host Name, Status (UP/DOWN/UNREACHABLE), Last Check timestamp, "
        "Duration in current state, and Status Information output from the host check command (e.g. 'PING OK - Packet loss = 0%')."
    ),
    (
        "What information is displayed in the 'Services' view in Nagios?",
        "Lists all monitored service checks grouped by host. Displays: Host, Service Description (e.g. HTTP, SSH, Root Partition), "
        "Status (OK/WARNING/CRITICAL/UNKNOWN), Last Check time, Duration, Attempt count (e.g. 1/3), and plugin performance data."
    ),
    (
        "What does the 'Service Problems' section show in the Nagios dashboard?",
        "Provides a filtered alert view showing ONLY services currently in non-OK states (WARNING, CRITICAL, or UNKNOWN), "
        "allowing operations engineers to focus immediately on active failures."
    ),
    (
        "What is the Event Log in Nagios, and how is it used during troubleshooting?",
        "The Event Log is a chronological audit record of all internal monitoring events: check executions, status transitions (OK → CRITICAL), "
        "notification emails dispatched, system shutdowns, and flap detections."
    ),
    (
        "What does the 'Notifications' view show in Nagios?",
        "Displays historical records of all alert notifications dispatched to contacts, indicating contact name, host/service, notification type (PROBLEM/RECOVERY), and timestamp."
    ),
    (
        "What is the Nagios Map feature?",
        "Map generates a visual network topology graph showing relationships and parent-child dependencies between routers, switches, and servers, "
        "visually highlighting which device failure caused dependent nodes to become unreachable."
    ),
    (
        "Explain the four Nagios service status codes, labels, and dashboard colors: 0, 1, 2, 3.",
        "• 0: OK (Green) — Service is functioning normally within threshold limits.\n"
        "• 1: WARNING (Yellow) — Service is functional but approaching critical thresholds (e.g. disk 85% full).\n"
        "• 2: CRITICAL (Red) — Service is down, unresponsive, or exceeding critical threshold (e.g. HTTP 500 error, port closed).\n"
        "• 3: UNKNOWN (Orange) — Plugin syntax error or plugin failed to execute properly."
    ),
    (
        "What are the two types of host status in Nagios? (UP, DOWN, UNREACHABLE)",
        "• UP: Host is responding to ping/check commands.\n"
        "• DOWN: Host is unresponsive, and all parent routers/switches are UP (the host itself has died).\n"
        "• UNREACHABLE: Host is unresponsive, but its parent gateway/router is ALSO down (network path broken, host may still be alive)."
    ),
    (
        "What is a 'Soft State' vs a 'Hard State' in Nagios?",
        "• Soft State: A service or host fails a check, but has not yet exceeded 'max_check_attempts'. Nagios retries checks at 'retry_interval' without sending alerts.\n"
        "• Hard State: Failure persists beyond 'max_check_attempts' (e.g. 3 consecutive failed checks). Nagios records a permanent hard failure and immediately dispatches alerts."
    ),
    (
        "What is 'max_check_attempts', and how does it transition a Soft state to a Hard state?",
        "'max_check_attempts' defines how many consecutive times a check must fail before triggering an alert. "
        "If set to 3, attempt 1/3 (Soft) → attempt 2/3 (Soft) → attempt 3/3 (Hard State triggered → email sent)."
    ),
    (
        "Where are Nagios configuration files located inside the container? (/opt/nagios/etc/)",
        "Inside the container at '/opt/nagios/etc/'. Key object definition files reside under '/opt/nagios/etc/objects/'."
    ),
    (
        "What is 'nagios.cfg', and what role does it play?",
        "'nagios.cfg' is the primary master configuration file. It controls daemon behavior, specifies log file locations, "
        "sets check intervals, and includes all object definition configuration files via 'cfg_file=' directives."
    ),
    (
        "What is the purpose of 'objects/hosts.cfg'?",
        "Defines physical and virtual machines to be monitored, including hostnames, IP addresses, parent relationships, check intervals, and contact groups."
    ),
    (
        "What is the purpose of 'objects/services.cfg'?",
        "Defines specific checks performed against monitored hosts (e.g. checking HTTP on port 9090, ping latency, SSH responsiveness, disk usage)."
    ),
    (
        "What is the purpose of 'objects/commands.cfg'?",
        "Maps high-level check commands (e.g. 'check_http') to physical executable plugin binaries and arguments on disk (e.g. '$USER1$/check_http -H $HOSTADDRESS$ -p $ARG1$')."
    ),
    (
        "What is the purpose of 'objects/contacts.cfg' and 'contactgroups.cfg'?",
        "'contacts.cfg' defines administrator identities, email addresses, and notification time periods. 'contactgroups.cfg' bundles contacts into logical teams (e.g. devops-admins)."
    ),
    (
        "What is the purpose of 'objects/templates.cfg'?",
        "Contains common object templates ('linux-server', 'generic-service') defining default check intervals, retry attempts, and notification periods inherited by other definitions via 'use <template>'."
    ),
    (
        "How do you define a monitored host in Nagios? (Explain fields)",
        "define host {\n"
        "    use                     linux-server\n"
        "    host_name               oltrs-web-app\n"
        "    alias                   Online Ticket Reservation\n"
        "    address                 172.17.0.1\n"
        "    max_check_attempts      3\n"
        "    check_period            24x7\n"
        "    notification_interval   30\n"
        "    notification_period     24x7\n"
        "}"
    ),
    (
        "How do you define a monitored service in Nagios? (Explain fields)",
        "define service {\n"
        "    use                     generic-service\n"
        "    host_name               oltrs-web-app\n"
        "    service_description     HTTP Port 9090 Status\n"
        "    check_command           check_http!-p 9090 -u /ROOT/\n"
        "    check_interval          1\n"
        "    retry_interval          1\n"
        "    max_check_attempts      2\n"
        "    notification_period     24x7\n"
        "}"
    ),
    (
        "What is a Nagios Plugin?",
        "A Nagios Plugin is an independent executable program or script (written in C, Bash, Python, or Perl) that performs a specific monitoring test "
        "and exits with a standardized exit code (0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN) along with a single line of status text on stdout."
    ),
    (
        "Where are standard Nagios plugins installed? (/opt/nagios/libexec/)",
        "In the container, plugins reside at '/opt/nagios/libexec/' (referenced by the macro '$USER1$'). On native Ubuntu, they are at '/usr/lib/nagios/plugins/'."
    ),
    (
        "What does the 'check_ping' plugin do, and what are warning/critical arguments?",
        "'check_ping' sends ICMP ECHO packets to test network reachability, packet loss, and round-trip time (RTT).\n"
        "Syntax: 'check_ping -H <ip> -w <rtt,loss%> -c <rtt,loss%>'.\n"
        "Example: '-w 100.0,20% -c 500.0,60%' triggers Warning if latency exceeds 100ms or loss >20%; Critical if >500ms or >60%."
    ),
    (
        "What does the 'check_http' plugin do, and how do you monitor a specific port (e.g. 9090)?",
        "'check_http' connects to an HTTP/HTTPS web server, verifies TCP port connection, and validates HTTP status codes (expecting 200/300).\n"
        "To check port 9090: 'check_http!-p 9090 -u /ROOT/'."
    ),
    (
        "What does the 'check_ssh' plugin do?",
        "'check_ssh' connects to TCP port 22 on the target host and validates that the SSH server banner (e.g. OpenSSH_8.9) is returned."
    ),
    (
        "What does the 'check_disk' plugin do?",
        "'check_disk' checks available storage space on local filesystem mount points, triggering Warning/Critical when free disk space falls below thresholds (e.g. '-w 15% -c 5%')."
    ),
    (
        "What does the 'check_tcp' plugin do?",
        "'check_tcp -H <ip> -p <port>' attempts a raw TCP socket connection on the specified port (useful for MySQL port 3306 or Redis port 6379)."
    ),
    (
        "How do you write a custom Nagios plugin script? (Exit codes: 0, 1, 2, 3)",
        "Write a shell script that performs a check, prints a summary message, and exits with:\n"
        "• exit 0 for OK\n"
        "• exit 1 for WARNING\n"
        "• exit 2 for CRITICAL\n"
        "• exit 3 for UNKNOWN"
    ),
    (
        "How do you run the pre-flight verification command to test Nagios configuration syntax?",
        "Execute inside the container:\n"
        "$ docker exec -it nagios /opt/nagios/bin/nagios -v /opt/nagios/etc/nagios.cfg\n"
        "Validates syntax across all configuration files and reports 'Total Errors: 0'."
    ),
    (
        "Why is running pre-flight verification essential before restarting Nagios?",
        "If a configuration file has a syntax error or missing closing bracket, restarting Nagios will cause the daemon to crash immediately and fail to start, "
        "leaving the entire infrastructure unmonitored."
    ),
    (
        "How do you reload or restart Nagios to apply configuration changes?",
        "Restart the container or send SIGHUP:\n"
        "$ docker restart nagios\n"
        "Or inside container: $ /etc/init.d/nagios reload"
    ),
    (
        "What is Active Checking vs Passive Checking in Nagios?",
        "• Active Checking: Nagios daemon initiates checks on a scheduled polling timer (e.g. every 5 minutes) by invoking plugins.\n"
        "• Passive Checking: External applications or remote hosts initiate checks asynchronously and push results back to Nagios via NSCA (Nagios Service Check Acceptor)."
    ),
    (
        "What is NRPE (Nagios Remote Plugin Executor), and why is it used?",
        "NRPE is an addon that allows Nagios to execute plugins on remote Linux/Ubuntu hosts to monitor local resources that cannot be queried over the network (e.g. CPU load, memory usage, local disk space)."
    ),
    (
        "How does NRPE execute plugins on remote Ubuntu servers?",
        "The Nagios server runs 'check_nrpe', which connects via SSL to the 'nrpe' daemon on the remote Ubuntu host. "
        "The remote daemon runs the local plugin and returns the exit code and text output back to the Nagios server."
    ),
    (
        "What is NSClient++, and what operating system is it used for? (Windows monitoring)",
        "NSClient++ is a lightweight monitoring agent installed on Microsoft Windows servers to allow Nagios to monitor Windows performance counters, Event Logs, and Windows Services."
    ),
    (
        "What is check scheduling in Nagios? (check_interval and retry_interval)",
        "• 'check_interval': The normal polling interval (in minutes) when the service is in an OK state (e.g. check every 5 minutes).\n"
        "• 'retry_interval': The aggressive polling interval (e.g. every 1 minute) used when a service enters a Soft failure state until max_check_attempts is reached."
    ),
    (
        "What is flapping in Nagios monitoring, and how does flap detection prevent alert spam?",
        "Flapping occurs when a service rapidly switches between OK and CRITICAL states (e.g. intermittent network cable). "
        "Flap detection tracks state change history percentage; when flapping is detected, Nagios temporarily suppresses email notifications to prevent alert storms."
    ),
    (
        "How does Nagios send email alerts to system administrators?",
        "When a Hard failure triggers, Nagios passes contact email, host details, and alert text to a local mail transport agent (like 'mail' or 'sendmail') defined in 'commands.cfg' under 'notify-service-by-email'."
    ),
    (
        "How do you configure Nagios alongside application containers in Docker Compose (SET 8)?",
        "Add a 'nagios' service in 'docker-compose.yml' connected to the same custom bridge network as the application container. "
        "Nagios uses the Docker service name (e.g. 'http://app:8080') to monitor the application container directly."
    ),
    (
        "How does Nagios communicate with target containers on the same Docker bridge network?",
        "Containers on the same user-defined bridge network communicate via Docker's embedded DNS. Nagios resolves the target container name to its container IP directly."
    ),
    (
        "How do you schedule maintenance downtime for a host in Nagios to silence alerts?",
        "In the Nagios Web UI: Navigate to Host → Click 'Schedule downtime for this host' → Specify start time, end time, and comment. "
        "Nagios continues monitoring during this window but suppresses all email notifications."
    ),
    (
        "What is an escalation in Nagios notification rules?",
        "Escalations define rules where notifications are sent to higher-level management or on-call engineers if an alert remains unacknowledged in CRITICAL state after a specified duration."
    ),
    (
        "What are the primary differences between Nagios Core and Nagios XI?",
        "• Nagios Core: Free, open-source command-line-driven monitoring daemon with basic web interface.\n"
        "• Nagios XI: Commercial enterprise edition featuring automated configuration wizards, database backend, advanced reporting, graphical dashboard designer, and role-based access control."
    ),
    (
        "How does Nagios compare with modern observability tools like Prometheus and Grafana?",
        "Nagios is primarily a host/service status monitoring and alerting tool based on discrete checks. "
        "Prometheus is a time-series metric aggregation database that scrapes continuous telemetry metrics (CPU%, latency percentiles) paired with Grafana for rich dynamic metric visualization."
    )
]

print(f"Nagios questions compiled: {len(NAGIOS_QUESTIONS)}")
