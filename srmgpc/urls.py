from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # home page
    path('',views.index,name='home'),
    path('home/',views.home,name='homepage'),

    # register system
    path('signup/',views.signupPage,name='signup'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),

    # dashboard
    path('adminpage/',views.adminPage,name='adminpage'),
    path('userdashboard/',views.userPage,name='userpage'),

    # public event
    path('starnight/',views.starnight,name='starnight'),
    path('xeronight/',views.xeronight,name='xeronight'),

    #team and event
    path('team/',views.team,name='teampage'),
    path('events/',views.events,name='eventpage'),
    
    #result & updates of events
    path('updates/',views.updates,name='updates'),

    # abhivyakti details 
    path('about/',views.about,name='about'),

    #profile for admin
    path('profile/<str:user>/',views.profile,name='profile'),

    # developers page
    path('developers/',views.developers,name='developers'),

    # cell event page links urls
    path('events/choreography_cell/',views.eventChoreography,name='eventChoreography'),
    path('events/euphony_cell/',views.eventEuphony,name='eventEuphony'),
    path('events/dracula_cell/',views.eventDracula,name='eventDracula'),
    path('events/ritumbhara_cell/',views.eventRitumbhara,name='eventRitumbhara'),
    path('events/photography_cell/',views.eventPhotography,name='eventPhotography'),
    path('events/media_cell/',views.eventMedia,name='eventMedia'),
    path('events/compairing_cell/',views.eventCompairing,name='eventCompairing'),
    path('events/decoration_cell/',views.eventDecoration,name='eventDecoration'),
    path('events/creative_canvas_club/',views.eventCreative,name='eventCreative'),
    path('events/informal_cell/',views.eventInformal,name='eventInformal'),
    path('events/literati_cell/',views.eventLiterati,name='eventLiterati'),
    path('events/newspaper_cell/',views.eventNewspaper,name='eventNewspaper'),

    #registration
    path('registration/<str:cell>/<str:event_naam>/<str:team>/',views.registration,name='registration'),
    path('delete/<int:id>/',views.deleteRegistrations,name='delete'),
    path('thankyou/',views.thankyou,name='thankyou'),


    
]