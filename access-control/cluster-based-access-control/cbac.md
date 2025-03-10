
## ClusterRole and ClusterRoleBinding ## 
- Used for managing access control and permissions at the cluster level. They define what actions can be performed on what resources in the Kubernetes cluster

## role and binding ##
kubectl apply -f access-control/cluster-based-access-control/cluster-role.yaml
kubectl apply -f access-control/cluster-based-access-control/cluster-role-binding.yaml

## Test access ##
kubectl auth can-i list pods --as John