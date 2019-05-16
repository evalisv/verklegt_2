from django.shortcuts import render
from .models import SearchQuery
from estate.models import Estate
from django.core.paginator import Paginator
from django.db.models import Q


def search_view(request):
    query_url = request.GET.urlencode()
    query = request.GET.get('q', None)
    pnrhofud = request.GET.getlist('postal-hofudborgarsvaedid')
    pnrvestur = request.GET.getlist('postal-vesturland')
    pnrnordvesturland = request.GET.getlist('postal-nordvesturland')
    pnrnorth = request.GET.getlist('postal-nordurland')
    pnreast = request.GET.getlist('postal-austurland')
    pnrsouthwest = request.GET.getlist('postal-sudvesturland')
    pnrsouth = request.GET.getlist('postal-sudurland')
    type1 = request.GET.getlist('type1')
    lyfta = request.GET.get('lyfta')
    if lyfta == 'on':
        lyfta = True

    serinngangur = request.GET.get('serinngangur')
    if serinngangur == 'on':
        serinngangur = True

    bilskur = request.GET.get('bilskur')
    if bilskur == 'on':
        bilskur = True

    staerdfra = request.GET.get('staerdfra')
    if staerdfra == '':
        staerdfra = 0

    staerdtil = request.GET.get('staerdtil')
    if staerdtil == '':
        staerdtil = 100000

    verdfra = request.GET.get('verdfra')
    if verdfra == '':
        verdfra = 0

    verdtil = request.GET.get('verdtil')
    if verdtil == '':
        verdtil = 300000000

    herbergifra = request.GET.get('herbergifra')
    if herbergifra == '':
        herbergifra = 0

    herbergitil = request.GET.get('herbergitil')
    if herbergitil == '':
        herbergitil = 10

    #tékk fyrir því að til stærðin sé ekki minni en frá
    if herbergitil < herbergifra:
        herbergitil = herbergifra

    if verdtil < verdfra:
        verdtil = verdfra

    if staerdtil < staerdfra:
        staerdtil = staerdfra

    #Fylki fyrir array sem innihalda póstnúmer sem hakað er við og tegund húsnæðis
    pnr_arr = []
    type_arr = []

    #Náum í öll gildi sem hakað var við, sem birtast sem listar
    for i in type1:
        type_arr.append(i)

    for i in pnrhofud:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

    for i in pnrvestur:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

    for i in pnrnordvesturland:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

    for i in pnrnorth:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

    for i in pnreast:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

    for i in pnrsouthwest:
        ii = int(i.split('postal')[1])
        pnr_arr.append(ii)

    for i in pnrsouth:
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

        if lyfta:
            lookup2 = (Q(elevator=lyfta))
        else:
            lookup2 = (Q(elevator=True) | Q(elevator=False))

        if serinngangur:
            lookup3 = (Q(entry=serinngangur))
        else:
            lookup3 = (Q(entry=True) | Q(entry=False))

        if bilskur:
            lookup4 = (Q(garage=bilskur))
        else:
            lookup4 = (Q(garage=True) | Q(garage=False))

        lookup5 = (Q(size__gte=staerdfra) & Q(size__lte=staerdtil))
        lookup6 = (Q(price__gte=verdfra) & Q(price__lte=verdtil))
        lookup7 = (Q(bedrooms__gte=herbergifra) & Q(bedrooms__lte=herbergitil))

        if len(type_arr) > 0 and len(pnr_arr) == 0:
            estates = Estate.objects.filter(lookup)\
                .filter(type__in=type_arr)\
                .filter(lookup2)\
                .filter(lookup3)\
                .filter(lookup4)\
                .filter(lookup5)\
                .filter(lookup6)\
                .filter(lookup7)
        elif len(type_arr) > 0 and len(pnr_arr) > 0:
            estates = Estate.objects.filter(lookup)\
                .filter(postal_code__postal_code__in=pnr_arr)\
                .filter(type__in=type_arr)\
                .filter(lookup2)\
                .filter(lookup3)\
                .filter(lookup4)\
                .filter(lookup5)\
                .filter(lookup6)\
                .filter(lookup7)
        elif len(type_arr) == 0 and len(pnr_arr) > 0:
            estates = Estate.objects.filter(lookup)\
                .filter(postal_code__postal_code__in=pnr_arr)\
                .filter(lookup2)\
                .filter(lookup3)\
                .filter(lookup4)\
                .filter(lookup5)\
                .filter(lookup6)\
                .filter(lookup7)
        else:
            estates = Estate.objects.filter(lookup)\
                .filter(lookup2)\
                .filter(lookup3)\
                .filter(lookup4)\
                .filter(lookup5)\
                .filter(lookup6)\
                .filter(lookup7)

        paginator = Paginator(estates, 6)
        page = request.GET.get('page')

        estates = paginator.get_page(page)

        context['estates'] = estates
        context['query'] = query_url

    return render(request, 'search/search_results.html', context)

def view_search_words(request):
    filtered_search_query = SearchQuery.objects.filter(user_id=request.user).exclude(query='').order_by('-timestamp')
    context = {'searches': filtered_search_query}
    return render(request, 'search/search_words.html', context)

def search_history(request):
    return render(request, 'search/search_history.html')