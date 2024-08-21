from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'tasks_tasks'

    def __str__(self):
        return self.title