from ast import literal_eval

import odoo
from odoo.tests.common import BaseCase


def __init__(self, methodName='runTest'):
    old_init_func(self, methodName)
    dbname = odoo.tools.config['db_name']
    registry = odoo.registry(dbname)
    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        # check if by_pass_restrictive_test is enabled
        by_pass_restrictive_test = literal_eval(
            env['ir.config_parameter'].get_param(
                'by_pass_restrictive_test.by_pass_restrictive_test', 'False'
            )
        )
        if by_pass_restrictive_test:
            custom_test_methods = env['ir.config_parameter'].get_param(
                'by_pass_restrictive_test.by_pass_restrictive_test_names'
            )
            # Skip method if it is in list
            if methodName in custom_test_methods:
                method = getattr(self, methodName)
                method.__dict__['__unittest_skip__'] = True


old_init_func = BaseCase.__init__
BaseCase.__init__ = __init__
