import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError



class Journal(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField('date published', null=True, blank=True)
    last_edited = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True, null=True)

    def is_published(self):
        return self.published

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title

    def clean(self):
        # overriding clean to provide some of my own validations, called when
        # full_clean is called
        if len(self.title) < 1 or len(self.content) < 1:
            raise ValidationError("Title and Content must be filled out")

    def save(self, *args, **kwargs):
        # full_clean is never called, so here i must override the save method
        # and call a full_clean myself, and then save. Otherwise, invalid form
        # data will slide through without errors, full_clean() will run my
        # clean method
        self.full_clean()
        super(Journal, self).save(*args, **kwargs)
