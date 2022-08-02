from django.http import HttpResponse
from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request, title):
    if util.get_entry(title) is not None:
        content = markdown2.markdown(util.get_entry(title))
        return render(request, f"encyclopedia/entry.html",
        {
            "content":content,
            "title":title
        })
    else:
        return HttpResponse("Error, page not found")