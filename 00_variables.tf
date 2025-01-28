variable "project_id" {
  description = "The Google Cloud project ID"
}

variable "credentials_file_path" {
    description = "Path to the service account key file (JSON)"
}

variable "gcs_bucket_csv_name" {
    description = "Name of the Google Cloud Storage bucket where the CSV files will be stored"
}

variable "dataset_id" {
    description = "Name of the dataset to be created in bigquery"
}

######### has values

variable "region" {
  description = "The Google Cloud region (e.g., us-central1)"
  default     = "us-central1" # Optional default value
}

variable "zone" {
  description = "The Google Cloud zone (e.g., us-central1-a)"
  default     = "us-central1-a" # Optional default value
}
