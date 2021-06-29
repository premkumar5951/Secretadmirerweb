from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class txtmsg(models.Model):
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def ___str__(self):
        return self.user


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  picture = models.ImageField(upload_to='images' ,default='user.png')

  def ___str__(self):
      return self.user

class feedbackform(models.Model):
    email=models.EmailField(max_length=100)
    feedtxt=models.TextField(max_length=500)

    def __str__(self):
        return "feed from "+ self.email
