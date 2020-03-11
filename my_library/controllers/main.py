from odoo import http
from odoo.http import request

@http.route('/books', type='http', auth="user",website=True)
class Main(http.Controller):
    def library_books(self):
    return request.render(
    'my_library.books', {
    'books':
    request.env['library.book'].search([]),
    })