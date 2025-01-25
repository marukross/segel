{
    'name': 'Productos Personalizados Segel',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Modulo de la prueba tecnica para Segel',
    'depends': ['stock'],
    'data': [
        'views/producto_personalizado_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}