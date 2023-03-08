from django.db import models


class Schema(models.Model):
    """ Schema Model """
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, blank=False)

    def __str__(self):
        """ String representation """
        return self.name

    class Meta:
        """ Representation in admin panel """
        verbose_name = 'Schema'
        verbose_name_plural = 'Schemas'
