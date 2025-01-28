terraform {
  required_version = ">= 1.3.0" # Specify the required Terraform version
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0" # Use a stable version of the Google provider
    }
  }
}

provider "google" {
    credentials = file(var.credentials_file_path)
    project = var.project_id
    region = var.region
    zone = var.zone
}

