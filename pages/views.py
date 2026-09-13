from django.shortcuts import render
from django.http import Http404

COMPONENTS = [
    {"slug": "button", "label": "Button", "category": "General"},
    {"slug": "badge", "label": "Badge", "category": "General"},
    {"slug": "alert", "label": "Alert", "category": "Feedback"},
    {"slug": "card", "label": "Card", "category": "Layout"},
    {"slug": "separator", "label": "Separator", "category": "Layout"},
    {"slug": "table", "label": "Table", "category": "Layout"},
    {"slug": "tabs", "label": "Tabs", "category": "Navigation"},
    {"slug": "dropdown", "label": "Dropdown", "category": "Navigation"},
    {"slug": "modal", "label": "Modal", "category": "Overlay"},
    {"slug": "toast", "label": "Toast", "category": "Feedback"},
    {"slug": "input", "label": "Input", "category": "Form"},
    {"slug": "textarea", "label": "Textarea", "category": "Form"},
    {"slug": "select", "label": "Select", "category": "Form"},
    {"slug": "checkbox", "label": "Checkbox", "category": "Form"},
    {"slug": "radio", "label": "Radio", "category": "Form"},
]

ROLE_CHOICES = [
    ("admin", "Admin"),
    ("editor", "Editor"),
    ("viewer", "Viewer"),
]


def getting_started(request):
    return render(request, "pages/getting-started.html", {"components": COMPONENTS})


def blocks(request):
    return render(request, "pages/blocks.html", {"components": COMPONENTS})


def htmx(request):
    return render(request, "pages/htmx.html", {"components": COMPONENTS})


def home(request):
    return render(request, "pages/home.html", {"components": COMPONENTS})


def component(request, component):
    match = next((c for c in COMPONENTS if c["slug"] == component), None)
    if not match:
        raise Http404
    return render(request, f"pages/components/{component}.html", {
        "components": COMPONENTS,
        "current": match,
        "role_choices": ROLE_CHOICES,
    })
