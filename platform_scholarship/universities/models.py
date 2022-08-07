from django.db import models

#University information 

class University(models.Model):
    university_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    study_field = models.CharField(max_length=200)
    scholarship_name = models.CharField(max_length=200)
    scholarship_system = models.CharField(max_length=200)
    scholarships_available = models.CharField(max_length=200)
    start_convocatory = models.CharField(max_length=200)
    end_convocatory = models.CharField(max_length=200)
    results_selected_day = models.CharField(max_length=200)
    start_scholarship = models.CharField(max_length=200)
    end_scholarship = models.CharField(max_length=200)

   
   
    class Meta:
        db_table = 'universities' 

    def __str__(self):

        return self.university_name
