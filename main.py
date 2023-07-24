import requests
import boto3
from datetime import datetime


#################
# DATA COLLECTION 
#################
 


# Alpha Vantage API URL for daily stock data
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

# Get the data
response = requests.get(url)
data = response.json()

# Convert the data to a string
data_str = str(data)

# Get today's date
today = datetime.now().strftime('%Y-%m-%d')

# Create a file name using today's date
filename = 'stock_data_' + today + '.txt'

# Write the data to a file
with open(filename, 'w') as file:
    file.write(data_str)

# Create an S3 client
s3 = boto3.client('s3')

# Specify the S3 bucket
bucket_name = 'my_bucket'

# Upload the file to S3
s3.upload_file(filename, bucket_name, filename)

