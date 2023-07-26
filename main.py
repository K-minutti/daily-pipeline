import boto3
import os
import requests
from datetime import datetime
from abc import ABC, abstractmethod
from botocore.exceptions import BotoCoreError, ClientError
from typing import Dict
from requests.exceptions import RequestException

class DataSource(ABC):
    @abstractmethod
    def fetch_data(self, symbol: str) -> Dict:
        pass

class AlphaVantageSource(DataSource):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    def fetch_data(self, symbol: str) -> Dict:
        response = requests.get(self.url.format(api_key=self.api_key, symbol=symbol))
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.
        return response.json()

class S3Uploader:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket_name = os.getenv("AWS_BUCKET_NAME") 

    def upload(self, data: str, filename: str):
        try:
            self.s3.put_object(Body=data, Bucket=self.bucket_name, Key=filename)
        except (BotoCoreError, ClientError) as error:
            print(f"Something went wrong with the upload: {error}")
            return
        print(f"Uploaded {filename} to {self.bucket_name}")

api_key = os.getenv("ALPHA_VANTAGE_API_KEY") 
api_key = "demo"
data_source = AlphaVantageSource(api_key=api_key)
s3_uploader = S3Uploader()

try:
    # Fetch data
    data = data_source.fetch_data(symbol="IBM")
    data_str = str(data)

    # Get today's date and create a file name
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f'stock_data_{today}.txt'

    # Write the data to a file
    with open(filename, 'w') as file:
        file.write(data_str)


    # Upload data to S3
    s3_uploader.upload(data=data_str, filename=filename)

except RequestException as err:
    print(f"Request failed: {err}")
