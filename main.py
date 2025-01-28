from flask import Flask, request, render_template, redirect
from google.cloud import storage
import os

app = Flask(__name__)

# Configure GCS bucket and credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/credentials.json"  # Update the path
GCS_BUCKET_NAME = "" # Add a name HERE

def upload_to_gcs(file, bucket_name, destination_blob_name):
    """Uploads a file to GCS bucket."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_file(file)
        return True
    except Exception as e:
        print(f"Error uploading to GCS: {e}")
        return False


@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        # Check if the POST request has the file part
        if "file" not in request.files:
            message = "No file part in the request."
            return render_template("index.html", message=message)

        file = request.files["file"]
        # If the user does not select a file
        if file.filename == "":
            message = "No selected file."
            return render_template("index.html", message=message)

        # Upload the file to GCS
        if upload_to_gcs(file, GCS_BUCKET_NAME, file.filename):
            message = "File uploaded successfully!"
        else:
            message = "Failed to upload file. Please try again."

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
