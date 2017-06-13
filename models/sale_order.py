# -*- coding: utf-8 -*-
from openerp import models, fields, _


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def _make_invoice(self, cr, uid, order, lines, context=None):
        # TODO: Find the v10 method
        """ After invoice creation, update it with the additional values. """
        res = super(SaleOrder, self)._make_invoice(cr, uid, order, lines)

        invoice_obj = self.pool.get('account.invoice')

        values = {
            'partner_shipping_id': order.partner_shipping_id.id,
            'customer_contact': order.customer_contact.id,
            'header_text': order.header_text,
            'customer_order_number': order.customer_order_number,
            'client_order_ref': order.client_order_ref,
        }

        invoice_obj.write(cr, uid, [res], values)

        return res
