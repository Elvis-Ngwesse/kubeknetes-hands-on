
## GlusterFS ##
Using a DaemonSet ensures that GlusterFS is deployed on every node in the cluster, which is a better practice than using a StatefulSet in some case

## Base 64 encode ##
echo -n "docker-username" | base64
echo -n "docker-password" | base64

## Create GlusterFS service ##
kubectl apply -f volume/glusterFS/glusterfs-daemonset.yaml

## Verify service status ##
kubectl exec -it <pod-name> -c glusterfs -- /bin/bash
glusterfsd --version
ps aux | grep glusterd
gluster volume status

## Create brick ##
To create a brick for GlusterFS in your Minikube environment, you'll need to set up GlusterFS to create a volume, and a "brick" is essentially a directory on a GlusterFS node that acts as the storage backend for a volume

## Verify brick ##
kubectl exec -it <pod-name> -c glusterfs -- /bin/bash
ls /mnt/glusterfs/

## Idendify file system ##
df -T
lsblk -f

## Print IP and Hostnames ##
kubectl get pods -l app=glusterfs -o=custom-columns="IP:.status.podIP, NAME:.metadata.name"

## Edit host files ##
- login to pods, add IP and Hostname of other pod on their respective hosts files
echo "10.244.1.13   glusterfs-msbr9" >> /etc/hosts
echo "10.244.2.32   glusterfs-vvrcx" >> /etc/hosts

## Pair both clusters ##
- login to pod and pair both pods
gluster peer probe glusterfs-msbr9
gluster peer status

## Create the volume ##

gluster volume create myvolume replica 2 \
  glusterfs-msbr9:/mnt/glusterfs/glusterfs-msbr9 \
  glusterfs-vvrcx:/mnt/glusterfs/glusterfs-vvrcx \
  force



## Start the volume ##
kubectl exec glusterfs-0 -c glusterfs -- gluster volume start myvolume






brick-minikube-m03-glusterfs-fh7h5



gluster volume create gv0 replica 2 transport tcp \
              "glusterfs-8w2pc:/mnt/glusterfs/brick-minikube-m02-glusterfs-8w2pc" \
              "glusterfs-fh7h5:/mnt/glusterfs/brick-minikube-m03-glusterfs-fh7h5" \
              force


            
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:gluster/glusterfs-9
sudo apt update
sudo apt install -y glusterfs-server
sudo systemctl start glusterd
sudo systemctl enable glusterd
sudo systemctl status glusterd



sudo mkdir -p /gluster/brick1
sudo chown -R gluster:gluster /gluster/brick1

sudo mkdir -p /gluster/brick2
sudo chown -R gluster:gluster /gluster/brick2

sudo gluster peer probe minikube-m02

sudo gluster volume create myvolume replica 2 transport tcp \
    minikube-m02:/gluster/brick1 \
    minikube-m03:/gluster/brick2 force

sudo gluster volume start myvolume
sudo gluster volume status myvolume

Create GlusterFS Endpoints
kubectl apply -f volume/glusterFS/glusterfs-endpoints.yaml


Create pvc and pv
kubectl apply -f volume/glusterFS/gluster-pvc-pv.yaml


Create pod
kubectl apply -f volume/glusterFS/gluster-pod.yaml


Verify mount in pod
kubectl exec -it my-gluster-pod -- df -h

kubectl exec -it my-gluster-pod -- cat /mnt/gluster/logs/debug.log

