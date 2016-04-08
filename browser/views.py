from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Gtin, Nutrition, Brand, Brand_owner, Search

# import for REST

from browser.serializers import GtinSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests

# --------------------------------------------------------------------
#  WEBSITE BROWSER
# --------------------------------------------------------------------


def search_gtin(request):
    if Search.objects.filter(pk=request.POST['gtin']).exists():
        search_gtin = Search.objects.get(pk=request.POST['gtin'])
        search_gtin.SEARCH_NB += 1
        search_gtin.save()
    else:
        new_entry = Search(GTIN_CD = request.POST['gtin'], SEARCH_NB = 1)
        new_entry.save()

    try:
        if request.POST['gtin']:
            gtin = Gtin.objects.get(pk=request.POST['gtin'])
    except (KeyError, Gtin.DoesNotExist):
        return render(request, 'browser/home.html', {
            'error_message': "This GTIN is not in the database",
        })
    else:
        return HttpResponseRedirect(reverse('browser:gtin', args=(gtin,)))

class ViewGtin(generic.DetailView):
    template_name = 'browser/gtin.html'
    model = Gtin

    queryset = Gtin.objects.all()

    def get_object(self):
        object = super(ViewGtin, self).get_object()
        if object.GTIN_CD and object.GTIN_CD[0:1] == "0":
            object.UPC_CD = object.GTIN_CD[1:12]
        object.save()
        return object

class ViewBrandList(generic.ListView):
    template_name = 'browser/brand_list.html'
    context_object_name = 'page_brand_list'
    model = Brand

    def get_context_data(self, **kwargs):
        context = super(ViewBrandList, self).get_context_data(**kwargs)
        context.update({
            'page_id': self.kwargs['page_id'],
        })
        return context

    def get_queryset(self):
        page_id = 'A'
        page_id = self.kwargs['page_id']
        return Brand.objects.filter(BRAND_NM__istartswith=page_id).order_by('BRAND_NM')

class ViewBsin(generic.ListView):
    template_name = 'browser/bsin.html'
    context_object_name = 'gtin_list'
    model = Gtin

    def get_context_data(self, **kwargs):
        context = super(ViewBsin, self).get_context_data(**kwargs)
        context.update({
            'bsin_detail': Brand.objects.get(pk=self.kwargs['bsin']),
        })
        return context

    def get_queryset(self):
        bsin = self.kwargs['bsin']
        return Gtin.objects.filter(BSIN=bsin).order_by('PRODUCT_LINE','PKG_UNIT','GTIN_NM')

class ViewOwnerList(generic.ListView):
    template_name = 'browser/brand_owner_list.html'
    context_object_name = 'owner_list'
    model = Brand_owner

    def get_queryset(self):
        """Return the last five published questions."""
        return Brand_owner.objects.order_by('OWNER_NM')

class ViewOwner(generic.ListView):
    template_name = 'browser/brand_owner.html'
    context_object_name = 'brand_list'
    model = Brand

    def get_context_data(self, **kwargs):
        context = super(ViewOwner, self).get_context_data(**kwargs)
        context.update({
            'owner_detail': Brand_owner.objects.get(pk=self.kwargs['owner']),
        })
        return context

    def get_queryset(self):
        """Return the last five published questions."""
        owner = self.kwargs['owner']
        return Brand.objects.filter(OWNER_CD=owner).order_by('BRAND_NM')

# --------------------------------------------------------------------
#   REST API DRF
# --------------------------------------------------------------------

# gtin for test : 0836093401314    0857063002652

class RestViewGtinDetail(APIView):
    def get_object(self, pk):
        try:
            return Gtin.objects.get(pk=pk)
        except Gtin.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        gtin = self.get_object(pk)
        serializer = GtinSerializer(gtin)
        return Response(serializer.data)
