resource "google_service_account" "docker" {
  account_id = "docker"
}

resource "google_project_iam_member" "github_token_creator" {
  project = var.gcp_project_id
  role    = "roles/iam.serviceAccountTokenCreator"
  member  = "serviceAccount:${google_service_account.docker.email}"
}

resource "google_project_iam_member" "github_artifact_writer" {
  project = var.gcp_project_id
  role    = "roles/artifactregistry.writer"
  member  = "serviceAccount:${google_service_account.docker.email}"
}

resource "google_artifact_registry_repository" "backend" {
  location      = var.gcp_project_region
  repository_id = "backend"
  format        = "DOCKER"
  project       = var.gcp_project_id
}
