from sqlalchemy.testing import db

from database import UserModel


def get_user_by_id(user_id: int):
    user = db.execute(UserModel if UserModel.id == user_id else None)

    return user
