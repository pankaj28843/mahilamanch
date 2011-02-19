import random, string
from report.models import *
from datetime import date, timedelta
import time


def __main__():
    for i in range(20):
        d = District(name = ''.join(random.choice(string.ascii_uppercase) for x in range(6)), center = str(26.79644 - 2*random.random()) + "," + str(82.198639 - 9*random.random()))
        d.save()

    d_list = District.objects.all()

    for i in range(500):
        d = d_list[random.randint(0,len(d_list)-1)]
        s = d.center.split(",")
        b = Block(name = ''.join(random.choice(string.ascii_uppercase) for x in range(6)), center = str(string.atof(s[0]) + 0.9*random.random()) + "," + str(string.atof(s[1]) + 0.9*random.random()), district = d)
        b.save()

    for i in range(5000):
        d = d_list[random.randint(0,len(d_list)-1)]
        b_list = Block.objects.all()
        b = b_list[random.randint(0,len(b_list)-1)]
        s = b.center.split(",")
        hc = HealthCenter(name = ''.join(random.choice(string.ascii_uppercase) for x in range(6)), center = str(string.atof(s[0]) + 0.2*random.random()) + "," + str(string.atof(s[1]) + 0.2*random.random()), district = d, block = b, code = 1000+i)
        hc.save()
    current_date = date.today()
    end_date = date.today() + timedelta(days=60) 

    while current_date <= end_date:
        print current_date
        for i in range(random.randint(1,50)):
            d = d_list[random.randint(0,len(d_list)-1)]    
            b_list = Block.objects.all()
            b = b_list[random.randint(0,len(b_list)-1)]    
            hc_list = HealthCenter.objects.all()
            hc = hc_list[random.randint(0,len(hc_list)-1)]
            s = hc.center.split(",")
            event = Event(reporting_date = current_date,reporting_time = time.time(), district = d, block = b, target_health_center = hc, category = random.randint(1,3), money = random.randint(1, 99999))
            event.save()
        current_date += timedelta(days=1)
