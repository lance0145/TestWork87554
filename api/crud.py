from database import db_context
from models import User, Transaction
from schemas import UserIn, UserOut, TransactionIn, TransactionOut


def crud_add_user(user: UserIn):
    db_user = User(**user.dict())
    with db_context() as db:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user


def crud_get_user(user_id: int):
    with db_context() as db:
        user = db.query(User).filter(User.id == user_id).first()
    if user:
        return UserOut(**user.__dict__)
    return None


def crud_add_transaction(transaction: TransactionIn):
    db_transaction = Transaction(**transaction.dict())
    with db_context() as db:
        exist = (
            db.query(Transaction)
            .filter(Transaction.city == transaction.city, Transaction.date == transaction.date)
            .first()
        )
        if exist:
            return None
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
    return db_transaction


def crud_get_transaction(city: str):
    with db_context() as db:
        transaction = (
            db.query(Transaction)
            .filter(Transaction.city == city)
            .order_by(Transaction.date.desc())
            .limit(7)
            .all()
        )
    if transaction:
        result = []
        for item in transaction:
            result.append(TransactionOut(**item.__dict__))
        return {city: result[::-1]}
    return None


def crud_error_message(message):
    return {"error": message}
