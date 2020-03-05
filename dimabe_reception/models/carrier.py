from odoo import models, fields, api
class Carrier(models.Model):

    _name = 'custom.carrier'

    
    carrier_id = fields.Many2one(
        string='Conductor',
        comodel_name='res.partner'
    )

    truck_patent = fields.Char('Patente de camión')

    cart_patent = fields.Char('Patente de carro')



    @api.model
    def create(self, values_list):
        values_list = self._prepare_data(values_list)
        return super(Carrier, self).create(values_list)

    @api.multi
    def write(self, vals):
        vals = self._prepare_data(vals)
        return super(Carrier, self).write(vals)

    def _prepare_data(self, values_list):
        if 'truck_patent' in values_list:
            values_list['truck_patent'] = str.upper(values_list['truck_patent'])
        if 'cart_patent' in values_list:
            values_list['cart_patent'] = str.upper(values_list['cart_patent'])
        return values_list


    @api.multi
    def _compute_name(self):
        for item in self:
            item.name=item.truck_patent