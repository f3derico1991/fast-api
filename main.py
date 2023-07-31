from fastapi import FastAPI 
app = FastAPI()

@app.get("/")
def reaad_root():
    return {"mensaje":"hola comunidad humai"}