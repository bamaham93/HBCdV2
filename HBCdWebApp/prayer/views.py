from django.shortcuts import render
from prayer.forms import RequestForm
from prayer.models import Request
from django.contrib.auth.models import User, Group


def is_member_of(user, group_name: str, user_groups):
    """
    :param user The user making the request
    :param user_groups The groups to which that user belongs.
    :return: Bool

    Checks to see if the user is a member of the group, e.g. group_name='Prayer Group'
    """
    # print(user.groups.filter(name=group_name).exists)
    # if user.groups.filter(name=group_name.exists()):
    #     return True
    # else:
    #     return False

    if group_name in user_groups:
        return True
    else:
        return False

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
            form.save()
            print('Form is saved! Hallelujah!')

    # print(is_member_of(user=request.user, group_name="Prayer Group", user_groups=request.user.groups.all()))
    # print(request.user.groups.all())

    if request.user.is_authenticated:
        # print('I know me!')
        context['requests'] = Request.objects.all()

    return render(request, 'prayer/home.html', context)
