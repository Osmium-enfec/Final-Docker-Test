from django.http import JsonResponse

def greet(request):
    # TODO: implement this function
    return JsonResponse({'greeting': 'Hello, World!'})
