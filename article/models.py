from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Müəllif")
    title = models.CharField(max_length=50, verbose_name="Başlıq")
    content = models.TextField(verbose_name="Məzmun")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    def __str__(self):
        return(self.title)
    

