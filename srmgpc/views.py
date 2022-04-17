from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import Group

from .forms import CreateUserForm,ContactForm,ProfileForm
from .models import Volunteer,CellName,CompetitionName,Registration,TeamPost,TeamMemberName,Update,EventName,EventResult,RulesOfEvent,PerformingEvent,Registration,TechnicalTeam
from .decorators import unauthenticated_user,allowed_users,admin_only

# from django.contrib.auth.models import User
# from django import forms
from .tasks import register_mail, event_register_mail

import os
from dotenv import load_dotenv

load_dotenv()


# Create your views here.

@unauthenticated_user
def index(request):
    context={}
    return render(request,'home.html',context)

@unauthenticated_user
def signupPage(request):
    form = CreateUserForm()
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            Volunteer.objects.create(user=user,name_admin=str(user),email=user.email) 
            group = Group.objects.get(name='volunteer')
            user.groups.add(group)
            register_mail(name=user.username, email=user.email)
            messages.success(request,'Your account has been successfully created')
            return redirect('login')
        else:
            messages.error(request,'This username already exist or password cannot be taken')

    context={'form':form}
    return render(request,'signup.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('adminpage')
        else :           
            messages.info(request,'Username or password is incorrect')
                
    context={}
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    context={}
    return render(request,'home.html',context)


@login_required(login_url = 'login')
@admin_only
def adminPage(request):
    # context={}
    # return render(request,'adminpage.html',context)
    return HttpResponse("Hello Admin")


@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Technical Team'])
def deleteRegistrations(request, id):
    registration = Registration.objects.get(id=id)
    registration.delete()
    return redirect('adminpage')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['volunteer'])
def userPage(request):
    profile = request.user.volunteer
    registration = Registration.objects.filter(volunteer = request.user.pk)
    form = ProfileForm(instance=profile)
    
    if request.method=="POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        form.save()
        return redirect('adminpage')
        # return redirect('userpage')

    context={'profile':profile,'form':form,'registration':registration}
    return render(request,'userpage.html',context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Security Cell'])
def profile(request,user):
    profile = Volunteer.objects.get(name_admin=user)
    reg = Registration.objects.filter(volunteer=profile.user)
    context = {'profile':profile, 'reg':reg}
    return render(request,'profile.html',context)


def events(request):
    context={}
    return render(request,'events.html',context)

def starnight(request):
    context={}
    return render(request,'star_night.html',context)


def xeronight(request):
    context={}
    return render(request,'xeronight.html',context)


def team(request):
    faculty_convenors = TeamMemberName.objects.filter(post=1)
    joint_faculty = TeamMemberName.objects.filter(post=2)
    convenors = TeamMemberName.objects.filter(post=3)
    veteran_convenors = TeamMemberName.objects.filter(post=4)
    joint_convenors = TeamMemberName.objects.filter(post=5)
    asst_convenors = TeamMemberName.objects.filter(post=6)
    exe_coordinator = TeamMemberName.objects.filter(post=7)
    controller_ad = TeamMemberName.objects.filter(post=8)
    controller_cn = TeamMemberName.objects.filter(post=9)
    finance_controller = TeamMemberName.objects.filter(post=10)
    # cells
    choreography = TeamMemberName.objects.filter(cell=1)
    euphony = TeamMemberName.objects.filter(cell=2)
    draco = TeamMemberName.objects.filter(cell=3)
    ritumbhara = TeamMemberName.objects.filter(cell=4)
    photography = TeamMemberName.objects.filter(cell=5)
    media = TeamMemberName.objects.filter(cell=6)
    compairing = TeamMemberName.objects.filter(cell=7)
    decoration = TeamMemberName.objects.filter(cell=8)
    creative = TeamMemberName.objects.filter(cell=9)
    informal = TeamMemberName.objects.filter(cell=10)
    literati = TeamMemberName.objects.filter(cell=11)
    npc = TeamMemberName.objects.filter(cell=12)
    security = TeamMemberName.objects.filter(cell=13)
    control = TeamMemberName.objects.filter(cell=14)
    epc = TeamMemberName.objects.filter(cell=15)
    ipc = TeamMemberName.objects.filter(cell=16)
    
    context={'convenors':convenors,'faculty_convenors':faculty_convenors,'joint_faculty':joint_faculty,'veteran_convenors':veteran_convenors,'joint_convenors':joint_convenors,'asst_convenors':asst_convenors,'exe_coordinator':exe_coordinator,'controller_ad':controller_ad,'controller_cn':controller_cn,'finance_controller':finance_controller,'choreography':choreography,'euphony':euphony,'draco':draco,'ritumbhara':ritumbhara,'photography':photography,'media':media,'compairing':compairing,'decoration':decoration,'creative':creative,'informal':informal,'literati':literati,'npc':npc,'security':security,'control':control,'epc':epc,'ipc':ipc}
    return render(request,'team.html',context)


def about(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            volunteer=form.save()
            messages.success(request,'Thankyou for contacting us!')
        return redirect('/about/')

    context={'form':form}
    return render(request,'about.html',context)


def updates(request):
    update = Update.objects.all()
    solista = EventResult.objects.filter(event_name=1)
    squadron = EventResult.objects.filter(event_name=2)
    impromptu = EventResult.objects.filter(event_name=3)
    swarjeet = EventResult.objects.filter(event_name=5)
    swarmel = EventResult.objects.filter(event_name=6)
    crooner = EventResult.objects.filter(event_name=7)
    mono_act = EventResult.objects.filter(event_name=8)
    ad_mad = EventResult.objects.filter(event_name=9)
    kavyaansh = EventResult.objects.filter(event_name=10)
    rangbaazi = EventResult.objects.filter(event_name=36)
    graffiti = EventResult.objects.filter(event_name=56)
    gd = EventResult.objects.filter(event_name=57)
    debate = EventResult.objects.filter(event_name=58)
    mm = EventResult.objects.filter(event_name=59)
    tf = EventResult.objects.filter(event_name=60)
    ppd = EventResult.objects.filter(event_name=61)
    pictionary = EventResult.objects.filter(event_name=62)
    tt = EventResult.objects.filter(event_name=63)
    om = EventResult.objects.filter(event_name=64)
    rc = EventResult.objects.filter(event_name=65)
    sq = EventResult.objects.filter(event_name=66)
    jam = EventResult.objects.filter(event_name=67)
    dc = EventResult.objects.filter(event_name=68)
    ag = EventResult.objects.filter(event_name=37)
    bnw = EventResult.objects.filter(event_name=39)
    osps = EventResult.objects.filter(event_name=38)
    tp = EventResult.objects.filter(event_name=40)
    pns = EventResult.objects.filter(event_name=42)
    rangoli = EventResult.objects.filter(event_name=41)
    ypia = EventResult.objects.filter(event_name=69)
    fq = EventResult.objects.filter(event_name=70)
    cg = EventResult.objects.filter(event_name=71)
    
    context={'update':update,'solista':solista,'squadron':squadron,'impromptu':impromptu,'swarjeet':swarjeet,'swarmel':swarmel,'crooner':crooner,'mono_act':mono_act,'ad_mad':ad_mad,'kavyaansh':kavyaansh,'rangbaazi':rangbaazi,'graffiti':graffiti, 'gd':gd, 'debate':debate, 'mm':mm, 'tf':tf, 'ppd':ppd, 'pictionary':pictionary, 'tt':tt, 'om':om, 'rc':rc, 'sq':sq, 'jam':jam,'dc':dc, 'ag':ag, 'bnw':bnw, 'osps':osps, 'tp':tp, 'pns':pns, 'rangoli':rangoli, 'ypia':ypia, 'fq':fq, 'cg':cg}
    return render(request,'updates.html',context)


def eventChoreography(request):
    choreography = PerformingEvent.objects.filter(cell=1)
    solista = EventName.objects.get(event_name="Solista")
    solista_rule = RulesOfEvent.objects.filter(event_name=1)
    squadron = EventName.objects.get(event_name="Squadron")
    squadron_rule = RulesOfEvent.objects.filter(event_name=2)
    impromptu = EventName.objects.get(event_name="Impromptu")
    impromptu_rule = RulesOfEvent.objects.filter(event_name=3)

    context={'solista':solista,'solista_rule':solista_rule,'choreography':choreography,'squadron':squadron,'squadron_rule':squadron_rule,'impromptu':impromptu,'impromptu_rule':impromptu_rule}
    return render(request,'event/choreography.html',context)

def eventEuphony(request):
    euphony = PerformingEvent.objects.filter(cell=2)
    swarjeet = EventName.objects.get(event_name="Swarjeet")
    swarjeet_rule = RulesOfEvent.objects.filter(event_name=5)
    swarmel = EventName.objects.get(event_name="Swarmel")
    swarmel_rule = RulesOfEvent.objects.filter(event_name=6)
    crooner = EventName.objects.get(event_name="Crooner")
    crooner_rule = RulesOfEvent.objects.filter(event_name=7)

    context={'euphony':euphony,'swarjeet':swarjeet,'swarjeet_rule':swarjeet_rule,'swarmel':swarmel,'swarmel_rule':swarmel_rule,'crooner':crooner,'crooner_rule':crooner_rule}
    return render(request,'event/euphony.html',context)

def eventDracula(request):
    dracula = PerformingEvent.objects.filter(cell=3)
    monoact = EventName.objects.get(event_name="Mono Act")
    monoact_rule = RulesOfEvent.objects.filter(event_name=8)
    admad = EventName.objects.get(event_name="Ad Mad")
    admad_rule = RulesOfEvent.objects.filter(event_name=9)
    kavyaansh = EventName.objects.get(event_name="Kavya Ansh")
    kavyaansh_rule = RulesOfEvent.objects.filter(event_name=10)
    rangbaazi = EventName.objects.get(event_name="Rangbaazi")
    rangbaazi_rule = RulesOfEvent.objects.filter(event_name=36)

    context={'dracula':dracula,'monoact':monoact,'monoact_rule':monoact_rule,'admad':admad,'admad_rule':admad_rule,'kavyaansh':kavyaansh,'kavyaansh_rule':kavyaansh_rule,'rangbaazi':rangbaazi,'rangbaazi_rule':rangbaazi_rule}
    return render(request,'event/dracula.html',context)

def eventRitumbhara(request):
    ritumbhara = PerformingEvent.objects.filter(cell=4)
    context={'ritumbhara':ritumbhara}
    return render(request,'event/ritumbhara.html',context)


def eventPhotography(request):
    photography = PerformingEvent.objects.filter(cell=5)
    selfiecontest = EventName.objects.get(event_name="Selfie Contest")
    selfiecontest_rule = RulesOfEvent.objects.filter(event_name=16)
    photofilm = EventName.objects.get(event_name="Photo Film")
    photofilm_rule = RulesOfEvent.objects.filter(event_name=17)
    mobilephotography = EventName.objects.get(event_name="Mobile Photography")
    mobilephotography_rule = RulesOfEvent.objects.filter(event_name=18)
    duetphotoshoot = EventName.objects.get(event_name="Duet Photoshoot Contest")
    duetphotoshoot_rule = RulesOfEvent.objects.filter(event_name=19)
    videography = EventName.objects.get(event_name="Videography")
    videography_rule = RulesOfEvent.objects.filter(event_name=20)
    bestpose = EventName.objects.get(event_name="Best Pose Contest")
    bestpose_rule = RulesOfEvent.objects.filter(event_name=21)

    context={'photography':photography,'selfiecontest':selfiecontest,'selfiecontest_rule':selfiecontest_rule,'photofilm':photofilm,'photofilm_rule':photofilm_rule,'mobilephotography':mobilephotography,'mobilephotography_rule':mobilephotography_rule,'duetphotoshoot':duetphotoshoot,'duetphotoshoot_rule':duetphotoshoot_rule,'videography':videography,'videography_rule':videography_rule,'bestpose':bestpose,'bestpose_rule':bestpose_rule}
    return render(request,'event/photography.html',context)

def eventMedia(request):
    media = PerformingEvent.objects.filter(cell=6)
    mascot = EventName.objects.get(event_name="Mascot Drawing")
    mascot_rule = RulesOfEvent.objects.filter(event_name=22)
    flex = EventName.objects.get(event_name="Flex Making")
    flex_rule = RulesOfEvent.objects.filter(event_name=23)
    rjhunt = EventName.objects.get(event_name="RJ Hunt")
    rjhunt_rule = RulesOfEvent.objects.filter(event_name=24)
    context={'media':media,'mascot':mascot,'mascot_rule':mascot_rule,'flex':flex,'flex_rule':flex_rule,'rjhunt':rjhunt_rule}
    return render(request,'event/media.html',context)

def eventCompairing(request):
    compairing = PerformingEvent.objects.filter(cell=7)
    context={'compairing':compairing}
    return render(request,'event/compairing.html',context)

def eventDecoration(request):
    decoration = PerformingEvent.objects.filter(cell=8)
    context={'decoration':decoration}
    return render(request,'event/decoration.html',context)

def eventLiterati(request):
    graffiti = EventName.objects.get(event_name="Graffiti")
    graffiti_rule = RulesOfEvent.objects.filter(event_name=56)
    gd = EventName.objects.get(event_name="Group Discussion")
    gd_rule =RulesOfEvent.objects.filter(event_name=57)
    debate = EventName.objects.get(event_name="Debate")
    debate_rule = RulesOfEvent.objects.filter(event_name=58)
    mm = EventName.objects.get(event_name="Maymay Mania")
    mm_rule = RulesOfEvent.objects.filter(event_name=59)
    tf = EventName.objects.get(event_name="Trivia Fever")
    tf_rule = RulesOfEvent.objects.filter(event_name=60)
    ppd = EventName.objects.get(event_name="PPD")
    ppd_rule = RulesOfEvent.objects.filter(event_name=61)
    pictionary = EventName.objects.get(event_name="Pictionary")
    pictionary_rule = RulesOfEvent.objects.filter(event_name=62)
    tat = EventName.objects.get(event_name="Twist & Tale")
    tat_rule = RulesOfEvent.objects.filter(event_name=63)
    om = EventName.objects.get(event_name="Open Mic")
    om_rule = RulesOfEvent.objects.filter(event_name=64)
    rc = EventName.objects.get(event_name="Reader's Circle")
    rc_rule = RulesOfEvent.objects.filter(event_name=65)
    ss = EventName.objects.get(event_name="Scripturesqueue")
    ss_rule = RulesOfEvent.objects.filter(event_name=66)
    jam = EventName.objects.get(event_name="JAM")
    jam_rule = RulesOfEvent.objects.filter(event_name=67)
    dc = EventName.objects.get(event_name="Doodler's Combat")
    dc_rule = RulesOfEvent.objects.filter(event_name=68)
    context={'graffiti':graffiti, 'graffiti_rule':graffiti_rule, 'gd':gd, 'gd_rule':gd_rule, 'debate':debate, 'debate_rule':debate_rule, 'mm':mm, 'mm_rule':mm_rule, 'tf':tf, 'tf_rule':tf_rule, 'ppd':ppd, 'ppd_rule':ppd_rule, 'pictionary':pictionary, 'pictionary_rule':pictionary_rule, 'tat':tat, 'tat_rule':tat_rule, 'om':om, 'om_rule':om_rule, 'rc':rc, 'rc_rule':rc_rule, 'ss':ss, 'ss_rule':ss_rule, 'jam':jam, 'jam_rule':jam_rule, 'dc':dc, 'dc_rule':dc_rule}
    return render(request, 'event/literati.html', context)

def eventCreative(request):
    ccc = PerformingEvent.objects.filter(cell=9)
    artgallery = EventName.objects.get(event_name="Art Gallery")
    artgallery_rule = RulesOfEvent.objects.filter(event_name=37)
    baw = EventName.objects.get(event_name="Black & White")
    baw_rule = RulesOfEvent.objects.filter(event_name=39)
    pencilsketching = EventName.objects.get(event_name="On Spot Pencil Sketching")
    pencilsketching_rule = RulesOfEvent.objects.filter(event_name=38)
    themepainting = EventName.objects.get(event_name="Theme Painting")
    themepainting_rule = RulesOfEvent.objects.filter(event_name=40)
    rangoli = EventName.objects.get(event_name="Rangoli")
    rangoli_rule = RulesOfEvent.objects.filter(event_name=41)
    paintnspray = EventName.objects.get(event_name="Paint & Spray")
    paintnspray_rule = RulesOfEvent.objects.filter(event_name=42)
    context={'ccc':ccc,'artgallery':artgallery,'artgallery_rule':artgallery_rule,'baw':baw,'baw_rule':baw_rule,'pencilsketching':pencilsketching,'pencilsketching_rule':pencilsketching_rule,'themepainting':themepainting,'themepainting_rule':themepainting_rule,'rangoli':rangoli,'rangoli_rule':rangoli_rule,'paintnspray':paintnspray,'paintnspray_rule':paintnspray_rule}
    return render(request,'event/creative.html',context)

def eventNewspaper(request):
    ypia = EventName.objects.get(event_name='You Peek I Answer')
    ypia_rule = RulesOfEvent.objects.filter(event_name=69)
    fq = EventName.objects.get(event_name='Fun Quiz')
    fq_rule = RulesOfEvent.objects.filter(event_name=70)
    context = {'ypia':ypia, 'ypia_rule':ypia_rule, 'fq':fq, 'fq_rule':fq_rule}
    return render(request, 'event/newspaper.html', context)

def eventInformal(request):
    graffiti = EventName.objects.get(event_name="Graffiti")
    graffiti_rule = RulesOfEvent.objects.filter(event_name=56)
    gd = EventName.objects.get(event_name="Group Discussion")
    gd_rule =RulesOfEvent.objects.filter(event_name=57)
    debate = EventName.objects.get(event_name="Debate")
    debate_rule = RulesOfEvent.objects.filter(event_name=58)
    mm = EventName.objects.get(event_name="Maymay Mania")
    mm_rule = RulesOfEvent.objects.filter(event_name=59)
    tf = EventName.objects.get(event_name="Trivia Fever")
    tf_rule = RulesOfEvent.objects.filter(event_name=60)
    ppd = EventName.objects.get(event_name="PPD")
    ppd_rule = RulesOfEvent.objects.filter(event_name=61)
    pictionary = EventName.objects.get(event_name="Pictionary")
    pictionary_rule = RulesOfEvent.objects.filter(event_name=62)
    tat = EventName.objects.get(event_name="Twist & Tale")
    tat_rule = RulesOfEvent.objects.filter(event_name=63)
    om = EventName.objects.get(event_name="Open Mic")
    om_rule = RulesOfEvent.objects.filter(event_name=64)
    rc = EventName.objects.get(event_name="Reader's Circle")
    rc_rule = RulesOfEvent.objects.filter(event_name=65)
    ss = EventName.objects.get(event_name="Scripturesqueue")
    ss_rule = RulesOfEvent.objects.filter(event_name=66)
    jam = EventName.objects.get(event_name="JAM")
    jam_rule = RulesOfEvent.objects.filter(event_name=67)
    dc = EventName.objects.get(event_name="Doodler's Combat")
    dc_rule = RulesOfEvent.objects.filter(event_name=68)
    context={'graffiti':graffiti, 'graffiti_rule':graffiti_rule, 'gd':gd, 'gd_rule':gd_rule, 'debate':debate, 'debate_rule':debate_rule, 'mm':mm, 'mm_rule':mm_rule, 'tf':tf, 'tf_rule':tf_rule, 'ppd':ppd, 'ppd_rule':ppd_rule, 'pictionary':pictionary, 'pictionary_rule':pictionary_rule, 'tat':tat, 'tat_rule':tat_rule, 'om':om, 'om_rule':om_rule, 'rc':rc, 'rc_rule':rc_rule, 'ss':ss, 'ss_rule':ss_rule, 'jam':jam, 'jam_rule':jam_rule, 'dc':dc, 'dc_rule':dc_rule}
    return render(request,'event/informal.html',context)

@login_required(login_url = 'login')
def registration(request, cell, event_naam, team):
    volunteer = request.user
    cell = cell.replace('_', " ")
    event_naam = event_naam.replace('_', " ")
    event_id = EventName.objects.get(event_name=event_naam)
    event_rule = RulesOfEvent.objects.filter(event_name=event_id)
    cell_id = CellName.objects.get(cell_name=cell)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        college_rn = request.POST.get('college_rn')
        city = request.POST.get('city')
        t = request.POST.get('team')
        form = Registration(volunteer=volunteer, cell=cell_id, event_name=event_id, name=name, email=email, phone=phone, college=college, college_rn=college_rn, city=city, team=t)
        if Registration.objects.filter(volunteer=volunteer, event_name=event_id).exists():
            messages.error(request,'You have already registered for this event!')
        else:
            try:
                form.save()
                event_register_mail(name=name, email=email, event=event_naam, date=event_id.event_date.strftime("%d/%m/%Y"), cell=cell)
                return redirect('thankyou')
            except:
                return HttpResponse("Error!")
    context={'event_naam':event_naam,'event_rule':event_rule,'team':team}
    return render(request,'registration.html',context)

@login_required(login_url = 'login')
def thankyou(request):
    context={}
    return render(request,'thankyou.html',context)


def developers(request):
    tt = TechnicalTeam.objects.all()
    context = {'tt':tt}
    return render(request, 'developers.html', context)


    """
def developers(request):
    context={}
    return render(request,'developers.html',context)
    """
