# FastAPI
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


@app.get("/personajes",
         tags=["Personajes"],
         response_model=schemas.Personaje,
         summary="Lista los personajes del libro")
def get_personajes(request: Request, db: Session = Depends(db.get_db)):
    result = db.query(models.Personaje).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("characters.html", {"request": request, "personajes": response, "title": "Lista Personajes"})


@app.get('/personajes/{id}',
         response_class=HTMLResponse,
         status_code=status.HTTP_200_OK,
         tags=["Personajes"],
         response_model=schemas.Personaje,
         summary="Muestra todos los datos del personaje")
def perfil_personaje(request: Request, id: str, db: Session = Depends(db.get_db)):
    result = db.query(models.Personaje).filter(
        models.Personaje.id == id).first()
    personaje = jsonable_encoder(result)
    response = templates.TemplateResponse("perfil.html", {"request": request, "personaje": personaje, "title": f"Perfil | {id}"})
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
    return response

@app.get("/tecnologias",
         response_class=RedirectResponse,
         tags=["Tecnologias"],
         response_model=schemas.Personaje,
         summary="Muestra las tecnoligas del libro")
def get_tecnologias(request: Request, db: Session = Depends(db.get_db)):
    result = db.query(models.Tecnologia).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("tecnologias.html", {"request": request, "tecnologias": response, "title": "Tecnologias"})


@app.get("/aventura",
         response_class=RedirectResponse,
         tags=["Aventura"],
         response_model=schemas.Personaje,
         summary="Cuenta la aventura que se presenta en el libro")
def get_aventuras(request: Request, db: Session = Depends(db.get_db)):
    result = db.query(models.Personaje).all()
    result2 = jsonable_encoder(result)
    response = []
    for persona in result2:
        response.append((persona))
    return templates.TemplateResponse("aventura.html", {"request": request, "personajes": response, "title": "Aventura"})


@app.get("/reseña",
         response_class=HTMLResponse,
         status_code=status.HTTP_200_OK,
         tags=["Reseña"],
         summary="Presenta la reseña del libro")
def get_reseña(request: Request):
    return templates.TemplateResponse("reseña.html", {"request": request, "title": "Reseña"})
