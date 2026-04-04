from testes.conftest import client



def test_root_disponivel():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['msg'] == 'tudo ok'



def test_docs_disponiveis():
    response = client.get('/docs')
    assert response.status_code == 200



def test_openapi_disponivel():
    response = client.get('/openapi.json')
    assert response.status_code == 200
