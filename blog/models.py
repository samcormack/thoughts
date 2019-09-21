from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index


class BlogIndexPage(Page):
    content_panels = Page.content_panels

    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogPage']


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('text', blocks.RichTextBlock()),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []