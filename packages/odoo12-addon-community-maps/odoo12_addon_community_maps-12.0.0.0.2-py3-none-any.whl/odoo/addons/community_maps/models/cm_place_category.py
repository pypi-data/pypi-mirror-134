from odoo import models, api, fields
from odoo.tools.translate import _

class CmPlaceCategory(models.Model):
  _name = 'cm.place.category'

  _inherit = ["cm.slug.id.mixin"]

  name = fields.Char(string=_("Name"))
  icon = fields.Char(string=_("Icon"))
  color = fields.Char(string=_("Color"))
  description = fields.Char(string=_("Description"))

  allowed_in_map_mids = fields.Many2many('cm.map', 'cm_maps_place_categories', 'place_category_id', 'map_id',
    string=_("Allowed in maps"))