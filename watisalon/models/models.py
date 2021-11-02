# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ModelDasar(models.Model):
    _name = 'watisalon.base'
    _description = 'Model dasar Wati Salon'

    # treatment = fields.Selection(string="Treatment tambahan", selection=[('Creambath', 'creambath'),
    #     ('Pijat', 'pijat'), ('Creambath & Pijat', 'creambath & pijat'), ('Tidak Ada', 'tidak ada')])

    layanan = fields.Selection(string="Pilihan Layanan", selection=[('potong rambut', 'Potong Rambut'),
        ('keriting rambut','Keriting Rambut'), ('smoothing rambut','Smoothing Rambut'), ('cat rambut','Cat Rambut')])

class watisalon(models.Model): #traditional inherit by python
    _name = 'watisalon.jenislayanan'
    _description = 'Daftar jenis-jenis layanan'
    _inherit = 'watisalon.base' #delegation inherit by odoo = inherit ke berbagai macam class

    name = fields.Char(string='ID Layanan', required=True)
    jenis = fields.Char(string='Jenis Rambut', required=True)
    harga = fields.Integer(string='Harga layanan', required=True)
    active = fields.Boolean(default=True)
    tipe = fields.Many2one(comodel_name='watisalon.tipe', string='Tipe', required=True )
    

