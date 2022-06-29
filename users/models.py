from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return str(self.name)

        