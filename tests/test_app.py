from http import HTTPStatus

from fast_zero.schemas import UserPublicSchema


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
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublicSchema.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': user.id,
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token
