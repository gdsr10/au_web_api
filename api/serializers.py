""" Serializer module to serialize/de-serialize table objects from/to JSON
"""
from rest_framework import serializers
from backend import models

class UserAccountSerializer(serializers.ModelSerializer):
    """ UserAccountSerializer to map the Model instance into JSON format
    """
    class Meta:
        model = models.UserAccount
        fields = '__all__'
        
class LoginSerializer(serializers.ModelSerializer):
    """ LoginSerializer to map the Model instance into JSON format
    """
    class Meta:
        model = models.UserAccount
        fields = ['UserCode', 'UserName', 'UserPass']
        
        
class CenterMasterSerializer(serializers.ModelSerializer):
    """ CenterMasterSerializer to map the Model instance into JSON format
    """
    class Meta:
        model = models.MedicalCenterMaster
        fields = '__all__'
        
        
class EntryDetailsSerializer(serializers.ModelSerializer):
    """ EntryDetailsSerializer to map the Model instance into JSON format
    """
    class Meta:
        model = models.EntryDetails
        fields = '__all__'