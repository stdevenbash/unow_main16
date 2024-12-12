# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    project_ids = fields.One2many(
        'employee.project',
        'employee_id',
        string="Projects"
    )
    total_projects = fields.Integer(
        string="Total Projects",
        compute='_compute_total_projects',
        store=True
    )

    @api.depends('project_ids')
    def _compute_total_projects(self):
        for rec in self:
            rec.total_projects = len(rec.project_ids)

    def action_open_employee_projects(self):
        """Acción para abrir los proyectos relacionados con el empleado."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Proyectos del Empleado',
            'res_model': 'employee.project',
            'view_mode': 'tree,form',
            'domain': [('employee_id', '=', self.id)],
            'context': {'default_employee_id': self.id},
        }
