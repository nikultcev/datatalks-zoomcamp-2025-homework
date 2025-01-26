terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.17.0"
    }
  }
}

provider "google" {
  credentials = "./keys/credentials.json"
  project = var.project
  region  = var.location
}

resource "google_storage_bucket" "terraform-bucket-1" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "terraform-bigquery-dataset-1" {
  dataset_id                  = var.bq_dataset_id
  friendly_name               = "Terraform Dataset 1"
  description                 = "Test dataset for Terraform"
  location                    = var.location
}