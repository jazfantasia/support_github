# -*- coding: utf-8 -*-
from typing import Type
from odoo import api, fields, models
import time
from datetime import datetime

class ComplaintReport(models.Model):
    _name = "complaint.report"
    _description = "Complaint Report"

    period = fields.Selection(
        string='Period',
        selection=[(' ', ' '), (' ', ' ')]
    )

    to_selection = fields.Selection(
        string='To',
        selection=[(' ', ' '), (' ', ' ')]
    )

class MonthlyReport(models.Model):
    _name = "monthly.report"
    _description = "Monthly Report"

    customers_names = fields.Selection(
        string='Customer Name',
        selection=[(' ', ' '), (' ', ' ')]
    )

    period = fields.Selection(
        string='Period',
        selection=[(' ', ' '), (' ', ' ')]
    )

    to_selection = fields.Selection(
        string='To',
        selection=[(' ', ' '), (' ', ' ')]
    )

    cust_id = fields.One2many(
        string='Customer ID',
        comodel_name='report.location',
        inverse_name='service_location',
    )

class ReportLocation(models.Model):
    _name = "report.location"
    _description = "Complaint Customer"

    
    service_location = fields.Many2one(
        string='Service Location',
        comodel_name='report.location'
    )
    traffic = fields.Text(string='Traffic Utilization')

class ReportingLocation(models.Model):
    _name = "reporting.location"
    _description = "Complaint Customer"

    
    cust_name = fields.Selection(
        string='Customer Name',
        selection=[(' ', ' '), (' ', ' ')]
    )

    service_id = fields.Selection(
        string='Service ID',
        selection=[(' ', ' '), (' ', ' ')]
    )

    period = fields.Selection(
        string='Period',
        selection=[(' ', ' '), (' ', ' ')]
    )

    to = fields.Selection(
        string='To',
        selection=[(' ', ' '), (' ', ' ')]
    )