import os
import zipfile

# Set Kaggle configuration
os.environ["KAGGLE_CONFIG_DIR"] = os.path.expanduser("~/.kaggle")

# Dataset identifier
dataset = "ankitverma2010/ecommerce-customer-churn-analysis-and-prediction"

# Download dataset
os.system(f"kaggle datasets download -d {dataset}")

# Extract dataset
zip_file = "ecommerce-customer-churn-analysis-and-prediction.zip"  # Name of the downloaded zip file
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall("dataset")  # Extract contents to the 'dataset' folder

print("Dataset downloaded and extracted successfully!")

