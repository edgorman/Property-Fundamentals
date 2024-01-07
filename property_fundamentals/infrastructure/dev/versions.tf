terraform {
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "2.12.1"
    }
    google = {
      source  = "hashicorp/google"
      version = "5.10.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.24.0"
    }

  }

  # Can't use tf variables here
  cloud {
    organization = "property-fundamentals-dev"
    workspaces {
      name = "property-fundamentals"
    }
  }
}
