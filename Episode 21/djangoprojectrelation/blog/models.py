from django.db import models

# Create your models here.
class Publication(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    fill = models.TextField()
    OPTION_CATEGORY = [
        ('python','python'),
        ('django','django'),
        ('javascript','javascript'),
    ]
    categories = models.CharField(max_length=50, choices=OPTION_CATEGORY)
    publications = models.ForeignKey(Publication, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
class ReadList(models.Model):
    readers = models.ForeignKey(Reader, on_delete=models.CASCADE)
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.articles.title} - {self.readers.name}"