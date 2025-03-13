*********************
# kubeknetes-hands-on
minikube start
minikube delete
*********************

## Deploy nginx containers ##
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
kubectl create namespace ops
helm install apache-release bitnami/apache --namespace ops --set replicaCount=2
kubectl get pods -n ops
kubectl port-forward svc/apache-release 8080:80 -n ops

## Get contexts ##
kubectl config get-contexts
kubectl config current-context
kubectl config use-context <context-name>
kubectl config delete-context <context-name>

## Create context ##
kubectl config set-context local --cluster=minikube --user=elvisngwesse
kubectl config use-context local

## List of actions (verbs) related to pods ##
verbs: ["get", "list", "create", "watch", "update", "patch", "delete", "deletecollection"]

## Uninstall ##
helm uninstall apache-release --namespace ops

## Kube config ##
cat ~/.kube/config
rm ~/.kube/config

## venv ##
python3 -m venv venv
source venv/bin/activate

## install dependencies ##
pip install -r requirements.txt

## Architechture ##

- Master Node
	- API Server
		- Authentication using headers
		- Authorization based on RBAC rules
		- Admission
		* Informs Kubelet on workload to execute

	- Scheduler
		- Resources
		- Taints
		- Toleration
		- Node affinity
		* Schedules pode on node
		* Sends back info to api server
	- Control Manager
		- Replication controller
		- Deamon-set controller
		- Statefull set controller
	- ETCD
		- Stores all info and config of cluster
		- Cluster state is maintained in ETCD
		- API server updates ETCD

- Worker Node
	- Kubelet
		- Request work load from api server
		- Uses container runtime such as docker to run container based on config
		- 
	- Kube-proxy
		- Manages all network communication


