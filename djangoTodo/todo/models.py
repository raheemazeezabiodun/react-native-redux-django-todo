from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo
