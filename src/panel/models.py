from django.db import models

class Port(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class WeekDay(models.Model):
    dayIndex = models.IntegerField()
    dayName = models.CharField(max_length=8)
    def __str__(self):
        return self.dayName    

class PhoneTime(models.Model):
    name = models.CharField(max_length=200)
    dayOfTheWeek = models.ManyToManyField(WeekDay)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    def __str__(self):
        return self.name    


class Server(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    name = models.CharField(max_length=200)
    name_on_reseller = models.CharField(max_length=200)
    server_address = models.CharField(max_length=200, null=True, blank=True)
    #ssh_username = models.CharField(max_length=200, null=True, blank=True)
    #ssh_password = models.CharField(max_length=200, null=True, blank=True)
    root_permissions =  models.BooleanField(choices=BOOL_CHOICES,  default=False)
    ping_test =  models.BooleanField(choices=BOOL_CHOICES,  default=False)
    ports = models.ManyToManyField(Port)
    PhoneTime = models.ManyToManyField(PhoneTime)
    core = models.IntegerField(default='1')
    ram = models.IntegerField(default='512')
    def __str__(self):
        return self.name

class Site(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    server=models.ForeignKey(Server,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Email(models.Model):
    name = models.CharField(max_length=200)
    server=models.ForeignKey(Server,on_delete=models.CASCADE)
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    def __str__(self):
        return self.name        


class History(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    
    server=models.ForeignKey(Server,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_ok = models.BooleanField(choices=BOOL_CHOICES,  default=True)
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.server.name + ' / ' + str(self.date.day) +'-'+ str(self.date.month)+'-'+str(self.date.year)+' '+str(self.date.hour) + ':'+str(self.date.minute)+ ':'+str(self.date.second)+' / ' + str(self.is_ok)



