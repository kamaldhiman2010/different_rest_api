
from csv import Dialect
from time import sleep
from .models import Movie

from celery import shared_task
import datetime
from django.core.mail import send_mail
import pathlib
import os
import time

import clevercsv


path = "/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv"
 
# Both the variables would contain time
# elapsed since EPOCH in float
ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)
 
# Converting the time in seconds to a timestamp
c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)
 
print(f"The file located at the path {path} \
was created at {c_ti} and was "
      f"last modified at {m_ti}")





# @shared_task
# def get_time():
# with open("/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv", "r", newline="", encoding="utf-8") as fp:
#     reader = clevercsv.reader(fp, delimiter=",", quotechar="", escapechar="\\")
#     rows = list(reader)
#     print(rows)
    # return "Got the Time"

@shared_task
def count_movies():
    movie_data = Movie.objects.count()
    print(movie_data)
    return movie_data

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"



@shared_task
def send_email_task(*args,**kwargs):
    sleep(10)
    send_mail('celery task worked!',
    'This is proof the task worked!',
    'kamaldhiman2010@gmail.com',
    ['kkuljit2010@gmail.com','kamaldhiman2010@gmail.com'])

    return None

@shared_task
def append_data_in_file(*args,**kwargs):
    file_object = open('sample.txt', 'a')

    file_object.write('hello')
    file_object.write('\n')

    file_object.close()
    return "Data appended successfully"
