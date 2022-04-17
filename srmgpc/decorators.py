from django.http import HttpResponse
from django.shortcuts import render, redirect
from sklearn.preprocessing import scale
from .models import Volunteer,CellName,CompetitionName,Registration


#Decorators
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group= request.user.groups.all()[0].name
        
        if group == 'volunteer':
            return redirect('userpage')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

        if group == "Technical Team":
            registrations = Registration.objects.all()
            context={'registrations':registrations}
            return render(request,'adminpage.html',context)

        if group == 'Choreography Cell':
            solista = Registration.objects.filter(cell=1, event_name=1)
            squadron = Registration.objects.filter(cell=1, event_name=2)
            impromptu = Registration.objects.filter(cell=1, event_name=3)
            context={'solista':solista, 'squadron':squadron, 'impromptu':impromptu}
            return render(request,'cell/choreography.html',context)

        if group == 'Euphony Cell':
            swarjeet = Registration.objects.filter(cell=2, event_name=5)
            swarmel = Registration.objects.filter(cell=2, event_name=6)
            crooner = Registration.objects.filter(cell=2, event_name=7)
            context={'swarjeet':swarjeet, 'swarmel':swarmel, 'crooner':crooner}
            return render(request,'cell/euphony.html',context)

        if group == 'Dracula Cell':
            ma = Registration.objects.filter(cell=3, event_name=8)
            am = Registration.objects.filter(cell=3, event_name=9)
            kavyaansh = Registration.objects.filter(cell=3, event_name=10)
            rangbaazi = Registration.objects.filter(cell=3, event_name=36)
            context={'ma':ma, 'am':am, 'kavyaansh':kavyaansh, 'rangbaazi':rangbaazi}
            return render(request,'cell/dracula.html',context)

        if group == 'Literati Cell':
            graffiti = Registration.objects.filter(cell=11, event_name=56)
            gd = Registration.objects.filter(cell=11, event_name=57)
            debate = Registration.objects.filter(cell=11, event_name=58)
            mm = Registration.objects.filter(cell=11, event_name=59)
            tf = Registration.objects.filter(cell=11, event_name=60)
            ppd = Registration.objects.filter(cell=11, event_name=61)
            pictionary = Registration.objects.filter(cell=11, event_name=62)
            tt = Registration.objects.filter(cell=11, event_name=63)
            om = Registration.objects.filter(cell=11, event_name=64)
            rc = Registration.objects.filter(cell=11, event_name=65)
            sq = Registration.objects.filter(cell=11, event_name=66)
            jam = Registration.objects.filter(cell=11, event_name=67)
            dc = Registration.objects.filter(cell=11, event_name=68)
            context={'graffiti':graffiti, 'gd':gd, 'debate':debate, 'mm':mm, 'tf':tf, 'ppd':ppd, 'pictionary':pictionary, 'tt':tt, 'om':om, 'rc':rc, 'sq':sq, 'jam':jam, 'dc':dc}
            return render(request,'cell/literati.html',context)

        if group == 'Photography Cell':
            sc = Registration.objects.filter(cell=5, event_name=16)
            pf = Registration.objects.filter(cell=5, event_name=17)
            mp = Registration.objects.filter(cell=5, event_name=18)
            dpc = Registration.objects.filter(cell=5, event_name=19)
            videography = Registration.objects.filter(cell=5, event_name=20)
            bpc = Registration.objects.filter(cell=5, event_name=21)
            context={'sc':sc, 'pf':pf, 'mp':mp, 'dpc':dpc, 'videography':videography, 'bpc':bpc}
            return render(request,'cell/photography.html',context)

        if group == "Newspaper Cell":
            ypia = Registration.objects.filter(cell=12, event_name=69)
            fq = Registration.objects.filter(cell=12, event_name=70)
            context = {'ypia':ypia, 'fq':fq}
            return render(request, 'cell/newspaper.html', context)

        if group == 'Media Cell':
            md = Registration.objects.filter(cell=6, event_name=22)
            fm = Registration.objects.filter(cell=6, event_name=23)
            rj = Registration.objects.filter(cell=6, event_name=24)
            context={'md':md, 'fm':fm, 'rj':rj}
            return render(request,'cell/media.html',context)

        if group == 'Creative Canvas Club':
            ag = Registration.objects.filter(cell=9, event_name=37)
            bw = Registration.objects.filter(cell=9, event_name=39)
            osps = Registration.objects.filter(cell=9, event_name=38)
            tp = Registration.objects.filter(cell=9, event_name=40)
            rangoli = Registration.objects.filter(cell=9, event_name=41)
            ps = Registration.objects.filter(cell=9, event_name=42)
            context={'ag':ag, 'bw':bw, 'osps':osps, 'tp':tp, 'rangoli':rangoli, 'ps':ps}
            return render(request,'cell/ccc.html',context)

        if group == 'Informal Cell':
            mc = Registration.objects.filter(cell=10, event_name=44)
            tow = Registration.objects.filter(cell=10, event_name=45)
            housie = Registration.objects.filter(cell=10, event_name=46)
            kk = Registration.objects.filter(cell=10, event_name=47)
            cricket = Registration.objects.filter(cell=10, event_name=48)
            kw = Registration.objects.filter(cell=10, event_name=49)
            darts = Registration.objects.filter(cell=10, event_name=50)
            chess = Registration.objects.filter(cell=10, event_name=51)
            lr = Registration.objects.filter(cell=10, event_name=52)
            sr = Registration.objects.filter(cell=10, event_name=53)
            susd = Registration.objects.filter(cell=10, event_name=54)
            tlr = Registration.objects.filter(cell=10, event_name=55)
            context={'mc':mc, 'tow':tow, 'housie':housie, 'kk':kk, 'cricket':cricket, 'kw':kw, 'darts':darts, 'chess':chess,'lr':lr, 'sr':sr, 'susd':susd, 'tlr':tlr}
            return render(request,'cell/ccc.html',context)

        if group == "Security Cell":
            return HttpResponse("Hello, Security Cell")

    return wrapper_func