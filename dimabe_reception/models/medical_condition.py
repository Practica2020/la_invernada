from odoo import models, fields, api

class Medical_condition(models.Model):

    _name = 'medical.condition'

    dimabe_health_care_id = fields.Many2one(
        string='Contacto de emergencia',
        comodel_name='res.partner'
    )

    most_severe_disease = fields.Char('Condición más severa')

    description = fields.Text('Descripción de la condición')

    imagen = fields.Binary(string='imagen', attachment=True, help="for the lolz")
    
    certificado = fields.Binary(string='certificado', attachment=True)
    
    

    @api.model
    def create(self, values_list):
        values_list = self._prepare_data(values_list)
        return super(Medical_condition, self).create(values_list)

    @api.multi
    def write(self, vals):
        vals = self._prepare_data(vals)
        return super(Medical_condition, self).write(vals)




  

