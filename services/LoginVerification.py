from repository import UserRepository

def loginVerification(email, password):

    res = UserRepository.getUser(email)
    
    email_received_db = res[3]
    password_received_db = res[4]

    if email == email_received_db and password == password_received_db:
        return True
    
    return False


