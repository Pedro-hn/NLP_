from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load('app/model.joblib')

@app.post('/predict')
def predict(texto: str):
    categoria = model.predict([texto])[0]
    return {"categoria": categoria}