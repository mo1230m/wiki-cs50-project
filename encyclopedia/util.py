import re
from markdown2 import Markdown
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django import forms

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        data = f.read()
        markdowner = Markdown()
        html = markdowner.convert(data)
        return html
    except FileNotFoundError:
        return None

class entryForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'title_box'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'content_box'}))


# def MD_to_HTML(title):
#     replacements = [
#         ('^#\s+(.*)', '<h1>\\1</h1>'), # H1
#         ('^##\s+(.*)', '<h2>\\1</h2>'), # H2
#         ('^###\s+(.*)', '<h3>\\1</h3>'), # H3
#         ('^####\s+(.*)', '<h4>\\1</h4>'), # H4
#         ('^#####\s+(.*)', '<h5>\\1</h5>'), # H5
#         ('^######\s+(.*)', '<h6>\\1</h6>'), # H6
#         ('\[(.*?)\]\((.*?)\)', '<a href="\\2">\\1</a>') # links
#     ]
#     with open(f"entries/{title}.md") as f:
#         data = f.read()
#         for pat, repl in replacements:
#             data = re.sub(pat, repl, data)