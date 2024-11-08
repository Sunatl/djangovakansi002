from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Vakansi(models.Model):
    title  = models.CharField(max_length=50)
    description =  models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images",null=True,blank=True)
    
    def __str__(self):
        return  self.title
    
    
class Application(models.Model):
    vakansi = models.ForeignKey(Vakansi, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    resume = models.FileField(upload_to='static/images',null=True,blank=True)
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.vakansi.title}"
    
    
    
from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    company = models.CharField(max_length=50,null=True)
    desc = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.name}"
