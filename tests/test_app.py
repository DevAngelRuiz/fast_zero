from http import HTTPStatus


def test_root_should_return_ok_and_ola(client):
    # cliente = TestClient(app) #arrange,
    # nessa parte estamos organizando o teste,
    # criando um cliente para fazer a requisição
    response = client.get(
        '/'
    )  # act, nessa parte estamos executando o teste, fazendo a requisição
    assert (
        response.status_code == HTTPStatus.OK
    )  # assert, nessa parte estamos verificando se o teste passou ou não
    assert response.json() == {
        'message': 'olar mundo'
    }  # assert, nessa parte estamos validado o que a função tem que exibir


def test_creat_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Lucas',
            'email': 'teste@teste.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Lucas',
        'email': 'teste@teste.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'username': 'Lucas', 'email': 'teste@teste.com'}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Lucas',
            'email': 'lucas@lucas.com',
            'password': '123456',
        },
    )
    assert response.json() == {
        'id': 1,
        'username': 'Lucas',
        'email': 'lucas@lucas.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'user deleted'}
    assert response.status_code == HTTPStatus.OK
    response = client.get('/users/')
    assert response.json() == {'users': []}
