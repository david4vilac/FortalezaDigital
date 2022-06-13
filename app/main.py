# FastAPI
from typing import Optional

from fastapi import FastAPI, Request, Depends, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder

# Database
import app.models as models
import app.schemas as schemas
import app.database as db
from sqlalchemy.orm import Session

from starlette.responses import HTMLResponse
from fastapi.responses import RedirectResponse


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})


@app.get("/personajes")
def get_personajes(request: Request, db: Session = Depends(db.get_db)):
    result = db.query(models.Personaje).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("characters.html", {"request": request, "personajes": response, "title": "List persoanejs"})

@app.post("/perfil", response_class=RedirectResponse)
def perfil_usuario(id: str):
    return RedirectResponse("/cars/" + id, status_code=status.HTTP_302_FOUND)


@app.get('/personajes/{id}',
         response_class=HTMLResponse,
         status_code=status.HTTP_200_OK,)
def perfil_personaje(request: Request, id: str, db: Session = Depends(db.get_db)):
    result = db.query(models.Personaje).filter(
        models.Personaje.id == id).first()
    personaje = jsonable_encoder(result)
    response = templates.TemplateResponse("perfil.html", {"request": request, "personaje": personaje, "title": "Perfil | {{personaje['id']}}"})
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
    return response

@app.get("/tecnologias")
def get_tecnologias(request: Request, db: Session = Depends(db.get_db)):
    result = db.query(models.Tecnologia).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("tecnologias.html", {"request": request, "tecnologias": response, "title": "Home"})


@app.get("/aventura")
def get_aventuras(request: Request, db: Session = Depends(db.get_db)):
    result = db.query(models.Personaje).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("aventura.html", {"request": request, "personajes": response, "title": "Home"})


@app.get("/reseña")
def get_reseña(request: Request):
    return templates.TemplateResponse("reseña.html", {"request": request, "title": "Home"})
