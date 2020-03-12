from odoo import models, api, fields


class HealthStockPicking(models.Model):
    _inherit = 'stock.picking'
    _order = 'date desc'

    

  #  carrier_id = fields.Many2one('res.partner', 'Conductor')

  #  truck_in_date = fields.Datetime(
  #      'Entrada de Camión',
  #      readonly=True
  #  )

   

  #  carrier_truck_patent = fields.Char(
  #      'Patente de camión'
  #  )

  #  carrier_cart_patent = fields.Char(
  #       'Patente de carro'
  #  )