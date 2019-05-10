from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from estate.models import Estate, EstateImage, EstatePictures
from estate.forms.estate_form import RegisterEstateForm, UpdateEstateForm
from user_role.models import UserRole
from django.contrib.auth.decorators import login_required

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

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

            # TODO: færa þetta inn í for lykkuna fyrir myndir
            file_type = estate.images.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    "estate": estate,
                    "form": form,
                    "error_message": "Mynd þarf að vera af gerðinni PNG, JPG, eða JPEG",
                }
                return render(request, 'estate/register_estate.html', context)

            user_roles_set = UserRole.objects.filter(user=estate.estate_seller_id)
            user_roles = list(user_roles_set.values_list("role", flat=True))
            user_role_exists = False
            try:
                if user_roles.index("seller"):
                    user_role_exists = True
            except:
                print("The user_id ", estate.estate_seller_id, " is not a seller")
            if user_role_exists == False:
                user_role = UserRole(role="seller", user=estate.estate_seller)
                user_role.save()

            return redirect('estate-index')
    else:
        form = RegisterEstateForm()
    return render(request, 'estate/register_estate.html', {
        'form' : form
    })


@login_required
def delete_estate(request, id):
    estate = get_object_or_404(Estate, pk=id)
    estate.delete()
    return redirect('estate-index')

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

