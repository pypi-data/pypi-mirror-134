from collections import OrderedDict

from rest_framework.fields import Field
from wagtail.images.models import SourceImageIOError


class ImageRenditionField(Field):

    def __init__(self, filter_specs, *args, cache_renditions=False, **kwargs):
        self.filter_specs = filter_specs or {"original": "original"}
        self.cache_renditions = cache_renditions
        super().__init__(*args, **kwargs)

    def to_representation(self, image):
        if self.cache_renditions:
            image = image.__class__.objects.filter(
                pk=image.pk).prefetch_related("renditions").first()
        try:
            data = OrderedDict([])
            for name, rule in self.filter_specs.items():
                thumbnail = image.get_rendition(rule)
                data[name] = thumbnail.attrs_dict
            return data
        except SourceImageIOError:
            return OrderedDict(
                [
                    ("error", "SourceImageIOError"),
                ]
            )
