from django.db import models

# Create your models here.
#This model basically controls the images to be dispalyed at the top of the homepage
class Photos(models.Model):
    photo = models.ImageField(upload_to='photos', max_length=30)
    desc = models.CharField(max_length=50)
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),

    )
    position = models.CharField(max_length=30, choices = CHOICES, null=True, blank=True)

    def __str__(self):
        return f' {self.desc}'


#This model controls the images that will be displayed on the welcome page as well as the welcome link on the homepage
class WelcImgs(models.Model):
    welcImg = models.ImageField(upload_to='welcome', max_length=30 )
    extraImg1 = models.ImageField(upload_to='welcome', max_length=30, blank=True, null=True)
    extraImg2 = models.ImageField(upload_to='welcome', max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.id}'

# This model controls the write up on the welcome page

    

class Welcometab3(models.Model):
    resources = models.CharField(max_length=150, blank=True, null=True)

    email1 = models.EmailField()
    email2 = models.EmailField(blank=True, null=True)
    contact1 = models.CharField(max_length=100)
    contact2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.id}'


class Welcometab4(models.Model):
    file1 = models.FileField(upload_to='welcFiles', max_length=50)
    displayName1 = models.CharField(max_length=50)
    file2 = models.FileField(upload_to='welcFiles', max_length=50, blank=True, null=True)
    displayName2 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.id}'


#This model borrows from WelcImg to serve as an img that links to the welcome page
class WelcLeaders(models.Model):
    welcLeader = models.ImageField(upload_to='welcome', max_length=30 )
    extraLeader1 = models.ImageField(upload_to='welcome', max_length=30)
    extraLeader2 = models.ImageField(upload_to='welcome', max_length=30)

    def __str__(self):
        return f'{self.id}'

# This model controls the images and description for each news article
class News(models.Model):
    newsImg = models.ImageField(upload_to='photos', max_length=30)
    desc = models.CharField(max_length=80)
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),

    )
    position = models.CharField(max_length=30, choices = CHOICES, null=True, blank=True)

    def __str__(self):
        return f' {self.desc}'

class newsDetail(models.Model):  
    newsBody = models.TextField()



class Welcometab(models.Model):
    img1 = models.OneToOneField(WelcImgs, on_delete=models.CASCADE, related_name='welcHome', blank=True, null=True)
    img1L = models.OneToOneField(WelcLeaders, on_delete=models.CASCADE, related_name='welcLead', blank=True, null=True)

    writeHead1 = models.CharField(max_length=100)
    write1 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}'

class Welcometab2(models.Model):
    img2 = models.OneToOneField(WelcImgs, on_delete=models.CASCADE, related_name='welcHome2', blank=True, null=True)
    img2L = models.OneToOneField(WelcLeaders, on_delete=models.CASCADE, related_name='welcLead2', blank=True, null=True)
    writeHead2 = models.CharField(max_length=100)
    write2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}'

class about(models.Model):
    img = models.ImageField(upload_to='about', max_length=50)
    title = models.CharField(max_length=40)
    body = models.TextField()

class about2(models.Model):
    img2 = models.ImageField(upload_to='about', max_length=50)
    title2 = models.CharField(max_length=40)
    body2 = models.TextField()

class about3(models.Model):
    img3 = models.ImageField(upload_to='about', max_length=50)
    title3 = models.CharField(max_length=40)
    body3 = models.TextField()

class Steps(models.Model):
    
    step = models.TextField()
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),

    )
    position = models.CharField(max_length=30, choices = CHOICES, null=True, blank=True)

    def __str__(self):
        return f' {self.desc}'

class admitfiles(models.Model):
    file1 = models.FileField(upload_to='admission_files', null=True)
    name1 = models.CharField(max_length=60, blank=True, null=True)

    file2 = models.FileField(upload_to='admission_files', blank=True, null=True)
    name2 = models.CharField(max_length=60, blank=True, null=True)

    file3 = models.FileField(upload_to='admission_files', blank=True, null=True)
    name3 = models.CharField(max_length=60, blank=True, null=True)

#This point and below is related to pupils and teachers
# Thfrom django.db import models
from datetime import date
# Create your models here.

# Nursery1 is a model containing details about students in Nursery1 including their result details
# for each term
class Nursery1(models.Model):
    # Student biodata
    student_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=35)
    name = models.CharField(max_length=30)
    
    about = models.CharField(max_length=150, blank=True)
    note = models.CharField(max_length=150, blank=True)

    #DOB is used to automatically update the age field
    DOB = models.DateField(blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    #The class they are in
    classRoom = models.CharField(max_length=15, choices = (('Nursery1', 'Nursery1'), ), default='Nursery1')

    #This holds the result of each pupil
    Term1 = models.FileField(upload_to='term1', blank=True)
    Term2 = models.FileField(upload_to='term2', blank=True)
    Term3 = models.FileField(upload_to='term3', blank=True)

    #Remark is what the teacher has to stay about if the student is promoted, repeating or there is
    #No change e.g during the second term
    remark = models.CharField(max_length=15, choices=[
        ('promote', 'promote'), ('repeat', 'repeat'), ('noChange', 'noChange')
    ], default='noChange')

    #Status determines whether details about the student will be available to teachers of the class
    # If active, then the details of the pupil will be available to the class teacher, else, it wont
    status = models.CharField(max_length=15, choices=[('active', 'active'), ('dormant', 'dormant')], default='active')

    #This is the function that causes age to automatically update
    @property
    def age(self):
        today = date.today()
        born = self.DOB

        #If it is up to the month and year of birth, rest = 1, else if not, rest should be 0
        rest = 1 if (today.month, today.day) < (born.month, born.day) else 0 
        

        return today.year - born.year - rest
    

    def __str__(self):
        return f'{self.student_id} - {self.name} age: {self.age}'

class Nursery2(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=35)
    name = models.CharField(max_length=30)
    
    about = models.CharField(max_length=150, blank=True)
    note = models.CharField(max_length=150, blank=True)
    

    classRoom = models.CharField(max_length=15, choices = (('Nursery2', 'Nursery2'), ), default='Nursery2')

    Term1 = models.FileField(upload_to='term1', blank=True)
    Term2 = models.FileField(upload_to='term2', blank=True)
    Term3 = models.FileField(upload_to='term3', blank=True)
    DOB = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    
    remark = models.CharField(max_length=15, choices=[
        ('promote', 'promote'), ('repeat', 'repeat'), ('noChange', 'noChange')
    ], default='noChange')
    status = models.CharField(max_length=15, choices=[('active', 'active'), ('dormant', 'dormant')], default='active')


    @property
    def age(self):
        today = date.today()
        born = self.DOB

        #If 
        rest = 1 if (today.month, today.day) < (born.month, born.day) else 0
        

        return today.year - born.year - rest

    def __str__(self):
        return f'{self.student_id} - {self.name} age: {self.age}'
    


#Class allows privacy to teachers, so only the teacher have access to her class' info
class Class(models.Model):
    classRoom = models.CharField(max_length=30, choices=[('Nursery1','Nursery1'), ('Nursery2', 'Nursery2')])
    password  = models.CharField(max_length=20) 
    classMail = models.EmailField()
    phone = models.CharField(max_length=15)
    teacher = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.classRoom}'

#Access key is used to store access_key values for password reset
class AccessKeys(models.Model):
    student_id = models.CharField(max_length=30)
    access_key = models.CharField(max_length=15)


class Logo(models.Model):
    logo = models.ImageField(upload_to='logo')
    def __str__(self):
        return f'{self.id}'

class Footerdetails(models.Model):
    school_name = models.CharField(max_length=200)
    school_address = models.CharField(max_length=500)
    school_motto = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.id}'

class Footerabout(models.Model):
    school_about = models.TextField(max_length=600)
    
    def __str__(self):
        return f'{self.id}'

class Footercontact(models.Model):
    
    school_phone = models.CharField(max_length=15, default='12345')
    school_mail = models.EmailField(max_length=60, default='schoolmail')
    def __str__(self):
        return f'{self.id}'