from testes.conftest import client, cadastrar_e_logar



def test_saldo_inicial_da_carteira_e_1000():
    usuario = cadastrar_e_logar(prefixo='saldo_inicial')

    response = client.get('/carteira/saldo', headers=usuario['headers'])

    assert response.status_code == 200
    body = response.json()
    assert body['usuario_id'] > 0
    assert body['saldo'] == 1000.0



def test_saldo_exige_autenticacao():
    response = client.get('/carteira/saldo')
    assert response.status_code in [401, 403]
