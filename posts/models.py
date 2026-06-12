from django.db import models

# Create your models here.
# C-R-U-D

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


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название тега") 

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок") 
    content = models.TextField(verbose_name="Контент")
    rate = models.IntegerField(verbose_name="Рейтинг")
    user = models.CharField(max_length=255, null=True, blank=True, verbose_name="Автор")
    
 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    tags = models.ManyToManyField('Tag', blank=True, verbose_name="Теги")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
   
        category_title = self.category.title if self.category else "-"
        return f"{self.title} -- {category_title}"