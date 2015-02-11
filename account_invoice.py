# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class AccountInvoice(osv.Model):

    _inherit = "account.invoice"

    _columns = {
        'partner_shipping_id': fields.many2one('res.partner', "Delivery address"),                
        'customer_contact': fields.many2one('res.partner', "Customer's contact"),
        'header_text': fields.char(string='Invoice header', size=128),
        'customer_order_number':    fields.char('Customer order number'),
        'client_order_ref':    fields.char('Customer reference'),
    }
