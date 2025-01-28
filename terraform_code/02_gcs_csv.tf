resource "google_storage_bucket" "bucket_csv" {
  name     = var.gcs_bucket_csv_name   # The name of the GCS bucket
  location = "US"      # The region where the bucket is created
  project  = var.project_id     # The Google Cloud project ID
  force_destroy = true          # Allows deleting non-empty buckets (be cautious)

  # Enable Uniform Bucket-Level Access
  uniform_bucket_level_access = true

  # Ensure the bucket does not allow public access
  public_access_prevention = "enforced"  # Ensures public access is blocked

  lifecycle {
    prevent_destroy = false     # Set to true if you don't want the bucket to be destroyed accidentally
  }
}

