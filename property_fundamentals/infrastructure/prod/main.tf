terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }

  cloud {
    organization = "property-fundamentals-prod"
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

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}
