import requests
apikey = '' #web api found in project overview, for console.firebase.google.com


def CreateUser(email, password):
    details = {
        'email': email,
        'password': password,
        'returnSecureToken': True
    }

    req = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={}'.format(apikey), data=details)
    if 'error' in req.json().keys():
        return {'status': 'error', 'message': req.json()['error']['message']}
    if 'idToken' in req.json().keys():
        return {'status': 'success', 'idToken': req.json()['idToken']}


email = input("enter email: \n")
password = input("enter your Password: \n")

CreateUser(email, password)
