from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np

model = load("model/pokemon-stats-v1.joblib")

app = FastAPI()
class PokemonStats(BaseModel):
    HP: float
    Attack: float
    Defense: float
    SP_Atk: float
    SP_Def: float
    Speed: float

@app.post("/predict")
def predict(stats: PokemonStats):
    input_data = np.array([[stats.HP, stats.Attack, stats.Defense, stats.SP_Atk, stats.SP_Def, stats.Speed]])
    prediction = model.predict(input_data)
    return {"Total": prediction[0]}

