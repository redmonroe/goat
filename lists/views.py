from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render

# Create your views here.
def home_page(request):
     return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''), # .get supplies a default value of empty string
    })
    # return HttpResponse('<html><title>To-Do lists</title><html>')
