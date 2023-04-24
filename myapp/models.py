from django.db import models
from django.utils import timezone

class Timer(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    elapsed_time = models.DurationField(null=True, blank=True)

    def start(self):
        self.start_time = timezone.now()
        self.save()

    def pause(self):
        if self.start_time:
            self.end_time = timezone.now()
            self.elapsed_time = self.end_time - self.start_time
            self.save()

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        self.save()

    def save_time(self):
        if self.elapsed_time:
            SavedTime.objects.create(time=self.elapsed_time)

class SavedTime(models.Model): time = models.DurationField()