import pandas as pd
import pathlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump
from google.cloud import storage

bucket_name = "pokedex-model.appspot.com"
source_blob_name = "pokedex.csv"
destination_file_name = "data/pokedex.csv"

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Downloaded storage object {source_blob_name} to local file {destination_file_name}.")

download_blob(bucket_name, source_blob_name, destination_file_name)

df = pd.read_csv(destination_file_name)

X = df[['HP', 'Attack', 'Defense', 'SP. Atk.', 'SP. Def', 'Speed']]
y = df['Total']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

pathlib.Path('model').mkdir(parents=True, exist_ok=True)

dump(model, 'model/pokemon-stats-v1.joblib')

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Model Performance: MSE = {mse}, R2 = {r2}")

