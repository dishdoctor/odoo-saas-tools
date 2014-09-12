from openerp.osv import fields, osv

class saas_portal_config_wizard(osv.osv_memory):
    _name = 'saas_portal.config.settings'
    _inherit = 'res.config.settings'
    _columns = {
        'base_saas_domain': fields.char('Base saas domain',
                                        help="e.g. odoo.com"),
    }

    def get_default_base_saas_domain(self, cr, uid, ids, context=None):
        base_saas_domain = self.pool.get("ir.config_parameter").get_param(cr, uid, "saas_portal.base_saas_domain", default=None, context=context)
        if base_saas_domain is None:
            domain = self.pool.get("ir.config_parameter").get_param(cr, uid, "web.base.url", context=context)
            try:
                base_saas_domain = urlparse.urlsplit(domain).netloc.split(':')[0]
            except Exception:
                pass
        return {'base_saas_domain': base_saas_domain or False}

    def set_base_saas_domain(self, cr, uid, ids, context=None):
        config_parameters = self.pool.get("ir.config_parameter")
        for record in self.browse(cr, uid, ids, context=context):
            config_parameters.set_param(cr, uid, "saas_portal.base_saas_domain", record.base_saas_domain or '', context=context)
