import json
from odoo import models, api, fields
from odoo.tools.translate import _
from odoo.addons.community_maps.models.cm_utils import CmUtils

class CmMap(models.Model):
  _name = 'cm.map'

  _inherit = ["cm.slug.id.mixin"]

  name = fields.Char(string=_("Name"))
  config_id = fields.Many2one('cm.map.config',string=_("Config"))
  allowed_form_model_mids = fields.Many2many('cm.form.model', 
    'cm_maps_form_models', 'map_id', 'form_model_id',string=_("Allowed forms"))
  allowed_place_category_mids = fields.Many2many('cm.place.category', 
    'cm_maps_place_categories', 'map_id', 'place_category_id',string=_("Allowed categories"))
  allowed_presenter_model_mids = fields.Many2many('cm.presenter.model', 
    'cm_maps_presenter_models', 'map_id', 'presenter_model_id',string=_("Allowed persenters"))
  place_ids = fields.One2many('crm.team','map_id',string=_("Places"))
  crowdfunding_type = fields.Selection(
    selection=CmUtils.get_system_crowdfunding_types_selection(),
    default='none', required=True, string=_("Crowdfunding type"))

  # TODO: add constrains to not allow map creation without categories and presenters.

  def get_config_datamodel_dict(self):
    return self.config_id.get_datamodel_dict()

  def get_form_models_datamodel_dict(self):
    form_models = {}
    for form_model in self.allowed_form_model_mids:
      form_models[form_model.slug_id] = {
        'jsonSchema': json.loads(form_model.json_schema),
        'uiSchema': json.loads(form_model.json_uischema)
      }
    return form_models

  def get_categories_datamodel_dict(self):
    categories = {}
    for place_category in self.allowed_place_category_mids:
      categories[place_category.slug_id] = {
        'slug': place_category.slug_id,
        'map_slug': self.slug_id,
        'name': place_category.name,
        'iconKey': place_category.icon,
        'iconColor': place_category.color,
        'description': place_category.description
      }
    return categories

  def get_places_datamodel_dict(self):
    places = []
    for place in self.place_ids:
      places.append(place.get_datamodel_dict())
    return places