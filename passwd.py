user = "liuyan"
passswd = "123456"
_name = input('user:')
_passwd = input('passwd:')
if _name == user and _passwd == passswd:
    print('Welcome to {name} login...'.format(name=_name))
else:
    print('Invalid username or passwd')