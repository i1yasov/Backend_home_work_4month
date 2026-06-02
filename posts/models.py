from django.db import models

# Create your models here.
 #C-R-U-D

# C - create
# INSERT INTO (fields) VALUES (values);
# Model.objects.create(name='asdasd', rate=2)
# user = User(name="islam", age=22)
# user.save()

# R - read
# SELECT * FROM table_name WHERE id=1;
# users = User.objects.all()

# U - update
# UPDATE table_name SET field_name=value;
# user = User.objects.get(name="islam")
# user.name = "Islam"
# user.save()

# D - delete
# DELETE table_name WHERE id=1;
# user = User.objects.get(name="islam")
# user.delete()

class Category(models.Model):
    name = models.CharField()
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    rate = models.IntegerField()
    user = models.CharField(max_length=255,null=True,blank=True)