# -*- coding: utf-8 -*-
from odoo import http


class Watisalon(http.Controller):
    @http.route('/watisalon/watisalon/', auth='public')
    def index(self, **kw):
        return "Hello, world"