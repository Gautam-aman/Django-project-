from django.db import models
import uuid

# Create your models here.

class Basemodel(models.Model):
    uid = models.UUIDField(default= uuid.uuid4(), editable=False, primary_key=True)
    created_at= models.DateField(auto_created=True)
    updated_at= models.DateField(auto_created=True)
    
    class Meta:
        abstract=True  #python will consider as base class not a model 
        
    

class Product (Basemodel):
   product_slug=models.SlugField(unique=True)
   product_name= models.CharField(max_length=100)
   product_description= models.TextField()
   product_price= models.IntegerField(default=0)
   product_demoprice= models.IntegerField(default=0)
  
   
   
class ProductMetaInformation(Basemodel):
    products= models.OneToOneField(Product, on_delete=models.CASCADE , related_name="meta_info")
    product_quantity= models.IntegerField(null= True, blank=True)
    product_measuring = models.CharField(max_length = 100, null= True, blank=True, choices=(("KG","KG"),("ML","ML"),(None, None )))
    is_restrict = models.BooleanField(default= False)
    restrict_quantity= models.IntegerField()
    
    
    
class ProductImages(Basemodel):
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_image = models.ImageField(upload_to="products")
   
    
class Dummy_model(Basemodel):
  pass
    
    
    
    
