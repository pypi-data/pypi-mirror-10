# -#- coding: utf-8 -#-

from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from elephantblog.models import Entry
from leonardo.module.web.models import Widget


class RecentBlogPostsWidget(Widget):
    post_count = models.PositiveIntegerField(
        verbose_name=_("post count"), default=3)
    show_button = models.BooleanField(
        default=True, verbose_name=_("show link button"))

    def get_last_posts(self):
        return Entry.objects.all().order_by('-published_on')[:self.post_count]

    def get_all_posts(self):
        return Entry.objects.filter(published_on__in=[50, 60]).order_by('-published_on')

    class Meta:
        abstract = True
        verbose_name = _("recent blog posts")
        verbose_name_plural = _("recent blog posts")
