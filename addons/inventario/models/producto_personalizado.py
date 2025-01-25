from odoo import models, fields

class ProductoPersonalizado(models.Model):
    _name = 'producto.personalizado'
    _description = 'Producto Personalizado'

    name = fields.Char('Nombre del Producto', required=True)
    description = fields.Text('Descripción del Producto')
    price = fields.Float('Precio', required=True)
    stock = fields.Integer('Cantidad en Inventario', default=0)