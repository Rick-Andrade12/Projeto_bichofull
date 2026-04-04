from fastapi.testclient import TestClient
import uuid

from main import app


client = TestClient(app)


def gerar_email(prefixo: str = 'teste'):
    return f"{prefixo}_{uuid.uuid4().hex[:10]}@gmail.com"



def cadastrar_usuario(nome='Teste', senha='123456789', prefixo='teste'):
    email = gerar_email(prefixo)
    response = client.post(
        '/auth/cadastrar',
        json={
            'nome': nome,
            'email': email,
            'senha': senha,
        },
    )
    return response, email, senha



def cadastrar_e_logar(nome='Teste', senha='123456789', prefixo='teste'):
    cadastro, email, senha = cadastrar_usuario(nome=nome, senha=senha, prefixo=prefixo)
    assert cadastro.status_code in [200, 201], cadastro.text

    login = client.post(
        '/auth/login',
        json={
            'email': email,
            'senha': senha,
        },
    )
    assert login.status_code == 200, login.text

    token = login.json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    return {
        'email': email,
        'senha': senha,
        'headers': headers,
    }
