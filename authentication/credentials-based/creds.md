
## Managing User Permissions ##
If you're using Kubeconfig for managing different users and contexts, you can modify the access control in Minikube by configuring kubectl with different user contexts. You can use kubectl config commands to manage contexts, clusters, and users

## Set creds ##
kubectl config set-credentials elvisngwesse --username=elvis --password=password
kubectl config set-context elvis-context --cluster=minikube --user=elvisngwesse
kubectl config use-context elvis-context
