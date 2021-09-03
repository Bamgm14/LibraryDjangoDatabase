from django.db import models
from django.db.models.fields import CharField
from django.core.validators import RegexValidator

class bookslist(models.Model):
    Title = models.CharField(max_length=200)
    Slug = models.SlugField(unique=True)
    ISBN = models.CharField(max_length=200, primary_key=True)
    Author_Name = models.CharField(max_length=200)
    description = models.TextField() 
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.Title}-{self.Slug}' 

class reader(models.Model):
    account_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=13) # validators should be a list
    email_id = models.EmailField()
    def __str__(self):
        return f'{self.first_name}-{self.last_name}' 

class issued_list(models.Model):
    ISBN = models.ForeignKey(bookslist, on_delete = models.RESTRICT)
    account_id = models.ForeignKey(reader, on_delete = models.CASCADE)
    issued_time = models.DateTimeField()




