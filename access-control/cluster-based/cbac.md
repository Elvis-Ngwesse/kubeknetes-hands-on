
## ClusterRole and ClusterRoleBinding ## 
- Used for managing access control and permissions at the cluster level

## role and binding ##
kubectl apply -f access-control/cluster-based/cluster-role.yaml
kubectl apply -f access-control/cluster-based/cluster-role-binding.yaml

## Test access ##
kubectl auth can-i list pods --as elvisngwesse