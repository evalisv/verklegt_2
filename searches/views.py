from django.shortcuts import render
from .models import SearchQuery
from estate.models import Estate
from django.core.paginator import Paginator
from django.db.models import Q

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {'query': query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        lookup = (Q(address__icontains=query) |
                  Q(description__icontains=query) |
                  Q(postal_code__postal_code__icontains=query) |
                  Q(postal_code__municipality__icontains=query))
        estates = Estate.objects.all().filter(lookup)

        #paginator = Paginator(estates, 6)
        #page = request.GET.get("page")
        #estates = paginator.get_page(page)

        context['estates'] = estates
        print(context)
    return render(request, 'search/search_results.html', context)

def view_search_words(request, id):
    filtered_search_query = SearchQuery.objects.filter(user_id=request.user).order_by('-timestamp')
    context = {'searches': filtered_search_query}
    return render(request, 'search/search_words.html', context)

def search_history(request, id):
    return render(request, 'search/search_history.html')