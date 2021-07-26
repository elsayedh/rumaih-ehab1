# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CustomAccountPaymentPo(models.Model):
    _inherit = 'account.move'
    _description = 'account print report'

    #

    def action_print_report(self):
        return self.env.ref('bi_print_journal_entries.journal_entry_report_id').report_action(self)

    def action_print_report_ar(self):
        return self.env.ref('bi_print_journal_entries.journal_entry_report_id_ar').report_action(self)

