from odoo.addons.base_rest import restapi
from werkzeug.exceptions import BadRequest, NotFound
from odoo.addons.base_rest.http import wrapJsonException
from odoo.addons.component.core import Component
from odoo.addons.base_rest_base_structure.models.api_services_utils import APIServicesUtils
from odoo.tools.translate import _

class CmMapService(Component):
  _inherit = "base.rest.private_abstract_service"
  _name = "cm.map.service"
  _usage = "map"
  _description = """
      Map Service
  """

  @restapi.method(
    [(["/<string:slug>/config"], "GET")],
    auth="api_key",
  )
  def config(self,_slug):
    record = self.env["cm.map"].search(
      [("slug_id", "=", _slug)]
    )
    if record:
      try:
        record.ensure_one()
      except:
        return {
          'code': 404,
          'name': _("More than one map found for %s") % _slug
        }
      return {
        "config": record.get_config_datamodel_dict(),
        "forms": record.get_form_models_datamodel_dict(),
        "categories": record.get_categories_datamodel_dict()
      }
    else:
      return {
        'code': 404,
        'name': _("No map record for id %s") % _slug
      }
    return False

  # @restapi.method(
  #   [(
  #     [
  #       "/<string:map_slug>/places/<string:place_slug>",
  #       "/<string:map_slug>/places/"
  #     ],
  #     "GET"
  #   )],
  #   auth="api_key",
  # )
  def places(self,_map_slug,_place_slug=None):
    record = self.env["cm.map"].search([
      ("slug_id", "=", _map_slug)
    ])
    if record.exists():
      try:
        record.ensure_one()
      except:
        return {
          'code': 404,
          'name': _("More than one map found for %s") % _map_slug
        }
      if _place_slug:
        place_record = self.env["crm.team"].search([
          ("slug_id", "=", _place_slug),
          ("team_type", "=", 'map')
        ])
        if place_record.exists():
          try:
            place_record.ensure_one()
          except:
            return {
              'code': 404,
              'name': _("More than one place found for %s") % _place_slug
            }
          return place_record.get_datamodel_dict(True)
        else:
          return {
            'code': 404,
            'name': _("No place record for id %s") % _place_slug
          }
      else:
        return record.get_places_datamodel_dict()
    else:
      return {
        'code': 404,
        'name': _("No map record for id %s") % _map_slug
      }
    return False
