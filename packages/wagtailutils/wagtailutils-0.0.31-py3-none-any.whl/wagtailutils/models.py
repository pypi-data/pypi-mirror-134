from django_json_widget.widgets import JSONEditorWidget
from django.db import models

from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _
from wagtail.snippets.models import register_snippet

from wagtail.contrib.settings.models import BaseSetting
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

#
# ──────────────────────────────────────────────────────── I ──────────
#   :::::: S E T T I N G S : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────
#


class GlobalSettings(BaseSetting):
    default_og_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        blank=True,
        null=True,
    )
    address = RichTextField(blank=True, default="")
    google_map_key = models.CharField(
        _("Google Map API Key"), max_length=250, blank=True, null=True
    )
    map_style = models.JSONField(blank=True, default=list)
    copyright_text = models.CharField(
        _("Copyright Text"), max_length=350, blank=True, null=True
    )

    panels = [
        ImageChooserPanel("default_og_image"),
        MultiFieldPanel(
            [
                FieldPanel("google_map_key"),
                FieldPanel("map_style"),
            ],
            heading="Map",
        ),
        MultiFieldPanel(
            [FieldPanel("address"), FieldPanel("copyright_text")],
            heading="Footer Address",
        ),
    ]

    class Meta:
        abstract = True


class SocialMediaSettings(BaseSetting):
    facebook_url = models.CharField(
        max_length=255, null=True, blank=True, help_text="Facebook URL"
    )

    twitter_url = models.CharField(
        max_length=255, null=True, blank=True, help_text="Twitter URL"
    )

    linkedin_url = models.CharField(
        max_length=255, null=True, blank=True, help_text="Linkedin URL"
    )

    pinterest_url = models.CharField(
        max_length=255, null=True, blank=True, help_text="Pinterest URL"
    )

    instagram_url = models.CharField(
        max_length=255, null=True, blank=True, help_text="Instagram URL"
    )

    panels = [
        FieldPanel("facebook_url"),
        FieldPanel("twitter_url"),
        FieldPanel("linkedin_url"),
        FieldPanel("pinterest_url"),
        FieldPanel("instagram_url"),
    ]

    class Meta:
        abstract = True


class AnalyticsSettings(BaseSetting):
    google_analytics_id = models.CharField(
        max_length=255, null=True, blank=True, help_text="Google Analytics ID"
    )

    gtm_head_element = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="Google Tag Manager Head Script",
    )
    gtm_body_element = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="Google Tag Manager Body Script",
    )

    panels = [
        FieldPanel("google_analytics_id"),
        MultiFieldPanel(
            [FieldPanel("gtm_head_element"), FieldPanel("gtm_body_element")],
            heading="Google Tag Manager",
        ),
    ]

    class Meta:
        abstract = True


@register_snippet
class StructDataSnippet(models.Model):
    snippet = models.JSONField()
    for_all = models.BooleanField(default=False)

    panels = [
        FieldPanel("snippet", widget=JSONEditorWidget),
        FieldPanel("for_all"),
    ]
