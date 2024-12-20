from django.db import models

# Create your models here .
class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    birth_date = models.DateField(null = True , blank = True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=250)
    context = models.TextField()
    cteated_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField( auto_now_add=True)
    is_published = models.BooleanField(default = False)
    published_date = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
