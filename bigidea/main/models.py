from django.db import models

class Contact(models.Model):
    name = models.CharField( max_length=100 )
    email = models.EmailField()
    phone = models.CharField( max_length=20 )
    age = models.IntegerField()

    def __unicode__(self):
        return '%s => %s' % (self.name, self.phone)
