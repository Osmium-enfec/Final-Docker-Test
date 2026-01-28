# Python F-String Formatting

## What are F-Strings?

F-strings (formatted string literals) allow you to embed expressions inside string literals.

### Syntax
```python
name = "Alice"
message = f"Hello, {name}!"
print(message)  # Output: Hello, Alice!
```

### Examples
```python
# Simple variable insertion
name = "Bob"
greeting = f"Hello, {name}!"

# Expression evaluation
age = 25
message = f"Next year I'll be {age + 1}"

# Method calls
text = "hello"
formatted = f"{text.upper()}"  # "HELLO"

# Multiple variables
first = "John"
last = "Doe"
full_name = f"{first} {last}"
```

### For This Assignment
```python
def greet(request):
    name = request.GET.get('name', 'World')
    # Using f-string to create greeting
    greeting = f"Hello, {name}!"
    return JsonResponse({'greeting': greeting})
```

### Common Patterns
- `f"{variable}"` - Insert variable
- `f"{expression}"` - Evaluate expression
- `f"{variable:format}"` - Format number/date
