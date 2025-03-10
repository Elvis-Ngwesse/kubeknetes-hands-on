
## Role-Based Access Control (RBAC) ##
- Controls access to resources based on the roles assigned to users or service accounts

## Deloy nginx containers ##
kubectl create namespace ops
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install apache-release bitnami/apache --namespace ops --set replicaCount=2
kubectl get pods -n ops
kubectl port-forward svc/apache-release 8080:80 -n ops

## Create a Role ##
- Roles define what actions can be performed on resources within a namespace
- pod-reader.yaml file created
- kubectl apply -f access-control/role-based-access-control/pod-reader.yaml


## Create a RoleBinding ##
- RoleBindings assign a role to a user or service account
- pod-reader-rolebinding.yaml file created
- kubectl apply -f access-control/role-based-access-control/pod-reader-rolebinding.yaml

## Get role and role-binding ##
kubectl get roles -n ops
kubectl get rolebindings -n ops

## Test Access ##
kubectl auth can-i get pods --as john -n ops
kubectl auth can-i get pods --as elvisngwesse -n ops
