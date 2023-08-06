from ast import arg
import string as _string
import random
import secrets

#### 0123456789
digits = _string.digits

#### Return random integer value
def integer(length=6, prefix=None):

    print(prefix)

    #### Prefix should be of type int
    if not isinstance(prefix, int):
        raise Exception('Prefix should be of type int')
    
    randomInteger = int(''.join(random.choice(digits) for i in range(length)))

    #### Add prefix
    if not prefix == None:
        randomInteger = int(str(prefix) + str(randomInteger))
        
    return randomInteger

#### Return random string value
def string(length=6, prefix=None):

    alphabet = _string.ascii_letters + _string.digits
    generated = ''.join(secrets.choice(alphabet) for i in range(length))

    if not prefix == None:
        generated = str(prefix) + generated

    return str(generated)

def password(length=10, prefix=None):

    alphabet = _string.ascii_letters + _string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password

#### Wrapper for secrets by TODO change to switchcase when apache2 supports py3.10
def secret(*args, length=32, type='bytes'):
    if type == 'bytes':
        return secrets.token_bytes(length)
    elif type == 'hex':
        return secrets.token_hex(length)
    elif type == 'urlsafe':
        generated = secrets.token_urlsafe(length)
        if 'encoded' in args:
            generated  = generated.encode()
        return generated
    else:
        raise Exception('Unable to generate a secret key of type {}'.format(type))


#### Check database cursor....
def database(cursor, *args, **kwargs):
    
    print(kwargs)

    method = 'string' if not 'method' in kwargs else kwargs['method']
    del kwargs['method'] #### Kwargs need to be passed to generation functions, method is useless here

    idExists = True

    count = 1
    while idExists:

        generatedID = string(*args, **kwargs) if method == 'string' else integer(*args, **kwargs) if method == 'integer' else None

        cursor['cursor'].execute('SELECT "{}" FROM {} WHERE {} = "{}"'.format(cursor['column'], cursor['table'], cursor['column'], generatedID))

        if not len(cursor['cursor'].fetchall()):
            idExists = False

        count += 1

    return generatedID