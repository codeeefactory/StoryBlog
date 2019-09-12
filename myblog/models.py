# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from django.conf import settings
from django.utils import timezone
import django.contrib.auth.models
class story(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='nevisandeh')
    email = models.EmailField(default="example@example.com")
    title1 = models.CharField("oonvan dastan", max_length=50)
    matn = RichTextUploadingField(_('matn'), config_name='default')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title1 + "<br>" + self.matn

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class META():
        verbose_name = _('story')
        verbose_name_plural = _('stories')
# Create your models here.
