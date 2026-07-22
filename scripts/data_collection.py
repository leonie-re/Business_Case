# Install dependencies as needed:
#pip install kagglehub[pandas-datasets] 
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to
#  the file you'd like to load
file_path = "retail_store_sales.csv"

import scripts.API_Keys

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

df.info()
df = df.drop(columns=['Payment Method', 'Discount Applied'])

# Einzelne Columns müssen sich angesehen und bereinigt werden. 
# Prüfen wie viele unique values es in Strings gibt und ob diese sinnvoll sind.
print(df['Transaction ID', ].unique())
# Zählt die leeren Felder in dieser spezifischen Spalte
print(df['Transaction ID'].isna().sum())
print(df['Transaction ID'].value_counts())

print(df['Customer ID'].unique())
print(df['Customer ID'].isna().sum())
print(df['Customer ID'].value_counts())

print(df['Category'].unique())
print(df['Category'].isna().sum())

print(df['Item'].unique()) 
print(df['Item'].isna().sum()) # Einige Missing enthalten, hier muss entschieden werden ob diese gelöscht werden oder nicht.  

print(df['Location'].unique())
print(df['Location'].isna().sum())

print(df['Transaction Date'].unique())
print(df['Transaction Date'].isna().sum())
print(df['Transaction Date'].value_counts())

# Nachhaltigkeit simulieren 

# Eventdata: 
from google.cloud import bigquery # Das hier funktioniert noch nicht. 

client = bigquery.Client(project="business-case-project-503020 ")

query = """
SELECT
  GLOBALEVENTID,
  SQLDATE,
  Actor1Name,
  Actor2Name,
  EventCode,
  GoldsteinScale,
  AvgTone,
  ActionGeo_FullName
FROM `gdelt-bq.gdeltv2.events`
WHERE SQLDATE = 20260715
LIMIT 1000
"""

df = client.query(query).to_dataframe()
df.head()

job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
query_job = client.query(query, job_config=job_config)
print(f"Diese Abfrage würde {query_job.total_bytes_processed / 1e9:.2f} GB verarbeiten")

