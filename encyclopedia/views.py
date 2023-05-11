from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django import forms

import random
from markdown2 import markdown

from . import util


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), label="Content")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    # Get the content of the entry
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html")
    content = content.split('\n', 1)[1]

    # Convert the Markdown content to HTML
    html_content = markdown(content)

    context = {
        'title': title,
        'content': html_content
    }

    return render(request, "encyclopedia/entry.html", context)


def search(request):
    query = request.GET.get('q', '')
    entry = util.get_entry(query)

    if entry is not None:
        return redirect('entry', title=query)
    else:
        entries = util.list_entries()
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()]

        return render(request, "encyclopedia/search_results.html", {
            "query": query,
            "entries": matching_entries
        })
    

def new_page(request, message=None, category=None):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                return redirect('new_page_with_message', message="Page already exists", category="danger")
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=[title]))
    else:
        form = NewEntryForm()

    return render(request, "encyclopedia/new_page.html", {
        "form": form,
        "message": message,
        "category": category,
    })


def edit_page(request, title):
    # Get the content of the entry with the given title
    content = util.get_entry(title)

    if request.method == "POST":
        # Get the new content of the entry from the form
        new_content = request.POST["content"]
        
        # Save the new content to the file
        util.save_entry(title, new_content)
        
        # Redirect to the edited entry's page
        return HttpResponseRedirect(reverse("entry", args=[title]))
    
    # Render the edit page template with the current content of the entry
    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content": content
    })


def random_page(request):
    # get a list of all available encyclopedia entries
    entries = util.list_entries()
    
    # choose a random entry from the list
    random_entry = random.choice(entries)
    
    # redirect to the page of the random entry
    return redirect('entry', title=random_entry)