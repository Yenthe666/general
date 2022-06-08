# -*- coding: utf-8 -*-
{
    'name': "Database UID check",

    'summary': """
        Check database UID
    """,

    'description': """
        When restoring database as a copy, the database UID is changed.
        By creating a copy of the UID when installing this module on a production database, we can check if the copy is the same as the actual database UID.
        With this check, we can prevent things like POST calls to API endpoints from happening on a copy of a production database.
    """,

    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [],

    'post_init_hook': 'post_init_hook',
}
