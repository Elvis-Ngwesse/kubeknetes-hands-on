*********************
# kubeknetes-hands-on
*********************

## Deploy nginx containers ##
kubectl create namespace ops
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install apache-release bitnami/apache --namespace ops --set replicaCount=2
kubectl get pods -n ops
kubectl port-forward svc/apache-release 8080:80 -n ops

## Get contexts ##
kubectl config get-contexts
kubectl config current-context
kubectl config use-context <context-name>
kubectl config delete-context <context-name>

## List of actions (verbs) related to pods ##
verbs: ["get", "list", "create", "watch", "update", "patch", "delete", "deletecollection"]
