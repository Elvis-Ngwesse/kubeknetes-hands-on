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

## Deploy with SA ##
kubectl label serviceaccount sa-object -n ops app.kubernetes.io/managed-by=Helm
kubectl annotate serviceaccount sa-object -n ops meta.helm.sh/release-name=apache-release
kubectl annotate serviceaccount sa-object -n ops meta.helm.sh/release-namespace=ops

helm install apache-release bitnami/apache --namespace ops --set replicaCount=2 --set serviceAccount.name=sa-object


## Get contexts ##
kubectl config get-contexts
kubectl config current-context
kubectl config use-context <context-name>
kubectl config delete-context <context-name>

## List of actions (verbs) related to pods ##
verbs: ["get", "list", "create", "watch", "update", "patch", "delete", "deletecollection"]

## Uninstall ##
helm uninstall apache-release --namespace ops
