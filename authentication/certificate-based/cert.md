## Kubernetes Certificate-Based Authentication ##
You can create a client certificate for each user and configure Kubernetes to authenticate them based on those certificates. This method is most common when managing local or self-hosted Kubernetes clusters like Minikube

## Generate the certificate for the user ##
openssl genrsa -out authentication/certificate-based/john.key 2048
openssl req -new -key authentication/certificate-based/john.key -out authentication/certificate-based/john.csr -subj "/CN=john"
openssl genpkey -algorithm RSA -out authentication/certificate-based/ca.key -aes256 ## phrase is: testing
openssl req -key authentication/certificate-based/ca.key -new -x509 -out authentication/certificate-based/ca.crt -days 3650
openssl x509 -req -in authentication/certificate-based/john.csr -CA authentication/certificate-based/ca.crt -CAkey authentication/certificate-based/ca.key -CAcreateserial -out authentication/certificate-based/john.crt -days 365

## Add the user to Kubernetes' kubeconfig ##
kubectl config set-credentials john --client-certificate=authentication/certificate-based/john.crt --client-key=authentication/certificate-based/john.key --embed-certs=true

## Create a kubectl context for the new user ##
kubectl config set-context john-context --cluster=minikube --user=john --namespace=ops
kubectl config use-context john-context

