"""
Viva Question and Answer Data Store for Topic 8: AWS EC2 & Cloud Deployment (50 questions).
"""

AWS_QUESTIONS = [
    (
        "What is Cloud Computing, and what are the three main service models? (IaaS, PaaS, SaaS)",
        "Cloud Computing is the on-demand delivery of compute power, database storage, applications, and other IT resources via the internet with pay-as-you-go pricing.\n"
        "• Infrastructure as a Service (IaaS, e.g. AWS EC2): Provides raw virtual servers, storage, and networking; user manages OS and software.\n"
        "• Platform as a Service (PaaS, e.g. AWS Elastic Beanstalk, Heroku): Provides a managed platform for deploying code without managing underlying servers.\n"
        "• Software as a Service (SaaS, e.g. Gmail, Microsoft 365): Complete end-user applications managed by provider."
    ),
    (
        "What is Amazon Web Services (AWS)?",
        "AWS is Amazon's comprehensive, globally distributed cloud computing platform offering over 200 fully featured services including compute (EC2), "
        "storage (S3, EBS), database (RDS), networking (VPC), and developer automation tools."
    ),
    (
        "What is Amazon EC2 (Elastic Compute Cloud)?",
        "Amazon EC2 provides resizable compute capacity in the cloud. It allows users to launch virtual servers (called 'EC2 instances') "
        "with customized operating systems, CPU, memory, storage, and security controls within minutes."
    ),
    (
        "What is an AMI (Amazon Machine Image)?",
        "An AMI is a pre-configured template that contains the operating system, architecture, and installed software needed to launch an EC2 instance. "
        "It acts as a master disk image blueprint (e.g. Ubuntu Server 22.04 LTS)."
    ),
    (
        "Which AMI is used in our laboratory sessions? (Ubuntu Server 22.04 LTS HVM)",
        "Ubuntu Server 22.04 LTS (HVM), SSD Volume Type, 64-bit (x86). "
        "It provides a stable, enterprise-grade Linux environment with 5-year long-term support and complete compatibility with Docker and Git."
    ),
    (
        "What is an EC2 Instance Type, and what does 't2.micro' signify?",
        "Instance types represent hardware configurations optimized for different workloads.\n"
        "• 't': Burstable general-purpose instance family.\n"
        "• '2': Generation number (second generation).\n"
        "• 'micro': Size designation providing 1 vCPU and 1 GiB of RAM."
    ),
    (
        "What are the specifications of t2.micro, and why is it chosen for student labs?",
        "Specifications: 1 vCPU, 1 GiB Memory, EBS storage only, Low to Moderate network performance. "
        "It is chosen because it is 100% Free Tier eligible, allowing students to complete laboratory exercises without incurring cloud charges."
    ),
    (
        "What is AWS Free Tier, and what are its limits for EC2?",
        "AWS Free Tier provides new accounts with 750 hours per month of Linux and Windows t2.micro (or t3.micro) instances for 12 months, "
        "along with 30 GiB of EBS storage, 500 MB container registry storage, and 15 GB data transfer out."
    ),
    (
        "What is an AWS Region vs an Availability Zone (AZ)?",
        "• AWS Region: A separate geographic area in the world (e.g. 'ap-south-1' Mumbai or 'us-east-1' N. Virginia) containing multiple physical data centers.\n"
        "• Availability Zone (AZ): One or more discrete data centers within a region with redundant power, networking, and connectivity (e.g. 'ap-south-1a', 'ap-south-1b')."
    ),
    (
        "Why should you select a region geographically close to you (e.g. ap-south-1 Mumbai)?",
        "Selecting a nearby region minimizes network latency (faster SSH terminal response and web page loading) and complies with local data residency regulations."
    ),
    (
        "What is a Key Pair in AWS EC2?",
        "A Key Pair consists of a public key stored on the EC2 instance and a private key file ('.pem') downloaded to the developer's computer. "
        "It uses asymmetric cryptography to authenticate SSH connections securely without transmitting passwords over the network."
    ),
    (
        "What key format is downloaded for SSH on Ubuntu/Linux? (.pem format)",
        "The '.pem' (Privacy Enhanced Mail) format, containing an OpenSSH RSA or ED25519 private key. (The '.ppk' format is used specifically for PuTTY on Windows)."
    ),
    (
        "What encryption algorithm is used by default for EC2 key pairs? (RSA or ED25519)",
        "RSA (Rivest-Shamir-Adleman, 2048-bit) or ED25519. Both provide strong public-key cryptographic authentication."
    ),
    (
        "Why does SSH fail with 'UNPROTECTED PRIVATE KEY FILE' on Ubuntu if key permissions are not modified?",
        "The OpenSSH client on Ubuntu strictly enforces permission checks on private key files. If the file permissions are accessible by group or others "
        "(e.g. default 0644 or 0755), SSH refuses to use the key because it is insecure, aborting with 'Permission denied (publickey)'."
    ),
    (
        "What exact command fixes private key permissions on Ubuntu? (chmod 400 ~/.ssh/key.pem)",
        "Run: $ chmod 400 ~/.ssh/devops-key.pem\n"
        "This sets permissions to read-only for the owner and denies all permissions to group and others ('-r--------')."
    ),
    (
        "What is the SSH command to connect to an Ubuntu EC2 instance from Ubuntu terminal?",
        "Run:\n"
        "$ ssh -i ~/.ssh/devops-key.pem ubuntu@<EC2-PUBLIC-IP>\n"
        "Where '-i' specifies the identity private key file, 'ubuntu' is the login user, and '<EC2-PUBLIC-IP>' is the instance's public IPv4 address."
    ),
    (
        "What is the default SSH username for Ubuntu AMI vs Amazon Linux AMI? (ubuntu vs ec2-user)",
        "• Ubuntu Server AMI: 'ubuntu'\n"
        "• Amazon Linux / RHEL / CentOS AMI: 'ec2-user'\n"
        "Using the wrong username causes 'Permission denied (publickey)' errors."
    ),
    (
        "What is EC2 Instance Connect, and how does it allow browser-based terminal access?",
        "EC2 Instance Connect is an AWS browser-based terminal client that pushes a temporary single-use SSH public key to instance metadata for 60 seconds, "
        "allowing users to connect directly from the AWS Console without needing a local SSH client or downloaded '.pem' file."
    ),
    (
        "What is a VPC (Virtual Private Cloud)?",
        "Amazon VPC is a logically isolated virtual network dedicated to your AWS account, resembling a traditional physical data center network. "
        "You control IP address ranges, subnets, route tables, and network gateways."
    ),
    (
        "What is a Subnet in AWS VPC? (Public Subnet vs Private Subnet)",
        "A Subnet is a segment of a VPC's IP address range designated to a specific Availability Zone.\n"
        "• Public Subnet: Has a direct route to an Internet Gateway (IGW); instances receive public IPs accessible from the internet.\n"
        "• Private Subnet: Has no direct route to the internet; used for backend databases and private microservices."
    ),
    (
        "What is an Internet Gateway (IGW)?",
        "An Internet Gateway is a horizontally scaled, redundant VPC component that enables communication between instances in your VPC and the internet, "
        "performing network address translation (NAT) between private and public IPv4 addresses."
    ),
    (
        "What is a Security Group in AWS?",
        "A Security Group acts as a virtual firewall for your EC2 instance to control incoming and outgoing network traffic at the hypervisor level."
    ),
    (
        "Are AWS Security Groups stateful or stateless? What does stateful mean?",
        "Security Groups are STATEFUL. 'Stateful' means that if you allow an inbound request (e.g. incoming HTTP traffic on port 80), "
        "the response traffic is automatically allowed outbound, regardless of outbound rules."
    ),
    (
        "What is an Inbound Rule vs an Outbound Rule in a Security Group?",
        "• Inbound Rule: Filters traffic coming INTO the instance from external networks (e.g. allowing port 22 for SSH or port 9090 for web app).\n"
        "• Outbound Rule: Filters traffic originating from inside the instance going OUT to external networks (e.g. downloading software packages)."
    ),
    (
        "By default, what inbound traffic is allowed in a newly created Security Group? (None, all blocked)",
        "By default, a new custom security group has NO inbound rules. All incoming traffic from the internet is completely blocked until explicit rules are added."
    ),
    (
        "By default, what outbound traffic is allowed in a newly created Security Group? (All outbound allowed)",
        "By default, an outbound rule allows ALL IPv4 traffic ('0.0.0.0/0') on all ports and protocols to leave the instance."
    ),
    (
        "Why must Port 22 be open in the Security Group? (SSH remote access)",
        "TCP Port 22 is the standard port used by the Secure Shell (SSH) protocol. If Port 22 is closed, all SSH terminal connection attempts will time out."
    ),
    (
        "Why must Port 80 and 443 be open?",
        "• Port 80: Standard unencrypted HTTP web traffic.\n"
        "• Port 443: Standard encrypted HTTPS (SSL/TLS) web traffic."
    ),
    (
        "You deploy an application on EC2 on port 9090, but the browser times out with ERR_CONNECTION_TIMED_OUT. What is the root cause?",
        "The EC2 instance's Security Group does not have an Inbound Rule allowing incoming TCP traffic on port 9090. "
        "The AWS hypervisor drops all packets destined for port 9090, causing the browser to hang and time out."
    ),
    (
        "Step-by-step, how do you add a Custom TCP inbound rule for port 9090 in AWS Management Console?",
        "1. In EC2 Console left sidebar → Under 'Network & Security', click 'Security Groups'.\n"
        "2. Click your instance's security group name → Click 'Inbound rules' tab in lower panel.\n"
        "3. Click 'Edit inbound rules' → Click 'Add rule' at bottom.\n"
        "4. Set Type: 'Custom TCP' | Port range: '9090' | Source: 'Anywhere-IPv4' (0.0.0.0/0).\n"
        "5. Click orange 'Save rules' button. Port unblocks instantly."
    ),
    (
        "What does 0.0.0.0/0 mean in CIDR notation for Security Group source?",
        "'0.0.0.0/0' represents all possible IPv4 addresses in the world. In a security group rule, it means the port is open to incoming requests from any computer on the public internet."
    ),
    (
        "What is Public IPv4 Address vs Private IPv4 Address on EC2?",
        "• Public IPv4 Address: Routable over the global internet. Used by users, browsers, and remote developers to connect to the instance.\n"
        "• Private IPv4 Address: Routable only within the VPC network (e.g. 172.31.x.x). Used for secure inter-instance communication within AWS."
    ),
    (
        "What happens to the Public IPv4 address when an EC2 instance is stopped and started?",
        "The instance releases its dynamic Public IPv4 address back to the AWS pool! "
        "When started again, AWS assigns a BRAND-NEW public IP address, breaking existing SSH bookmarks and web URLs."
    ),
    (
        "What is an Elastic IP address in AWS?",
        "An Elastic IP is a static, persistent public IPv4 address allocated to your AWS account that does NOT change when the instance is stopped, restarted, or rebooted."
    ),
    (
        "How does an Elastic IP address solve the problem of changing public IP addresses?",
        "Because an Elastic IP remains permanently tied to your AWS account and instance, DNS records and client bookmarks continue working seamlessly across instance stop/start events."
    ),
    (
        "How do you allocate and associate an Elastic IP address in AWS Management Console?",
        "1. EC2 Console left sidebar → 'Elastic IPs' → Click 'Allocate Elastic IP address' → Click 'Allocate'.\n"
        "2. Select the allocated IP → Click 'Actions' dropdown → Click 'Associate Elastic IP address'.\n"
        "3. Choose Resource type: 'Instance' → Select your running EC2 instance → Click 'Associate'."
    ),
    (
        "Does AWS charge for an allocated Elastic IP that is NOT associated with a running instance?",
        "YES! AWS charges a small hourly fee for Elastic IPs that are allocated but NOT attached to a running instance, to discourage hoarding scarce public IPv4 addresses."
    ),
    (
        "What is Amazon EBS (Elastic Block Store)?",
        "Amazon EBS provides persistent, raw block-level network storage volumes attached to EC2 instances, functioning like a physical virtual hard disk (SSD/HDD)."
    ),
    (
        "What is the difference between EBS root volume and instance store?",
        "• EBS Volume: Network-attached persistent storage. Data survives instance stop/start cycles.\n"
        "• Instance Store (ephemeral): Physically attached directly to host server hardware. Data is permanently wiped when the instance is stopped."
    ),
    (
        "How do you ensure database data persists across EC2 instance stop and start cycles?",
        "Store the database files on an Amazon EBS volume (the default root volume or an attached EBS secondary volume) with 'Delete on Termination' disabled."
    ),
    (
        "What is the difference between 'Stopping' an EC2 instance and 'Terminating' an EC2 instance?",
        "• Stopping: Shuts down instance compute. EBS storage remains intact and incurs standard storage fees. Can be restarted later.\n"
        "• Terminating: Permanently deletes the virtual server and attached root volume. The instance cannot be recovered, and all billing halts completely."
    ),
    (
        "Why must students always 'Terminate' EC2 instances at the end of their lab exam? (To prevent unexpected billing)",
        "Stopped instances still consume EBS storage allocation and can incur charges if left unattended. Terminating the instance releases all compute and storage resources, completely eliminating bill shock."
    ),
    (
        "How do you install Docker, Git, Java, and Maven inside an Ubuntu EC2 instance?",
        "Execute inside the EC2 SSH shell:\n"
        "$ sudo apt update && sudo apt upgrade -y\n"
        "$ sudo apt install -y docker.io git openjdk-17-jdk maven\n"
        "$ sudo systemctl enable --now docker"
    ),
    (
        "Why must you run 'sudo usermod -aG docker ubuntu && newgrp docker' on EC2?",
        "By default, only root can interact with the Docker daemon. Adding the 'ubuntu' user to the 'docker' group allows running docker commands without typing 'sudo'."
    ),
    (
        "How do you clone a GitHub repository and build a project inside an EC2 instance?",
        "$ git clone https://github.com/archanareddyse/OLTRS.git\n"
        "$ cd OLTRS\n"
        "$ mvn clean package -DskipTests\n"
        "Builds the WAR file inside 'target/' on the EC2 instance."
    ),
    (
        "How do you run a multi-container Docker application using Docker Compose inside an EC2 instance?",
        "Create 'docker-compose.yml' using nano on EC2:\n"
        "$ nano docker-compose.yml\n"
        "Then start the multi-container application:\n"
        "$ docker compose up -d"
    ),
    (
        "What is AWS IAM (Identity and Access Management)?",
        "AWS IAM is a web service that helps you securely control access to AWS resources. "
        "It manages authentication (who can sign in) and authorization (what permissions and policies they possess)."
    ),
    (
        "What is the difference between an IAM User and an IAM Role?",
        "• IAM User: An identity with long-term credentials (password, access keys) used by a specific human developer.\n"
        "• IAM Role: An identity with short-term, temporary credentials assigned to an AWS service (such as an EC2 instance) allowing it to securely access S3 or DynamoDB without hardcoding access keys."
    ),
    (
        "Why should you never use root AWS account credentials for day-to-day deployment tasks?",
        "The root account has unrestricted, god-mode access to all billing and cloud resources. If leaked or compromised, attackers can delete all infrastructure or launch expensive cryptomining farms. Principle of Least Privilege dictates using IAM users."
    ),
    (
        "What is Amazon CloudWatch, and how does it monitor EC2 instance CPU utilization and status checks?",
        "Amazon CloudWatch is AWS's native monitoring service. It automatically collects EC2 telemetry metrics every 5 minutes (or 1 minute with detailed monitoring), "
        "tracking CPUUtilization, NetworkIn/Out, DiskRead/Write, and System/Instance Status Checks, triggering alarms when thresholds are breached."
    )
]

print(f"AWS questions compiled: {len(AWS_QUESTIONS)}")
