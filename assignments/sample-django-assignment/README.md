# Django View Assignment

## Task
Implement a Django view function named `greet` in `views.py` that returns a JSON response `{ "greeting": "Hello, <name>!" }` where `<name>` is a query parameter. If no name is provided, default to `World`.

## Example
- GET /?name=Alice → { "greeting": "Hello, Alice!" }
- GET /           → { "greeting": "Hello, World!" }
