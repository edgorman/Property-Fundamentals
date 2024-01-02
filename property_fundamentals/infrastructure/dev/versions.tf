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

provider "google" {
  project     = var.gcp_project_id
  region      = var.gcp_project_region
  zone        = var.gcp_project_zone
  credentials = var.gcp_terraform_sa_credentials
}
