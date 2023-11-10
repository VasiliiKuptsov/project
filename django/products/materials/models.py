from django.db import models
class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='материал')
    body = models.TextField(verbose_name='содержимое')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

