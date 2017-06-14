# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        res = super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        res.write({
            'customer_contact': order.customer_contact and order.customer_contact.id or False,
            'header_text': order.header_text,
            'customer_order_number': order.customer_order_number,
            'client_order_ref': order.client_order_ref
        })
