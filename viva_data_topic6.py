"""
Viva Question and Answer Data Store for Topic 6: Kubernetes & Minikube (50 questions).
"""

K8S_QUESTIONS = [
    (
        "What is Kubernetes (K8s), and why was it created?",
        "Kubernetes is an open-source container orchestration platform originally developed by Google. "
        "It was created to automate the deployment, scaling, health-checking, load-balancing, and lifecycle management of multi-container applications across clusters of physical or virtual machines."
    ),
    (
        "What are the key features of Kubernetes?",
        "• Automated Self-Healing: Restarts failed containers, replaces pods, and reschedules pods when nodes die.\n"
        "• Horizontal Auto-Scaling: Dynamically scales application replicas based on CPU/memory usage.\n"
        "• Service Discovery & Load Balancing: Assigns stable internal DNS names and load-balances network traffic across pods.\n"
        "• Automated Rollouts and Rollbacks: Progressively deploys image updates with zero downtime and enables one-click rollbacks.\n"
        "• Storage Orchestration: Mounts local, cloud (EBS), or network storage (NFS) automatically."
    ),
    (
        "What is the difference between Docker and Kubernetes?",
        "• Docker: A container runtime platform used to build, package, and execute containers on a single host machine.\n"
        "• Kubernetes: A cluster orchestration engine that coordinates hundreds of Docker containers across multiple nodes, handling auto-scaling, fault tolerance, high availability, and network routing."
    ),
    (
        "What is Minikube?",
        "Minikube is a tool that provisions a lightweight, single-node Kubernetes cluster locally on a developer's computer. "
        "It packages all control plane and worker node components into a single virtual environment, ideal for learning and testing Kubernetes workflows."
    ),
    (
        "What hypervisor/driver does Minikube use on Ubuntu? (Docker driver)",
        "On Ubuntu Linux, Minikube uses the 'docker' driver by default ('minikube start --driver=docker'). "
        "The entire Kubernetes node runs inside an optimized Docker container on the host system without requiring VirtualBox or KVM."
    ),
    (
        "How do you install Minikube and kubectl on Ubuntu?",
        "# Install Minikube:\n"
        "$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64\n"
        "$ sudo install minikube-linux-amd64 /usr/local/bin/minikube\n"
        "# Install kubectl:\n"
        "$ curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"\n"
        "$ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl"
    ),
    (
        "What command starts the Minikube cluster? (minikube start --driver=docker)",
        "Run: $ minikube start --driver=docker\n"
        "Initializes the control plane, starts etcd and kubelet, and configures the local kubeconfig context to point to the minikube cluster."
    ),
    (
        "What does 'kubectl cluster-info' show?",
        "Displays the active Kubernetes control plane endpoint URL (e.g. 'Kubernetes control plane is running at https://192.168.49.2:8443') "
        "and CoreDNS service endpoints."
    ),
    (
        "What does 'kubectl get nodes' show?",
        "Lists all physical or virtual cluster worker/master nodes, showing: NAME (minikube), STATUS (Ready), ROLES (control-plane), "
        "AGE, and Kubernetes VERSION (v1.28.x)."
    ),
    (
        "What is the Kubernetes Control Plane (Master Node), and what are its key components?",
        "The Control Plane manages global cluster state, schedules workloads, and responds to cluster events. Its components are:\n"
        "1. kube-apiserver: Central gateway exposing the REST API.\n"
        "2. etcd: Consistent, highly-available distributed key-value store.\n"
        "3. kube-scheduler: Evaluates resource constraints and assigns newly created pods to healthy worker nodes.\n"
        "4. kube-controller-manager: Runs core control loops (Node Controller, Replication Controller, Endpoints Controller)."
    ),
    (
        "What is the role of etcd in Kubernetes?",
        "'etcd' is an open-source distributed key-value store that acts as the single source of truth for Kubernetes. "
        "Every piece of cluster state, manifest specification, pod status, and secret data is stored in etcd."
    ),
    (
        "What are the components of a Kubernetes Worker Node?",
        "1. kubelet: Node agent that communicates with the API server and ensures container pods described in PodSpecs are running and healthy.\n"
        "2. kube-proxy: Network proxy maintaining network rules on nodes and enabling Kubernetes service routing.\n"
        "3. Container Runtime: Software (e.g. containerd, CRI-O, Docker) responsible for physically pulling and running container images."
    ),
    (
        "What is a Pod in Kubernetes?",
        "A Pod is the smallest and simplest deployable unit in Kubernetes. "
        "A Pod represents a single instance of a running process in your cluster, encapsulating one or more tightly coupled containers, shared storage volumes, and a unique network IP address."
    ),
    (
        "Can a Pod contain more than one container? When is this pattern used (Sidecar)?",
        "Yes (Multi-container Pod). Containers in the same pod share localhost network interface and storage volumes. "
        "Used in the 'Sidecar' pattern, where a helper container assists the main container (e.g. logging agent, proxy sidecar like Envoy, or metrics collector)."
    ),
    (
        "Why are Pods ephemeral?",
        "Pods are mortal and disposable. They can be created, killed, or rescheduled at any moment due to node failures, resource exhaustion, or scaling events. "
        "When a pod dies, its private IP is lost permanently. Therefore, deployments and services are used rather than managing standalone pods directly."
    ),
    (
        "What is a Deployment in Kubernetes?",
        "A Deployment is a higher-level declarative controller that manages a set of identical Pods via a ReplicaSet. "
        "It provides declarative updates, automated scaling, rolling upgrades, and instant rollbacks."
    ),
    (
        "What is a ReplicaSet, and what is its relationship to Deployments and Pods?",
        "A ReplicaSet's sole purpose is to maintain a stable set of replica Pods running at any given time. "
        "A Deployment manages ReplicaSets, and a ReplicaSet manages Pods. When a Deployment is updated, it creates a new ReplicaSet and scales down the old one."
    ),
    (
        "How do you create a Deployment imperatively using kubectl create deployment?",
        "Run: $ kubectl create deployment oltrs-app --image=dheerajmalavath/oltrs:latest\n"
        "Creates a deployment object named 'oltrs-app' running 1 replica pod of the specified Docker Hub image."
    ),
    (
        "How do you view all deployments in a cluster?",
        "Run: $ kubectl get deployments\n"
        "Displays: NAME, READY (e.g. 4/4), UP-TO-DATE, AVAILABLE, and AGE."
    ),
    (
        "What does 'kubectl describe deployment <name>' provide?",
        "Provides extensive diagnostic metadata: selector labels, replica counts, rolling update strategy (Max Surge, Max Unavailable), "
        "pod template specifications, and recent events (scaling events, replica set creation)."
    ),
    (
        "How do you list all running Pods with IP addresses and assigned nodes? (kubectl get pods -o wide)",
        "Run: $ kubectl get pods -o wide\n"
        "Displays pod name, status (Running), restart count, IP address (e.g. 10.244.0.5), and NODE (minikube)."
    ),
    (
        "How do you inspect Pod logs using kubectl logs?",
        "Run: $ kubectl logs <pod-name>\n"
        "Stream live logs with: $ kubectl logs -f <pod-name>"
    ),
    (
        "How do you execute an interactive shell inside a Pod? (kubectl exec -it <pod> -- /bin/bash)",
        "Run: $ kubectl exec -it <pod-name> -- /bin/bash\n"
        "Opens an interactive terminal prompt inside the pod container."
    ),
    (
        "How do you delete a Pod? What happens immediately after a Pod belonging to a Deployment is deleted?",
        "Run: $ kubectl delete pod <pod-name>\n"
        "The pod enters 'Terminating' status. Immediately, the parent ReplicaSet observes current count (3) < desired count (4) "
        "and instantly creates a brand-new replacement pod with a new name and IP to maintain the desired count."
    ),
    (
        "Explain Kubernetes Self-Healing: How does it automatically recover crashed or deleted pods?",
        "Kubernetes continuously executes a reconciliation control loop comparing CURRENT state against DESIRED state. "
        "If a container crashes or a pod is deleted, the ReplicaSet controller detects the discrepancy in etcd and schedules a replacement pod on a healthy node automatically."
    ),
    (
        "How do you scale a Deployment to 4 replicas using kubectl scale? (Exam favorite)",
        "Run: $ kubectl scale deployment oltrs-app --replicas=4\n"
        "Verify with: $ kubectl get pods\n"
        "All 4 pods will transition from ContainerCreating to Running status."
    ),
    (
        "What happens if cluster resources are insufficient when scaling to 4 replicas? (Pending status)",
        "Pods enter 'Pending' status. The kube-scheduler cannot find any worker node with sufficient CPU or memory to host the pod. "
        "Diagnose via '$ kubectl describe pod <pending-pod>' which shows 'FailedScheduling: Insufficient memory/cpu'."
    ),
    (
        "What is a Kubernetes Service, and why is it necessary given that Pods are ephemeral and have dynamic IPs?",
        "A Service is an abstraction that defines a logical set of Pods and a policy to access them. "
        "Because Pods are ephemeral and receive new dynamic IPs when replaced, a Service provides a single, permanent IP address and DNS name that load-balances traffic across all matching healthy pods."
    ),
    (
        "What are the three primary types of Kubernetes Services? (ClusterIP, NodePort, LoadBalancer)",
        "1. ClusterIP (Default): Exposes the service on a cluster-internal IP. Reachable ONLY from within the cluster.\n"
        "2. NodePort: Exposes the service on each Node's IP at a static port (30000–32767). Accessible from external browsers.\n"
        "3. LoadBalancer: Provisions a cloud provider's external load balancer (e.g. AWS NLB/ALB) and assigns a public routable IP."
    ),
    (
        "What is ClusterIP service, and when is it used?",
        "ClusterIP provides an internal virtual IP and DNS name for internal microservice communication (e.g. backend web app connecting to internal MySQL database). "
        "It prevents exposing internal databases directly to the public internet."
    ),
    (
        "What is a NodePort service, and what is the standard port range? (30000–32767)",
        "NodePort allocates a high-range port between 30000 and 32767 on all cluster nodes. "
        "External traffic sent to '<NodeIP>:<NodePort>' is automatically routed by kube-proxy to the service's target pods."
    ),
    (
        "What is a LoadBalancer service, and where is it typically deployed?",
        "LoadBalancer integrates directly with cloud platforms (AWS, GCP, Azure). When created, AWS automatically provisions an Elastic Load Balancer (ELB) "
        "pointing to cluster NodePorts, giving the application a globally accessible public DNS endpoint."
    ),
    (
        "How do you expose a Deployment as a NodePort service using kubectl expose?",
        "Run: $ kubectl expose deployment oltrs-app --type=NodePort --port=8080 --target-port=8080\n"
        "Verify with: $ kubectl get svc"
    ),
    (
        "How do you retrieve the external browser access URL for a NodePort service in Minikube? (minikube service <name> --url)",
        "Run: $ minikube service oltrs-app --url\n"
        "Outputs accessible URL: http://192.168.49.2:31254, which can be opened in browser or tested with 'curl -I'."
    ),
    (
        "What is a Rolling Update in Kubernetes?",
        "A Rolling Update incrementally replaces old pod instances with new pod instances with zero application downtime. "
        "Kubernetes spins up new pods, waits for readiness checks to pass, and only then terminates the old pods."
    ),
    (
        "How do you trigger a rolling update to a new container image using kubectl set image?",
        "Run: $ kubectl set image deployment/oltrs-app oltrs=dheerajmalavath/oltrs:v2\n"
        "Kubernetes initiates rolling update to version v2."
    ),
    (
        "How do you monitor rollout progress using kubectl rollout status?",
        "Run: $ kubectl rollout status deployment/oltrs-app\n"
        "Prints progress: 'Waiting for deployment \"oltrs-app\" rollout to finish: 2 of 4 updated replicas are available... deployment successfully rolled out'."
    ),
    (
        "How do you check rollout history using kubectl rollout history?",
        "Run: $ kubectl rollout history deployment/oltrs-app\n"
        "Displays revision numbers (e.g. 1, 2) and change-cause annotations."
    ),
    (
        "How do you undo/rollback a failed update in Kubernetes? (kubectl rollout undo)",
        "Run: $ kubectl rollout undo deployment/oltrs-app\n"
        "Reverts pods back to the previous stable ReplicaSet revision instantly."
    ),
    (
        "What is a Declarative YAML manifest in Kubernetes?",
        "A YAML manifest defines the desired state of Kubernetes objects (Deployments, Services, ConfigMaps). "
        "Rather than typing imperative commands, manifests are version-controlled in Git and applied via 'kubectl apply -f'."
    ),
    (
        "What are the required top-level fields in any Kubernetes YAML manifest?",
        "1. 'apiVersion': API version (e.g. 'apps/v1' for Deployments, 'v1' for Services/Pods).\n"
        "2. 'kind': Type of object (Deployment, Service, Pod).\n"
        "3. 'metadata': Object name, namespace, labels.\n"
        "4. 'spec': Desired state specification (replicas, containers, ports, selectors)."
    ),
    (
        "What is the purpose of Labels and Selectors (matchLabels) in Kubernetes YAML?",
        "Labels are key-value tags attached to objects (e.g. 'app: oltrs'). "
        "Selectors ('matchLabels') are queries used by Deployments and Services to identify and group which Pods they control and route traffic to."
    ),
    (
        "How do you apply YAML configuration files using kubectl apply -f?",
        "Run: $ kubectl apply -f deployment.yaml\n"
        "Creates or updates the resource to match the YAML specification without deleting existing unaffected state."
    ),
    (
        "What is a Namespace in Kubernetes, and what are the default namespaces?",
        "A Namespace provides logical cluster partitioning and resource isolation within a physical cluster.\n"
        "Default namespaces: (1) 'default' (user workloads), (2) 'kube-system' (control plane components), (3) 'kube-public', and (4) 'kube-node-lease'."
    ),
    (
        "What is a ConfigMap, and how does it decouple configuration from container images?",
        "A ConfigMap stores non-confidential configuration data as key-value pairs (e.g. DB URLs, app settings). "
        "Pods consume ConfigMaps as environment variables or mounted files, allowing application configurations to change without rebuilding container images."
    ),
    (
        "What is a Kubernetes Secret, and how does it store sensitive data?",
        "A Secret stores confidential data (passwords, tokens, SSH keys, TLS certs) encoded in Base64. "
        "Secrets are mounted into pod memory (tmpfs) rather than written to persistent node storage, minimizing exposure risk."
    ),
    (
        "What is a PersistentVolume (PV) and PersistentVolumeClaim (PVC)?",
        "• PersistentVolume (PV): A piece of storage provisioned in the cluster (e.g. AWS EBS, NFS, local disk).\n"
        "• PersistentVolumeClaim (PVC): A request for storage by a developer (requesting e.g. 10Gi with ReadWriteOnce access). Kubernetes binds matching PVCs to PVs."
    ),
    (
        "What is a Liveness Probe vs a Readiness Probe in Kubernetes?",
        "• Liveness Probe: Checks if container is alive. If probe fails, kubelet kills the container and restarts it according to restartPolicy.\n"
        "• Readiness Probe: Checks if application is ready to accept user network traffic. If probe fails, the service stops routing traffic to the pod until it recovers."
    ),
    (
        "What does 'kubectl get all' show?",
        "Returns a comprehensive snapshot of all resources in the active namespace: pods, services, daemonsets, deployments, and replicasets."
    ),
    (
        "How do you cleanly delete a Deployment and its associated Service?",
        "Run:\n"
        "$ kubectl delete deployment oltrs-app\n"
        "$ kubectl delete service oltrs-app\n"
        "Terminates all pods, stops traffic routing, and frees cluster resources."
    )
]

print(f"Kubernetes questions compiled: {len(K8S_QUESTIONS)}")
