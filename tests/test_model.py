from joblib import load
import numpy as np

def test_model_prediction():
    model = load("model/pokemon-stats-v1.joblib")
    input_data = np.array([[45, 49, 49, 65, 65, 45]])  # Ejemplo de entrada de stats
    prediction = model.predict(input_data)
    assert prediction[0] > 0  # Verificar que el resultado de la predicción sea positivo
