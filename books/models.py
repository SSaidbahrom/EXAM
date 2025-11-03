from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=204)
    created_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images/')
    description = models.TextField()
    file = models.FileField(upload_to='book_files/')
    author = models.CharField(max_length=100)
    number_of_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

    def __str__(self):
        pass