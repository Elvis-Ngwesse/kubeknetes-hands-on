
## GlusterFS ##
Using a DaemonSet ensures that GlusterFS is deployed on every node in the cluster, which is a better practice than using a StatefulSet in some case

kubectl create secret docker-registry glusterfs-registry-secret \
  --docker-server=quay.io \
  --docker-username=ajangngwesse \
  --docker-password=pykfyz-Cakkij-6xozgi \
  --docker-email=ajangngwesse@gmail.com

kubectl get secret glusterfs-registry-secret --output=yaml


kubectl apply -f volume/glusterFS/glusterfs-daemonset.yaml

ajangngwesse@gmail.com
ajangngwesse
pykfyz-Cakkij-6xozgi


docker build -t my-glusterfs-image .
