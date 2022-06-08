# -*- coding: utf-8 -*-
from . import models
from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    db_uuid = env['ir.config_parameter'].get_param('database.uuid')
    env['ir.config_parameter'].set_param('database_uid_check.uuid', db_uuid)
