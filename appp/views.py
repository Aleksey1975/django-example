from django.shortcuts import render, redirect

from django.http import (
    HttpResponse, HttpResponseNotFound, Http404,
    HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

def test(r):
    return HttpResponse('Test')

