from django.db import models

class Car(models.Model):
    license_plate = models.CharField(
        verbose_name="Гос номер",
        max_length=10,
        null=True,
        unique=True,
    )
    
    brand = models.CharField(
        verbose_name="Марка машины",
        max_length=200
    )
    
    model = models.CharField(
        verbose_name="Модел машины",
        max_length=200
    )
    
    year = models.PositiveBigIntegerField(
        verbose_name='Год выпуска'
    )
    
    color = models.CharField(
        verbose_name="Цвет авто",
        max_length=200
    )
    
    redder_location = models.CharField(
        verbose_name="Расположение руля",
        max_length=100
    )
    
    engine_volume = models.PositiveBigIntegerField(
        verbose_name="Объем двигателя"
    )

    def __str__(self):
        return f"{self.license_plate}"
    
    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural ="Автомобили"
     

