from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField(default='제품 설명란입니다.')
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='image_storage', blank=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name