class SolarSystem:
    def __init__(self):
        self.GrabityFactor ={
            "Mercurio": 3.7,
            "Venus": 8.87,
            "Marte": 3.71,
            "Júpiter": 24.79,
            "Saturno": 10.44,
            "Urano": 8.69,
            "Neptuno": 11.15
            }

    def CalculateWeight(self,p,weightT):
        GrabityT = 9.81
        pesocalculado = weightT * (self.GrabityFactor.get(p)/GrabityT)
        return pesocalculado
