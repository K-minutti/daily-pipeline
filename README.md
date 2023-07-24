# daily-pipeline
---

# Stock Data Collection and Storage

This project collects daily stock data from Alpha Vantage and stores it in an AWS S3 bucket.

## Prerequisites

1. **Python:** This project is written in Python, so you'll need to have Python installed on your system.

2. **AWS Account:** You need an AWS account to create and manage the S3 bucket used for data storage.

3. **Terraform:** Terraform is used to manage the AWS resources. Install Terraform and make sure it's in your system's PATH.

4. **Alpha Vantage API Key:** This project fetches data from Alpha Vantage's API, which requires an API key. You can get it from the Alpha Vantage website.

## Getting Started

1. **Clone the repository:**
   Use `git clone` to clone this repository to your local machine.

2. **Install dependencies:**
   Run `pip install -r requirements.txt` to install the required Python packages.

3. **Set up AWS Credentials:**
   Terraform uses your AWS credentials to create resources. You can provide these by setting the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables. Optionally, you might also need to set `AWS_SESSION_TOKEN` if you are using temporary security credentials.

4. **Initialize Terraform:**
   Navigate to the directory containing your `.tf` file(s) and run `terraform init`.

5. **Create AWS Resources:**
   Use `terraform apply` to create the AWS resources. Review the planned actions and enter `yes` when prompted to create the resources.

6. **Run the Python Script:**
   Finally, run the Python script using `python script_name.py`. This will fetch the stock data and upload it to your S3 bucket.

## Note

- S3 bucket names must be globally unique, not just within your AWS account or region. If "my_bucket" is already taken, you will need to choose a different name.
- Please replace the "us-west-2" region in the Terraform configuration with your desired AWS region.
- Make sure the AWS credentials used by Terraform have sufficient permissions to create S3 buckets.
