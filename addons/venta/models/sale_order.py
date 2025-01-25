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
        # Verifica si el cliente cuenta con facturas vencidas al confirmar la cotizacion
        for order in self:
            if order.tipo_cotizacion == 'promocion':
                overdue_invoices = self.env['account.invoice'].search([
                    ('partner_id', '=', order.partner_id.id),
                    ('state', '=', 'open'),
                    ('date_due', '<', fields.Date.today())
                ])
                if overdue_invoices:
                    raise UserError('No se puede confirmar una cotización de "Promoción" si el cliente tiene facturas vencidas.')
