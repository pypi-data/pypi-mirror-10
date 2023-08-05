# -*- coding: utf-8 -*-
"""
Django Uploader uses jQuery file upload to allow drag-and-drop file upload of
any file type in the Django Admin.
"""
__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 1,
    'releaselevel': 'final',
    'serial': 1
}


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (
            __version_info__['releaselevel'][0], __version_info__['serial']))
    return ''.join(vers)

__version__ = get_version()

from registration import autodiscover  # NOQA
