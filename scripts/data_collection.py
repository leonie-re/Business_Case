# Install dependencies as needed
import numpy as np

#pip install kagglehub[pandas-datasets] #installed via R when initiating project
import kagglehub
#from kagglehub import KaggleDatasetAdapter

kagglehub.login()
# API KEY: KGAT_0278333821e05ced51079eaea3da2388

# Set the path to the file you'd like to load
file_path = "data/raw.nosync/retail_data.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())
