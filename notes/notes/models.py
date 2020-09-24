from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def niceCreated(self):
        return self.created_at.strftime("Created on %A at %I:%M %p %z")

    def niceUpdated(self):
        return self.updated_at.strftime("Last updated on %A at %I:%M %p %z")

    def __str__(self):
        return f"{self.title}"
