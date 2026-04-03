from testes.conftest import client, cadastrar_usuario, cadastrar_e_logar, gerar_email



def test_cadastro():
    response, _, _ = cadastrar_usuario(prefixo='cadastro')
    assert response.status_code in [200, 201]
    assert response.json()['mensagem'] == 'cadastro feito'



def test_login():
    cadastro, email, senha = cadastrar_usuario(prefixo='login')
    assert cadastro.status_code in [200, 201]

    response = client.post(
        '/auth/login',
        json={
            'email': email,
            'senha': senha,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert 'access_token' in body
    assert 'refresh_token' in body
    assert body['token_type'].lower() == 'bearer'



def test_login_senha_errada():
    cadastro, email, _ = cadastrar_usuario(prefixo='senha_errada', senha='123456')
    assert cadastro.status_code in [200, 201]

    response = client.post(
        '/auth/login',
        json={
            'email': email,
            'senha': 'errada',
        },
    )

    assert response.status_code in [400, 401]



def test_login_usuario_inexistente():
    response = client.post(
        '/auth/login',
        json={
            'email': gerar_email('inexistente'),
            'senha': '123456',
        },
    )

    assert response.status_code in [400, 401, 404]



def test_cadastro_email_duplicado():
    email = gerar_email('duplicado')
    payload = {
        'nome': 'Duplicado',
        'email': email,
        'senha': '123456',
    }

    primeira = client.post('/auth/cadastrar', json=payload)
    segunda = client.post('/auth/cadastrar', json=payload)

    assert primeira.status_code in [200, 201]
    assert segunda.status_code in [400, 409]



def test_refresh_com_token_valido():
    usuario = cadastrar_e_logar(prefixo='refresh')

    response = client.get(
        '/auth/refresh',
        headers=usuario['headers'],
    )

    assert response.status_code == 200
    body = response.json()
    assert 'access_token' in body
    assert body['token_type'].lower() == 'bearer'



def test_me_retorna_usuario_logado():
    usuario = cadastrar_e_logar(prefixo='me')

    response = client.get('/auth/me', headers=usuario['headers'])

    assert response.status_code == 200
    body = response.json()
    assert body['email'] == usuario['email']
    assert 'senha' not in body
