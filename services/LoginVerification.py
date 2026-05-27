from repository import UserRepository

import bcrypt

import bcrypt

def loginVerification(Request):

    res = UserRepository.getUser(Request["email"])

    if not res:
        return False

    email_received_db = res[3]
    password_hash_db = res[4]

    if (
        Request["email"] == email_received_db and
        bcrypt.checkpw(
            Request["password"].encode("utf-8"),
            password_hash_db.encode("utf-8")
        )
    ):
        return True

    return False