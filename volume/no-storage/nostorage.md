## No storage ##
The pod busybox-nostorage does not have any persistent storage or volumes configured. Therefore, the data written to /var/log.txt will be stored within the container's filesystem, which is ephemeral

kubectl apply -f volume/no-storage/busybox-nostorage.yaml

## File system ##
ls into the container to see its file system

kubectl exec -it busybox-nostorage -- /bin/sh

## File location ##
The log file log.txt will be written to the container's filesystem at the path /var/log.txt

kubectl exec -it busybox-nostorage -- cat /var/log.txt
