from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
