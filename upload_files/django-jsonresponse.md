# Django JsonResponse Tutorial

## What is JsonResponse?

`JsonResponse` is a Django class that returns JSON data with the correct content-type header.

### Syntax
```python
from django.http import JsonResponse

response = JsonResponse({'key': 'value'})
```

### Basic Example
```python
def greet(request):
    data = {
        'greeting': 'Hello, World!',
        'status': 'success'
    }
    return JsonResponse(data)
```

### Response Headers
When using `JsonResponse`, Django automatically sets:
- `Content-Type: application/json`
- HTTP Status: 200 OK

### Status Codes
```python
# Success
JsonResponse({'result': 'ok'})  # HTTP 200

# Not Found
JsonResponse({'error': 'Not found'}, status=404)

# Bad Request
JsonResponse({'error': 'Invalid input'}, status=400)
```

### Common Mistakes
❌ Wrong: `return {'greeting': 'Hello'}`  
✓ Correct: `return JsonResponse({'greeting': 'Hello'})`
