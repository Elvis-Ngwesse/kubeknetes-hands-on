
## Deploy NFS-Server ##
This YAML file defines a Kubernetes deployment that runs an NFS server in a pod, exposes the necessary network ports for NFS communication, and ensures the NFS server has the required file system access and privileges. The data on the host's /var/nfs directory is made available to the NFS server in the container

kubectl apply -f volume/nfs-storage/nfs-server.yaml

## Create roles/binding ##
kubectl apply -f volume/nfs-storage/rbac.yaml

## Create storage-class ##
kubectl apply -f volume/nfs-storage/storage-class.yaml

## Create NFS-Provisioner
kubectl apply -f volume/nfs-storage/nfs-provisioner.yaml

kubectl apply -f nfs/busybox-nfs.yaml