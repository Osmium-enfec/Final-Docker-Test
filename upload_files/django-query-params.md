# Django HttpRequest Query Parameters Guide

## Accessing Query Parameters

In Django, query parameters from the URL are accessed via `request.GET`.

### Syntax
```python
value = request.GET.get('parameter_name', 'default_value')
```

### Example
```python
from django.http import JsonResponse

def greet(request):
    # Get 'name' parameter, default to 'World'
    name = request.GET.get('name', 'World')
    return JsonResponse({'greeting': f'Hello, {name}!'})
```

### URL Examples
- `/greet/?name=Alice` → name = 'Alice'
- `/greet/` → name = 'World' (default)
- `/greet/?name=Bob&age=30` → name = 'Bob' (age ignored in this example)

### Key Points
- `request.GET` is a dictionary-like object
- Use `.get()` to safely retrieve values
- Always provide a default value to handle missing parameters
