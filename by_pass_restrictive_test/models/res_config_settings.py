from odoo import models, fields, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    by_pass_restrictive_test = fields.Boolean(
        string="By pass restrictive test",
        config_parameter="by_pass_restrictive_test.by_pass_restrictive_test",
        default=False
    )

    by_pass_restrictive_test_names = fields.Char(
        string="Restrictive test names",
        help="A comma separated string listing method names",
        config_parameter="by_pass_restrictive_test.by_pass_restrictive_test_names",
    )
