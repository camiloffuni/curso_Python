from fastapi import FastAPI 
import random

app = FastAPI()

# Ruta raíz
@app.get("/")
def home():
    return {"message": "Mi primera API en Python está funcionando"}

# Simula una ruleta (0 - 36)
@app.get("/ruleta")
def girar_ruleta():
    numero = random.randint(0, 36)
    return {
        "resultado": numero
    }

#resultado
@app.get("/ruleta2")
def girar_ruleta():
    numero=random.randint(0, 36)
    return{"resultado":numero}

# Saludo personalizado
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {
        "mensaje": f"Hola {nombre}, bienvenido a mi API"
    }

