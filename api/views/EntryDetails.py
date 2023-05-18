""" API to create/get Register records
"""
from django.http import JsonResponse, QueryDict
from rest_framework import views
from django.db.models import Max
from backend import models
from ..serializers import EntryDetailsSerializer

class EntryDetailsView(views.APIView):
    """ API view to add EntryDetailsView Data """
    # def post(self, request):
    #     serializer = EntryDetailsSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return JsonResponse({'success': True, 'data': serializer.data}, status=201)
    
    def post(self, request):
        """ POST method handler to add EntryDetailsView
        """
        data = request.data.dict() if isinstance(request.data, QueryDict) else request.data
        EntryDetails_qs = models.EntryDetails.objects.filter(EntryDetailsCode = data['EntryDetailsCode'])
        EntryDetailsDate_qs = models.EntryDetails.objects.filter(EntryDate = data['EntryDate'])
        UserAccount_qs = models.UserAccount.objects.all()
        MedicalCenter_qs = models.MedicalCenterMaster.objects.all()
        if EntryDetails_qs.exists():
            return JsonResponse({'success': False, 'message': 'Entry details already exists.!'}, status=202)
        
        if EntryDetailsDate_qs.exists():
            return JsonResponse({'success': False, 'message': 'Entry details already exists.!'}, status=202)

        EntryDetailsCode_Key = 1
        entryDetails_qs = models.EntryDetails.objects.all()
        if entryDetails_qs.exists():
            EntryDetailsCode_Key = entryDetails_qs.aggregate(Max('EntryDetailsCode'))['EntryDetailsCode__max'] + 1
        models.EntryDetails(EntryDetailsCode = EntryDetailsCode_Key,
                      UserCode = UserAccount_qs.filter(UserCode=data['UserCode']).last(),
                      MedicalCenterCode = MedicalCenter_qs.filter(MedicalCenterCode=data['MedicalCenterCode']).last(),
                      EntryDate = data['EntryDate'],
                      Status = data['Status']
            ).save()
        return JsonResponse({'success': True, 'message': '', 'data': [{'ResultId': EntryDetailsCode_Key,'Result': 'Entry Details Information added successfully.'}]}, status=201)