from odoo import models, fields, api
from odoo.exceptions import ValidationError
 
class Partner(models.Model):
    # kalo ga pake _name => tidak membuat model baru atau hanya menambah atribut
    # res.partner = nama model dari module contact
    _inherit = "res.partner"
    
    # boolean akan berbentuk ceklis
    is_pegawainya = fields.Boolean(string="Pegawai", default=False)
    is_customernya = fields.Boolean(string="Pelanggan", default=False)