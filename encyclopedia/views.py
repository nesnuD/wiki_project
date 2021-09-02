from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    page_info = util.get_entry(title)
    return render(request, "encyclopedia/title.html", {
        "info" : page_info,
        "title" : title,  
    })