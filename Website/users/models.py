from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=50, default="123 North Street")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    promo_register = models.BooleanField(default=False)
    card_number = models.CharField(max_length=16, default="1234123412341234")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            ouput_size = (300, 300)
            img.thumbnail(output_size)
            img.save()
