
## Secrets ##
To use Kubernetes Secrets with an API version, you'll typically interact with the Secret resource, which stores sensitive data such as passwords, OAuth tokens, SSH keys, etc. Secrets in Kubernetes are stored and accessed in base64 encoding, and you can create, view, and use them in your Kubernetes configurations.

## Create ssh key ##
ssh-keygen -t rsa -b 2048 -f /tmp/temp_ssh_key -N ""
Private-key: /tmp/temp_ssh_key
public-key: /tmp/temp_ssh_key.pub
ssh-add /tmp/temp_ssh_key
ssh -i /tmp/temp_ssh_key user@remote_host

## Creating a Secret ##
base64 -i /tmp/temp_ssh_key.pub | pbcopy
kubectl apply -f secrets/my-secret.yaml
kubectl get secrets my-secret -o yaml

## Create Ubuntu Pod with SSH ##
kubectl apply -f secrets/ubuntu-ssh-pod.yaml
kubectl port-forward pod/ubuntu-ssh-pod 2222:22

## SSH into the Pod ##
ssh -i /tmp/temp_ssh_key -p 2222 root@localhost

## Clean Up ##
rm -f /tmp/temp_ssh_key /tmp/temp_ssh_key.pub
ssh-add -D  # Remove all keys from the SSH agent
