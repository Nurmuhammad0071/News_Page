from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    eamil = models.EmailField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class New(models.Model):
    STATUS = (
        ('active', "Active"),
        ('noactive', "NoActive")
    )
    title = models.CharField(max_length=250)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='news')
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Yangliklar"

    def __str__(self):
        return self.title

    object = models.Manager()
