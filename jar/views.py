from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'jar/sorry_jar.html')


# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import SorryCount

def sorry_jar_view(request):
    # Get or create initial counts for Vika and Eskil
    vika_count, _ = SorryCount.objects.get_or_create(user="Vika")
    eskil_count, _ = SorryCount.objects.get_or_create(user="Eskil")
    
    # Pass counts to template
    context = {
        "vika_count": vika_count.count,
        "eskil_count": eskil_count.count,
    }
    return render(request, "jar/sorry_jar.html", context)

@csrf_exempt
def increment_sorry(request, user):
    # Update the sorry count for the specified user
    if request.method == "POST" and user in ["Vika", "Eskil"]:
        sorry_count, _ = SorryCount.objects.get_or_create(user=user)
        sorry_count.count += 1
        sorry_count.save()
        return JsonResponse({"success": True, "new_count": sorry_count.count})
    return JsonResponse({"success": False, "error": "Invalid user"})
