from django.db import models
from django.utils import timezone
import re
from django.core.exceptions import ValidationError
# Create your models here.




def no_special_chars_validator(value):
    if re.search(r'[^А-я0-9A-z]', value):
        raise ValidationError("Заголовок не должен содержать спецсимволы или теги.")

def validate_max_length(value):
    if len(value) > 200:
        raise ValidationError("Заголовок не должен превышать 200 символов.")

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False,
                             validators=[no_special_chars_validator, validate_max_length])
    content = models.TextField(max_length=5000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author
