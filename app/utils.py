from passlib.context import CryptContext

# Telling passlib we want to use bcrypt as our hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


# bcrypt version 4.3.0 and older automatically truncate the hash. Version 5 does not.
# I was getting an error to truncate the hash manually when I used bcrypt version 5


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
