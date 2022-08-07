from django.db import models

#Grantee information 

class Scholar(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    study_field = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    scope_field = models.CharField(max_length=200)
    scholarship_system = models.CharField(max_length=200)
   
    class Meta:
        db_table = 'scholars' 

    def __str__(self):

        return self.name
