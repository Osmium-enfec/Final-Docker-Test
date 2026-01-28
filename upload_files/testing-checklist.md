# Testing Your Solution Checklist

## Before Submitting, Verify:

### ✓ Function Definition
- [ ] Function is named `greet`
- [ ] Function accepts `request` parameter
- [ ] Function is in `views.py`

### ✓ Query Parameter Handling
- [ ] Code reads the 'name' query parameter
- [ ] Default value is 'World' when name is not provided
- [ ] Parameter is accessed using `request.GET.get()`

### ✓ Response Format
- [ ] Returns JSON response
- [ ] JSON contains key 'greeting'
- [ ] Uses f-string or format: `f"Hello, {name}!"`

### ✓ Test Cases
Test your function locally:

```bash
# Test with name parameter
curl "http://localhost:8000/?name=Alice"
# Expected: {"greeting": "Hello, Alice!"}

# Test without name parameter
curl "http://localhost:8000/"
# Expected: {"greeting": "Hello, World!"}

# Test with different names
curl "http://localhost:8000/?name=Bob"
# Expected: {"greeting": "Hello, Bob!"}
```

### ✓ Common Issues
- ❌ Function returns string instead of JSON → Use `JsonResponse`
- ❌ Wrong key in JSON → Use 'greeting' not 'greet'
- ❌ No default value → Add `'World'` as second parameter in `.get()`
- ❌ Hard-coded name → Use `request.GET.get()` to get parameter
