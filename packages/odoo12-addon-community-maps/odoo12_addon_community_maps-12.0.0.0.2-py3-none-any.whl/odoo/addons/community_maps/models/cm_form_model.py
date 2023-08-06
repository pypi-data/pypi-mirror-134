from odoo import models, api, fields
from odoo.tools.translate import _

class CmFormModel(models.Model):
  _name = 'cm.form.model'

  _inherit = ["cm.slug.id.mixin"]

  name = fields.Char(string=_("Name"))

  allowed_in_map_mids = fields.Many2many('cm.map', 'cm_maps_form_models', 'form_model_id', 'map_id',
    string=_("Allowed in maps"))

  json_schema = fields.Text(string=_("Schema"))
  json_uischema = fields.Text(string=_("UiSchema"))


  def submit(self,data):
    # TODO: submit data into crmlead
    print("Base submit")
    return True
