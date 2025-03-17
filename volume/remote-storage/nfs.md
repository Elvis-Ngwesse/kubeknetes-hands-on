## Create a Persistent Volume (PV) for the Export Directory ##
First, define a persistent volume for your NFS server export directory. You can mount a directory from your NFS provisioner or Kubernetes node where the data will be stored

kubectl apply -f volume/remote-storage/pv-nfs-server.yaml

## Create a Persistent Volume Claim (PVC) for Accessing the NFS Server Directory ##
You will then need to create a PersistentVolumeClaim (PVC) to access this NFS share from your Kubernetes deployment

kubectl apply -f volume/remote-storage/pvc-nfs-server.yaml

## Configure NFS Server Export Using ConfigMap ##
In Kubernetes, you can configure the NFS server’s export settings using a ConfigMap. This would be required to define the export directory and its access permissions.
In this ConfigMap, the exports field is where you configure the NFS export. Here, /nfs/data is the directory being shared, and (rw,sync,no_subtree_check) are options for client access.

kubectl apply -f volume/remote-storage/configmap-nfs.yaml

## create roles/binding ##
kubectl apply -f volume/remote-storage/role.yaml
kubectl apply -f volume/remote-storage/role-binding.yaml
kubectl apply -f volume/remote-storage/cluster-role.yaml
kubectl apply -f volume/remote-storage/cluster-binding.yaml


## Deploy NFS Server with the ConfigMap ##
Deploy the NFS server using a Kubernetes Deployment. Mount the above ConfigMap to the NFS server pod, so that the NFS server uses the export configurations.

kubectl apply -f volume/remote-storage/nfs-server.yaml

## Add permissions ##
kubectl exec -it <nfs-server-pod> -- chown -R nobody:nobody /nfs/data
kubectl exec -it <nfs-server-pod> -- chmod -R 755 /nfs/data
kubectl logs <nfs-server-pod>


## Attach a pod to the pvc ##
kubectl apply -f volume/remote-storage/busybox-pv-1.yaml
kubectl get pods busybox-container-01

kubectl apply -f volume/remote-storage/busybox-pv-2.yaml
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


## Deburgging ##
kubectl exec -it <nfs-server-pod> -- cat /etc/exports
kubectl exec -it nfs-server-57485997c8-fbsxh -- ping nfs-server.default.svc.cluster.local
kubectl exec -it nfs-server-57485997c8-fbsxh -- dig nfs-server.default.svc.cluster.local
kubectl exec -it nfs-server-57485997c8-fbsxh -- nslookup nfs-server.default.svc.cluster.local
