## install nfs-server ##
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install nfs-server stable/nfs-server-provisioner -f volume/remote-storage/values.yaml

## Create a volume claim ##
kubectl apply -f volume/remote-storage/nfs-pvc.yaml
kubectl get pvc -n test
kubectl get pv

## Uninstall/delete ##
helm uninstall nfs-server
kubectl delete all --all










kubectl describe node
helm status nfs-storage -n storage

## Test export dir of nfs-server ##

- kubectl get pods -n storage
- kubectl get statefulsets -n storage
- kubectl get statefulsets nfs-pro-nfs-server-provisioner -o yaml -n storage
- kubectl logs nfs-pro-nfs-server-provisioner-0 -n storage
- kubectl exec -it nfs-pro-nfs-server-provisioner-0 -n storage -- sh -c "exportfs -v" 


#############################
Test host dir of minikube host
#############################
- minikube ssh
- ls -ld /mnt/disks/nfs_data/exports

 

 kubectl describe pvc nfs-pvc-01 -n test
kubectl describe pvc nfs-pvc-02 -n test
kubectl delete pvc --all -n test
kubectl delete pv --all
