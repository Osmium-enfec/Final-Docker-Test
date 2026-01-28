from django.http import JsonResponse

def greet(request):
    name = request.GET.get('name', 'World')
    return JsonResponse({'greeting': f'Hello, {name}!'})
