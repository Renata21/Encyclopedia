from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
import markdown2
from requests import get

from . import util

app_name = "encyclopedia"


def index(request):
    return render(request, "encyclopedia/index.html", 
    {"entries": util.list_entries()})


def get_page(request, title):
    if util.get_entry(title) is not None:
        content = markdown2.markdown(util.get_entry(title))
        return render(
            request, f"encyclopedia/entry.html", 
            {"content": content, "title": title}
        )
    else:
        return HttpResponse("Error, page not found " + title)


def search_page(request):
    title = request.GET.get('q')
    list_res = []
    if title in util.list_entries():
        return get_page(request, title)
    else:
        for element in util.list_entries():
            if title.lower() in element.lower():
                list_res.append(element)
        return render(
            request,
            f"encyclopedia/search_res.html",
            {"entries": list_res, "title": title},
        )
