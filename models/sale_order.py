# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        self.ensure_one()
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'partner_shipping_id': self.partner_shipping_id.id,
            'customer_contact': self.customer_contact.id,
            'header_text': self.header_text,
            'customer_order_number': self.customer_order_number,
            'client_order_ref': self.client_order_ref,
        })

        return res
