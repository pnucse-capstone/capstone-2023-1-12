from django.db import models

# Create your models here.

class RestaurantServiceName(models.Model):
    idx          = models.AutoField(primary_key=True)
    service      = models.CharField(max_length=100)
    name         = models.CharField(max_length=100)
    is_use       = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}"
    

    
class Restaurant(models.Model):
    '''
    Restaurant에 대한 기본 정보\n
    name: 이름\n
    x_coordinate: 카테고리\n
    y_coordinate: 중부원점TM좌표\n
    full_address: 소재지 전체 주소\n
    road_address: 도로명 전체 주소
    '''
    idx          = models.AutoField(primary_key=True)
    # 식당 이름
    name         = models.CharField(max_length=100)
    # 식당 서비스 종류
    service      = models.ForeignKey(
        RestaurantServiceName,
        on_delete=models.RESTRICT,
    )
    # 식당의 TM중부원점좌표
    x_coordinate = models.DecimalField(max_digits=15, decimal_places=9)
    y_coordinate = models.DecimalField(max_digits=15, decimal_places=9)
    # 식당의 소재지 전체 주소
    full_address = models.CharField(max_length=100, null=True, blank=True)
    # 식당의 도로명 전체 주소
    road_address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.service.name}'