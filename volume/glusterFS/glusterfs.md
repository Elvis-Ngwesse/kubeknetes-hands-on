
## GlusterFS ##
Using a DaemonSet ensures that GlusterFS is deployed on every node in the cluster, which is a better practice than using a StatefulSet in some case

## Base 64 encode ##
echo -n "docker-username" | base64
echo -n "docker-password" | base64

