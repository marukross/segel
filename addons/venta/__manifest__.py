{
    'name': 'Extension Sale Segel',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Se exitende la funcionalidad el modulo sale',
    'depends': ['sale_management', 'account'],
    'data': [
        'views/sale_order_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
