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

@app.get("/personajes")
def get_personajes(request: Request, db:Session=Depends(db.get_db)):
    result=db.query(models.Personaje).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("characters.html", {"request":request, "personajes":response, "title":"List persoanejs"})

@app.get("/tecnologias")
def get_tecnologias(request: Request):
    return templates.TemplateResponse("tecnologias.html", {"request": request, "title": "Home"})

@app.get("/aventuras")
def get_aventuras(request: Request, db:Session=Depends(db.get_db)):
    result=db.query(models.Personaje).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("aventuras.html", {"request": request,"personajes":response ,"title": "Home"})

@app.get("/reseña")
def get_reseña(request: Request):
    return templates.TemplateResponse("reseña.html", {"request": request, "title": "Home"})



