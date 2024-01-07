provider "google" {
  project     = var.gcp_project_id
  region      = var.gcp_project_region
  zone        = var.gcp_project_zone
  credentials = var.gcp_terraform_sa_credentials
}
