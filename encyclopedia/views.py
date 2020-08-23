from markdown2 import markdown_path
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    html = util.get_entry(entry)
    if not html:
        return render(request, "encyclopedia/404.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": entry,
            "content": html
        })


# Create new wiki entry
def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if title in util.list_entries():
            return render(request, "encyclopedia/404.html")
        else:
            with open(f"entries/{title}.md", 'w') as f:
                f.write(content)
            return redirect('entry', entry=title)

    return render(request, "encyclopedia/new.html", {
        "form": util.entryForm()
    })


# Search for an existing entry
def search(request):
    if request.method == "POST":
        query = request.POST["q"]
        if util.get_entry(query) is not None:
            return redirect('entry', entry=query)
        else:
            found = []
            for filename in util.list_entries():
                if query.lower() in filename.lower():
                    found.append(filename)
            return render(request, "encyclopedia/search.html", {
                "results": found,
                "title": query
            })

def edit(request, title):
    if request.method == "POST":
        util.save_entry(request.POST["title"], request.POST["content"])
        return redirect('entry', entry=title)


    data = open(f'entries/{title}.md', 'r')
    data = data.read()
    form = util.entryForm({'title': title, 'content': data})
    return render(request, "encyclopedia/edit.html", {
        "form": form
    })

def random_page(request):
    entries = util.list_entries()
    page = random.choice(entries)
    return redirect('entry', entry=page)