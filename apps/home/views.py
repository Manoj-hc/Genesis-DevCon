from django.shortcuts import render

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.member.serializers import DevconMemberSerializer, SpeakerSerializer, ProspectSerializer
from .mailchimp_api import add_user_to_mailchimp


# Create your views here.
def home(request):
    data = {
        'show_buy_tickets': True,
        'show_earth_video': True,
    }
    return render(request, 'home/index.html', data)


def speakers(request):
    data = {
        'cover_image': 'img/speaker-DevCon.jpg',
    }
    return render(request, 'home/speakers.html', data)


def sponsors(request):
    data = {
        'cover_image': 'img/sponsor-DevCon.jpg',
    }
    return render(request, 'home/sponsors.html', data)


def attendees(request):
    data = {
        'cover_image': 'img/efw.jpg',
    }
    return render(request, 'home/attendees.html', data)


def our_story(request):
    data = {}
    return render(request, 'home/our-story.html', data)

def agenda(request):
    data = {}
    return render(request, 'home/agenda.html', data)


def contest(request):
    data = {}
    return render(request, 'home/contest.html', data)


def devcon(request):
    data = {}
    return render(request, 'genesisdevcon2020/index.html', data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def subscribe_user(request):
    serializer = DevconMemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data

        mailchimp_data = {
          "email_address": data['email'],
          "status": "subscribed",
          "merge_fields": {
              "NAME": data['name'],
              "PHONE": data['phone'],
              "COMPANY": data['company'],
              "DESIGNA": data['designation'],
          }
        }
        mailchimp_response = add_user_to_mailchimp(mailchimp_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def speaker_application(request):
    serializer = SpeakerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def prospect_application(request):
    serializer = ProspectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
