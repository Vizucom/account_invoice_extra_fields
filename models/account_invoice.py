# -*- coding: utf-8 -*-
from openerp import models, fields, _


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    customer_contact = fields.Many2one('res.partner', "Customer's Contact")
    header_text = fields.Char('Invoice Header', size=128)
    customer_order_number = fields.Char('Customer Order Number')
    client_order_ref = fields.Char('Customer Reference')
