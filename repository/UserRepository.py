from services.Database import NoneParamsSQL, WithParamsSQL


def createUser(nameUser, date, email, password):

    WithParamsSQL("CALL create_user(%s, %s, %s, %s)", (nameUser, date, email, password))

    return None

def getUser(email):

    WithParamsSQL("CALL get_user(%s)", (email))

    return None

def updateUser(email, password):

    WithParamsSQL("CALL update_user(%s, %s)", (email, password))

    return None

def deleteUser(id):

    WithParamsSQL("CALL delete_user(%s)", (id))

    return None





def getAllUsers():

    print(NoneParamsSQL("SELECT * FROM users;"))    
    
    return None
