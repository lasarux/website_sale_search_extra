# -*- coding: utf-8 -*-
from openerp import http

# class WebsiteSaleSearchExtra(http.Controller):
#     @http.route('/website_sale_search_extra/website_sale_search_extra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_search_extra/website_sale_search_extra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_search_extra.listing', {
#             'root': '/website_sale_search_extra/website_sale_search_extra',
#             'objects': http.request.env['website_sale_search_extra.website_sale_search_extra'].search([]),
#         })

#     @http.route('/website_sale_search_extra/website_sale_search_extra/objects/<model("website_sale_search_extra.website_sale_search_extra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_search_extra.object', {
#             'object': obj
#         })

class WebsiteSaleSearchExtra(http.Controller):
    @http.route('/shop/search', auth='public', type='json')
    def temp(self, **kwargs):
        print '>>> status', kwargs

        return {
            'status': 'ok',
            'query': kwargs['query']
        }