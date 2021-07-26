from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hashP(value):
    return pwd_context.hash(value)
def verify(plan,hashe):
    return pwd_context.verify(plan,hashe)