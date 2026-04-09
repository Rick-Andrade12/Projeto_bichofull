#.\venv\Scripts\Activate.ps1 ==ativar venv
#uvicorn main:app --reload   ==rodar o servidor 

from fastapi import FastAPI
from routes.auth_routes import auth_router
from routes.apostas_routes import aposta_router
from routes.sorteio_routes import sorteio_router
from routes.carteira_routes import carteira_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



@app.get("/")
def root():
    return {"msg": "tudo ok"}

app.include_router(auth_router)
app.include_router(aposta_router)
app.include_router(sorteio_router)
app.include_router(carteira_router)




app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
