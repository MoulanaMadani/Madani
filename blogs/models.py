from django.db import models

class Blog(models.Model):

    Title = models.CharField(max_length=200)
    
    Date = models.DateTimeField()
    
    Body = models.TextField(max_length=750)
    
    image = models.ImageField(upload_to='images/')


    def __str__(self):
    	return self.Title


    def summary(self):
    	return self.Body[:100]

    def Date_wot(self):
    	return self.Date.strftime('%b %e %Y')