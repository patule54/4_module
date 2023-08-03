from django.db import models


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='отметьте, если торг уместен')
    created_at = models.DateTimeField('дата и время создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата и время изменения', auto_now=True)
    class Meta:
        db_table = 'advertisments'
    
    def __str__(self):
        return f'Advertisement(id-{self.id}, title={self.title}, price={self.price})'