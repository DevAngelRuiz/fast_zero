from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='test', password='password', email='teste@teste.com'
    )

    session.add(new_user)
    session.commit()
    user = session.scalar(select(User).where(User.email == 'teste@teste.com'))

    assert user.email == 'teste@teste.com'
