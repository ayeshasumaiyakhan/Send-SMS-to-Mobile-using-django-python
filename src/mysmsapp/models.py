from django.db import models


# Create your models here.
class Contact_details(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    phone_number = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular instance."""
        return reverse('Index', args=[str(self.id)])
