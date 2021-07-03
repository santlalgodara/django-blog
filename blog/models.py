from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def total_posts(self):
        return self.posts.count()

    def __str__(self):
        return self.full_name()


class Category(models.Model):
    title = models.CharField(max_length=150)
   
    def total_posts(self):
        return self.posts.count()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True, null=True)
    excerpt = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="posts")
    def categories(self):
        return ", ".join([cat.title for cat in self.category.all()])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])
