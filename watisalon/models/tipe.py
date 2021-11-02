# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class Tipe(models.Model):
    # ini akan berbentuk tabel nanti
    _name = 'watisalon.tipe'
    _description = 'Tipe Quality of Treatment'
    
    # ini merupakan field yang dibutuhkan untuk suatu record
    name = fields.Selection(string='Nama Tipe', selection=[('basic A', 'Basic A'), ('basic B', 'Basic B'), 
                            ('standard A','Standard A'), ('standard B','Standard B'), ('premium A','Premium A'), 
                            ('premium B','Premium B')])

    treatment = fields.Selection(string="Treatment tambahan", selection=[('tidak ada', 'Tidak Ada'), 
                            ('pijat', 'Pijat'), ('creambath & pijat', 'Creambath & Pijat')])
    
    kerusakan =  fields.Selection(string='Tipe Kerusakan Rambut',
                            selection=[('ringan', 'Ringan'), ('berat', 'Berat')], required=True)
    
    tersedia = fields.Boolean(string='Tersedia', default=True)
    
    pj = fields.Many2one(
        comodel_name='res.partner', 
        string='Penanggung jawab',
        domain = "[('is_pegawainya','=',True)]"
        )