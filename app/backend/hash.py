import bcrypt


def create_hash(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def check_password_hash(password_hashed, password):
    return bcrypt.checkpw(password.encode('utf-8'), password_hashed.encode('utf-8'))
