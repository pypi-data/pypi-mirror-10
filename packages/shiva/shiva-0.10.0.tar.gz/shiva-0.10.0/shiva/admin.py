# -*- coding: utf-8 -*-
"""Basic admin manager for Shiva.

Usage:
    shiva-admin user create [<email>]
    shiva-admin user activate <email_or_id>
    shiva-admin user deactivate <email_or_id>
    shiva-admin user delete <email_or_id>
    shiva-admin (-h | --help)

Options:
    -h --help   Show this help message and exit
"""
import getpass
import logging
import sys

from docopt import docopt

from shiva.app import app
from shiva.auth import Roles
from shiva.models import db, User
from shiva.utils import get_logger

log = get_logger()


class UserExistsError(Exception):
    pass


def main():
    arguments = docopt(__doc__)
    ctx = app.test_request_context()
    ctx.push()

    if arguments['user']:
        if arguments['create']:
            create_user(arguments['<email>'], interactive=True)
        elif arguments['activate']:
            activate_user(arguments['<email_or_id>'])
        elif arguments['deactivate']:
            deactivate_user(arguments['<email_or_id>'])
        elif arguments['delete']:
            delete_user(arguments['<email_or_id>'])

    ctx.pop()


def create_user(email=None, password='', is_public=False, is_active=True,
                is_admin=None, interactive=False):
    """
    User creation function. If the `interactive` flag is set, it will delegate
    the task to the create_user_interactive() function.
    """

    if interactive:
        return create_user_interactive(email, password, is_public, is_active,
                                       is_admin)

    if not email:
        raise ValueError

    if get_user(email) is not None:
        raise UserExistsError

    if not isinstance(password, basestring):
        raise ValueError

    if password == '':
        is_active = False

    user = mk_user(email, password, is_public, is_active, is_admin)

    return user


def create_user_interactive(email=None, password='', is_public=False,
                            is_active=True, is_admin=True):
    """
    This function will interactively prompt for the required information. In
    case of error, instead of throwing exceptions will print human readable
    messages to stderr and exit with code 1.
    """

    if not email:
        email = raw_input('E-mail: ').strip()
        if not email:
            log.error('Error: E-mail cannot be empty.')
            sys.exit(1)

    if get_user(email) is not None:
        log.error('Error: User exists.')
        sys.exit(1)

    if not password:
        password = getpass.getpass()
        if not password:
            is_active = False

        pw_again = getpass.getpass('Again: ')

        if password != pw_again:
            log.error('Error: Password do not match.')
            sys.exit(1)

    if password == '':
        is_active = False
        log.info('Password is empty. User will not be active until a password '
                 'is set.')
    else:
        is_active = confirm('Is active?')

    is_public = confirm('Is public?')

    if is_admin is None:
        is_admin = confirm('Is admin?')

    preview = {
        'email': email,
        'password': '(Empty)' if password == '' else '(Not shown)',
        'active': 'Yes' if is_active else 'No',
        'public': 'Yes' if is_public else 'No',
        'admin': 'Yes' if is_admin else 'No',
    }
    log.info('\nE-mail: %(email)s\nPassword: %(password)s\nActive: %(active)s'
             '\nPublic: %(public)s\nAdmin: %(admin)s\n' % preview)

    if not confirm('Are values correct?'):
        log.error('Aborting.')
        sys.exit(1)

    user = mk_user(email, password, is_public, is_active, is_admin)

    log.info("User '%s' created successfuly." % user.pk)

    return user


def mk_user(email, password, is_public, is_active, is_admin):
    role = Roles.get('ADMIN' if is_admin else 'USER')
    user = User(email=email, password=password, is_public=is_public,
                is_active=is_active, role=role)

    db.session.add(user)
    db.session.commit()

    return user


def confirm(question):
    answer = raw_input('%s [Y/n]: ' % question).strip().lower()
    if answer not in ('', 'y', 'yes', 'n', 'no'):
        log.error('Error: Invalid value.')
        sys.exit(1)

    return (answer in ('', 'y', 'yes'))


def get_user(email_or_id):
    query = User.query

    is_id = len(str(email_or_id).split('-')) == 5
    if is_id:
        user = query.get(email_or_id)
    else:
        user = query.filter_by(email=email_or_id).first()

    return user


def activate_user(email_or_id):
    user = get_user(email_or_id)
    if not user:
        log.error('Error: User does not exists.')
        sys.exit(1)

    user.is_active = True

    db.session.add(user)
    db.session.commit()

    log.info("User '%s' activated." % user.pk)


def deactivate_user(email_or_id):
    user = get_user(email_or_id)
    if not user:
        log.error('Error: User does not exists.')
        sys.exit(1)

    user.is_active = False

    db.session.add(user)
    db.session.commit()

    log.info("User '%s' deactivated." % user.pk)


def delete_user(email_or_id):
    user = get_user(email_or_id)
    if not user:
        log.error('Error: User does not exists.')
        sys.exit(1)

    _pk = user.pk

    db.session.delete(user)
    db.session.commit()

    log.info("User '%s' deleted." % _pk)
