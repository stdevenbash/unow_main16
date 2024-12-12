# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class EmployeeProjectPortal(http.Controller):

    @http.route(['/my/projects'], type='http', auth='user', website=True)
    def list_projects(self, **kwargs):
        user = request.env.user
        employee = request.env['hr.employee'].search([('user_id', '=', user.id)], limit=1)

        if not employee:
            return request.render('website.403')
        domain = [('employee_id', '=', employee.id)]
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')

        if start_date:
            domain.append(('start_date', '>=', start_date))
        if end_date:
            domain.append(('end_date', '<=', end_date))

        projects = request.env['employee.project'].sudo().search(domain)
        return request.render('employee_projects.portal_my_projects', {
            'projects': projects,
            'employee': employee,
            'start_date': start_date,
            'end_date': end_date,
        })

    @http.route(['/my/projects/create'], type='http', auth='user', website=True, csrf=False)
    def create_project(self, **kwargs):
        user = request.env.user
        employee = request.env['hr.employee'].search([('user_id', '=', user.id)], limit=1)

        if not employee:
            return request.render('website.403')
        if request.httprequest.method == 'POST':
            name = kwargs.get('name')
            description = kwargs.get('description')
            start_date = kwargs.get('start_date')
            end_date = kwargs.get('end_date')

            if not name or not start_date:
                return request.render('employee_projects.portal_create_project', {
                    'employee': employee,
                    'error': 'El nombre y la fecha de inicio son obligatorios.',
                })

            project = request.env['employee.project'].sudo().create({
                'name': name,
                'description': description,
                'employee_id': employee.id,
                'start_date': start_date,
                'end_date': end_date,
            })
            return request.redirect('/my/projects')

        return request.render('employee_projects.portal_create_project', {
            'employee': employee,
        })

    @http.route(['/my/project/<int:project_id>'], type='http', auth='user', website=True)
    def view_project(self, project_id, **kwargs):
        user = request.env.user
        employee = request.env['hr.employee'].search([('user_id', '=', user.id)], limit=1)

        if not employee:
            return request.render('website.403')

        project = request.env['employee.project'].sudo().browse(project_id)

        if not project or project.employee_id.id != employee.id:
            return request.render('website.403')

        return request.render('employee_projects.portal_view_project', {
            'project': project,
        })
