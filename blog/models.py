import os
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    liked = models.ManyToManyField(User, related_name='like_post')
    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)

    def get_date(self):
        """ RETURN CREATED AT DATE AS STRING """
        time = datetime.now()
        if self.created_at.year == time.year:
            if self.created_at.month == time.month:
                if self.created_at.day == time.day:
                    if self.created_at.hour == time.hour:
                        if self.created_at.minute == time.minute:
                            return "just now"
                        else:
                            minute = time.minute - self.created_at.minute
                            if minute == 1:
                                return "one minute ago"
                            else:
                                return str(minute) + " " + "minutes ago"
                    else:
                        hour = time.hour - self.created_at.hour
                        if hour == 1:
                            return "one hour ago"
                        else:
                            return str(hour) + " " + "hours ago"
                else:
                    day = time.day - self.created_at.day
                    if day == 1:
                        return "yesterday"
                    else:
                        return str(day) + " " + "days ago"
            else:
                month = time.month - self.created_at.month
                if month == 1:
                    return "one month ago"
                else:
                    return str(month) + " " + "months ago"
        else:
            year = time.year - self.created_at.year
            if year == 1:
                return "last year"
            else:
                return str(year) + " " + "years ago"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_single', kwargs={'slug':self.slug})

    def like_num(self):
        return self.liked.count()

    class Meta:
        ordering = ['-last_update']


@receiver(models.signals.post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """ DELETE POST IMAGE AUTOMATICALLY FROM MEDIA AFTER DELETEING POST """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Post)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """ DELETE POST IMAGE AUTOMATICALLY FROM MEDIA AFTER UPDATING POST """
    if not instance.pk:
        return False
    try:
        old_file = Post.objects.get(pk=instance.pk).image
    except Post.DoesNotExist:
        return False
    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.user} liked {self.post}")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    user_commented = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField()

    class Meta:
        ordering = ['-commented_at']

    def __str__(self):
        return str(f"{self.user_commented} commented on {self.post}")
