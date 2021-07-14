import odoo
import json
import logging

_logger = logging.getLogger(__name__)


class WebsiteProduct(odoo.addons.website_sale.main.WebsiteSale):

    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):
        # use super to call prevously defined checkout methods so we not overriding the method but extend it.
        res = super(WebsiteSale, self).checkout(**post)
        # code your bugs in here ;)