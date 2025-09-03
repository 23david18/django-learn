from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
class DataBook(models.Model):
    description = models.TextField()
    is_purchase = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    