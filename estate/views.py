from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from estate.models import Estate, EstatePictures, Municipality
from estate.forms.estate_form import RegisterEstateForm, UpdateEstateForm
from django.contrib.auth.decorators import login_required
from vhistory.views import update_vhistory

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    estate_list = Estate.objects.filter(on_sale=True).order_by('address')
    paginator = Paginator(estate_list, 6)

    page = request.GET.get("page")
    estates = paginator.get_page(page)

    context = {
        'estates': estates,
        'postal_codes': Municipality.objects.all()
    }
    return render(request, "estate/index.html", context)


def get_estate_by_id(request, id):
    estate = get_object_or_404(Estate, pk=id)
    if request.user.is_authenticated:
        update_vhistory(request.user, estate)
    return render(request, 'estate/estate_details.html', {
      'estate' : estate
    })


@login_required
def register_estate(request):
    if request.method == 'POST':
        form = RegisterEstateForm(request.POST, request.FILES)
        if form.is_valid():
            estate = form.save(commit=False)
            estate.estate_seller = request.user
            estate.images = request.FILES['images']
            estate.save()
            pics = request.FILES.getlist('images')
            for img in pics:
                estate_picture = EstatePictures(url=img, estate=estate)
                estate_picture.save()
            return redirect('estate-index')
    else:
        form = RegisterEstateForm()
    return render(request, 'estate/register_estate.html', {
        'form' : form
    })


@login_required
def delete_estate(request, id):
    estate = get_object_or_404(Estate, pk=id)
    if request.user == estate.estate_seller:
        estate.delete()
    return redirect('seller_estates')

@login_required
def update_estate(request, id):
    instance = get_object_or_404(Estate, pk=id)
    if request.method == 'POST':
        form = UpdateEstateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            estate = form.save(commit=False)
            estate.images = request.FILES['images']
            estate.save()
            pics = request.FILES.getlist('images')
            for img in pics:
                estate_picture = EstatePictures(url=img, estate=estate)
                estate_picture.save()
            return redirect('estate_details', id=id)
    else:
        form = UpdateEstateForm(instance=instance)
    return render(request, 'estate/update_estate.html', {
        'form': form,
        'id': id,
        'estate': instance
    })


def sort_estates(request):
    order_by = request.GET.get('order_by', 'defaultOrderField')
    estate_list = Estate.objects.filter(on_sale=True).order_by(order_by)

    paginator = Paginator(estate_list, 6)
    page = request.GET.get("page")

    sorting = request.GET.get('-order_by')

    estates = paginator.get_page(page)

    context = {
        'estates': estates,
        'sorting': sorting
    }
    return render(request, 'estate/index.html', context)


@login_required
def seller_index(request):
    list_of_estates = []
    for estate in Estate.objects.filter(on_sale=True):
        if estate.estate_seller == request.user:
            list_of_estates.append(estate)
    paginator = Paginator(list_of_estates, 6)

    page = request.GET.get("page")
    estates = paginator.get_page(page)

    context = {"estates": estates}
    return render(request, "estate/my_estates.html", context)
