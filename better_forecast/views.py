from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from better_forecast.forms import *
from better_forecast.models import RainFavourite, SnowFavourite, SunFavourite
from random import randint

def register(request):
    if request.method == 'POST':
        form = WeatherUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            if request.user.choice == "YOURCHOICE":
                return redirect("favourites")
            else:
                return redirect("home")
    else:
        form = WeatherUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


# def favourites(request):
#     if request.method == 'POST':
#         rainform = RainFavouriteSet(request.POST)
#         sunform = SunFavouriteSet(request.POST)
#         snowform = SnowFavouriteSet(request.POST)
#         if rainform.is_valid() and sunform.is_valid() and snowform.is_valid():
#             user = request.user
#             choice1 = rainform.cleaned_data[0]['choice1']
#             choice2 = rainform.cleaned_data[1]['choice1']
#             choice3 = rainform.cleaned_data[2]['choice1']
#             choice4 = rainform.cleaned_data[3]['choice1']
#             choice5 = rainform.cleaned_data[4]['choice1']
#             choice6 = rainform.cleaned_data[5]['choice1']
#             choice7 = rainform.cleaned_data[6]['choice1']
#             choice8 = rainform.cleaned_data[7]['choice1']
#             choice9 = rainform.cleaned_data[8]['choice1']
#             choic1 = sunform.cleaned_data[0]['choice2']
#             choic2 = sunform.cleaned_data[1]['choice2']
#             choic3 = sunform.cleaned_data[2]['choice2']
#             choic4 = sunform.cleaned_data[3]['choice2']
#             choic5 = sunform.cleaned_data[4]['choice2']
#             choic6 = sunform.cleaned_data[5]['choice2']
#             choic7 = sunform.cleaned_data[6]['choice2']
#             choic8 = sunform.cleaned_data[7]['choice2']
#             choic9 = sunform.cleaned_data[8]['choice2']
#             choi1 = snowform.cleaned_data[0]['choice3']
#             choi2 = snowform.cleaned_data[1]['choice3']
#             choi3 = snowform.cleaned_data[2]['choice3']
#             choi4 = snowform.cleaned_data[3]['choice3']
#             choi5 = snowform.cleaned_data[4]['choice3']
#             choi6 = snowform.cleaned_data[5]['choice3']
#             choi7 = snowform.cleaned_data[6]['choice3']
#             choi8 = snowform.cleaned_data[7]['choice3']
#             choi9 = snowform.cleaned_data[8]['choice3']
#             RainFavourite.objects.create(user=user, choice=choice1)
#             RainFavourite.objects.create(user=user, choice=choice2)
#             RainFavourite.objects.create(user=user, choice=choice3)
#             RainFavourite.objects.create(user=user, choice=choice4)
#             RainFavourite.objects.create(user=user, choice=choice5)
#             RainFavourite.objects.create(user=user, choice=choice6)
#             RainFavourite.objects.create(user=user, choice=choice7)
#             RainFavourite.objects.create(user=user, choice=choice8)
#             RainFavourite.objects.create(user=user, choice=choice9)
#             SunFavourite.objects.create(user=user, choice=choic1)
#             SunFavourite.objects.create(user=user, choice=choic2)
#             SunFavourite.objects.create(user=user, choice=choic3)
#             SunFavourite.objects.create(user=user, choice=choic4)
#             SunFavourite.objects.create(user=user, choice=choic5)
#             SunFavourite.objects.create(user=user, choice=choic6)
#             SunFavourite.objects.create(user=user, choice=choic7)
#             SunFavourite.objects.create(user=user, choice=choic8)
#             SunFavourite.objects.create(user=user, choice=choic9)
#             SnowFavourite.objects.create(user=user, choice=choi1)
#             SnowFavourite.objects.create(user=user, choice=choi2)
#             SnowFavourite.objects.create(user=user, choice=choi3)
#             SnowFavourite.objects.create(user=user, choice=choi4)
#             SnowFavourite.objects.create(user=user, choice=choi5)
#             SnowFavourite.objects.create(user=user, choice=choi6)
#             SnowFavourite.objects.create(user=user, choice=choi7)
#             SnowFavourite.objects.create(user=user, choice=choi8)
#             SnowFavourite.objects.create(user=user, choice=choi9)
#
#             return redirect("/")
#     else:
#         rainform = RainFavouriteSet()
#         sunform = SunFavouriteSet()
#         snowform = SnowFavouriteSet()
#
#     return render(request, "favourites.html", {
#         'rainform': rainform, 'sunform': sunform, 'snowform': snowform
#     })

def favourites(request):
    if request.user.choice == 'YOURCHOICE':
        username = request.user
        return render(request, 'favourites.html', {'username': username})
    else:
        return render(request, 'home.html', {})


def home(request):
    if request.user.is_authenticated():
        # Most of this view can be abstracted out into functions so it's more DRY
        # You could have a function called get_random_rain_favourite() which does the randomint and makes the query
        if request.user.choice == "YOURCHOICE":
            if len(RainFavourite.objects.filter(user=request.user)) < 4 or len(SunFavourite.objects.filter(user=request.user)) < 4 or len(SnowFavourite.objects.filter(user=request.user)) < 4:
                number0 = randint(0,2)
                number1 = randint(0,2)
                number2 = randint(0,2)
                number3 = randint(0,2)
                number4 = randint(0,2)
                number5 = randint(0,2)
                number6 = randint(0,2)
                number7 = randint(0,2)
            else:
                number0 = randint(0,4)
                number1 = randint(0,4)
                number2 = randint(0,4)
                number3 = randint(0,4)
                number4 = randint(0,4)
                number5 = randint(0,4)
                number6 = randint(0,4)
                number7 = randint(0,4)
            rain0 = RainFavourite.objects.filter(user__username=request.user)[number0]
            rain1 = RainFavourite.objects.filter(user__username=request.user)[number2]
            rain2 = RainFavourite.objects.filter(user__username=request.user)[number3]
            rain3 = RainFavourite.objects.filter(user__username=request.user)[number4]
            rain4 = RainFavourite.objects.filter(user__username=request.user)[number5]
            rain5 = RainFavourite.objects.filter(user__username=request.user)[number6]
            rain6 = RainFavourite.objects.filter(user__username=request.user)[number7]
            rain7 = RainFavourite.objects.filter(user__username=request.user)[number1]
            sun0 = SunFavourite.objects.filter(user__username=request.user)[number6]
            sun1 = SunFavourite.objects.filter(user__username=request.user)[number2]
            sun2 = SunFavourite.objects.filter(user__username=request.user)[number3]
            sun3 = SunFavourite.objects.filter(user__username=request.user)[number4]
            sun4 = SunFavourite.objects.filter(user__username=request.user)[number7]
            sun5 = SunFavourite.objects.filter(user__username=request.user)[number5]
            sun6 = SunFavourite.objects.filter(user__username=request.user)[number6]
            sun7 = SunFavourite.objects.filter(user__username=request.user)[number0]
            snow0 = SnowFavourite.objects.filter(user__username=request.user)[number1]
            snow1 = SnowFavourite.objects.filter(user__username=request.user)[number7]
            snow2 = SnowFavourite.objects.filter(user__username=request.user)[number6]
            snow3 = SnowFavourite.objects.filter(user__username=request.user)[number4]
            snow4 = SnowFavourite.objects.filter(user__username=request.user)[number1]
            snow5 = SnowFavourite.objects.filter(user__username=request.user)[number2]
            snow6 = SnowFavourite.objects.filter(user__username=request.user)[number3]
            snow7 = SnowFavourite.objects.filter(user__username=request.user)[number5]
            return render(request, 'home.html', {'rain0': rain0, 'rain1': rain1, 'rain2': rain2, 'rain3': rain3, 'rain4': rain4, 'rain5': rain5,'rain6': rain6, 'rain7': rain7,
                                                 'sun1': sun1, 'sun2': sun2, 'sun3': sun3, 'sun0': sun0, 'sun4': sun4, 'sun5': sun5, 'sun6': sun6, 'sun7': sun7,
                                                 'snow0': snow0, 'snow1': snow1, 'snow2': snow2, 'snow3': snow3, 'snow4': snow4, 'snow5': snow5, 'snow6': snow6, 'snow7': snow7})
        else:
            # if len(RainFavourite.objects.filter(user=request.user)) < 4:
            #     numb = randint(0,2)
            # elif request.user.CHOICES == "Random":
            numb1 = randint(0,6)
            numb2 = randint(0,6)
            numb3 = randint(0,6)
            numb4 = randint(0,6)
            numb5 = randint(0,6)
            numb6 = randint(0,6)
            numb7 = randint(0,6)
            numb8 = randint(0,6)

            rain0 = RainFavourite.objects.filter(user__username='a')[numb1]
            rain1 = RainFavourite.objects.filter(user__username='a')[numb2]
            rain2 = RainFavourite.objects.filter(user__username='a')[numb3]
            rain3 = RainFavourite.objects.filter(user__username='a')[numb4]
            rain4 = RainFavourite.objects.filter(user__username='a')[numb5]
            rain5 = RainFavourite.objects.filter(user__username='a')[numb6]
            rain6 = RainFavourite.objects.filter(user__username='a')[numb7]
            rain7 = RainFavourite.objects.filter(user__username='a')[numb8]
            sun0 = SunFavourite.objects.filter(user__username='a')[numb6]
            sun1 = SunFavourite.objects.filter(user__username='a')[numb2]
            sun2 = SunFavourite.objects.filter(user__username='a')[numb3]
            sun3 = SunFavourite.objects.filter(user__username='a')[numb4]
            sun4 = SunFavourite.objects.filter(user__username='a')[numb7]
            sun5 = SunFavourite.objects.filter(user__username='a')[numb5]
            sun6 = SunFavourite.objects.filter(user__username='a')[numb6]
            sun7 = SunFavourite.objects.filter(user__username='a')[numb1]
            snow0 = SnowFavourite.objects.filter(user__username='a')[numb8]
            snow1 = SnowFavourite.objects.filter(user__username='a')[numb7]
            snow2 = SnowFavourite.objects.filter(user__username='a')[numb6]
            snow3 = SnowFavourite.objects.filter(user__username='a')[numb4]
            snow4 = SnowFavourite.objects.filter(user__username='a')[numb1]
            snow5 = SnowFavourite.objects.filter(user__username='a')[numb2]
            snow6 = SnowFavourite.objects.filter(user__username='a')[numb3]
            snow7 = SnowFavourite.objects.filter(user__username='a')[numb5]
            return render(request, 'home.html', {'rain0': rain0, 'rain1': rain1, 'rain2': rain2, 'rain3': rain3, 'rain4': rain4, 'rain5': rain5,'rain6': rain6, 'rain7': rain7,
                                                 'sun1': sun1, 'sun2': sun2, 'sun3': sun3, 'sun0': sun0, 'sun4': sun4, 'sun5': sun5, 'sun6': sun6, 'sun7': sun7,
                                                 'snow0': snow0, 'snow1': snow1, 'snow2': snow2, 'snow3': snow3, 'snow4': snow4, 'snow5': snow5, 'snow6': snow6, 'snow7': snow7})
    if request.user.is_authenticated() == False:
        return redirect('login')
@login_required
def profile(request):
    return render(request, 'profile.html', {})
