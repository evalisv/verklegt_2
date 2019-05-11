from django.shortcuts import render
from .models import SearchQuery
from estate.models import Estate

# Create your views here.
def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {'query': query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        estates = Estate.objects.all().filter(address__icontains=query)
        context['estates'] = estates
    return render(request, 'search/search_results.html', context)


