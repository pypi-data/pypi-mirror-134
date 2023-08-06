import requests

from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from .models import AuxSilo, IntentSilo
from .serializers import AuxSiloSerializer
from django.http import HttpResponse
from io import StringIO
import hashlib

import ast
import csv
import random  
import string  
import os
from datetime import datetime, date, timezone
from cryptography.fernet import Fernet
#import smtplib
from email.mime.text import MIMEText
from django.core.mail import send_mail

from .utils import uscalt_task

class UploadData(APIView):
    def post(self, request, *args, **kwargs):
        #If user silo already exists, replace the data
        if AuxSilo.objects.filter(name=request.data.get('name')).exists():
            d_hash = hashlib.md5(request.data.get('data').encode('UTF-8'))
            ax = AuxSilo.objects.filter(link=request.data.get('off_id'), time=datetime.now())
            ax.data_hash, ax.data = data_hash=d_hash, data=request.data.get('data')
            ax.save()
        else:
            #If not, Create a silo and temp store data
            d_hash = hashlib.md5(request.data.get('data').encode('UTF-8'))
            ax = AuxSilo(name=request.data.get('name'), data=request.data.get('data'), 
            link=request.data.get('off_id'), time=datetime.now(timezone.utc), data_hash=d_hash)
            ax.save()
        
        return Response({"task": "success"})

class RegIntent(APIView):
    def post(self, request, *args, **kwargs):
        #Register the users intent to share data
        ins = IntentSilo(identifier=request.data.get('identifier'), link=request.data.get('link'))
        ins.save()
        return Response({"task": "success"})



class CheckIfExists(APIView):
    """Used by client-side devices to check if they need to send data in again"""
    def post(self, request, *args, **kwargs):
        #Check if the user already has data sent in
        try:
            exist = AuxSilo.objects.get(name=request.data.get('name'))
        except AuxSilo.DoesNotExist:
            exist = None

        if exist is not None:
            aux = AuxSilo.objects.get(name=request.data.get('name'))
            u_time = aux.time
            if (datetime.now(timezone.utc) - u_time).seconds > 7200:
                if request.data.get('hash') == aux.data_hash:
                    response = Response({"status": True})
            else:
                response = Response({"status": False})
        else:
            response = Response({"status": True})
        
        return response

class CloudDownload(APIView):
    """
    Retrieve data from the database
    """
    def get(self, request, *args, **kwargs):
        mets = uscalt_task.methods()
        link = request.query_params.get('off_id')
        fields = request.query_params.get('fields')

        if link in mets:
            cls_ins = mets[link][1].Uscalt()
            data = getattr(cls_ins, link)(link)

            tmp_list = []
            for i in data:
                tmp_list.append(list(i.values()))

            token, key, fname = PrepareForDownload(tmp_list, fields, cloud=True)

            send_mail(
                'test',
                key.decode("utf-8"),
                settings.EMAIL_HOST_USER,
                [request.query_params.get('email')],
                fail_silently=True,
            )

            os.remove(f'{fname}.csv')
            
            response = Response({'file': token})
        else:
            response = Response({'file': 'The company has not set up this room link for cloud downloading yet'})

        return response

class Download(APIView):
    """
    Create dataset from user sent data
    """
    def get(self, request, *args, **kwargs):
        Auxs = AuxSilo.objects.filter(link=request.query_params.get('off_id'))
        print(Auxs)

        fields = request.GET.get('fields').split(',')

        token, key, fname = PrepareForDownload(Auxs, fields)
        print(request.query_params.get('email'))

        send_mail(
            'test',
            key.decode("utf-8"),
            settings.EMAIL_HOST_USER,
            [request.query_params.get('email')],
            fail_silently=True,
        )
        """
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
        """
        

        Auxs.delete()
        os.remove(f'{fname}.csv')

        return Response({'file': token})

def PrepareForDownload(data, fields, cloud=False):
    temp_list = []

    if cloud:
        pass   
    else:
        for item in data:
            temp_list.append(item.data.split(','))

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    fname = ''.join((random.choice(string.ascii_lowercase) for x in range(30)))

    with open(f'{fname}.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)

        for i in temp_list:
            write.writerow(i)

    with open(f'{fname}.csv', 'rb') as original_file:
        original = original_file.read()

    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(original)

    return token, key, fname