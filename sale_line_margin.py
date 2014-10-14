
# -*- coding: utf-8 -*- 

from openerp import models, fields, api

class sale_line_margin(models.Model):

        _inherit = "sale.order.line"

        mar_p = fields.Float(string='% Margen', digits=(6,3),compute='margin_line')


        @api.one
        @api.depends('price_unit','purchase_price','discount')
        def margin_line(self):
                if self.purchase_price == 0:
                    self.mar_p = 0.0;
                else:
                    self.mar_p=(self.price_unit - self.discount*self.price_unit/100 - self.purchase_price)/self.purchase_price*100
