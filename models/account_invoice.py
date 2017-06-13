# -*- coding: utf-8 -*-
from openerp import models, fields, _


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    customer_contact = fields.Many2one('res.partner', "Customer's contact")
    header_text = fields.Char('Invoice header', size=128)
    customer_order_number = fields.Char('Customer order number')
    client_order_ref = fields.Char('Customer reference')
