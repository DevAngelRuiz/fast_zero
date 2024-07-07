from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import (
    Message,
    UserDB,
    UserListSchema,
    UserPublicSchema,
    UserSchema,
)

app = FastAPI()

dataBase = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olar mundo'}


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(dataBase) + 1,
        **user.model_dump(),
        # convertendo todos os dados (chave e valor) em um dicionário
    )

    dataBase.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserListSchema)
def list_users():
    return {'users': dataBase}


@app.put('/users/{user_id}', response_model=UserPublicSchema)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(dataBase) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_index = user_id - 1

    user_with_id = UserDB(
        id=user_id,
        **user.model_dump(),
    )

    dataBase[user_index] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    if user_id > len(dataBase) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del dataBase[user_id - 1]

    return {'message': 'user deleted'}
