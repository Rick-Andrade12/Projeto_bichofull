from testes.conftest import client, cadastrar_e_logar



def test_listar_sorteios_retorna_registros_gerados_por_aposta(monkeypatch):
    usuario = cadastrar_e_logar(prefixo='listar_sorteios')

    valores = [10, 1111, 20, 2222, 3, 3333, 4, 4444, 5, 5555]

    def fake_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr('services.sorteio_service.random.randint', fake_randint)

    apostar = client.post(
        '/apostas/apostar',
        json={
            'tipo': 'grupo',
            'numero': '10',
            'valor': 10.0,
        },
        headers=usuario['headers'],
    )
    assert apostar.status_code == 200, apostar.text

    response = client.get('/sorteio/listar')

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) >= 5

    cinco_mais_recentes = body[:5]
    rodada = cinco_mais_recentes[0]['rodada']

    assert all(item['rodada'] == rodada for item in cinco_mais_recentes)
    assert [item['posicao'] for item in cinco_mais_recentes] == [1, 2, 3, 4, 5]



def test_sorteio_listado_tem_campos_esperados(monkeypatch):
    usuario = cadastrar_e_logar(prefixo='campos_sorteio')

    valores = [1, 1111, 2, 2222, 3, 3333, 4, 4444, 5, 5555]

    def fake_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr('services.sorteio_service.random.randint', fake_randint)

    apostar = client.post(
        '/apostas/apostar',
        json={
            'tipo': 'grupo',
            'numero': '99',
            'valor': 1.0,
        },
        headers=usuario['headers'],
    )
    assert apostar.status_code == 200, apostar.text

    response = client.get('/sorteio/listar')

    assert response.status_code == 200
    item = response.json()[0]
    assert 'id' in item
    assert 'rodada' in item
    assert 'posicao' in item
    assert 'grupo' in item
    assert 'milhar' in item
    assert isinstance(item['milhar'], str)
    assert len(item['milhar']) == 4
