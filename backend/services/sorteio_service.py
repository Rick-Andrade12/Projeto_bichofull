import random
from sqlalchemy.orm import Session
from sqlalchemy import func

from models.sorteio import Sorteio
from models.bicho import Bicho
from models.carteira import Carteira


MULTIPLICADORES = {
    "milhar": {
        1: 4000,
        2: 2000,
        3: 900,
        4: 500,
        5: 100,
    },
    "grupo": {
        1: 18,
        2: 15,
        3: 10,
        4: 6,
        5: 4,
    }
}


def gerar_nova_rodada(session: Session) -> int:
    ultima_rodada = session.query(func.max(Sorteio.rodada)).scalar()
    if ultima_rodada is None:
        return 1
    return ultima_rodada + 1


def realizar_sorteio(session: Session):
    rodada = gerar_nova_rodada(session)
    sorteios_criados = []

    for posicao in range(1, 6):
        grupo_sorteado = random.randint(1, 25)
        milhar_sorteada = str(random.randint(0, 9999)).zfill(4)

        novo_sorteio = Sorteio(
            rodada=rodada,
            posicao=posicao,
            grupo=grupo_sorteado,
            milhar=milhar_sorteada
        )

        session.add(novo_sorteio)
        sorteios_criados.append(novo_sorteio)

    session.commit()

    resultado = []

    for sorteio in sorteios_criados:
        session.refresh(sorteio)

        bicho = session.query(Bicho).filter(Bicho.grupo == sorteio.grupo).first()

        resultado.append({
            "id": sorteio.id,
            "rodada": sorteio.rodada,
            "posicao": sorteio.posicao,
            "grupo": sorteio.grupo,
            "milhar": sorteio.milhar,
            "bicho": bicho.nome if bicho else "Desconhecido"
        })

    return {
        "rodada": rodada,
        "sorteios": resultado
    }


def conferir_aposta(session: Session, aposta, resultado_sorteio):
    ganhou = False
    premio = 0.0
    posicao_premiada = None

    sorteios = resultado_sorteio["sorteios"]

    for item in sorteios:
        if aposta.tipo == "grupo" and str(aposta.numero) == str(item["grupo"]):
            ganhou = True
            posicao_premiada = item["posicao"]
            premio = aposta.valor * MULTIPLICADORES["grupo"][posicao_premiada]
            break

        if aposta.tipo == "milhar" and str(aposta.numero).zfill(4) == str(item["milhar"]).zfill(4):
            ganhou = True
            posicao_premiada = item["posicao"]
            premio = aposta.valor * MULTIPLICADORES["milhar"][posicao_premiada]
            break

    if ganhou:
        aposta.status = "ganhou"
        aposta.premio = premio
        aposta.posicao_premiada = posicao_premiada

        carteira = session.query(Carteira).filter(Carteira.usuario_id == aposta.usuario_id).first()
        if carteira:
            carteira.saldo += premio
    else:
        aposta.status = "perdeu"
        aposta.premio = 0.0
        aposta.posicao_premiada = None

    session.commit()
    session.refresh(aposta)

    return aposta


def listar_sorteios_service(session: Session):
    return session.query(Sorteio).order_by(Sorteio.rodada.desc(), Sorteio.posicao.asc()).all()