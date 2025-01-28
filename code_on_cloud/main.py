import functions_framework
from google.cloud import storage, bigquery
import os
import json

# job_config is a class, you can view it online.

"""
What are storage and bigquery clients?
storage is intialised
then you can access a bucket and call it "bucket"
then you can use "bucket" to access a file in a
bucket and call it "blob".

"""

# Triggered by a change in a storage bucket
# That's the point of framework, cloud event.
# the event is the change.
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"] # name of bucket
    name = data["name"] # name of file uploaded
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")

    # The code above is default.
    # Call the function to load the file to BigQuery
    load_file_to_bigquery(bucket, name)

"""Function loads file from GCS to BigQuery"""
def load_file_to_bigquery(bucket_name, file_name):
    # Initialize clients
    storage_client = storage.Client()
    bigquery_client = bigquery.Client()

    # Define BigQuery dataset and table
    dataset_id = "sales"  # Update with your dataset ID
    table_id = "orders"      # Update with your table ID

    # Get the file from Cloud Storage
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    file_path = f"/tmp/{file_name}"

    # Download the file locally
    blob.download_to_filename(file_path)
    print(f"Downloaded {file_name} to {file_path}")

    # Load the file into BigQuery
    # Appends since not set.
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,  # Update format if needed
        autodetect=True,
        skip_leading_rows=1  # Skip header row if present
    )

    with open(file_path, "rb") as file: # read as binary its what bq expects
        load_job = bigquery_client.load_table_from_file(
            file, table_ref, job_config=job_config
        )

    load_job.result()  # Wait for the job to complete

    print(f"Loaded {file_name} into {dataset_id}.{table_id}")

    # Clean up
    os.remove(file_path)
    print(f"Deleted temporary file: {file_path}")