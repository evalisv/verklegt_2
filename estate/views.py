from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from estate.models import Estate, EstateImage
from estate.forms.estate_form import RegisterEstateForm, UpdateEstateForm
# Create your views here.


def index(request):
    estate_list = Estate.objects.all().order_by("address")
    paginator = Paginator(estate_list, 6)

    page = request.GET.get("page")
    estates = paginator.get_page(page)

    context = {"estates": estates}
    return render(request, "estate/index.html", context)


def get_estate_by_id(request, id):
    return render(request, 'estate/estate_details.html', {
      'estate' : get_object_or_404(Estate, pk=id)
    })

def register_estate(request):
    if request.method == 'POST':
        form = RegisterEstateForm(data=request.POST)
        if form.is_valid():
            estate = form.save()
            estate_image = EstateImage(image=request.POST['image'], estate=estate)
            estate_image.save()
            return redirect('estate-index')
    else:
        form = RegisterEstateForm()
    return render(request, 'estate/register_estate.html', {
        'form' : form
    })

def delete_estate(request, id):
    estate = get_object_or_404(Estate, pk=id)
    estate.delete()
    return redirect('estate-index')

def update_estate(request, id):
    instance = get_object_or_404(Estate, pk=id)
    if request.method == 'POST':
        form = UpdateEstateForm(data=request.POST, instance=instance)
        if form.is_valid():
            estate = form.save()
            estate_image = EstateImage(image=request.POST['image'], estate=estate)
            estate_image.save()
            return redirect('estate_details', id=id)
    else:
        form = UpdateEstateForm(instance=instance)
    return render(request, 'estate/update_estate.html', {
        'form': form,
        'id': id
    })

def search(request):
    queryset = Estate.objects.all().order_by("address")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(address__icontains=query)

    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        queryset_list = paginator.page(1)
    except EmptyPage:
        queryset_list = paginator.page(paginator.num_pages)

    context = {
        "estates": queryset,
        "title": "Leitarniðurstöður"
    }
    return render(request, "index.html", context)