# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class callCenter(models.Model):
    _name = 'callcenter.call_center'
    _description = ''

    start_time = fields.Datetime()
    stop_time = fields.Datetime()
    duration = fields.Float(compute="compute_duration", store=True)
    source = fields.Char()
    destination = fields.Char()
    name = fields.Char(defualt='New')
    station = fields.Many2one(comodel_name='callcenter.call_station')
    tags = fields.Many2many(comodel_name='callcenter.call_tags')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('invoiced', 'Invoiced'),
    ], default='draft', string='Status')
    partner_id = fields.Many2one(comodel_name='res.partner')

    @api.constrains('stop_time')
    def check_stop_time(self):
        for rec in self:
            if rec.stop_time < rec.start_time:
                raise ValidationError('Stop time must be bigger start time!!')

    @api.depends('stop_time', 'start_time')
    def compute_duration(self):
        for record in self:
            if(record.start_time is not False and record.stop_time is not False):
                record.duration = (record.stop_time - record.start_time).seconds / 60



    def create_invoice(self):
        invoice_obj = self.env['account.move'].create({
            'partner_id': self.partner_id.id,
            'type': 'out_invoice'
        })

        invoice_line_obj = self.env['account.move.line'].create({
            'product_id': 1,
            'name':  '[EXP_REST] Restaurant Expenses',
            'move_id': invoice_obj.id,
            'price_unit': self.duration * 1.30,
            'account_id': self.partner_id.property_account_receivable_id.id,
        })




class callStation(models.Model):
    _name = 'callcenter.call_station'

    name = fields.Char()
    calls = fields.One2many(comodel_name='callcenter.call_center', inverse_name='station')


class Tags(models.Model):
    _name = 'callcenter.call_tags'

    name = fields.Char()


