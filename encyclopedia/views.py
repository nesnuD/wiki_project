from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from encyclopedia.forms import SearchForm
from django.shortcuts import render
from . import util
import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_page(request, title):
    page_info = util.get_entry(title)
    if show_page is None:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/title.html", {
        "info" : page_info,
        "title" : title,  
    })


def search_encyclopedia(request):
    if request.method =="GET":
        searched = request.GET['q']
        entries = util.get_entry(searched)
        if searched == entries:
            return render(request, "encyclopedia/search-page.html", {
                "searched" : searched,
                "entry" : searched 
            })
        else:
            entries = util.list_entries()
            result = ["Nothing Found!"]
            test = "this is a test"
            searched = request.GET['q']
            for entry in entries:
                if searched.lower() in entry.lower():
                    result = entry
            return render(request, "encyclopedia/search-page.html", {
                "entry" : result, 
                "searched" : searched 
            })


