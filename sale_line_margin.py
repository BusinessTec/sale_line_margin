# -*- coding: utf-8 -*- 

from openerp import models, fields, api

class sale_line_margin(models.Model):

        _inherit = "sale.order.line"
      
        mar_p = fields.Float(string='% Margen', digits=(6,3),compute='margin_line')


        @api.one
        @api.depends('price_unit','purchase_price')
        def margin_line(self):
                if self.price_unit == 0:
                    self.mar_p = 0.0;
                else:
                    self.mar_p=(self.price_unit - self.purchase_price)
