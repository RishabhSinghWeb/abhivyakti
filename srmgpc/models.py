
from django.db import models
from django.contrib.auth.models import User
import qrcode 
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.


class Volunteer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,on_delete=models.CASCADE)
    name_admin = models.CharField(max_length=200,default="", null=True)
    name = models.CharField(max_length=200,default="", null=True)
    phone = models.CharField(max_length=200,default="", null=True)
    email = models.CharField(max_length=200,default="", null=True)
    college = models.CharField(max_length=200,default="", null=True)
    profile_pic = models.ImageField(upload_to='profile',default='profile.png',null=True,blank=True)
    qr_code = models.ImageField(upload_to='',blank=True)
    
    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        userr = str(self.user)
        qrcode_img = qrcode.make(f'http://127.0.0.1:8000/profile/{userr}/')
        canvas = Image.new('RGB',(400,400),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{userr}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)



class CellName(models.Model):
    cell_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.cell_name


class CompetitionName(models.Model):
    cell = models.ForeignKey(CellName, null=True,on_delete=models.SET_NULL)
    competition_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.competition_name




class TeamPost(models.Model):
    post_name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.post_name



BRANCH=(
    ('EE','EE'),
    ('ECE','ECE'),
    ('CSE','CSE'),
    ('IT','IT'),
    ('ME','ME'),
    ('CE','CE'),
    ('BBA','BBA'),
    ('BCA','BCA'),
    ('MBA','MBA'),
)
YEARS=(
    ('1st year','1st year'),
    ('2nd year', '2nd year'),
    ('3rd year', '3rd year'),
    ('4th year', '4th year'),
)
CELLPOST =(
    ('Coordinator','Coordinator'),
    ('Assistant Coordinator','Assistant Coordinator'),
)


class TeamMemberName(models.Model):
    post = models.ForeignKey(TeamPost, null=True,on_delete=models.SET_NULL)
    cell = models.ForeignKey(CellName,null=True,blank=True,help_text='only for Coordinator Post',on_delete=models.SET_NULL)
    cell_post = models.CharField(max_length=200,null=True,help_text='only for Coordinator Post',blank=True,choices=CELLPOST)
    name = models.CharField(max_length=200,null=True,default='')
    branch = models.CharField(max_length=100,blank=True,choices=BRANCH)
    year = models.CharField(max_length=100,blank=True,choices=YEARS)
    linkedin = models.CharField(max_length=500,null=True,blank=True)
    instagram = models.CharField(max_length=500,null=True,blank=True)
    facebook = models.CharField(max_length=500,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='team-profile',default='profile.png',null=True,blank=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    first_name = models.CharField(max_length=30,null=True,default='')
    last_name = models.CharField(max_length=30,null=True,default='')
    email = models.EmailField(max_length=30,null=True,default='')
    phone = models.CharField(max_length=30,null=True,default='')
    message = models.CharField(max_length=500,null=True,default='')

    def __str__(self):
        name = self.first_name+"_"+self.last_name
        return name


class EventName(models.Model):
    event_name = models.CharField(max_length=300, null=True)
    cell = models.ForeignKey(CellName,null=True,blank=True,on_delete=models.SET_NULL)
    place = models.CharField(max_length=100,blank=True,null=True,help_text="place of the event")
    coordinator = models.CharField(max_length=100,blank=True,null=True,help_text="coordinator name for the event")
    contact = models.CharField(max_length=100,blank=True,null=True,help_text="number of the coordinator")
    event_date = models.DateField()
    

    def __str__(self):
        return self.event_name


POSITION=(
    ('1st','1st'),
    ('2nd','2nd'),
    ('3rd','3rd'),
)

class EventResult(models.Model):
    event_name = models.ForeignKey(EventName, null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=200,null=True,help_text='participant name')
    college = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Update(models.Model):
    news_detail = models.CharField(max_length=400,null=True)
    update_time = models.TimeField(auto_now=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.news_detail

class RulesOfEvent(models.Model):
    event_name = models.ForeignKey(EventName, null=True,on_delete=models.SET_NULL)
    rule_number = models.CharField(max_length=10,null=True)
    rule = models.CharField(max_length=1000,default='',null=True)

    def __str__(self):
        return self.rule_number


class PerformingEvent(models.Model):
    cell = models.ForeignKey(CellName, null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=100,null=True,help_text="name of performing event(in capital letter)")
    about = models.CharField(max_length=1000,null=True,help_text="about the event")

    def __str__(self):
        return self.name


class Registration(models.Model):
    volunteer = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    cell = models.ForeignKey(CellName, null=True,on_delete=models.SET_NULL)
    event_name = models.ForeignKey(EventName, null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    college = models.CharField(max_length=200,null=True)
    college_rn = models.CharField(max_length=100,null=True,blank=True,default='')
    phone = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now=True)
    team = models.CharField(max_length=200,null=True,blank=True,default='NA')

    def __str__(self):
        return self.name


class TechnicalTeam(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ImageField(upload_to='tt-profile',default='profile.png',null=True,blank=True)
    name = models.CharField(max_length=60, null=True)
    branch = models.CharField(max_length=200, null=True)
    insta = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    fb = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name




