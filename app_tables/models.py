from django.db import models
from django.utils.html import format_html 
from .colors_models_str_format import colors

# Create your models here.

class motorcycle(models.Model):
    manufacturer = models.CharField(max_length=15, blank=False)
    motorcycle = models.CharField(max_length=15)
    year = models.CharField(max_length=9)

    def __str__(self):
        text = f"{self.motorcycle} / ({self.year})"
        return text
    
    def motorcycle_color(self): 
        if self.manufacturer in colors:
            return format_html(f"<span style='color: {colors[self.manufacturer]};'>{self.motorcycle}</span>")
        else:
            pass
    
class product(models.Model):
    code = models.CharField(max_length=9, unique=True)
    images = models.ImageField(upload_to="acc/", unique=True)
    accessory = models.CharField(max_length=30)
    compatibility = models.ForeignKey(motorcycle, on_delete=models.CASCADE)

    def __str__(self):
        text2 = f"{self.code} / {self.accessory} ({self.compatibility.year})"
        return text2

    def view_image(self):
        return format_html(f"<img src='{self.images.url}' width='60px' height='30px' alt='image'>")
    view_image.short_description = "Image"

class compatibility_acc(models.Model):
    code_product = models.OneToOneField(product, on_delete=models.CASCADE, unique=True, related_name="coded")
    code_ref = models.ForeignKey(product, on_delete=models.CASCADE, blank=True)



    
    


    



    
