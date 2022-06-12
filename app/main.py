#FastAPI
from typing import Optional

from fastapi import FastAPI, Request, Depends, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder

#Database
import app.models as models, app.schemas as schemas
import app.database as db
from sqlalchemy.orm import Session

from starlette.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})

@app.get("/reciclajes")
def get_reciclajes(request: Request, db:Session=Depends(db.get_db)):
    result=db.query(models.Personaje).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("characters.html", {"request":request, "personajes":response, "title":"List persoanejs"})



@app.post('/usuarios/',response_model=schemas.Personaje)
def create_users(entrada:schemas.Personaje, db:Session=Depends(db.get_db)):
    usuario = models.Personaje(id = entrada.id, rol = entrada.rol, caracteristicas = entrada.caracteristicas, imagen = entrada.c)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario



