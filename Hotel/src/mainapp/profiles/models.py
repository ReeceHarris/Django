from django.db import models


TYPE_CHOICES = {
    ('Mr.','Mr.'),
    ('Mrs.','Mrs.'),
    ('Ms.','Ms.'),
    ('', ''),
}

# Create your models here.
class profiles(models.Model):
    Prefix = models.CharField(max_length=6, default="", blank=True, null=False, choices=TYPE_CHOICES)
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60, default="", blank=True, null=False)
    Email = models.EmailField(max_length=254, default="", blank=True, null=False)
    Username = models.CharField(max_length=40, default="", blank=True, null=False )

    objects = models.Manager()

    def __mod__(self):
        return self.name

