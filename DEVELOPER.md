# Developer

This README contains descriptions of the repository as well as instructions for setting up the developer environment and cloud deployment.

## Repository

TBD

## Local Deployment

TBD

## Cloud Deployment

### Setup

Install Terraform:

```
https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli
```

Install GCloud:

```
https://cloud.google.com/sdk/docs/install#deb
```

Install Kubectl:

```
https://kubernetes.io/docs/tasks/tools/
```

To connect to the dev cluster:

```
gcloud container clusters get-credentials property-fundamentals-dev-cluster --region=europe-west1
```

To connect to the prod cluster:

```
gcloud container clusters get-credentials property-fundamentals-prod-cluster --region=europe-west1

```
