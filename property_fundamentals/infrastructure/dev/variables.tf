variable "environment" {
  type    = string
  default = "dev"
}

variable "gcp_project_id" {
  type    = string
  default = "property-fundamentals-dev"
}

variable "gcp_project_region" {
  type    = string
  default = "europe-west1"
}

variable "gcp_project_zone" {
  type    = string
  default = "europe-west1-b"
}

variable "gcp_terraform_sa_credentials" {
  type    = string
  default = ""
}

variable "gcp_kubernetes_num_nodes" {
  type    = number
  default = 1
}
