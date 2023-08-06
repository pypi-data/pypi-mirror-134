from odoo import models, api, fields
from odoo.tools.translate import _

class CmFormSubmission(models.Model):
  # _name = 'cm.form.submission'
  _inherit = 'crm.lead'

  team_type = fields.Char(string=_("Team type"),compute="_get_team_type",store=True)
  # name = fields.Char(string=_("Name"))
  form_submission_metadata_ids = fields.One2many('cm.form.submission.metadata',
    'submission_id',string=_("Submission metadata"))

  @api.depends('team_id')
  def _get_team_type(self):
    for record in self:
      team_type = False
      team = record.team_id
      if team:
        team_type = team.team_type
      record.team_type = team_type


  @api.constrains('team_id')
  def recompute_probability(self):
    for record in self:
      if record.team_id:
        for submission in record.team_id.form_submission_ids:
          submission.update_probability()
      else:
        submissions = self.env['crm.lead'].search([('team_type','=','map')])
        if submissions.exists():
          for submission in submissions:
            submission.update_probability()
      record.update_probability()#TODO: check if this line needed

  def update_probability(self):
    probability = 0
    if self.team_id:
      probability = self.team_id.completed_percentage
    self.write({
      'probability': probability
    })
