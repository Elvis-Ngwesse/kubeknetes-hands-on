
## Webhook ##
- Admission Webhooks
These are used to intercept and validate or modify resources when they're created, updated, or deleted in a cluster
    Mutating Admission Webhook: Modifies an object before it's persisted in the cluster
    Validating Admission Webhook: Validates an object to ensure it meets certain criteria before it's persisted
- Event Webhooks: These are used for sending notifications or triggering actions based on Kubernetes events (like pod creation, deletion, etc.)

## Create server ##
webhook/webhook_server.py

## Generate certificate
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes \
  -subj "/CN=webhook-server.default.svc" \
  -extensions SAN \
  -config <(echo "[req]
  distinguished_name = req_distinguished_name
  [req_distinguished_name]
  [SAN]
  subjectAltName = DNS:webhook-server.default.svc")

## Verify cert ##
openssl x509 -in cert.pem -text -noout


## Run the Webhook Server ##
python webhook_server.py

## Build and push the Docker image ##
docker buildx build --platform linux/amd64,linux/arm64 -t dockerelvis/webhook-server:latest --push .

## Deploy the Webhook Server in Kubernetes ##
kubectl create secret tls webhook-server-tls --cert=cert.pem --key=key.pem
or
webhook/webhook-secret.yaml
    cat cert.pem | base64 -w 0
    cat key.pem | base64 -w 0

kubectl apply -f webhook/webhook-secret.yaml
kubectl apply -f webhook/webhook-server-deployment.yaml

## Get CA-Bundle ##
cat ~/.kube/config
cat ~/.minikube/ca.crt | base64
or
kubectl get secret webhook-server-tls -o jsonpath='{.data.tls\.crt}' | base64 --decode > ca.crt

## Create Webhook Configuration ##
kubectl apply -f webhook/mutating-admission-webhook.yaml

## Test the Webhook ##
kubectl run test-pod --image=nginx

