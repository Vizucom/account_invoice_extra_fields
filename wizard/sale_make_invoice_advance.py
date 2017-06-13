# -*- coding: utf-8 -*-
from openerp import models, fields, _
import openerp.addons.decimal_precision as dp


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    def _prepare_advance_invoice_vals(self, cr, uid, ids, context=None):

        sale_model = self.pool.get('sale.order')
        sale_ids = context.get('active_ids', [])
        res = super(SaleAdvancePaymentInv, self)._prepare_advance_invoice_vals(cr, uid, ids, context)

        for order in sale_model.browse(cr, uid, sale_ids, context=context):
            for item in res:
                ''' res is a list of tuples, each tuple being in format: (ID of the Sale Order, dictionary of values to be passed to invoice)'''
                if item[0] == order.id:
                    item[1]['partner_shipping_id'] = order.partner_shipping_id and order.partner_shipping_id.id or False
                    item[1]['customer_contact'] = order.customer_contact and order.customer_contact.id or False
                    item[1]['header_text'] = order.header_text or ''
                    item[1]['customer_order_number'] = order.customer_order_number or ''
                    item[1]['client_order_ref'] = order.client_order_ref or ''

        return res
