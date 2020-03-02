from odoo import fields, models, api
from datetime import datetime
from ..helpers import date_helper


class OvenUse(models.Model):
    _name = 'oven.use'
    _description = 'datos de uso de los hornos'

    name = fields.Char(
        'Horno en uso',
        related='dried_oven_id.name'
    )

    init_date = fields.Datetime('Inicio de Proceso')

    finish_date = fields.Datetime('Termino de Proceso')

    active_seconds = fields.Integer('Segundos de Actividad')

    active_time = fields.Char(
        'Tiempo Transcurrido',
        compute='_compute_active_time',
        store=True
    )

    used_lot_ids = fields.Many2many(
        'stock.production.lot',
        string='Lotes a Secar'
    )

    init_active_time = fields.Integer('Inicio de tiempo activo')

    finish_active_time = fields.Integer('Fin de tiempo activo')

    dried_oven_id = fields.Many2one(
        'dried.oven',
        'horno',
        required=True
    )

    unpelled_dried_id = fields.Many2one('unpelled.dried', 'Proceso de secado')

    @api.multi
    @api.depends('active_seconds')
    def _compute_active_time(self):
        for item in self:
            item.active_time = date_helper.int_to_time(item.active_seconds)

    @api.multi
    def init_process(self):
        for item in self:
            if item.init_date:
                raise models.ValidationError('este proceso ya ha sido iniciado')
            if not item.dried_oven_id:
                raise models.ValidationError('Debe seleccionar el horno a iniciar')
            item.init_date = datetime.utcnow()
            item.init_active_time = item.init_date.timestamp()
            item.unpelled_dried_id.state = 'progress'
            item.dried_oven_id.is_in_use = True

    @api.multi
    def pause_process(self):
        for item in self:
            item.finish_active_time = datetime.utcnow().timestamp()
            item.active_seconds += item.finish_active_time - item.init_active_time

    @api.multi
    def resume_process(self):
        for item in self:
            item.init_active_time = datetime.utcnow().timestamp()
            item.finish_active_time = 0

    @api.multi
    def finish_process(self):
        for item in self:
            item.finish_date = datetime.utcnow()
            if item.finish_active_time == 0:
                item.finish_active_time = item.finish_date.timestamp()
                item.active_seconds += item.finish_active_time - item.init_active_time
            item.dried_oven_id.is_in_use = False
