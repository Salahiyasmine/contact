from odoo import fields, models 

class ContactLastName(models.Model):
     
      _inherit = 'res.partner',
      
      firstname = fields.Char()
      lastname = fields.Char()
       
       
       

            