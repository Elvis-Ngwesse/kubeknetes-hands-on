## ABAC ##
Setting up Minikube to work with ABAC (Attribute-Based Access Control) in Kubernetes involves a few steps. Minikube is a tool that allows you to create a local Kubernetes cluster, and ABAC is a method of managing access to Kubernetes resources based on attributes

## Apply policy ##
minikube start --extra-config=apiserver.Authorization.Mode=ABAC --extra-config=apiserver.Authorization.PolicyFile=access-control/attribute-based/abac-policy.json

## Deprecated ##
Kubernetes deprecated ABAC in favor of RBAC in version 1.8, and support for ABAC has been removed entirely in later versions
