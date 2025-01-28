resource "google_bigquery_dataset" "sales" {
  dataset_id = var.dataset_id  # The name of the dataset
  project    = var.project_id  # Replace with your project ID variable
  location   = "US"  # Specify the region for the dataset
  description = "Dataset to store sales data."
}