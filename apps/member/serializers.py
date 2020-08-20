from rest_framework import serializers
from .models import DevconMember, Speaker, Prospect


class DevconMemberSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254, min_length=None, allow_blank=False)
    name = serializers.CharField(max_length=128, allow_blank=False, trim_whitespace=True)
    phone = serializers.CharField(max_length=32, allow_blank=False, trim_whitespace=True)
    company = serializers.CharField(max_length=256, allow_blank=False, trim_whitespace=True)
    designation = serializers.CharField(max_length=256, allow_blank=False, trim_whitespace=True)

    def validate_email(self, value):
        if DevconMember.objects.filter(email=value).exists():
            raise serializers.ValidationError("You are already subscribed")
        return value

    def create(self, validated_data):
        """
        Create and return a new `DevconMember` instance, given the validated data.
        """
        return DevconMember.objects.create(**validated_data)


class SpeakerSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254, min_length=None, allow_blank=False)
    name = serializers.CharField(max_length=128, allow_blank=False, trim_whitespace=True)
    phone = serializers.CharField(max_length=32, allow_blank=False, trim_whitespace=True)
    company = serializers.CharField(max_length=256, allow_blank=False, trim_whitespace=True)
    designation = serializers.CharField(max_length=256, allow_blank=False, trim_whitespace=True)
    topic = serializers.CharField(max_length=256, allow_blank=False, trim_whitespace=True)
    topic_desc = serializers.CharField(max_length=512, allow_blank=False, trim_whitespace=True)

    def validate_email(self, value):
        if Speaker.objects.filter(email=value).exists():
            raise serializers.ValidationError("We have received your application")
        return value

    def create(self, validated_data):
        """
        Create and return a new `Speaker` instance, given the validated data.
        """
        return Speaker.objects.create(**validated_data)


class ProspectSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254, min_length=None, allow_blank=False)

    def validate_email(self, value):
        if Prospect.objects.filter(email=value).exists():
            raise serializers.ValidationError("You have downloaded prospectus")
        return value

    def create(self, validated_data):
        """
        Create and return a new `Prospectus` instance, given the validated data.
        """
        return Prospect.objects.create(**validated_data)
