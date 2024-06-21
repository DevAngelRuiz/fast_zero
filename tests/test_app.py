from http import HTTPStatus

from fastapi.testclient import TestClient  # type: ignore

from fast_zero.app import app


def test_root_should_return_ok_and_ola():
    cliente = TestClient(app) #arrange, nessa parte estamos organizando o teste, criando um cliente para fazer a requisição
    response = cliente.get('/') #act, nessa parte estamos executando o teste, fazendo a requisição
    assert response.status_code == HTTPStatus.OK #assert, nessa parte estamos verificando se o teste passou ou não
    assert response.json() == {'ola': 'mundo'} #assert, nessa parte estamos validado o que a função tem que exibir
