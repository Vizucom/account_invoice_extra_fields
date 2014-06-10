# -*- coding: utf-8 -*-

from openerp.osv.orm import Model, fields
from openerp.osv import osv
from openerp.tools.translate import _


class AccountInvoice(Model):

    _inherit = "account.invoice"

    _columns = {
        'partner_shipping_id': fields.many2one('res.partner', "Delivery address"),                
        'customer_contact': fields.many2one('res.partner', "Customer's contact"),
        'header_text': fields.char(string='Invoice header', size=128, help="A header text that will be printed on the invoice."),
        'customer_order_number':    fields.char('Customer order number'),        
    }
