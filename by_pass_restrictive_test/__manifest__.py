# -*- coding: utf-8 -*-
{
    'name': 'By pass restrictive test',
    'version': '15.0.1.0.0',
    'summary': 'This module allows you to by pass restrictive test.',
    'sequence': 400,
    'description': """
    This module allows you to by pass restrictive tests.
    You can specify tests as comma separated string listing method names in General settings.
    """,
    'category': 'Hidden',
    'author': "Mainframe Monkey BV",
    'website': 'https://www.mainframemonkey.com',
    'depends': ['base_setup'],
    'data': [
        'data/bypass_meta_data.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
