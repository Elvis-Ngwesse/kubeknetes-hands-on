## Token ##
To authenticate a user with a token in Kubernetes, you can set up your kubectl configuration to use a bearer token for authentication. This is commonly used in scenarios with service accounts or OIDC (OpenID Connect)

## Get the Token ##
You need a bearer token for authentication. If you are using a service account, Kubernetes automatically creates a token for that service account in the cluster. If you're using OIDC or another identity provider, you'll need to get the token from the identity provider.

kubectl create token pod-reader-sa -n ops > token-auth/token.txt

## Set up the Token in kubectl ##
kubectl config set-credentials john --token=$(cat token-auth/token.txt)

## Verify the credentials ##
kubectl config get-contexts

## Set the context ##
kubectl config set-context my-context --user=john --namespace=ops

## Switch to the new context ##
kubectl config use-context my-context
