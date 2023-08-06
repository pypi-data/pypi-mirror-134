import re
import logging

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from wagtailmenus.models import MainMenuItem, FlatMenuItem, FlatMenu
from wagtail.contrib.redirects.models import Redirect
from rest_framework import status

from .serializers import *


#
# ────────────────────────────────────────────────────────── I ──────────
#   :::::: M E N U   V I E W : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────
#


class MainMenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MainMenuItem.objects.all()
    serializer_class = MainMenuItemSerializer

    def get_serializer_context(self):
        context = super(MainMenuItemViewSet, self).get_serializer_context()
        context["request"] = self.request
        return context


class FlatMenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FlatMenu.objects.all()
    serializer_class = FlatMenuSerializer
    lookup_field = "handle"

    def get_serializer_context(self):
        context = super(FlatMenuViewSet, self).get_serializer_context()
        context["request"] = self.request
        return context


#
# ──────────────────────────────────────────────────────────────────────────── II ──────────
#   :::::: R E D I R E C T   P A G E   V I E W : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────────
#


class RedirectPageApiView(APIView):
    serializer_class = RedirectPageSerializer

    def get(self, request):
        path = self.request.query_params.get("path", None)
        try:
            path = path[:-1] if path[-1] == "/" else path
            regex = "^((http(s)?://)?{})?{}(/)?$".format(
                re.escape(self.request.site.hostname), re.escape(path)
            )
            queryset = Redirect.objects.filter(old_path__iregex=regex).first()
            serialize_data = self.serializer_class(queryset).data
            return Response(serialize_data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)