from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from estate.models import Estate, EstateImage
from estate.forms.estate_form import RegisterEstateForm, UpdateEstateForm
# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        estates = [ {
            'address': x.address,
            'price': x.price,
            'description': x.description,
            'firstImage': x.estateimage_set.first().image

        } for x in Estate.objects.filter(address__icontains=search_filter) ]
        return JsonResponse({ 'data': estates })
    context = {"estates": Estate.objects.all().order_by('address')}
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
            return redirect('profile')
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

