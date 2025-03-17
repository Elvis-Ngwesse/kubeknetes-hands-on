## install nfs-server ##
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm show values stable/nfs-server-provisioner > volume/remote-storage/values.yaml
helm install nfs-server stable/nfs-server-provisioner -f volume/remote-storage/values.yaml

## Get nfs pv/pvc volumes ##
kubectl get pvc
kubectl get pvc

This confirms that the Helm chart successfully created both a PVC and a PV (dynamically provisioned) based on my nfs-values.yaml configuration. The PVC is currently bound to the PV, and the volume is ready for use

## Attach a pod to the pvc ##
Create a Kubernetes pod that references the PVC (data-nfs-server-pod-0), which is already bound to the PV

kubectl apply -f volume/remote-storage/busybox-pv-1.yaml
kubectl apply -f volume/remote-storage/busybox-pv-2.yaml
kubectl get pods busybox-container-01
kubectl get pods busybox-container-02

## Verify data in the pv ##
kubectl exec -it busybox-container-01 -- /bin/sh
cat /mnt/nfs_share/data.txt
You should see the text [Hello, NFS! The time is Mon Mar 17 06:50:50 UTC 2025] being written to data.txt every 5 seconds as specified in the command part of the pod.

## Verify Data Logs in the pv ##






## Create a volume claim ##
kubectl apply -f volume/remote-storage/nfs-pvc.yaml
kubectl get pvc -n test



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

