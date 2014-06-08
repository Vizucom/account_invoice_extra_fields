# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from openerp.tools.translate import _

class sale_order(osv.Model):

    _inherit = 'sale.order'

    def _make_invoice(self, cr, uid, order, lines, context=None):
        """
        After invoice creation, update it with the additional values.
        This updating of invoice object works similarly as 
        in sale_basic_extensions module.
        """
        res = super(sale_order, self)._make_invoice(cr, uid, order, lines)
        
        invoice_obj = self.pool.get('account.invoice')

        values = {
                'partner_shipping_id': order.partner_shipping_id.id,
                'customer_contact': order.customer_contact.id,
                }

        invoice_obj.write(cr, uid, [res], values)
        
        return res


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
