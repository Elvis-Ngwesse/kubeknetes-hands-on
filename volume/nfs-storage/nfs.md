
## Deploy NFS-Server ##
This YAML file defines a Kubernetes deployment that runs an NFS server in a pod, exposes the necessary network ports for NFS communication, and ensures the NFS server has the required file system access and privileges. The data on the host's /var/nfs directory is made available to the NFS server in the container

kubectl apply -f volume/nfs-storage/nfs-server.yaml

## Create roles/binding ##
kubectl apply -f volume/nfs-storage/rbac.yaml

## Create storage-class ##
kubectl apply -f volume/nfs-storage/storage-class.yaml

## Create NFS-Provisioner
The nfs-client-provisioner is responsible for dynamically provisioning Persistent Volumes (PVs) in a Kubernetes cluster using an NFS server as the backend storage. When a user requests storage by creating a Persistent Volume Claim (PVC), the provisioner automatically creates a corresponding Persistent Volume (PV) backed by the NFS server

kubectl apply -f volume/nfs-storage/nfs-provisioner.yaml

## Attach a pod to nfs-server ##
kubectl apply -f volume/nfs-storage/busybox-nfs.yaml
kubectl exec -it busybox-nfs -- /bin/sh
cat /mnt/busybox-nfs.txt

- Check files on host path
minikube ssh
ls /var/nfs/exports

## Attach a pod to nfs-pvc ##
kubectl apply -f volume/nfs-storage/busybox-pvc.yaml
kubectl exec -it busybox-pvc -- /bin/sh
cat /mnt/nfs_share/busybox-pvc.txt

- Check files on host path
minikube ssh
ls /var/nfs/exports
- You will see created pv
- This is due to the pvc claim made
- A subdir is created in the nfs server using the storage class

## Empty dir ##
The emptyDir volume type in Kubernetes is used for temporary storage that is only available during the lifetime of a pod. When you define a volume as emptyDir, the volume is created when the pod is scheduled to a node and is deleted when the pod is deleted
kubectl apply -f volume/nfs-storage/busybox-emptydir.yaml

## No storage ##
The pod busybox-nostorage does not have any persistent storage or volumes configured. Therefore, the data written to /var/log.txt will be stored within the container's filesystem, which is ephemeral.
kubectl apply -f volume/nfs-storage/busybox-nostorage.yaml