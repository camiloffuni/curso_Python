from fastapi import FastAPI
from pydantic import BaseModel
import crud_historial

app = FastAPI()


# ------------------------------------
# MODELO DE DATOS PARA REQUEST BODY
# ------------------------------------
class Registro(BaseModel):
    numero: str
    color: str
    docena: str
    columna: str
    par: str
    impar: str
    mayor: str
    menor: str


# ------------------------------------
# ENDPOINT CREAR REGISTRO
# ------------------------------------
@app.post("/historial/crear")
def crear_registro(data: Registro):
    crud_historial.crear_registro(
        data.numero,
        data.color,
        data.docena,
        data.columna,
        data.par,
        data.impar,
        data.mayor,
        data.menor
    )
    return {"mensaje": "Registro creado correctamente."}


# ------------------------------------
# ENDPOINT OBTENER HISTORIAL
# ------------------------------------
@app.get("/historial")
def obtener_historial():
    registros = crud_historial.obtener_historial()
    return {"historial": registros}


# ------------------------------------
# ENDPOINT ACTUALIZAR
# ------------------------------------
@app.put("/historial/{id_registro}")
def actualizar_registro(id_registro: int, data: Registro):
    crud_historial.actualizar_registro(
        id_registro,
        data.numero,
        data.color,
        data.docena,
        data.columna,
        data.par,
        data.impar,
        data.mayor,
        data.menor
    )
    return {"mensaje": "Registro actualizado correctamente."}


# ------------------------------------
# ENDPOINT ELIMINAR
# ------------------------------------
@app.delete("/historial/{id_registro}")
def eliminar_registro(id_registro: int):
    crud_historial.eliminar_registro(id_registro)
    return {"mensaje": "Registro eliminado correctamente."}
