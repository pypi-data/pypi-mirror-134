import re
import logging
from django.urls import reverse
from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock as DefaultDocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock as DefaultImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock as CoreSnippetChooserBlock
from .utils import prepare_richtext_for_api
from django.core.validators import validate_unicode_slug
from django.utils.functional import cached_property
from django import forms
from wagtail.core.blocks.struct_block import StructBlockAdapter
from wagtail.core.telepath import register
logger = logging.getLogger()


class SnippetChooserBlock(CoreSnippetChooserBlock):
    def __init__(self, target_model, serializer=None, **kwargs):
        super().__init__(target_model, **kwargs)
        self.serializer = serializer

    def get_api_representation(self, value, context=None):
        if value:
            if self.serializer:
                self.serializer.Meta.model = self.target_model
                return self.serializer(value, context=context).data
            else:
                return self.get_prep_value(value)

    class Meta:
        icon = "snippet"


class DocumentChooserBlock(DefaultDocumentChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "name": value.title,
                "url": value.url,
                "view": reverse("serve-document", args=[value.id, value.filename]),
            }


class ImageChooserBlock(DefaultImageChooserBlock):
    def to_python(self, value):
        if value is None:
            return value
        else:
            try:
                return self.target_model.objects.filter(pk=value).prefetch_related('renditions').first()
            except self.target_model.DoesNotExist:
                return None

    def get_api_representation(self, value, context=None):
        if value:
            data = {
                "id": value.id,
                "title": value.title,
                "original": value.get_rendition("original").attrs_dict,
            }
            rules = getattr(self.meta, "rendition_rules", False)
            if rules:
                for name, rule in rules.items():
                    data[name] = value.get_rendition(rule).attrs_dict
            return data


class RichTextBlock(blocks.RichTextBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return prepare_richtext_for_api(value.source)
        else:
            return ""


class PageChooserBlock(blocks.PageChooserBlock):
    def to_python(self, value):

        if value is None:
            return value
        else:
            try:
                return (
                    self.target_model.objects.filter(pk=value)
                    .only("id", "title", "slug")
                    .first()
                )
            except self.target_model.DoesNotExist:
                return None

    def bulk_to_python(self, values):
        """Return the model instances for the given list of primary keys.
        The instances must be returned in the same order as the values and keep None values.
        """

        objects = self.target_model.objects.only("id", "title", "slug").in_bulk(values)
        return [objects.get(id) for id in values]
    
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "id": value.id,
                "link": value.get_url(context["request"]),
                "title": value.title,
            }


class PageOrLinkBlock(blocks.StreamBlock):
    page = PageChooserBlock(max_num=1)
    link = blocks.URLBlock(max_num=1)

    class Meta:
        max_num = 1
        icon = "link"

    def get_api_representation(self, value, context=None):
        try:
            val = value[0]
            link = (
                val.value.get_url(context["request"])
                if val.block_type == "page"
                else val.value
            )
            return {"type": val.block_type, "link": link}
        except Exception:
            return {"type": None, "link": None}


class CallToActionBlock(blocks.StructBlock):
    link = PageChooserBlock()
    anchor = blocks.CharBlock(required=False)

    class Meta:
        icon = "link"


YOUTUBE_REGEX = (
    r"^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*"
)


class YoutubeVideoBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    url = blocks.RegexBlock(
        regex=YOUTUBE_REGEX, error_messages={
            "invalid": "Not a valid youtube URL"}
    )

    def get_api_representation(self, value, context=None):
        if value:
            value["video_id"] = re.match(YOUTUBE_REGEX, value["url"]).group(7)
            return value

    class Meta:
        icon = "media"


"""
..######..########.########..##.....##..######..########....########..##........#######...######..##....##..######.
.##....##....##....##.....##.##.....##.##....##....##.......##.....##.##.......##.....##.##....##.##...##..##....##
.##..........##....##.....##.##.....##.##..........##.......##.....##.##.......##.....##.##.......##..##...##......
..######.....##....########..##.....##.##..........##.......########..##.......##.....##.##.......#####.....######.
.......##....##....##...##...##.....##.##..........##.......##.....##.##.......##.....##.##.......##..##.........##
.##....##....##....##....##..##.....##.##....##....##.......##.....##.##.......##.....##.##....##.##...##..##....##
..######.....##....##.....##..#######...######.....##.......########..########..#######...######..##....##..######.
"""

class BlockPanel:
    def __init__(self, handle, fields, label="", classnames=""):
        self.handle = handle
        self.fields = fields
        self.label = label or handle
        self.classnames = classnames

    def js_args(self):
        return {
            "handle": self.handle,
            "label": self.label,
            "classnames": self.classnames,
            "fields": [field.js_args() for field in self.fields],
        }


class BlockField:
    def __init__(self, field, classnames="", hide_label=False):
        self.field = field
        self.classnames = classnames
        self.hide_label = hide_label

    def js_args(self):
        return {
            "field": self.field,
            "classnames": self.classnames,
            "hide_label": self.hide_label,
        }


class TabbedStructBlock(blocks.StructBlock):
    MUTABLE_META_ATTRIBUTES = ["panels"]
    class Meta:
        panels = []
        
class TabbedStructBlockAdapter(StructBlockAdapter):
    js_constructor = "pages.blocks.TabbedStructBlock"

    def js_args(self, block):
        args = super().js_args(block)
        args[-1]["panels"] = [panel.js_args() for panel in block.meta.panels]

        return args

    @cached_property
    def media(self):
        struct_block_media = super().media
        return forms.Media(
            js=struct_block_media._js + ["wagtailutils/js/tabbed_struct.js"],
            css={
                "all": [
                    "https://cdnjs.cloudflare.com/ajax/libs/gridlex/2.7.1/gridlex.min.css",
                    "wagtailutils/css/tabbed_struct.css",
                ]
            },
        )

register(TabbedStructBlockAdapter(), TabbedStructBlock)