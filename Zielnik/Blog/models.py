from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class TeaProduct(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    benefits = models.TextField(help_text='Comma-separated list of benefits.')
    caffeine_free = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=200, blank=True)
    origin = models.CharField(max_length=200, blank=True)
    grows_where = models.TextField(blank=True)
    properties = models.TextField(blank=True)
    history = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def benefits_list(self):
        return [b.strip() for b in self.benefits.split(',') if b.strip()]

    @property
    def image_url(self):
        if not self.image:
            return '/media/sklep.png'
        if self.image.startswith('/'):
            return self.image
        return f"/media/{self.image}"


class TeaProductImage(models.Model):
    product = models.ForeignKey(TeaProduct, on_delete=models.CASCADE, related_name='images')
    image = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.image}"

    @property
    def image_url(self):
        if self.image.startswith('/'):
            return self.image
        return f"/media/{self.image}"
