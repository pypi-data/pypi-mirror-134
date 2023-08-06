from rest_framework import serializers
from wagtailmenus.conf import settings
from wagtail.core.models import Page
from wagtailmenus.models import MainMenuItem, FlatMenuItem
from wagtail.contrib.redirects.models import Redirect

import logging

logger = logging.getLogger()


class MenuPageChildSerializer(serializers.ModelSerializer):
    label = serializers.ReadOnlyField(source="title")
    link = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    menu_brief = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_link(self, model):
        return model.specific.get_url()

    def get_children(self, model):
        children = Page.objects.child_of(model).filter(show_in_menus=True)
        return MenuPageChildSerializer(children, many=True).data

    def get_menu_brief(self, model):

        if hasattr(model.specific, "menu_brief"):
            return model.specific.menu_brief
        else:
            return None

    def get_image(self, model):

        if hasattr(model.specific, "image") and model.specific.image:
            image_url = model.specific.image.get_rendition(
                "fill-551x551|jpegquality-60"
            ).url
            return {"url": image_url}
        return None

    class Meta:
        model = Page
        fields = ("id", "label", "link", "children", "menu_brief", "image")


class MainMenuItemSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    num_of_child = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    def get_label(self, model):
        return model.link_text or model.link_page.title

    def get_link(self, model):

        return model.link_url or model.link_page.specific.get_url(
            self.context["request"]
        )

    def get_num_of_child(self, model):
        try:
            count = (
                Page.objects.child_of(model.link_page)
                .filter(show_in_menus=True)
                .count()
            )
        except Exception:
            count = 0
        return count

    def get_children(self, model):
        if model.allow_subnav and model.link_page:
            children = Page.objects.child_of(model.link_page).filter(show_in_menus=True)
            return MenuPageChildSerializer(children, many=True).data
        else:
            return []

    class Meta:
        model = MainMenuItem
        fields = (
            "id",
            "link",
            "url_append",
            "handle",
            "label",
            "num_of_child",
            "children",
        )


class FlatMenuItemSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, model):
        return model.link_url or model.link_page.get_url(self.context["request"])

    class Meta:
        model = FlatMenuItem
        fields = ("id", "link", "url_append", "handle", "link_text")


class FlatMenuSerializer(serializers.ModelSerializer):
    menu_items = serializers.SerializerMethodField()

    def get_menu_items(self, instance):
        flat_menu_items = getattr(instance, settings.FLAT_MENU_ITEMS_RELATED_NAME).all()
        return FlatMenuItemSerializer(
            flat_menu_items, context=self.context, many=True
        ).data

    class Meta:
        model = None
        fields = "__all__"


class RedirectPageSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, model):
        if model.redirect_page:
            return {"type": "internal", "link": model.redirect_page.url}
        elif model.redirect_link:
            return {"type": "external", "link": model.redirect_link}
        return None

    class Meta:
        model = Redirect
        fields = ("is_permanent", "link")
