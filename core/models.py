from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class News(TimeStampedModel):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    body = models.TextField()
    image_url = models.URLField(blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    class Meta:
        ordering = ["-published_at", "-created_at"]
    def __str__(self): return self.title

class Diet(TimeStampedModel):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    calories_per_day = models.PositiveIntegerField(null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    class Meta:
        ordering = ["name"]
    def __str__(self): return self.name

class Podcast(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    audio_url = models.URLField()
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    class Meta:
        ordering = ["-published_at", "-created_at"]
    def __str__(self): return self.title

class Paper(TimeStampedModel):
    TYPE_DATA = "data"
    TYPE_JOURNAL = "journal"
    TYPE_CHOICES = [(TYPE_DATA, "Data"), (TYPE_JOURNAL, "Journal")]
    title = models.CharField(max_length=250)
    paper_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source_name = models.CharField(max_length=120, blank=True)
    link_url = models.URLField(blank=True)
    abstract = models.TextField(blank=True)
    published_at = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ["-published_at", "-created_at"]
    def __str__(self): return f"{self.title} ({self.paper_type})"

class About(TimeStampedModel):
    heading = models.CharField(max_length=200, default="About us")
    body = models.TextField()
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=40, blank=True)
    class Meta:
        verbose_name_plural = "About"
        ordering = ["-updated_at"]
    def __str__(self): return self.heading
