from testes.conftest import client, cadastrar_e_logar



def test_apostar_grupo_com_sucesso_retorna_estrutura_esperada(monkeypatch):
    usuario = cadastrar_e_logar(prefixo='aposta_grupo')

    valores = [10, 1111, 20, 2222, 3, 3333, 4, 4444, 5, 5555]

    def fake_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr('services.sorteio_service.random.randint', fake_randint)

    response = client.post(
        '/apostas/apostar',
        json={
            'tipo': 'grupo',
            'numero': '10',
            'valor': 10.0,
        },
        headers=usuario['headers'],
    )

    assert response.status_code == 200, response.text
    body = response.json()

    assert body['mensagem'] == 'aposta realizada com sucesso'
    assert body['tipo'] == 'grupo'
    assert body['numero_apostado'] == '10'
    assert body['status'] == 'ganhou'
    assert body['premio'] == 180.0
    assert body['posicao_premiada'] == 1
    assert body['saldo_atual'] == 1170.0
    assert isinstance(body['sorteios'], list)
    assert len(body['sorteios']) == 5



def test_apostar_milhar_ganhadora_em_terceira_posicao(monkeypatch):
    usuario = cadastrar_e_logar(prefixo='aposta_milhar')

    valores = [1, 9999, 2, 8888, 3, 1234, 4, 7777, 5, 6666]

    def fake_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr('services.sorteio_service.random.randint', fake_randint)

    response = client.post(
        '/apostas/apostar',
        json={
            'tipo': 'milhar',
            'numero': '1234',
            'valor': 2.0,
        },
        headers=usuario['headers'],
    )

    assert response.status_code == 200, response.text
    body = response.json()

    assert body['status'] == 'ganhou'
    assert body['premio'] == 1800.0
    assert body['posicao_premiada'] == 3
    assert body['saldo_atual'] == 2798.0



def test_aposta_perdedora_fica_com_status_perdeu(monkeypatch):
    usuario = cadastrar_e_logar(prefixo='aposta_perdeu')

    valores = [10, 1111, 20, 2222, 3, 3333, 4, 4444, 5, 5555]

    def fake_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr('services.sorteio_service.random.randint', fake_randint)

    response = client.post(
        '/apostas/apostar',
        json={
            'tipo': 'grupo',
            'numero': '9',
            'valor': 10.0,
        },
        headers=usuario['headers'],
    )

    assert response.status_code == 200, response.text
    body = response.json()

    assert body['status'] == 'perdeu'
    assert body['premio'] == 0.0
    assert body['posicao_premiada'] is None
    assert body['saldo_atual'] == 990.0



def test_aposta_com_tipo_invalido_retorna_erro():
    usuario = cadastrar_e_logar(prefixo='tipo_invalido')

    response = client.post(
        '/apostas/apostar',
        json={
            'tipo': 'dezena',
            'numero': '10',
            'valor': 10.0,
        },
        headers=usuario['headers'],
    )

    assert response.status_code == 400
    assert response.json()['detail'] == 'tipo de aposta inválido'



def test_aposta_com_saldo_insuficiente_retorna_erro():
    usuario = cadastrar_e_logar(prefixo='saldo_insuficiente')

    response = client.post(
        '/apostas/apostar',
        json={
            'tipo': 'grupo',
            'numero': '10',
            'valor': 1001.0,
        },
        headers=usuario['headers'],
    )

    assert response.status_code == 400
    assert response.json()['detail'] == 'saldo insuficiente'



def test_historico_mostra_aposta_finalizada(monkeypatch):
    usuario = cadastrar_e_logar(prefixo='historico')

    valores = [10, 1111, 20, 2222, 3, 3333, 4, 4444, 5, 5555]

    def fake_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr('services.sorteio_service.random.randint', fake_randint)

    apostar = client.post(
        '/apostas/apostar',
        json={
            'tipo': 'grupo',
            'numero': '10',
            'valor': 5.0,
        },
        headers=usuario['headers'],
    )
    assert apostar.status_code == 200, apostar.text

    response = client.get('/apostas/historico', headers=usuario['headers'])

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) >= 1
    ultima = body[-1]
    assert ultima['tipo'] == 'grupo'
    assert ultima['status'] == 'ganhou'
    assert ultima['posicao_premiada'] == 1
