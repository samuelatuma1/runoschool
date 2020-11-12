from django.shortcuts import render

schoolName = ['Runo Dayspring School', 'Runo Dayspring']     
#Make the necessary imports

# Additional imports we'll need:
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse


#Import access to only admin user
from django.contrib.admin.views.decorators import staff_member_required

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# THIS IMPORT ALLOWS US TO SEND Email to a user in django
from django.core.mail import send_mail


#Start coding here
# Import the necessary models
from .models import Photos, WelcImgs, WelcLeaders, News, Welcometab, Welcometab2, Welcometab3, Welcometab4, newsDetail, about
from .models import about2, about3, Steps, admitfiles, Logo, Footerdetails, Footerabout, Footercontact

#Imports for Footers
logo = Logo.objects.filter(pk=1).first()
Footerdetail = Footerdetails.objects.filter(pk=1).first()
Footerabout1 = Footerabout.objects.filter(pk=1).first()


    #Create a form that takes from photos
class PhotosForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('photo', 'desc', 'position')

    #Create a form that takes from WelcImgs
class WelcImgsForm(forms.ModelForm):
    class Meta:
        model = WelcImgs
        fields = ('welcImg', 'extraImg1', 'extraImg2')

    #CReate form that takes from WelcLeaders
class WelcLeadersForm(forms.ModelForm):
    class Meta:
        model = WelcLeaders
        fields = ('welcLeader', 'extraLeader1', 'extraLeader2')

    #Create form that takes from News
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('newsImg', 'desc', 'position')

#This is where we define the classes for our welcome page
class Welcometab1Form(forms.ModelForm):
    class Meta:
        model = Welcometab
        fields = ('writeHead1', 'write1')

class Welcometab2Form(forms.ModelForm):
    class Meta:
        model = Welcometab2
        fields = ('writeHead2', 'write2')

class Welcometab3Form(forms.ModelForm):
    class Meta:
        model = Welcometab3
        fields = ('email1', 'email2', 'contact1', 'contact2')

class Welcometab4Form(forms.ModelForm):
    class Meta:
        model = Welcometab4
        fields = ('file1', 'displayName1', 'file2', 'displayName2')

# Create your views here.

# Create url for admin to modify  photos from 
def adminindex(request):
    photos = Photos.objects.all()
    news = News.objects.all()
    total = WelcImgs.objects.count()
    WelcImg = WelcImgs.objects.filter(pk=int(1)).first()

    totalL = WelcLeaders.objects.count()
    WelcLeader = WelcLeaders.objects.filter(pk=int(1)).first()

    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    if request.method == 'POST':
        form = PhotosForm(request.POST, request.FILES)
        formWelcImgs = WelcImgsForm(request.POST, request.FILES)
        formWelcLeaders = WelcLeadersForm(request.POST, request.FILES)
        formNews = NewsForm(request.POST, request.FILES)



        if formNews.is_valid() and not form.is_valid() and not formWelcLeaders.is_valid():
            pos = int(formNews.cleaned_data['position'])
            photo = formNews.cleaned_data['newsImg'] 
            desc = formNews.cleaned_data['desc']
            position = formNews.cleaned_data['position']

            occupy = News.objects.filter(pk=pos).first()
            if occupy:
                occupy.newsImg = photo
                occupy.desc = desc
                occupy.position = position
                occupy.save()
                return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs,
                'form': form,'msg': "Successfully uploaded to News", 'photos': photos, 
                'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 'WelcLeader': WelcLeader
                ,'news': news, 'formNews': formNews,
                'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                'contactFooter': contactFooter })
            else:
                formNews.save()
                return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs,
                'form': form,'msg': "Successfully uploaded to News", 'photos': photos, 
                'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 'WelcLeader': WelcLeader
                ,'news': news, 'formNews': formNews,
                'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                'contactFooter': contactFooter })


        elif form.is_valid() and not formWelcImgs.is_valid() and not formWelcLeaders.is_valid():
            pos = int(form.cleaned_data['position']) + 19 #Note, please remove 19 later on. it was added because the database already had 19 items on it
            photo = form.cleaned_data['photo'] 
            desc = form.cleaned_data['desc']
            position = form.cleaned_data['position']

            occupy = Photos.objects.filter(pk=pos).first()
            if occupy:
                occupy.photo = photo
                occupy.desc = desc
                occupy.position = position
                occupy.save()
                return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs,
                'form': form,'msg': "Successfully uploaded to images", 'photos': photos, 
                'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 'WelcLeader': WelcLeader
                ,'news': news, 'formNews': formNews})
            else:
                form.save()
                return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs,
                'form': form,'msg': "Successfully uploaded to images", 'photos': photos, 
                'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 'WelcLeader': WelcLeader
                ,'news': news, 'formNews': formNews})

        #This part dictates the image that'll be displayed on page that will redirect to welcome to a particular session            
        elif formWelcImgs.is_valid() and not form.is_valid() and not formWelcLeaders.is_valid():
            formWelcImgs = WelcImgsForm(request.POST, request.FILES)
            if formWelcImgs.is_valid():
                welcImg = formWelcImgs.cleaned_data['welcImg']
                extraImg1 = formWelcImgs.cleaned_data['extraImg1']
                extraImg2 = formWelcImgs.cleaned_data['extraImg2']

                occupy = WelcImgs.objects.filter(pk=1).first()
                if occupy:
                    occupy.welcImg = welcImg
                    occupy.extraImg1 = extraImg1
                    occupy.extraImg2 = extraImg2
                    occupy.save()

                
                
                    return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs,
                    'form': form, 'msg': "Successfully uploaded to images", 'photos': photos, 
                    'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 'WelcLeader': WelcLeader
                    ,'news': news, 'formNews': formNews})
                else:
                    formWelcImgs.save()
                    return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs,
                    'form': form, 'msg': "Successfully uploaded to images", 'photos': photos, 
                    'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 'WelcLeader': WelcLeader
                    ,'news': news, 'formNews': formNews})
                    
        elif formWelcLeaders.is_valid() and not form.is_valid() and not formWelcImgs.is_valid():
            formWelcLeaders = WelcLeadersForm(request.POST, request.FILES)
            if formWelcLeaders.is_valid():
                
                
                welcLeader = formWelcLeaders.cleaned_data['welcLeader']
                extraLeader1 = formWelcLeaders.cleaned_data['extraLeader1']
                extraLeader2 = formWelcLeaders.cleaned_data['extraLeader2']

                occupy = WelcLeaders.objects.filter(pk=1).first()
                if occupy:
                    occupy.welcLeader = welcLeader
                    occupy.extraLeader1 = extraLeader1
                    occupy.extraLeader2 = extraLeader2
                    occupy.save()

                
                
                    return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs,
                    'form': form, 'msg': "Successfully uploaded to images", 'photos': photos, 
                    'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 'WelcLeader': WelcLeader
                    ,'news': news, 'formNews': formNews})
                else:
                    formWelcLeaders.save()


                    return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs,
                    'form': form, 'msg': "Successfully uploaded to images", 'photos': photos, 
                    'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 'WelcLeader': WelcLeader
                    ,'news': news, 'formNews': formNews})

        

    else:
        form = PhotosForm()
        formWelcImgs = WelcImgsForm()
        formWelcLeaders= WelcLeadersForm()
        formNews = NewsForm()

        return render(request, 'runo/adminindex.html', {'formWelcImgs': formWelcImgs, 
        'form': form, 'photos': photos, 'WelcImg': WelcImg, 'formWelcLeaders': formWelcLeaders, 
        'WelcLeader': WelcLeader ,'news': news, 'formNews': formNews})


# This page returns the homepage for users of the site
def index(request):
    photos=Photos.objects.all()

    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()
    
    
    WelcImg = WelcImgs.objects.filter(pk=1).first()
    
    WelcLeader = WelcLeaders.objects.filter(pk=2).first()
    news = News.objects.all()
    return render(request, 'runo/index.html', {'photos': photos, 'WelcImg': WelcImg, 'WelcLeader': WelcLeader,
    'news': news,
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter})


def adminwelcome(request):
    form1 = Welcometab1Form(request.POST, request.FILES)
    form2 = Welcometab2Form(request.POST)
    form3 = Welcometab3Form(request.POST)
    form4 = Welcometab4Form(request.POST, request.FILES)

    pos4 = Welcometab4.objects.filter(pk=1).first()

    
    if request.method =='POST':
        form1 = Welcometab1Form(request.POST, request.FILES)
        form2 = Welcometab2Form(request.POST, request.FILES)
        form3 = Welcometab3Form(request.POST, request.FILES)
        form4 = Welcometab4Form(request.POST, request.FILES)
        if form1.is_valid() and not form2.is_valid():   
            writeHead1 = form1.cleaned_data['writeHead1']
            write1 = form1.cleaned_data['write1']

            pos = Welcometab.objects.filter(pk=1).first()
            pos2 = Welcometab2.objects.filter(pk=1).first()
            pos3 = Welcometab3.objects.filter(pk=1).first()
        
            if pos:
                pos.writeHead1 = writeHead1
                pos.write1 = write1
                pos.img1 = WelcImgs.objects.filter(pk=1).first()
                pos.save()
                return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2': pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

            else:
                form1.save()
                return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2':pos2,'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

        
        elif form2.is_valid() and not form1.is_valid():
            writeHead2 = form2.cleaned_data['writeHead2']
            write2 = form2.cleaned_data['write2']

            pos = Welcometab.objects.filter(pk=1).first()
            pos2 = Welcometab2.objects.filter(pk=1).first()
            pos3 = Welcometab3.objects.filter(pk=1).first()
            if pos2:
                pos2.writeHead2 = writeHead2
                pos2.write2 = write2
                pos2.img2 = WelcImgs.objects.get(pk=1)
                pos2.save()
                return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

            else:
                form2.save()
                return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })


        elif form3.is_valid() and not form1.is_valid():
            email1 = form3.cleaned_data['email1']
            email2 = form3.cleaned_data['email2']

            contact1 = form3.cleaned_data['contact1']
            contact2 = form3.cleaned_data['contact2']

            pos = Welcometab.objects.filter(pk=1).first()
            pos2 = Welcometab2.objects.filter(pk=1).first()
            pos3 = Welcometab3.objects.filter(pk=1).first()
            
            if pos3:
                pos3.email1 = email1
                pos3.email2 = email2
                pos3.contact1 = contact1
                pos3.contact2 = contact2

                pos3.save()
                return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

            else:
                form3.save()
                return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

        elif form4.is_valid():
            file1 = form4.cleaned_data['file1']
            displayName1 = form4.cleaned_data['displayName1']
            file2 = form4.cleaned_data['file2']
            displayName2 = form4.cleaned_data['displayName2']

            pos = Welcometab.objects.filter(pk=1).first()
            pos2 = Welcometab2.objects.filter(pk=1).first()
            pos3 = Welcometab3.objects.filter(pk=1).first()

            pos4 = Welcometab4.objects.filter(pk=1).first()

            if pos4:
                pos4.file1 = file1
                pos4.displayName1 = displayName1

                pos4.file2 = file2
                pos4.displayName2 = displayName2
                
                pos4.save()

                return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

            else:
                form4.save()
                return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })
        
    pos = Welcometab.objects.filter(pk=1).first()
    pos2 = Welcometab2.objects.filter(pk=1).first()
    pos3 = Welcometab3.objects.filter(pk=1).first()
    
    return render(request, 'runo/adminwelcome.html', {'pos': pos, 'pos2': pos2, 'pos3': pos3, 'pos4': pos4,
        'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
    })

def welcome(request):
    pos = Welcometab.objects.filter(pk=1).first()
    pos2 = Welcometab2.objects.filter(pk=1).first()
    pos3 = Welcometab3.objects.filter(pk=1).first()
    pos4 = Welcometab4.objects.filter(pk=1).first()

    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()


    return render(request, 'runo/welcome.html', {'pos': pos, 'pos2': pos2, 'pos3': pos3, 'pos4': pos4,
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter
    
    })

def adminleadership(request):
    

    pos = Welcometab.objects.filter(pk=2).first()
    pos2 = Welcometab2.objects.filter(pk=2).first()
    pos3 = Welcometab3.objects.filter(pk=2).first()
    pos4 = Welcometab4.objects.filter(pk=2).first()

    
    if request.method =='POST':
        form1 = Welcometab1Form(request.POST, request.FILES)
        form2 = Welcometab2Form(request.POST, request.FILES)
        form3 = Welcometab3Form(request.POST, request.FILES)
        form4 = Welcometab4Form(request.POST, request.FILES)
        if form1.is_valid() and not form2.is_valid():   
            writeHead1 = form1.cleaned_data['writeHead1']
            write1 = form1.cleaned_data['write1']

            
        
            if pos:
                pos.writeHead1 = writeHead1
                pos.write1 = write1
                pos.img1L = WelcLeaders.objects.filter(pk=1).first()
                pos.save()
                return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2': pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

            else:
                form1.save()
                return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2':pos2,'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

        
        elif form2.is_valid() and not form1.is_valid():
            writeHead2 = form2.cleaned_data['writeHead2']
            write2 = form2.cleaned_data['write2']

            if pos2:
                pos2.writeHead2 = writeHead2
                pos2.write2 = write2
                pos2.img2L = WelcLeaders.objects.filter(pk=1).first()
                pos2.save()
                return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

            else:
                form2.save()
                return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })


        elif form3.is_valid() and not form1.is_valid():
            email1 = form3.cleaned_data['email1']
            email2 = form3.cleaned_data['email2']

            contact1 = form3.cleaned_data['contact1']
            contact2 = form3.cleaned_data['contact2']

            
            if pos3:
                pos3.email1 = email1
                pos3.email2 = email2
                pos3.contact1 = contact1
                pos3.contact2 = contact2

                pos3.save()
                return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

            else:
                form3.save()
                return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

        elif form4.is_valid():
            file1 = form4.cleaned_data['file1']
            displayName1 = form4.cleaned_data['displayName1']
            file2 = form4.cleaned_data['file2']
            displayName2 = form4.cleaned_data['displayName2']


            if pos4:
                pos4.file1 = file1
                pos4.displayName1 = displayName1

                pos4.file2 = file2
                pos4.displayName2 = displayName2
                
                pos4.save()

                return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

            else:
                form4.save()
                return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2':pos2, 'pos3': pos3, 'pos4': pos4,
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
                })

    form1 = Welcometab1Form()
    form2 = Welcometab2Form()
    form3 = Welcometab3Form()
    form4 = Welcometab4Form()
    return render(request, 'runo/adminleader.html', {'pos': pos, 'pos2': pos2, 'pos3': pos3, 'pos4': pos4,
        'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4
    })

def leadership(request):
    pos = Welcometab.objects.filter(pk=2).first()
    pos2 = Welcometab2.objects.filter(pk=2).first()
    pos3 = Welcometab3.objects.filter(pk=2).first()
    pos4 = Welcometab4.objects.filter(pk=2).first()

    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    return render(request, 'runo/leader.html', {'pos': pos, 'pos2': pos2, 'pos3': pos3, 'pos4': pos4,
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter
       
    })


class newsDetailForm(forms.ModelForm):
    class Meta:
        model = newsDetail
        fields = ('newsBody', )

def adminrunonews(request, news_id):

    id = news_id
    form = newsDetailForm()
    editNews = News.objects.filter(pk=int(id)).first()
    upload = newsDetail.objects.filter(pk=int(id)).first()
    news = News.objects.all()

    if request.method == 'POST':
        form = newsDetailForm(request.POST)
        if form.is_valid():
            upload = newsDetail.objects.filter(pk=int(id)).first()
            if upload:
                

                upload.newsBody = form.cleaned_data['newsBody']
                upload.save()
                return render(request, 'runo/adminrunonews.html', {'form': form, 'id': id, 'editNews': editNews,
                'upload': upload, 'news': news})
            else:
                form.save()
                return render(request, 'runo/adminrunonews.html', {'form': form, 'id': id, 'editNews': editNews,
                'upload': upload, 'news': news})
                
            


     
    return render(request, 'runo/adminrunonews.html', {'form': form, 'id': id, 'editNews': editNews,
     'upload': upload, 'news': news})


def runonews(request, news_id):
    id = news_id
    
    editNews = News.objects.filter(pk=int(id)).first()
    upload = newsDetail.objects.filter(pk=int(id)).first()
    news = News.objects.all()

      #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()


    return render(request, 'runo/runonews.html', {'id': id, 'editNews': editNews,
     'upload': upload, 'news': news,
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter})




class aboutForm(forms.ModelForm):
    class Meta:
        model = about
        fields = ('img', 'title', 'body')

class about2Form(forms.ModelForm):
    class Meta:
        model = about2
        fields = ('img2', 'title2', 'body2')

class about3Form(forms.ModelForm):
    class Meta:
        model = about3
        fields = ('img3', 'title3', 'body3')

def adminaboutus(request):
    form1 = aboutForm()
    form2 = about2Form()
    form3 = about3Form()
    allAbout = about.objects.all()
    allAbout2 = about2.objects.all()
    allAbout3 = about3.objects.all()
    

    if request.method == 'POST':
        form1 = aboutForm(request.POST, request.FILES)
        form2 = about2Form(request.POST, request.FILES)
        form3 = about3Form(request.POST, request.FILES)
        

        if form1.is_valid() and not form2.is_valid():
            
            upload = about.objects.filter(pk=1).first()
            if upload:
                upload.img = form1.cleaned_data['img']
                upload.title = form1.cleaned_data['title']
                upload.body = form1.cleaned_data['body']

                upload.save()
                return render(request, 'runo/adminaboutus.html', {'form1': form1,
                 'form2': form2, 'form3': form3, 'allAbout': allAbout,
                 'allAbout2': allAbout2, 'allAbout3': allAbout3 })

            else:
                form1.save()
                return render(request, 'runo/adminaboutus.html', {'form1': form1,
                 'form2': form2, 'form3': form3, 'allAbout': allAbout,
                 'allAbout2': allAbout2, 'allAbout3': allAbout3 })

        elif form2.is_valid():
            
            upload = about2.objects.filter(pk=1).first()
            if upload:
                upload.img2 = form2.cleaned_data['img2']
                upload.title2 = form2.cleaned_data['title2']
                upload.body2 = form2.cleaned_data['body2']

                upload.save()
                return render(request, 'runo/adminaboutus.html', {'form1': form1,
                 'form2': form2, 'form3': form3, 'allAbout': allAbout,
                 'allAbout2': allAbout2, 'allAbout3': allAbout3 })

            else:
                form2.save()
                return render(request, 'runo/adminaboutus.html', {'form1': form1,
                 'form2': form2, 'form3': form3, 'allAbout': allAbout,
                 'allAbout2': allAbout2, 'allAbout3': allAbout3 })

        elif form3.is_valid():
            
            upload = about3.objects.filter(pk=1).first()
            if upload:
                upload.img3 = form3.cleaned_data['img3']
                upload.title3 = form3.cleaned_data['title3']
                upload.body3 = form3.cleaned_data['body3']

                upload.save()
                return render(request, 'runo/adminaboutus.html', {'form1': form1,
                 'form2': form2, 'form3': form3, 'allAbout': allAbout,
                 'allAbout2': allAbout2, 'allAbout3': allAbout3 })

            else:
                form3.save()
                return render(request, 'runo/adminaboutus.html', {'form1': form1,
                 'form2': form2, 'form3': form3, 'allAbout': allAbout,
                 'allAbout2': allAbout2, 'allAbout3': allAbout3 })
            
        
        

    return render(request, 'runo/adminaboutus.html', {'form1': form1, 'form2': form2, 'form3': form3, 'allAbout': allAbout,
    'allAbout2': allAbout2, 'allAbout3': allAbout3 })

def aboutus(request):
    allAbout = about.objects.all()
    allAbout2 = about2.objects.all()
    allAbout3 = about3.objects.all()

      #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    return render(request, 'runo/aboutus.html', { 'allAbout': allAbout, 
    'allAbout2': allAbout2, 'allAbout3': allAbout3,
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter})

class StepsForm(forms.ModelForm):
    class Meta:
        model = Steps
        fields = ('step', 'position')

class admitfilesForm(forms.ModelForm):
    class Meta:
        model = admitfiles
        fields = ('file1', 'name1', 'file2', 'name2', 'file3', 'name3')


def adminadmission(request):
    form = StepsForm()
    steps = Steps.objects.all()

    admitform = admitfilesForm()
    posit = admitfiles.objects.filter(pk=1).first()

    if request.method == 'POST':
        form = StepsForm(request.POST)
        admitform = admitfilesForm(request.POST, request.FILES)

        if form.is_valid():
            step = form.cleaned_data['step']
            position = form.cleaned_data['position']

            pos = Steps.objects.filter(pk=int(position)).first()
            if pos:
                pos.step = step
                pos.position = position
                pos.save()
                return render(request, 'runo/adminadmission.html', {'form': form, 'steps': steps
                , 'posit': posit})
            else:
                form.save()
                return render(request, 'runo/adminadmission.html', {'form': form, 'steps': steps,
                'admitform': admitform, 'posit': posit})

        elif admitform.is_valid():
            posit = admitfiles.objects.filter(pk=1).first()

            if posit:
                posit.file1 = admitform.cleaned_data['file1']
                posit.name1 = admitform.cleaned_data['name1']
                posit.file2 = admitform.cleaned_data['file2']
                posit.name2 = admitform.cleaned_data['name2']
                posit.file3 = admitform.cleaned_data['file3']
                posit.name3 = admitform.cleaned_data['name3']
                posit.save()
            else:
                admitform.save()
                return render(request, 'runo/adminadmission.html', {'form': form, 'steps': steps,
                'admitform': admitform, 'posit': posit})



    return render(request, 'runo/adminadmission.html', {'form': form, 'steps': steps,
     'admitform': admitform, 'posit': posit})

def admission(request):
    posit = admitfiles.objects.filter(pk=1).first()
    steps = Steps.objects.all()
    school = Footerdetails.objects.filter(pk=1).first().school_name
    
    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    return render(request, 'runo/admission.html', {'steps': steps, 'school': school,
    'posit': posit,
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter})


# This part below is related to school
from django.shortcuts import render

from django.shortcuts import render

from .models import Nursery1, Nursery2, Class

# Additional imports we'll need:
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse


#Import access to only admin user
from django.contrib.admin.views.decorators import staff_member_required

from django import forms

# THIS IMPORT ALLOWS US TO SEND Email to a user in django
from django.core.mail import send_mail



class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('classRoom', 'password')

class ClassForm2(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('classRoom',)



# Create your views here.


def teacher(request):
    classForm = ClassForm()
    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()
   
    
    if request.method == 'POST':
        # Teacher allows a teacher that have access to a classroom view and maybe modify the contents of the class

        #AllClasses was included here, so that on every post, 
        #it makes a new request to the class Table, and returns with updated data
        AllClasses = {
            'Nursery1': Nursery1.objects.filter(status='active').all(),
            'Nursery2': Nursery2.objects.filter(status='active').all()
            }

        #Ensure the teacher has the right login credentials
        classForm = ClassForm(request.POST)
        if classForm.is_valid():
            classRoom = classForm.cleaned_data['classRoom']
            password = classForm.cleaned_data['password']

            #If the teacher has the right login details, log her into the classRoom
            classTeacher = Class.objects.filter(classRoom=classRoom).filter(password=password)
            
            if classTeacher:
                #Get the classRoom of the particular Teacher
                #classDetails returns he list of all the pupils in the classRoom
                classDetails = AllClasses[classRoom]

                #Return a html passing in classDetails and classRoom as arguments
                return render(request, 'school/classDetails.html', {
                    'classDetails': classDetails, 'classRoom': classRoom,
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })

                
                

            else:
                #If teacher doesnt have the correct login credentials, return to this page
                return render(request, 'school/classLogin.html', {
                    'classForm': classForm, 'msg': 'Invalid class or password, please try again',
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })
            

    return render(request, 'school/classLogin.html', {
        'classForm': classForm,
        'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
        'contactFooter': contactFooter
    })



#Here, we attempt to update pupil's result
# All the classes will be represented here
AllClass = {
    'Nursery1': Nursery1,   
    'Nursery2': Nursery2
}
def result(request):
    classForm = ClassForm()
    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    if request.method == 'POST':
        
        #Get details of the submitted form
        student_id = request.POST['pupil_id']
        classRoom = request.POST['classRoom']
        remark = request.POST['remark']
        
        Term = request.POST['term']
        
        
        try:
            #If result is not blank
            result = request.FILES['result']
        except:
            #Else, if result is blank
            #Get the class of the student
            classRoom = AllClass[classRoom]

            #Get the particular student
            student = classRoom.objects.filter(student_id=student_id).first()

            #Return error message that result was left blank
            return render(request, 'school/classDetails.html', {
                    'classDetails': classRoom.objects.filter(status='active').all(), 'classRoom': classRoom,
                    'msg': f" { student.name}'s result for {Term} was submitted empty and was not processed",
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })
        


        #If a file is submitted as result(This is done to prevent submitting blank files 
        # as result)
        if result:
            #Get the class of the student
            classRoom = AllClass[classRoom]

            #Get the particular student
            student = classRoom.objects.filter(student_id=student_id).first()

            #If first term, upload file to student's first term
            if Term == 'Term1':
                student.Term1 = result
                student.remark = remark
                student.save()

                #After saving data, return teacher to class Page,
                #classDetails here carries details about the students in the class
                return render(request, 'school/classDetails.html', {
                    'classDetails': classRoom.objects.filter(status='active').all() , 'classRoom': classRoom,
                    'msg': f"Successfully added { student.name}'s result for {Term}",
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })
                
            
            #If Second term, upload file to student's second term
            elif Term == 'Term2':
                student.Term2 = result
                student.remark = remark
                student.save()
                
                #After saving data, return teacher to class Page,
                #classDetails here carries details about the students in the class
                return render(request, 'school/classDetails.html', {
                    'classDetails': classRoom.objects.filter(status='active').all(), 'classRoom': classRoom,
                    'msg': f"Successfully added { student.name}'s result for {Term}",
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })

            #If Third term, upload file to student's third term
            elif Term == 'Term3':
                student.Term3 = result
                student.remark = remark
                
                student.save()
                #After saving data, return teacher to class Page,
                #classDetails here carries details about the students in the class
                return render(request, 'school/classDetails.html', {
                    'classDetails': classRoom.objects.filter(status='active').all(), 'classRoom': classRoom,
                    'msg': f"Successfully added { student.name}'s result for {Term}",
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })

        elif result == '':
            #After saving data, return teacher to class Page,
                #classDetails here carries details about the students in the class
                return render(request, 'school/classDetails.html', {
                    'classDetails': classRoom.objects.filter(status='active').all(), 'classRoom': classRoom,
                    'msg': f" { student.name}'s result for {Term} was submitted empty and was not processed",
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })

    else:
        return render(request, 'school/classLogin.html', {
                    'classForm': classForm, 'msg': f"Please, sign in to classroom to update results",
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })

                

#Require only admin to have access to this page
# This function allows the principal (admin) The right to approve or decline resultss
# Ultimately, students are promoted or repeat based on principal's approval
class ClassForm2(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('classRoom',)

# Admin is required
def principalRemark(request):
    #First of, admin is asked to choose from a list of all the available classes
    #The one she wishes to modify.

    classForm = ClassForm2()
    
    if request.method == 'POST':
        
        #Make a dictionary of all the classrooms
        classRooms = {
            'Nursery1': Nursery1,   
            'Nursery2': Nursery2
        }

        classForm = ClassForm2(request.POST)
        if classForm.is_valid():
            #Get the class the teacher wants to log in to
            classRoom = classForm.cleaned_data['classRoom']
            

            #If the principal has the right class, log her into the classRoom
            classInView = classRooms[classRoom]
            #If the class exists
            if classInView:
                
                #Get all the students in different categories of remark e.g repeat, promote, noChange that are active
                promoted = classInView.objects.filter(remark='promote').filter(status='active').all()
                repeated = classInView.objects.filter(remark='repeat').filter(status='active').all()
                noChanged = classInView.objects.filter(remark='noChange').filter(status='active').all()
                
                #Return to a html view that will use these data

                return render(request, 'school/principalRemark.html',{
                    'promoted': promoted, 'repeated': repeated, 'nochanged': noChanged
                })
                
                


    classForm = ClassForm2()
    classRooms = {'Nursery1': Nursery1, 'Nursery2': Nursery2}
    return render(request, 'school/adminLogin.html', {'classForm': classForm, 
    'msg': "Please, sign in to classroom to update results"})


#ADmin is required    
#Principal's approval houses the decisions ,ade by the principal
#It is where actually promotes, repeats, or unchanges a pupil
def principalApproval(request):
    # IF it is a post request, get all the posted data
    if request.method == 'POST':
        #Make a list housing dictionary items for each class
        #It is important for it to be a list, so we can loop through it
        #All casses should be represented here 
        classRooms = [
            {'Nursery1': Nursery1},   
            {'Nursery2': Nursery2}
        ]
        #Get post data
        student_id = request.POST['student_id']
        Class = request.POST['classRoom']
        remark = request.POST['remark']
        


        # Get the class index the student is currently in
        for i in range(len(classRooms)):
            if Class in classRooms[i]:

                # Get the student in question
                student = classRooms[i][Class].objects.filter(student_id=student_id).first()

                #If principal approves or chooses promote for the student
                if remark == 'promote':

                    #First of, change student status from active to dormant
                    #This makes the student invisible in the current class
                    student.status = 'dormant' 
                    student.remark = 'promote'
                    
                    student.save()

                    #Also, update table which parents will see


                    #Then take the student to the next class and keep status as active
                    #This should be done as long as the class is not the last class in the school
                    #Because, you cant promote a child to a non-existent class
                    if i != len(classRooms)-1:

                        #Get the dictionary key for the new class
                        for key in classRooms[i+1]: #This returns all the keys in the dictionary

                            #Get the new class model
                            className = classRooms[i+1][key] #This returns the model


                            #Check if student is already in class
                            student_already = className.objects.filter(student_id=student_id).first()

                            # If student already in class
                            # Change status of student already in class to active. that's all
                            if student_already:
                                # Fill in details of the student in the new class
                                student_already.status = 'active'
                                student_already.name = student.name
                                student_already.password = student.password
                                student_already.about = student.about
                                student_already.email = student.email
                                student_already.phone = student.phone
                                student_already.DOB = student.DOB
                                
                                student_already.save()
                                
                                #Return to remark page, with message successfully promoted student to the next class
                                promoted = classRooms[i][Class].objects.filter(remark='promote').filter(status='active').all()
                                repeated = classRooms[i][Class].objects.filter(remark='repeat').filter(status='active').all()
                                noChanged = classRooms[i][Class].objects.filter(remark='noChange').filter(status='active').all()
                        
                                return render(request, 'school/principalRemark.html',{'promoted': promoted, 
                                'repeated': repeated, 'nochanged': noChanged,'msg': f'promoted {student.name}'
                                })


                            #Else, if student not in class, add student to class

                            #Add student to her new class with status of active
                            new_class = className(student_id=student_id, name=student.name, status='active'
                            , email=student.email, phone=student.phone, about=student.about, password=student.password, DOB=student.DOB)

                            #save
                            new_class.save()

                            #Return to remark page, with message successfully promoted student to the next class
                            promoted = classRooms[i][Class].objects.filter(remark='promote').filter(status='active').all()
                            repeated = classRooms[i][Class].objects.filter(remark='repeat').filter(status='active').all()
                            noChanged = classRooms[i][Class].objects.filter(remark='noChange').filter(status='active').all()
                            
                            #Return to a html view that will use these data

                            return render(request, 'school/principalRemark.html',{
                                'promoted': promoted, 'repeated': repeated, 'nochanged': noChanged,
                                'msg': f'promoted {student.name}'
                            })
                    #If child in final class, change status to inactive, but don't promote
                    else:
                        #Return to remark page, with message. student is now a graduate of your school
                        promoted = classRooms[i][Class].objects.filter(remark='promote').filter(status='active').all()
                        repeated = classRooms[i][Class].objects.filter(remark='repeat').filter(status='active').all()
                        noChanged = classRooms[i][Class].objects.filter(remark='noChange').filter(status='active').all()
                            
                        #Return to a html view that will use these data

                        return render(request, 'school/principalRemark.html',{
                            'promoted': promoted, 'repeated': repeated, 'nochanged': noChanged,
                            'msg': f'{student.name} is now a graduate of your school'
                        })

                elif remark == 'repeat':
                    #First of, keep the student status as active
                    #This leaves the student visible in the current class
                    student.status = 'active' 
                    student.remark = 'repeat'
                    student.save()
                    #Return to remark page, with message. student is repeating the class
                    promoted = classRooms[i][Class].objects.filter(remark='promote').filter(status='active').all()
                    repeated = classRooms[i][Class].objects.filter(remark='repeat').filter(status='active').all()
                    noChanged = classRooms[i][Class].objects.filter(remark='noChange').filter(status='active').all()
                        
                    #Return to a html view that will use these data
                    return render(request, 'school/principalRemark.html',{
                        'promoted': promoted, 'repeated': repeated, 'nochanged': noChanged,
                        'msg': f'{student.name} is repeating the class'
                    })
                    
                
                elif remark == 'noChange':
                    #First of, keep the student status as active
                    #This leaves the student visible in the current class
                    student.status = 'active' 
                    student.remark = 'noChange'
                    student.save()

                    #Return to remark page, with message. student's status is unchanged
                    promoted = classRooms[i][Class].objects.filter(remark='promote').filter(status='active').all()
                    repeated = classRooms[i][Class].objects.filter(remark='repeat').filter(status='active').all()
                    noChanged = classRooms[i][Class].objects.filter(remark='noChange').filter(status='active').all()
                        
                    #Return to a html view that will use these data
                    return render(request, 'school/principalRemark.html',{
                        'promoted': promoted, 'repeated': repeated, 'nochanged': noChanged,
                        'msg': f'{student.name} is still in current class'
                    })


    #If request method is not post, return to remark page for admin to sign in to class
    else:
        return HttpResponseRedirect(reverse('principalRemark'))
    

#Now, for the pupils
def pupil(request):
    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    if request.method == 'POST':
        student_id = request.POST['student_id']
        password = request.POST['password']
        
        #Add a dictionary of all the classes. The student may have been in more than one class
        allClasses = {'Nursery1': Nursery1, 'Nursery2': Nursery2}
        
        #Create two lists to hold classes he is active in, and dormant in
        activeIn = [] 
        dormantIn = []

        #Get the values in the allClasses dictionary
        for x in allClasses:
            
            Class = allClasses[x]

            #Check if student is in the class
            in_class = Class.objects.filter(student_id=student_id).filter(password=password).first()
            
            #If student is in the class
            if in_class:
                #Ckeck status
                pupil_name = in_class.name
                status = in_class.status

                #If active, append to active group
                if status == 'active':
                    activeIn.append(in_class)
                #Else if dormant, append to dormant
                elif status == 'dormant':
                    dormantIn.append(in_class)
                else:
                    pass
        #If any of the length is longer than 0 (Meaning there is a pupil)
        if len(activeIn) > 0 or len(dormantIn) > 0:
            #Return student to student Page with details pertaining to her
            return render(request, 'school/student.html', {
                'dormantIn': dormantIn, 'activeIn': activeIn,
             'name': pupil_name,
             'student_id': student_id,
            'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
            'contactFooter': contactFooter
            })
            #return HttpResponse(f'active in: {len(activeIn)},  dormant in: {len(dormantIn)}')
            
            
            
        #Else, if no details of student found
        else:
            return render(request, 'school/pupillogin.html', {'msg': 'Student_id or password invalid, Please try again',
            'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
            'contactFooter': contactFooter})

            
    return render(request, 'school/pupillogin.html', {
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter})




# Next, let's allow for the principal to register students to her school
#@ admin is required
def regpupil(request):
    classForm = ClassForm2
    if request.method == 'POST':
        #Get class student to be registered is in
        form = ClassForm2(request.POST)
        if form.is_valid():
            # Get the class the student wants to be registered in
            Class = form.cleaned_data['classRoom']

            #classes contains the prefix that should be added to a students_id based on the class he is registered in
            classes = [{'Nursery1': Nursery1, 'prefix': '1'}, {'Nursery2': Nursery2, 'prefix': '2'}]

            #Get the class the student is registering in
            for i in range(len(classes)):
                if Class in classes[i]:
                    # Get the length of the class, to use as part of the student_id, also, get the index
                    length = classes[i][Class].objects.count()
                    prefix = classes[i]['prefix']

                    #Create a unique student_id consisting of prefix and length of class
                    student_id =   prefix + '-' + str(length+1)
                    password = 'runo54321'

                    #Pass these details to form 

                    return render(request, 'school/regstud.html', {
                        'student_id': student_id, 'password': password, 'Class': Class, 'msg': f'Register pupil in {Class}'
                    })
    
    classForm = ClassForm2
    return render(request, 'school/regpupil.html', {'classForm': classForm, 
    'msg': "Register new student"})

import datetime
from datetime import date

# @admin is required
def basicdata(request):
    classForm = ClassForm2
    if request.method == 'POST':
        classForm = ClassForm2
        #Get all the data pertaining to the student
        name = request.POST['name']
        student_id = request.POST['student_id']
        classRoom = request.POST['classRoom']
        password = request.POST['password']
        contact = request.POST['contact']
        email = request.POST['email']
        about = request.POST['about']

        #Get the date of birth
        year = int(request.POST['year'])
        month = int(request.POST['month'])
        day = int(request.POST['day'])
        #Use DOB to convert to a date object in django
        DOB = datetime.date(year, month, day)

        #Create the student instance in the class
        #Add a dictionary of all the classes. The student may have been in more than one class
        allClasses = {'Nursery1': Nursery1, 'Nursery2': Nursery2}
        
        if classRoom in allClasses:
            Class = allClasses[classRoom]
            # As a final precautionary step, check if pupil id already exist
            not_new = Class.objects.filter(student_id=student_id).first()
            
            #If pupil exist, return admin to regpupil page
            if not_new:
                
                return render(request, 'school/regpupil.html', {'classForm': classForm, 
                'msg': "Student_id already exist. Please try again"})

            # Else, register the pupil
            new_pupil = allClasses[classRoom](student_id=student_id,
                DOB=DOB, name=name, email=email, phone=contact, about=about,
                classRoom=classRoom, password=password
            )
            new_pupil.save()

            # Send mail to pupil with registration details 

            send_mail(f'Regitration for {new_pupil.name}', f'We are pleased to announce to you that your registration has been completed. details pertaining your registeration include name: {new_pupil.name}, student_id: {new_pupil.student_id}, class: {new_pupil.classRoom}  password: {new_pupil.password} contact: {new_pupil.phone}. Please, change the default password as soon as possible', 'atumasaake@gmail.com', [email], fail_silently=True)

            #Return to register pupil page 
            return render(request, 'school/regpupil.html', {'classForm': classForm, 
                'msg': f"{new_pupil.name} has been registered in {new_pupil.classRoom} default password is {new_pupil.password}. An email with details has been sent to {new_pupil.email}. Please change password as soon as possible"})

    #If request.method is not post
    return render(request, 'school/regpupil.html', {'classForm': classForm, 
    'msg': "Register new student"})


# Next, we are going to try to allow principal change access to classroom and get details about classes all in one go
class classForm3(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['classRoom', 'password', 'classMail', 'phone', 'teacher']

def teacherprofile(request):
    form = classForm3
    classes = Class.objects.all()
    if request.method == 'POST':
        form = classForm3(request.POST)
        if form.is_valid():
            # Get data from the submitted form
            classRoom = form.cleaned_data['classRoom']
            password = form.cleaned_data['password']
            classMail = form.cleaned_data['classMail']
            phone = form.cleaned_data['phone']
            teacher = form.cleaned_data['teacher']

            # check if class exists in the Class table
            class_exists = Class.objects.filter(classRoom=classRoom).first()
            #If class exists, update new data
            if class_exists:
                class_exists.password = password
                class_exists.classMail = classMail
                class_exists.phone = phone
                class_exists.teacher = teacher
                #save form
                class_exists.save()
            else:
                # submit form as it is
                form.save()
            
            # Return admin to page with msg, classRoom details have been changed successfully
            return render(request, 'school/teacherprofile.html', {
             'form' : form,
            'classes': classes,
            'msg': f'{classRoom} details was changed successfully'
            })
            

            
        

    return render(request, 'school/teacherprofile.html', {
       'form' : form,
       'classes': classes
    })


# Principal has access to each pupil's detail, all she has to do is have the sudent_id
def pupildetails(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        
        
        #Add a dictionary of all the classes. The student may have been in more than one class
        allClasses = {'Nursery1': Nursery1, 'Nursery2': Nursery2}
        
        #Create two lists to hold classes he is active in, and dormant in
        activeIn = [] 
        dormantIn = []

        #Get the values in the allClasses dictionary
        for x in allClasses:
            
            Class = allClasses[x]

            #Check if student is in the class
            in_class = Class.objects.filter(student_id=student_id).first()
            
            #If student is in the class
            if in_class:
                #Ckeck status
                pupil_name = in_class.name
                status = in_class.status

                #If active, append to active group
                if status == 'active':
                    activeIn.append(in_class)
                #Else if dormant, append to dormant
                elif status == 'dormant':
                    dormantIn.append(in_class)
                else:
                    pass
        #If any of the length is longer than 0 (Meaning there is a pupil)
        if len(activeIn) > 0 or len(dormantIn) > 0:
            #Return student to student Page with details pertaining to her
            return render(request, 'school/student.html', {
                'dormantIn': dormantIn, 'activeIn': activeIn,
             'name': pupil_name
            })
            #return HttpResponse(f'active in: {len(activeIn)},  dormant in: {len(dormantIn)}')
            
            
            
        #Else, if no details of student found
        else:
            return render(request, 'school/pupillog.html', {'msg': 'Student_id invalid, Please try again'})

            
    return render(request, 'school/pupillog.html')


# Next, lets implement allowing our pupils to change password
def changepass(request):
    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    if request.method == 'POST':
        # Get the values of their input
        student_id = request.POST['student_id']
        current_pass = request.POST['current_pass']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        

        #Add a dictionary of all the classes. The student may have been in more than one class
        allClasses = {'Nursery1': Nursery1, 'Nursery2': Nursery2}
        
        #Create two lists to hold classes he is active in, and dormant in
        activeIn = [] 
        dormantIn = []

        #Get the values in the allClasses dictionary
        for x in allClasses:
            
            Class = allClasses[x]

            #Check if student is in the class
            in_class = Class.objects.filter(student_id=student_id).first()
            #Check if the current password pupil entered is correct
            change_pass = Class.objects.filter(student_id=student_id).filter(password=current_pass).first()
            
            #If student is in the class
            if in_class:
                #Ckeck status
                pupil_name = in_class.name
                status = in_class.status
                #change the student password if the current password is correct
                if change_pass:
                    change_pass.password = password1
                    change_pass.save()
                    msg = "Password has been changed successfully"
                else:
                    msg = 'Incorrect password, please check and try again'

                #If active, append to active group
                if status == 'active':
                    activeIn.append(in_class)
                #Else if dormant, append to dormant
                elif status == 'dormant':
                    dormantIn.append(in_class)
                else:
                    pass
            
        #Next, loop through all classes to find the student with the id, and check
        # if current password tallies with pupil's password
        
            
            
        #If any of the length is longer than 0 (Meaning there is a pupil)
        if len(activeIn) > 0 or len(dormantIn) > 0:
            #Return student to student Page with details pertaining to her
            return render(request, 'school/student.html', {
                'dormantIn': dormantIn, 'activeIn': activeIn,
             'name': pupil_name,
             'student_id': student_id,
             'msg': msg,
            'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
            'contactFooter': contactFooter
            })
        


        
    
    
    
    return HttpResponseRedirect(reverse('pupil'))


#Finally for the must haves, lets implement forgotten password
from .models import AccessKeys
from django import forms
class forgotpassform(forms.Form):
    pupil_id = forms.CharField(max_length=12, label='pupil_id')
    email = forms.EmailField(label='email')
    
def forgotpass(request):
    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    if request.method == 'POST':
        #Get the details of the pupil
        form = forgotpassform(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['pupil_id']
            email = form.cleaned_data['email']

             #Add a dictionary of all the classes. The student may have been in more than one class
            allClasses = {'Nursery1': Nursery1, 'Nursery2': Nursery2}
            
            #Create a lists to hold classes he is/was in
            activeIn = [] 
            

            #Get the values in the allClasses dictionary
            for x in allClasses:
                
                Class = allClasses[x]

                #Check if student is in the class
                in_class = Class.objects.filter(student_id=student_id).first()
                
                
                #If student is in the class
                if in_class:
                    #append to activeIn
                    
                    
                    activeIn.append(in_class)
                    
            
                #If any of the length is longer than 0 (Meaning there is a pupil)
                if len(activeIn) > 0:
                    
                    #Check if the email and student_id match in at least one of the student's classes
                    any = -1
                    for j in range(len(activeIn)):
                        if activeIn[j].student_id == student_id and activeIn[j].email == email:
                            any = j
                        else:
                            pass
                    # If there is a match, get student_id and email, and send mail
                    if any >= 0:

                        #create sort of a random 10 character secret key to use for password reset
                        values = 'aAbBcCDdEeFfGgHhiJjKLMmNnOPqpRrQSsTtUuVvWwXxYyZz123456789'
                        access_key=''
                        
                        for i in range(10):
                            import random
                            random_val = random.randint(0, len(values)-1)
                            access_key += values[random_val]

                        #Next, we created a model table(AccessKeys) that will store access keys
                        #Access the access key table and update or store access_key value
                        give_access = AccessKeys.objects.filter(student_id=student_id).first()

                        # give_access, update access_key
                        if give_access:
                            give_access.access_key = access_key
                            give_access.save()
                            
                        #Else if it is their first time of forgetting password
                        else:
                            #Create access key
                            give_access = AccessKeys(student_id=student_id, access_key=access_key)
                            give_access.save()

                        send_mail(f'Hello pupil {student_id}', f'A request has been received to change the password for your RUNO account. Use the access_key: {give_access.access_key} and student_id: {student_id} to reset password. If you did not send this request, please contact us immediately', 'atumasaake@gmail.com', [email], fail_silently=True)

                        
                        return render(request, 'school/resetpassword.html', {
                        'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                        'contactFooter': contactFooter
                        })
                            
                            
                    
                    
            
        return render(request, 'school/forgotpass.html', {'form': forgotpassform(), 'msg': 
        'Student_id or email incorrect. Please check and try again',
        'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
        'contactFooter': contactFooter})

                   

                


            #return HttpResponse(f'{student_id} - {email}')

    return render(request, 'school/forgotpass.html', {'form': forgotpassform(),
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter})
    #return HttpResponse('Hello World')


def resetpassword(request):
    #Footer imports
    logo = Logo.objects.filter(pk=1).first()
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()

    if request.method == 'POST':
        # get details from post data
        student_id = request.POST['student_id']
        access_key = request.POST['access_key']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        

        #Do server side validation to ensure password1 == password2
        if password1 == password2:
            # Check if user has right access key
            has_access = AccessKeys.objects.filter(student_id=student_id).filter(access_key=access_key).first()

            #If she has access
            if has_access:
                allClasses = {'Nursery1': Nursery1, 'Nursery2': Nursery2}

                for Class in allClasses:

                    #Check if student is in each class, change password if she is
                    student_in = allClasses[Class].objects.filter(student_id=student_id).first()

                    # If student is in class, change password to new password
                    if student_in:
                        student_in.password = password1
                        student_in.save()
                    else:
                        pass

                #After changing student_password in all classes
                #Delete accesskey 
                has_access.delete()

                # return to login page
                return render(request, 'school/pupillogin.html', {
                    'msg': f'{student_id} password successfully changed, login to view student profile',
                    'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                    'contactFooter': contactFooter
                })
            
            else:
                return render(request, 'school/resetpassword.html', {'msg': 'pupil_id or access_key does not match, please try again',
                'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
                'contactFooter': contactFooter})


            #return HttpResponse('Hello World')
        else:
            return render(request, 'school/resetpassword.html', {'msg': 'new password and retype password does not match',
            'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
            'contactFooter': contactFooter})

            
#This modifies the contents displayed on the footer
class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ['logo',]

def footerUpdate(request):
    logoForm = LogoForm()
    logo = Logo.objects.filter(pk=1).first()
    Footerdetail = Footerdetails.objects.filter(pk=1).first()
    aboutFppter = Footerabout.objects.filter(pk=1).first()

    # Footer imports
    footerDetail = Footerdetails.objects.filter(pk=1).first()
    aboutFooter = Footerabout.objects.filter(pk=1).first()
    contactFooter = Footercontact.objects.filter(pk=1).first()


    if request.method == 'POST':
        logoForm = LogoForm(request.POST, request.FILES)
        whatTo = request.POST['whatTo']
        if whatTo == 'schooldetails':
            school_name = request.POST['school_name']
            school_address = request.POST['school_address']
            school_motto = request.POST['school_motto']

            schooldetail = Footerdetails.objects.filter(pk=1).first()
            if schooldetail:
                schooldetail.school_name = school_name
                schooldetail.school_address = school_address
                schooldetail.school_motto = school_motto
                schooldetail.save()
            else:
                schooldetail = Footerdetails(school_name=school_name, school_address=school_address, school_motto=school_motto)
                schooldetail.save()             
            Footerdetail = Footerdetails.objects.filter(pk=1).first()   
            
            return render(request, 'runo/footerUpdate.html', {'LogoForm': logoForm,
            'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
            'contactFooter': contactFooter})
        #return HttpResponse('Hello world')
        elif whatTo == 'schoolabout':
            school_about = request.POST['school_about']
            schoolabout = Footerabout.objects.filter(pk=1).first()
            if schoolabout:
                schoolabout.school_about = school_about
                schoolabout.save()
            else:
                schoolabout = Footerabout(school_about=school_about)
                schoolabout.save()
            Footerabout1 = Footerabout.objects.filter(pk=1).first()
            return render(request, 'runo/footerUpdate.html', {'LogoForm': logoForm,
            'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
            'contactFooter': contactFooter})
        
        elif whatTo == 'schoolcontact':
            phone = request.POST['phone']
            email = request.POST['email']
            contact = Footercontact.objects.filter(pk=1).first()
            if contact:
                contact.school_phone = phone
                contact.school_mail = email
                contact.save()

            else:
                contact = Footercontact(school_phone=phone, school_mail=email)
                contact.save()
            cont = Footercontact.objects.filter(pk=1).first()

            return render(request, 'runo/footerUpdate.html', {'LogoForm': logoForm,
            'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
            'contactFooter': contactFooter})
            

        
        elif logoForm.is_valid():
            school_logo = logoForm.cleaned_data['logo']
            schoolLogo = Logo.objects.filter(pk=1).first()
            if schoolLogo:
                schoolLogo.logo = school_logo
                schoolLogo.save()
                return HttpResponse('fool')
            else:
                logoForm.save()
                logo = Logo.objects.filter(pk=1).first()
                
            return render(request, 'runo/footerUpdate.html', {'LogoForm': logoForm,
            'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
            'contactFooter': contactFooter})
            
    return render(request, 'runo/footerUpdate.html', {'LogoForm': logoForm,
     'logo': logo, 'footerDetail': footerDetail, 'aboutFooter': aboutFooter,
      'contactFooter': contactFooter})

def editStudentProfile(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        
        
        #Add a dictionary of all the classes. The student may have been in more than one class
        allClasses = {'Nursery1': Nursery1, 'Nursery2': Nursery2}
        
        #Create two lists to hold classes he is active in, and dormant in
        activeIn = [] 
        dormantIn = []

        #Get the values in the allClasses dictionary
        for x in allClasses:
            
            Class = allClasses[x]

            #Check if student is in the class
            in_class = Class.objects.filter(student_id=student_id).first()
            
            #If student is in the class
            if in_class:
                #Ckeck status
                pupil_name = in_class.name
                pupil_id = in_class.student_id
                status = in_class.status
                pupil_DOB = in_class.DOB
                pupil_email = in_class.email
                pupil_phone = in_class.phone
                pupil_about = in_class.about
                

                #If active, append to active group
                if status == 'active':
                    pupil_class = in_class.classRoom
                    activeIn.append(in_class)
                #Else if dormant, append to dormant
                elif status == 'dormant':
                    dormantIn.append(in_class)
                else:
                    pass
        #If any of the length is longer than 0 (Meaning there is a pupil)
        if len(activeIn) > 0 or len(dormantIn) > 0:
            #Return student to student Page with details pertaining to her
            return render(request, 'school/studentEdit.html', {
                'dormantIn': dormantIn, 'activeIn': activeIn,
             'name': pupil_name, 'id':pupil_id, 'DOB':pupil_DOB,
             'email': pupil_email, 'phone': pupil_phone, 'about': pupil_about,
             'class': pupil_class
            })
            #return HttpResponse(f'active in: {len(activeIn)},  dormant in: {len(dormantIn)}')
            
            
            
        #Else, if no details of student found
        else:
            return render(request, 'school/pupillog2.html', {'msg': 'Student_id invalid, Please try again'})

            
    return render(request, 'school/pupillog2.html')


def editstudProfile(request):
    if request.method == 'POST':
        student_id = request.POST['id']

        edit = request.POST['edit']
        
        
        #Add a dictionary of all the classes. The student may have been in more than one class
        allClasses = {'Nursery1': Nursery1, 'Nursery2': Nursery2}
        
        activeIn = []
        dormantIn = []
        #Get the values in the allClasses dictionary
        for x in allClasses:
            
            Class = allClasses[x]

            #Check if student is in the class
            in_class = Class.objects.filter(student_id=student_id).first()
            
            #If student is in the class
            if in_class:
                

                #Get what to be edited
                #If name is what was edited, change name in each class
                if edit == 'pupil_name':
                    in_class.name = request.POST['name']
                    in_class.save()
                    msg = f'Name successfully changed to {request.POST["name"]}'
                    #return HttpResponse(msg)
                elif edit == 'pupil_email':
                    in_class.email = request.POST['email']
                    in_class.save()
                    msg = f'Email address successfully changed to {request.POST["email"]}'
                    #return HttpResponse(msg)

                elif edit == 'pupil_about':
                    in_class.about = request.POST["about"]
                    in_class.save()
                    msg = f'about student successfully changed to {request.POST["about"]}'
                    #return HttpResponse(msg)
                
                elif edit == 'pupil_DOB':
                    year = int(request.POST['year'])
                    month = int(request.POST['month'])
                    day = int(request.POST['day'])
                    #Use DOB to convert to a date object in django
                    DOB = datetime.date(year, month, day)
                    #return HttpResponse(f'{DOB}')
                    in_class.DOB = DOB
                    msg = f' Date of birth changed to {DOB}'
                    in_class.save()

                #Get details to be passed to html. 

                pupil_name = in_class.name
                pupil_id = in_class.student_id
                status = in_class.status
                pupil_DOB = in_class.DOB
                pupil_email = in_class.email
                pupil_phone = in_class.phone
                pupil_about = in_class.about
                

                #If active, append to active group
                if status == 'active':
                    pupil_class = in_class.classRoom
        
                    activeIn.append(in_class)
                #Else if dormant, append to dormant
                elif status == 'dormant':
                    dormantIn.append(in_class)
                else:
                    pass
        #If any of the length is longer than 0 (Meaning there is a pupil)
        if len(activeIn) > 0 or len(dormantIn) > 0:
            #Return student to student Page with details pertaining to her
            return render(request, 'school/studentEdit.html', {
                'dormantIn': dormantIn, 'activeIn': activeIn,
             'name': pupil_name, 'id':pupil_id, 'DOB':pupil_DOB,
             'email': pupil_email, 'phone': pupil_phone, 'about': pupil_about,
             'class': pupil_class, 'msg': msg
            })
    
    else:
        return render(request, 'school/pupillog2.html')