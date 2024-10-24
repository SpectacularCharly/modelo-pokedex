import pandas as pd
import pathlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump

# Load the dataset
df = pd.read_csv('data/pokedex.csv')

# Features and target variable
X = df[['HP', 'Attack', 'Defense', 'SP. Atk.', 'SP. Def', 'Speed']]
y = df['Total']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Create the directory if it doesn't exist
pathlib.Path('model').mkdir(parents=True, exist_ok=True)

# Save the trained model
dump(model, 'model/pokemon-stats-v1.joblib')

# Print model performance
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Model Performance: MSE = {mse}, R2 = {r2}")
