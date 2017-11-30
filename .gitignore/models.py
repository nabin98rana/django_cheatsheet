from django.db import models 
from django.utils.translation import ugettext_lazy as _

class CheatSheetModel(models.Model):
  model_name = models.CharField(_("Model name"), max_length=255, blank=True, null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True) 
  cheatsheet_level = models.CharField(
      choices=(
      ('0', 'beginners'),
      ('1', 'intermediate'),
      ('2', 'expert')
      )
     
  
  # Meta class 
  class Meta:
    # Order all the CheatsheetModel in reverse order while fetching from daabase
    ordering = ['-model_name', 'updated_date']
    # Name of a table
    db_table = "cheatsheet_model"
    # Verbose name in admin 
    verbose_name = _("Cheatsheet model")
    verbose_name_plural = _("Cheatsheet models")
 
  def __str__(self):
      return self.model_name 
    
  def get_absolute_url(self):
      """
      Returns the url to access a particular instance of the model.
      """
      return reverse('detail_view', kwargs={"id":self.id})
