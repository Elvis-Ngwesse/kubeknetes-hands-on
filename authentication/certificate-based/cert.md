## Kubernetes Certificate-Based Authentication ##
You can create a client certificate for each user and configure Kubernetes to authenticate them based on those certificates. This method is most common when managing local or self-hosted Kubernetes clusters like Minikube

## Generate the certificate for the user ##
openssl genrsa -out john.key 2048
openssl req -new -key john.key -out john.csr -subj "/CN=john"
openssl genpkey -algorithm RSA -out ca.key -aes256 (phrase is: testing)
openssl req -key ca.key -new -x509 -out ca.crt -days 3650
openssl x509 -req -in john.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out john.crt -days 365

## Add the user to Kubernetes' kubeconfig ##
kubectl config set-credentials john --client-certificate=john.crt --client-key=john.key --embed-certs=true

## Create a kubectl context for the new user ##
kubectl config set-context john-context --cluster=minikube --user=john --namespace=ops
kubectl config use-context john-context

