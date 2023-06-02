# -*- coding: utf-8 -*-
from typing import Type
from odoo import api, fields, models
import time
from datetime import datetime

class ComplaintTiket(models.Model):
    _name = "complaint.tiket"
    _description = "Complaint Tiket"
    
    email = fields.Char(string='Mail')

    ticket = fields.Selection(
        string='Regional',
        selection=[('[Reported] by Customer', '[Reported] by Customer',), ('[Detected] by Monitoring', '[Detected] by Monitoring'), ('[Preventive] Plain Maintenance','[Preventive] Plain Maintenance')
        ], tracking=True
    )

    date_and_time = fields.Datetime(
        string='Created Date and Time')
    reported = fields.Char(string='Reported By', tracking=True)
    name = fields.Selection(
        string='Customer Name',
        selection=[('M2O dari DB Customer', 'M2O dari DB Customer'), 
        (' ', ' ')],
        default='M2O dari DB Customer',
        tracking=True
    )
    is_show = fields.Boolean(
        string='Show Network Segment?')

    service_id = fields.Selection(
        string='Service ID',
        selection=[('M20 dari Service yg ada di DB Customer', 'M20 dari Service yg ada di DB Customer'), (' ', ' ')],
        default='M20 dari Service yg ada di DB Customer'
    )
    monthly_tarif = fields.Integer(string='Monthly Tarif')
    problem_indication = fields.Text(string='Problem Indication')
    support_team = fields.Selection(
        string='Support Team',
        selection=[('(CS FLOW,CS FRES,CS HOPE,CS RAVE,CS TIME,CS NOC,CS AND)', 'CS FLOW,CS FRES,CS HOPE,CS RAVE,CS TIME,CS NOC,CS AND'), (' ', ' ')],
        default='(CS FLOW,CS FRES,CS HOPE,CS RAVE,CS TIME,CS NOC,CS AND)'
    )
    assign = fields.Selection(
        string='Assign To',
        selection=[('(All Support Team)', '(All Support Team)'), (' ', ' ')],
        default='(All Support Team)'
    )
    
    # preventive 
    
    request_by= fields.Char(
        string='Request By',
    )
    objective = fields.Text(string='Objective of Maintenance')

    support_teams = fields.Selection(string='Support Team',
        selection=[('(CS FLOW,CS FRES,CS HOPE,CS RAVE,CS TIME,CS NOC,CS AND)', 'CS FLOW,CS FRES,CS HOPE,CS RAVE,CS TIME,CS NOC,CS AND'), (' ', ' ')],
        default='(CS FLOW,CS FRES,CS HOPE,CS RAVE,CS TIME,CS NOC,CS AND)'
    )
    assign_to = fields.Selection(
        string='Assign To',
        selection=[('(All Support Team)', '(All Support Team)'), (' ', ' ')],
        default='(All Support Team)'
    )
    regionals = fields.Selection(
        string='Regional',
        selection=[(' ', ' '), (' ', ' ')]
    )
    pop_names = fields.Selection(
        string='POP Name',
        selection=[(' ', ' '), (' ', ' ')]
    )
    monthlies_tarif  = fields.Integer(
        string='Montly Tarif',
    )
    current_condition = fields.Text(
        string='Current Condition',
    )
    attachment = fields.Image(
        string='Attachment',
    )
    detail_activity = fields.Text(
        string='Detail Activity Plan',
    )
    maintenace_type = fields.Selection(
        string='Maintenance Type',
        selection=[('Preventive', 'Preventive'), ('Emergency', 'Emergency'),('Urgent','Urgent')]
    )
    scheduled_date = fields.Datetime(
    string='Scheduled Date')
    to_date = fields.Datetime(
    string='To')

    notification_one = fields.Selection(
        string='Notification 1',
        selection=[(' ', ' '), (' ', ' ')]
    )
    notification_two = fields.Selection(
        string='Notification 2',
        selection=[(' ', ' '), (' ', ' ')]
    )
    

    # detected by monitoring
    detected_by = fields.Char(
        string='Detected By',
    )
    

    problem_category = fields.Selection(
        string='Problem Category',
        selection=[(' ', ' '), (' ', ' ')]
    )
    network_segment = fields.Selection(
        string='Network Segment',
        selection=[(' ', ' '), (' ', ' ')]
    )
    event_failure = fields.Selection(
        string='Event Failure',
        selection=[(' ', ' '), (' ', ' ')]
    )
    circuit_id = fields.Selection(
        string='Circuit ID',
        selection=[(' ', ' '), (' ', ' ')]
    )
    cid = fields.Char(
        string='CID Description',
    )
    
    service_impact = fields.Selection(
        string='Service Impact',
        selection=[(' ', ' '), (' ', ' ')]
    )
    problem_criticality = fields.Char(
        string='Problem Criticality',
    )
    
    scale = fields.Selection(
        string='Scale of Problem',
        selection=[('(All Customer,Partial Customer,Localize Customer,Single Customer)', '(All Customer,Partial Customer,Localize Customer,Single Customer)'), 
        (' ', ' ')],
        default='(All Customer,Partial Customer,Localize Customer,Single Customer)'
    )
    customer_name = fields.Selection(
        string='Customer Name',
        selection=[(' ', ' '), (' ', ' ')]
    )
    business_priority = fields.Selection(
        string='Business Priority',
        selection=[(' ', ' '), ('Very Important', 'Very Important')]
    )
    severity_code = fields.Char(
        string='Severity Code',
    )
    problem_desc = fields.Text(
        string='Problem Description',
    )
    acknoweledge_by = fields.Char(
        string='Acknowledge By'
    )
    acknoweledge_time = fields.Char(
        string='Acknowledge Time'
    )
    dispatch_to = fields.Selection(
        string='Dispatch To',
        selection=[(' ', ' '), (' ', ' ')]
    )
    partner_name = fields.Selection(
        string='Partner Name',
        selection=[(' ', ' '), (' ', ' ')]
    )
    contact_name = fields.Char(
        string='Contact Name',
    )

    cust_id = fields.One2many(
        string='Customer ID',
        comodel_name='complaint.customer',
        inverse_name='customer_name',
    )
    cust_ids = fields.One2many(
        string='Customer ID',
        comodel_name='complaint.customer',
        inverse_name='cust_name',
    )

    # button for mail
    
    def action_notify_ticket(self):
            template = self.env.ref("support.client_test_email_template")
            for rec in self:
                #template.send_mail(rec.id, force_send=True)
                template.send_mail(rec.id)
                lines =[]
                val = {
                        'dt' : datetime.now(),
                        'activity_type' : 'notify',
                        'pic' : "Administrator",
                        'details' : "Notify Customer",
                        'reference' : rec.id
                }
                lines.append((0,0,val))


class ComplaintCustomer(models.Model):
    _name = "complaint.customer"
    _description = "Complaint Customer"

    
    customer_name = fields.Many2one(
        string='Customer Name',
        comodel_name='complaint.customer'
    )
    cust_name = fields.Many2one(
        string='Customer Name',
        comodel_name='complaint.customer'
    )
    pop_name = fields.Char(string='POP Name'
    )
    regional = fields.Char(string='Regional')
    service_id_table = fields.Text(string='Service ID')
    product_category = fields.Selection(
        string='Product Category',
        selection=[('VELOcity', 'VELOcity'), ('VELOrap', 'VELOrap')]
    )
    monthly_tarif_table = fields.Integer(
        string='Monthly Tarif (IDR)',
    )
    
    # plan maitenance
    total_service = fields.Text(string='Total Service')
    busi_prio = fields.Text(string='Business Priority')
