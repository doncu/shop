#!/usr/bin/env python

import getpass

if __name__ == '__main__':
    import sys
    '.' not in sys.path and sys.path.insert(0, '.')
    from shop.admin import models

    username = input('Enter username: ')
    password = getpass.getpass()

    user = models.create_user(username, password, is_admin=True)
    print('Success create user: ', user.username)
