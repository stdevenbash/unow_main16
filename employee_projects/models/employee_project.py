# -*- coding: utf-8 -*-

from odoo import models, fields


class EmployeeProject(models.Model):
    _name = 'employee.project'
    _description = 'Employee Projects'

    name = fields.Char(string="Nombre del Proyecto", required=True)
    description = fields.Text(string="Descripción")
    employee_id = fields.Many2one(
        'hr.employee',
        string="Empleado",
        required=True,
        ondelete='cascade'
    )
    start_date = fields.Date(string="Fecha de Inicio")
    end_date = fields.Date(string="Fecha de Fin")
