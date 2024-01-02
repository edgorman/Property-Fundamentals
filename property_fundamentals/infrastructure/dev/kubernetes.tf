resource "google_container_cluster" "primary" {
  name                     = "${var.gcp_project_id}-cluster"
  location                 = var.gcp_project_zone
  remove_default_node_pool = true
  initial_node_count       = 1
  deletion_protection      = false
  network                  = google_compute_network.network.self_link
  subnetwork               = google_compute_subnetwork.subnetwork.self_link
  logging_service          = "logging.googleapis.com/kubernetes"
  monitoring_service       = "monitoring.googleapis.com/kubernetes"
  networking_mode          = "VPC_NATIVE"

  workload_identity_config {
    workload_pool = "${var.gcp_project_id}.svc.id.goog"
  }

  ip_allocation_policy {
    cluster_secondary_range_name  = "${var.gcp_project_id}-pod-range"
    services_secondary_range_name = "${var.gcp_project_id}-service-range"
  }

  private_cluster_config {
    enable_private_nodes    = true
    enable_private_endpoint = false
    master_ipv4_cidr_block  = "172.16.0.0/28"
  }
}

resource "google_service_account" "kubernetes" {
  account_id = "kubernetes"
}

resource "google_container_node_pool" "general" {
  name       = "${var.gcp_project_id}-node-pool"
  cluster    = google_container_cluster.primary.id
  node_count = var.gcp_kubernetes_num_nodes

  management {
    auto_repair  = true
    auto_upgrade = true
  }

  node_config {
    machine_type    = "e2-small"
    preemptible     = false
    spot            = true
    service_account = google_service_account.kubernetes.email
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
