# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from dependencies import pegar_sessao
# from typing import List
# from models.sorteio import Sorteio
# from schemas import SorteioResposta

# sorteio_router = APIRouter(prefix="/sorteio", tags=["sorteio"])


# @sorteio_router.get('/listar', response_model=List[SorteioResposta])
# async def listar_sorteios(session: Session = Depends(pegar_sessao)):
#     sorteios = session.query(Sorteio).all()
#     return sorteios

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from dependencies import pegar_sessao
from schemas.sorteio_schema import SorteioResposta
from services.sorteio_service import listar_sorteios_service

sorteio_router = APIRouter(prefix="/sorteio", tags=["sorteio"])


@sorteio_router.get("/listar", response_model=List[SorteioResposta])
async def listar_sorteios(session: Session = Depends(pegar_sessao)):
    return listar_sorteios_service(session)