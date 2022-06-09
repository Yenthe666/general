# -- coding: utf-8 --
from odoo import models
import logging

_logger = logging.getLogger(__name__)


class Base(models.AbstractModel):
    _inherit = 'base'

    def check_database_uid(self):
        config_param = self.env['ir.config_parameter'].sudo()
        is_valid = config_param.get_param('database.uuid') == config_param.get_param('database_uid_check.uuid')
        if not is_valid:
            _logger.warning("Database UID check failed. If you're running a copy of the database, this message can be ignored.")
        return is_valid
