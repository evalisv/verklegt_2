from django.shortcuts import render
from .models import SearchQuery
from estate.models import Estate
from django.core.paginator import Paginator
from django.db.models import Q


def search_view(request):
    query = request.GET.get('q', None)
    pnrhofud = request.GET.getlist('postal-hofudborgarsvaedid')
    pnrvestur = request.GET.getlist('postal-vesturland')
    pnrnordvesturland = request.GET.getlist('postal - nordvesturland')
    typel = request.GET.getlist('type1')
    fjolbyli = request.GET.getlist('Fjölbýlishús')


    pnr_arr = []
    type_arr = []
    einbyli = ''
    for i in typel:
        type_arr.append(i)

    for i in type_arr:
        print(i)


    for i in pnrhofud:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

    for i in pnrvestur:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

    for i in pnrvestur:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

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

        estates = Estate.objects.all().filter(postal_code__postal_code__in=pnr_arr)\
                                      .filter(estate__estatetype__type__in=type_arr).filter(lookup)

        #paginator = Paginator(estates, 6)
       # page = request.GET.get("page")
       # estates = paginator.get_page(page)

        context['estates'] = estates
        print(context)
    return render(request, 'search/search_results.html', context)

def view_search_words(request):
    filtered_search_query = SearchQuery.objects.filter(user_id=request.user).order_by('-timestamp')
    context = {'searches': filtered_search_query}
    return render(request, 'search/search_words.html', context)

def search_history(request):
    return render(request, 'search/search_history.html')