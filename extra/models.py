from django.db import models

from app_model.database.models import Restaurant

# Create your models here.


class RestaurantMenu(models.Model):
    idx          = models.AutoField(primary_key=True)
    restaurant   = models.ForeignKey(
        Restaurant, 
        on_delete=models.CASCADE,
        related_name='restaurant_menus',
    )
    name         = models.CharField(max_length=100)
    price        = models.IntegerField()

    # 아직 사용하지 X
    image        = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name}' + (f' ({self.price})' if self.price != 0 else '')
    

class RestaurantVideo(models.Model):
    idx          = models.AutoField(primary_key=True)
    restaurant   = models.ForeignKey(
        Restaurant, 
        on_delete=models.CASCADE,
        related_name='restaurant_videos'
    )
    name         = models.CharField(max_length=100, null=True, blank=True)
    address      = models.CharField(max_length=255)

    start_time   = models.IntegerField(default=0)
    end_time     = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        replaced_address = self.address
        if 'watch?v=' in replaced_address:
            replaced_address = replaced_address.split('watch?v=')[1]
            if '&' in replaced_address:
                replaced_address = replaced_address.split("&")[0]
        elif 'youtu.be' in replaced_address:
            replaced_address = replaced_address.split('youtu.be/')[1]
            if '?' in replaced_address:
                replaced_address = replaced_address.split("?")[0]
        self.address = replaced_address.replace("\n", "")
        super(RestaurantVideo, self).save(*args, **kwargs)

    def __str__(self):
        return f'점포명: {self.restaurant.name} [제목: {self.name}(주소: {self.address})]'


class RestaurantAdditionalInfo(models.Model):
    idx          = models.AutoField(primary_key=True)
    restaurant   = models.OneToOneField(
        Restaurant, 
        on_delete=models.CASCADE,
        related_name='restaurant_info'
    )


class Order(models.Model):
    idx         = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"{self.name}\n{self.description}"
