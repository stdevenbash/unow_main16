# -*- coding: utf-8 -*-

{
    'name': 'Employee Projects',
    'version': '1.0',
    'author': 'Wilberth Steven',
    'summary': 'Gestión de proyectos para empleados',
    'description': 'Módulo para gestionar proyectos asociados a empleados en Odoo.',
    'category': 'Human Resources',
    'depends': ['base', 'hr', 'website', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_project_views.xml',
        'views/hr_employee_views.xml',
        'views/portal_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/employee_projects/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
}
