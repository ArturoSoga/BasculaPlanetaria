from SolarSystem import SolarSystem
from fastapi import FastAPI

app = FastAPI()

@app.get("/BasculaPlanetaria/{elplaneta}/{tuPeso}")
def ReadBasculaPlanetaria(tuPeso: int,elplaneta: str):
    obj = SolarSystem()
    peso = obj.CalculateWeight(elplaneta,tuPeso)

    return {"tu peso en otro planeta es : ": peso}
