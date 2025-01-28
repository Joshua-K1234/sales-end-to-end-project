# sales-end-to-end-project
Developed an automated ETL pipeline and a web interface with Flask and Google Cloud to upload, process, and analyze data from CSV files. This is my second version after adding improvements such as using terraform to generate infrastructure and improve the aesthetics of the flask website.
- *GCS: means google cloud storage*

<img src="https://github.com/Joshua-K1234/sales-end-to-end-project/blob/main/images/cloud%20project%20components.JPG" alt="Components diagram" width="(200/9)16" height="200"/>

## Key Components

### Web Interface:
- **Python Flask Interface**: Developed a user-friendly interface using Python and Flask, enabling users to upload data (Csv) directly to a Google Cloud Storage bucket. It would let users know whether the file had been successfully uploaded to the cloud or not.
- **Connection**: Connected to the cloud using a created service account's credentials.

<img src="https://github.com/Joshua-K1234/sales-end-to-end-project/blob/main/images/website.JPG" alt="Components diagram" width="(400/9)16" height="400"/> 

### Cloud Storage Buckets:
- **Cloud file storage**: Created a google cloud storage bucket to store the uploaded files on the cloud.

### Cloud run function:
- **Automatic processing**: Configured a Google Cloud Run function to instantly detect file uploads in the storage bucket and send them to BigQuery for further processing.
- **Custom Trigger**: Changed the default trigger from "HTTPS" to "Cloud Storage" with the event set to "Finalized" (triggered when a file is uploaded) and linked it to the designated bucket.
- **Code Implementation**: Developed a Python script to load data from Google Cloud Storage (GCS) into BigQuery.

### Tools and Technologies:
- **Python**: Flask, Google.cloud (Storage and BigQuery) Libaries.
- **Google cloud**: Cloud storage bucket, Cloud run functions ,BigQuery, LookerStudio (Visualisation)
- **Terraform**: Used terraform to generate all the infrastructure in the project with the exception of cloud run (I tried but couldn't get it to work).

### Dataset
- The dataset used contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers. [Link to the dataset](https://www.kaggle.com/datasets/carrie1/ecommerce-data)

## Challenges
- **Cloud run functions code implementation**: Faced a slight challenge in using Cloud Run Functions for the first time but successfully implemented the code and gained valuable experience, however was unable to implement it in terraform.

## How to use
1. **Clone the repository**.  
2. **Set up Google Cloud**:
   - Create a service account and json key, store these in a folder named keys and name the credentials, `credentials.json`
   - Create and configure `terraform.tfvars`
   - Use the terraform to create the google cloud storage bucket and setup bigquery.
   - Deploy Cloud Run functions using the `cloud_run_functions.py` file.  **ENSURE** the `requirements.txt` file includes `functions-framework==3.*` and `google-api-python-client`.  
4. **Configure required variables**:  
   - Set `GCS_BUCKET_NAME` in `main.py`.  
   - Set `dataset_id` and `table_id` in `cloud_run_functions.py`.
5. **Install and configure the Google Cloud SDK**.  
6. **Run the web application**
7. Set up Looker Studio to connect to BigQuery for data analysis.
- Use the files in test data to ensure it works.

## Future Enchancements
- **Cloud run functionality**: I could try to tilter data (e.g., keep rows with country = "France") before loading it into BigQuery using pandas or /tmp.
