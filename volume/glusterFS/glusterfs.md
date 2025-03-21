
## GlusterFS ##
Using a DaemonSet ensures that GlusterFS is deployed on every node in the cluster, which is a better practice than using a StatefulSet in some case

## Base 64 encode ##
echo -n "docker-username" | base64
echo -n "docker-password" | base64

## Create GlusterFS service ##
kubectl apply -f volume/glusterFS/glusterfs-daemonset.yaml

## Verify Pod Communication ##
kubectl exec -it <pod-name> -c glusterfs -- /bin/bash


kubectl get pods -l app=glusterfs -o wide


kubectl apply -f https://k8s.io/examples/volume/glusterFS/glusterfs-dns.yaml



## Verify service status ##
kubectl exec -it <pod-name> -c glusterfs -- /bin/bash
glusterfsd --version
ps aux | grep glusterd
gluster volume status

## Create brick ##
To create a brick for GlusterFS in your Minikube environment, you'll need to set up GlusterFS to create a volume, and a "brick" is essentially a directory on a GlusterFS node that acts as the storage backend for a volume

## Create dir for brick ##
kubectl exec glusterfs-0 -c glusterfs -- /mnt/glusterfs/brick0
kubectl exec glusterfs-1 -c glusterfs -- /mnt/glusterfs/brick1
kubectl exec glusterfs-2 -c glusterfs -- /mnt/glusterfs/brick2

## check folder permission ## 
kubectl exec glusterfs-0 -c glusterfs -- ls -ld /mnt/glusterfs/brick0

## Create the volume by specifying the brick directories ##
chown -R gluster:gluster /mnt/glusterfs/brick2

kubectl exec glusterfs-0 -c glusterfs -- \
gluster volume create myvolume transport tcp \
glusterfs-0:/mnt/glusterfs/brick0 glusterfs-1:/mnt/glusterfs/brick1 glusterfs-2:/mnt/glusterfs/brick2 \
force


## Start the volume ##
kubectl exec glusterfs-0 -c glusterfs -- gluster volume start myvolume


