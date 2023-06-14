from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title
