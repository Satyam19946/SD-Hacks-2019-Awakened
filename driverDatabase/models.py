from django.db import models

# Create your models here.
class Driver( models.Model ):
    name_text = models.CharField( max_length=200 )
    date = models.DateTimeField('Time you started driving',default=0)
    end_date = models.DateTimeField('Time you ended driving',default=0)
    
    def __str__(self):
        return self.name_text
 