from django.db.models import models

class User(models.Model):
    name = models.Charfield(max_length=250)

    def __str__():
        return self.name

user = User()
user.name = "John"
user. save()
