# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Order(models.Model):
    # ini akan berbentuk tabel nanti
    _name = 'watisalon.order'
    _description = 'Daftar Order Salon'
    
    name = fields.Char(
        string="Kode Order", 
        required=True)

    pid = fields.Many2one(
        comodel_name='res.partner', 
        string='Nama Pemesan', 
        domain="[('is_customernya','ilike',True)]")

    ptgl = fields.Datetime(
        string='Tanggal Pesanan',
        default=fields.Datetime.now)

    detailpesanan_id = fields.One2many(
        comodel_name='watisalon.detailpesanan',
        inverse_name='o_id',
        string='Detail Order')

    total_harga = fields.Char(
        compute='_compute_total_harga', 
        string='Total Harga')
    
    @api.model
    def _compute_total_harga(self):
        # mapped = untuk mengambil satu atribut saja
        # self.env---.mapped = mengembalikan suatu list
        for record in self:
            total = sum(self.env['watisalon.detailpesanan'].search([('o_id','=',record.id)]).mapped('harga'))
            record.total_harga = total


class DetailPesanan(models.Model):
    _name = 'watisalon.detailpesanan'
    _description = 'Detail Pesanan'

    o_id = fields.Many2one(
        comodel_name='watisalon.order', 
        string='Jenis layanan')

    a_id = fields.Many2one(
        comodel_name='watisalon.jenislayanan', 
        string='Tipe Layanan')

# oofcompute
    harga = fields.Integer(
        compute='compute_harga', #method
        string='Harga per layanan')
    
    @api.depends('a_id')
    def compute_harga(self): #method ke kelas ini
        for record in self:
            record.harga = record.a_id.harga
        
    # jumlah_harga = fields.Integer(
    #     compute='compute_jumlah_harga', 
    #     string='Jumlah Harga')
    
    # @api.depends('berat')
    # def compute_jumlah_harga(self):
    #     for record in self:
    #         record.jumlah_harga = record.berat * record.harga

        
    
