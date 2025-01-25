from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    # se hereda modelo existente
    _inherit = 'sale.order'

    # se agrega campo de tipo select
    tipo_cotizacion = fields.Selection([
        ('normal', 'Normal'),
        ('promocion', 'Promoción')
    ], string='Tipo de Cotización', default='normal')

    # se crea la restriccion que lee el valor del campo tipo_cotizacion
    @api.constrains('tipo_cotizacion')
    def _check_invoice_due(self):
        for order in self:
            if order.tipo_cotizacion == 'promocion':
                # Se controla por la fecha de expiracion
                if order.validity_date and order.validity_date < fields.Date.today():
                    raise UserError('No se puede confirmar una cotización de "Promoción" si la cotización ha vencido.')
