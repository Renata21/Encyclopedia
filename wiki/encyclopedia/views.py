from cProfile import label
import markdown2
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from requests import HTTPError, get

from . import util

app_name = "encyclopedia"

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title of the page", widget=forms.TextInput(attrs={'name':'title', 'style':'width: 70%; margin: 10px; margin-left: 50px;'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'style':'width: 70%;  margin-left: 50px;', 'name':'content', 'rows':'3', 'cols':'5'}))

def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def get_page(request, title):
    if util.get_entry(title) is not None:
        content = markdown2.markdown(util.get_entry(title))
        return render(
            request, f"encyclopedia/entry.html", {"content": content, "title": title}
        )
    else:
        return HttpResponse("Error, page not found " + title)


def search_page(request):
    title = request.GET.get("q")
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


def create_page(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)

        if form.is_valid():    
            title = form.cleaned_data["title"]
            if title in util.list_entries():              
                return render(request, "encyclopedia/create_page.html", {"form":form, "error": True})
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return get_page(request, title)
        else:
            return render(request, "encyclopedia/create_page.html", {"form":form, "error": True})
    else:
        return render(request, "encyclopedia/create_page.html", {
            "form": NewEntryForm()
        })

def edit_page(request, title):
    
    return get_page(request, title)