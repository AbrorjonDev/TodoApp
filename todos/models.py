from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

process_status = [
    ('completed', 'completed'),
    ('not completed', 'not completed'),
    ('missed', 'missed')
]

class Todos(models.Model):

    todo = models.CharField(max_length=300, null=False)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=process_status, default='not completed')
    publish_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    slug = models.SlugField(max_length=300, null=False, unique=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.todo)
        return super(Todos, self).save(*args, **kwargs)

    def __str__(self):
        return self.todo

    def get_absolute_url(self):
        return reverse("todos")
    


@receiver(pre_save, sender=Todos)
def todo_save(sender, instance,*args, **kwargs):
    instance.slug = slugify(instance.todo)
    

