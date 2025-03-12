
## ConfigMaps ##
ConfigMaps in Kubernetes are used to store non-sensitive configuration data in a key-value format. They allow you to decouple configuration from your application code, enabling easier configuration updates without the need to rebuild Docker images

## Create a ConfigMap ##
- Configuring a Database Connection for an App
kubectl apply -f config-maps/db-configmap.yaml
kubectl get configmap db-config -o yaml

## Use the ConfigMap in a Pod ##
kubectl apply -f config-maps/db-app.yaml

## Check the Environment Variables Inside the Pod ##
kubectl exec -it db-app -- printenv

## Use the ConfigMap as a Mounted Volume ##
- Create file and mount on /usr/share/nginx/htmlin nginx container
kubectl apply -f config-maps/nginx-html-configmap.yaml
kubectl apply -f config-maps/nginx-pod-with-html-volume.yaml
http://localhost:8080

## Update a ConfigMap ##
- You can update the config while the container is running then apply the changes
- Change a text in the config-maps/nginx-html-configmap.yaml file
kubectl apply -f config-maps/db-configmap.yaml
kubectl apply -f config-maps/nginx-pod-with-html-volume.yaml

## Delete the ConfigMap ##
kubectl delete config-maps/db-configmap.yaml