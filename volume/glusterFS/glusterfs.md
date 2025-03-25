
## GlusterFS ##
Using a DaemonSet ensures that GlusterFS is deployed on every node in the cluster, which is a better practice than using a StatefulSet in some case

## Idendify file system ##
df -T
lsblk -f

## Check ports are open ##
sudo ufw allow 24007/tcp
sudo ufw allow 24007/udp
sudo ufw allow 24008/tcp
sudo ufw allow 24008/udp

## Run GlusterFS cluster on all 3 nodes ##        
sudo apt update 
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:gluster/glusterfs-9
sudo apt update
sudo apt install -y glusterfs-server
sudo systemctl start glusterd
sudo systemctl enable glusterd
sudo systemctl status glusterd

## Pair nodes ##
## Only on Controle-Plane ##
- login to minikube master
sudo gluster peer probe minikube-m02
sudo gluster peer probe minikube-m03
sudo gluster peer status

## Create volume dir ##
## On all 3 nodes ##
sudo mkdir -p /gluster/volume
sudo chown -R gluster:gluster /gluster/volume

## Setup a Gluster volume with two replicas and one arbiter ##
## Only on Controle-Plane ##
sudo gluster volume create k8s-volume replica 2 arbiter 1 transport tcp \
  minikube-m03:/gluster/volume \
  minikube-m02:/gluster/volume \
  minikube:/gluster/volume \
  force
sudo gluster volume start k8s-volume
sudo gluster volume status k8s-volume

Gluster process                             TCP Port  RDMA Port  Online  Pid
------------------------------------------------------------------------------
Brick minikube-m03:/gluster/volume          59245     0          Y       7242
Brick minikube-m02:/gluster/volume          55541     0          Y       7280
Brick minikube:/gluster/volume              59274     0          Y       8697
Self-heal Daemon on localhost               N/A       N/A        Y       8714
Self-heal Daemon on minikube-m03            N/A       N/A        Y       7259
Self-heal Daemon on minikube-m02            N/A       N/A        Y       7297

Task Status of Volume k8s-volume
------------------------------------------------------------------------------
There are no active volume tasks

## Info ##
The Arbiter node is a node that does not replicate data. Instead of data, it saves metadata of files. We use it to prevent storage split-brain with two replicas only

sudo gluster volume info k8s-volume

Volume Name: k8s-volume
Type: Replicate
Volume ID: 47f77310-8ef2-49d0-87c0-c6e6ffd2421d
Status: Started
Snapshot Count: 0
Number of Bricks: 1 x (2 + 1) = 3
Transport-type: tcp
Bricks:
Brick1: minikube-m03:/gluster/volume
Brick2: minikube-m02:/gluster/volume
Brick3: minikube:/gluster/volume (arbiter)
Options Reconfigured:
cluster.granular-entry-heal: on
storage.fips-mode-rchecksum: on
transport.address-family: inet
nfs.disable: on
performance.client-io-threads: off

## Prepare Kubernetes worker nodes ##
To enable Kubernetes workers to connect and use GlusterFS volume, you need to install glusterfs-client in WORKER nodes.

sudo apt install glusterfs-client

## Discovering GlusterFS in Kubernetes ##
GlusterFS cluster should be discovered in the Kubernetes cluster. To do that, 
you need to add an Endpoints object points to the servers of the GlusterFS cluster

kubectl get nodes -o wide (Edit ip addresses)
kubectl apply -f volume/glusterFS/glusterfs-endpoints.yaml
kubectl get endpoints
kubectl get endpoints glusterfs-cluster -o yaml


## Connecting to GlusterFS directly with Pod ##
kubectl apply -f volume/glusterFS/gluster-pod-direct-connect.yaml

## Connecting using the PersistentVolume ##
kubectl apply -f volume/glusterFS/gluster-pvc-pv.yaml
kubectl apply -f volume/glusterFS/gluster-pod-pvc-connect.yaml