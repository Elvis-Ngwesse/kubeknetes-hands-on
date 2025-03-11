
## Role-Based Access Control (RBAC) ##
- Controls access to resources based on the roles assigned to users

## Get and delete default cluster role ##
kubectl get clusterrolebindings
kubectl get clusterrole cluster-admin -o yaml
kubectl delete clusterrolebinding cluster-admin

## Create a Role ##
- Roles define what actions can be performed on resources within a namespace
- pod-reader.yaml file created
kubectl apply -f access-control/role-based/role.yaml


## Create a RoleBinding ##
- RoleBindings assign a role to a user or service account
- pod-reader-rolebinding.yaml file created
kubectl apply -f access-control/role-based/rolebinding.yaml

## Get role and role-binding ##
kubectl get roles -n ops
kubectl get rolebindings -n ops

## Stop/Start minikube ##
minikube stop
minikube start


## Test Access ##
kubectl auth can-i list pods --as elvisngwesse -n ops
kubectl auth can-i delete pods --as elvisngwesse -n ops
kubectl auth can-i get pods --as elvisngwesse -n ops
kubectl delete pod [pod-name] -n ops

## Delete ##
kubectl delete rolebinding rolebinding-object -n ops
kubectl delete role role-object -n ops
