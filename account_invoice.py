# -*- coding: utf-8 -*-

from openerp.osv.orm import Model, fields
from openerp.osv import osv
from openerp.tools.translate import _


class AccountInvoice(Model):
    """ Add account.condition_text to invoice"""

    _inherit = "account.invoice"

    _columns = {
        'partner_shipping_id': fields.many2one('res.partner', "Delivery address"),                
        'customer_contact': fields.many2one('res.partner', "Customer's contact"),
        
    }
