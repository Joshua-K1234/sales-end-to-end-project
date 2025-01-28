# sales-end-to-end-project
Developed an automated ETL pipeline and a web interface with Flask and Google Cloud to upload, process, and analyze data from CSV files.
- *GCS: means google cloud storage*

<img src="https://github.com/Joshua-K1234/sales-end-to-end-project/blob/main/images/cloud%20project%20components.JPG" alt="Components diagram" width="(200/9)16" height="200"/>

## Key Components

### Web Interface:
- **Python Flask Interface**: Developed a user-friendly interface using Python and Flask, enabling users to upload data (Csv) directly to a Google Cloud Storage bucket. It would let users know whether the file had been successfully uploaded to the cloud or not.
- **Connection**: Connecting to the cloud was done using google SDK

### Cloud Storage Buckets:
- **Cloud file storage**: Created a google cloud storage bucket to store the uploaded files on the cloud.

### Cloud run function:
- **Automatic processing**: Configured a Google Cloud Run function to instantly detect file uploads in the storage bucket and send them to BigQuery for further processing.
- **Custom Trigger**: Changed the default trigger from "HTTPS" to "Cloud Storage" with the event set to "Finalized" (triggered when a file is uploaded) and linked it to the designated bucket.
- **Code Implementation**: Developed a Python script to load data from Google Cloud Storage (GCS) into BigQuery.

### Tools and Technologies:
- **Python**: Flask, Google.cloud (Storage and BigQuery) Libaries.
- **Google cloud**: Cloud storage bucket, Cloud run functions ,BigQuery, LookerStudio (Visualisation)

### Dataset
- The dataset used contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers. [Link to the dataset](https://www.kaggle.com/datasets/carrie1/ecommerce-data)

## Challenges
- **Cloud run functions code implementation**: Faced a slight challenge in using Cloud Run Functions for the first time but successfully implemented the code and gained valuable experience.

## How to use
1. **Clone the repository**.  
2. **Set up Google Cloud**:  
   - Create a storage bucket.  
   - Create a BigQuery dataset.  
   - Deploy Cloud Run functions using the `cloud_run_functions.py` file.  **ENSURE** the `requirements.txt` file includes `functions-framework==3.*` and `google-api-python-client`.  
3. **Configure required variables**:  
   - Set `GCS_BUCKET_NAME` in `main.py`.  
   - Set `dataset_id` and `table_id` in `cloud_run_functions.py`.
4. **Install and configure the Google Cloud SDK**.  
5. **Run the web application**
6. Set up Looker Studio to connect to BigQuery for data analysis.
- Use the files in test data to ensure it works.

## Future Enchancements
- **Improve webpage aesthetics**: I was focused primarily on cloud functionality, leaving limited time for web design so it was simple.
- **Create cloud infrastructure with code**: Use Terraform to automate the creation of cloud components for better scalability and consistency.
- **Secure Variable Storage**: Store sensitive variables in configuration files or environment variables to prevent accidental exposure and improve security, whilist also reducing the hassle of manually removing them when sharing code, and make it easier for other users to configure and use the application.
