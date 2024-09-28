from django.shortcuts import render
from prayer.forms import RequestForm
from prayer.models import Request


# Create your views here.

def home(request):
    """
    :return:
    """
    request_form = RequestForm()
    context = {
        'form': request_form,
    }

    if request.method == 'POST':
        form = RequestForm(request.POST)
        print('I got a postcard!')
        if form.is_valid():
            print('The form is formed!')
            print(request.POST)

    if request.user.is_authenticated:
        # print('I know me!')
        context['requests'] = Request.objects.all()

    return render(request, 'prayer/home.html', context)
