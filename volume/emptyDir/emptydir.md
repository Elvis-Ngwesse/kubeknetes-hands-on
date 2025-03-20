## Empty dir ##
The emptyDir volume type in Kubernetes is used for temporary storage that is only available during the lifetime of a pod. When you define a volume as emptyDir, the volume is created when the pod is scheduled to a node and is deleted when the pod is deleted

kubectl apply -f volume/emptyDir/busybox-emptydir.yaml

## Verify mount ##
kubectl exec -it busybox-emptydir -- /bin/sh

cd /mnt

ls

## Verify data ##
kubectl exec -it busybox-emptydir -- /bin/sh

cat /mnt/log.txt

## See volume in pod ##
kubectl describe pod busybox-emptydir

Volumes:
  my-volume:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     
    SizeLimit:  <unset>