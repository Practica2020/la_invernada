from odoo import models, api, fields


class HealthStockPicking(models.Model):
    _inherit = 'stock.picking'


#    dimabe_health_care_id = fields.Many2one('dimabe.health.care', 'Cuidado')

#    dimabe_health_care_disease = fields.Char('Enfermedad más grave')

#    dimabe_health_care_emergency_contact =  fields.Many2one(
#        string='dimabe_health_care_emergency_contact',
#        comodel_name='dimabe_health_care.res_partner'     
#    )

#    dimabe_health_care_description = fields.Text('Descripción de condición')
