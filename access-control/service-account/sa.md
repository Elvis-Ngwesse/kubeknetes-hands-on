
## Service Accounts ##
- Service accounts are essential for pods to interact with the Kubernetes API

## Create sa ##
kubectl apply -f access-control/service-account/pod-reader-sa.yaml

## Update the ClusterRoleBinding ##
- You need to ensure that the ClusterRoleBinding references the service account in the ops namespace correctly. You can update your existing ClusterRoleBinding to specify the correct namespace for the service account

## Create binding ##
kubectl apply -f access-control/service-account/pod-reader-sa-binding.yaml