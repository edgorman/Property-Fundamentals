resource "google_compute_network" "network" {
  name                    = "${var.gcp_project_id}-network"
  routing_mode            = "REGIONAL"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnetwork" {
  name                     = "${var.gcp_project_id}-subnetwork"
  ip_cidr_range            = "10.0.0.0/18"
  region                   = var.gcp_project_region
  network                  = google_compute_network.network.id
  private_ip_google_access = true

  secondary_ip_range {
    range_name    = "${var.gcp_project_id}-pod-range"
    ip_cidr_range = "10.48.0.0/14"
  }
  secondary_ip_range {
    range_name    = "${var.gcp_project_id}-service-range"
    ip_cidr_range = "10.52.0.0/20"
  }
}
