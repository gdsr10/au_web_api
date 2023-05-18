""" API to create/get UserMaster records
"""
import datetime
from django.http import JsonResponse, QueryDict
from rest_framework import views
from django.db.models import Max
from backend import models
from ..serializers import UserAccountSerializer

class EntryFilterUSView(views.APIView):
    """ API view to get/add UserMasterView
    """
    def get(self, request):
        """ GET method handler to get UserMasterView
        """
        start_date = request.GET.get('StartDate')
        end_date = request.GET.get('EndDate')
        
        EntryDetails_sel = models.EntryDetails.objects.filter(UserCode=request.GET.get('UserCode'), EntryDate__range=[start_date, end_date])
        if EntryDetails_sel.exists():
            result = []
            for data_entry in EntryDetails_sel:
                result.append(
                    {
                        'Cd': data_entry.EntryDetailsCode,
                        'UsrCd': data_entry.UserCode.UserCode,
                        'UsrNm': data_entry.UserCode.FullName,
                        'MdCd': data_entry.MedicalCenterCode.MedicalCenterCode,
                        'MdNm': data_entry.MedicalCenterCode.MedicalCenterName,
                        'EntryDt': data_entry.EntryDate,
                    }
                )
            return JsonResponse({'success': True, 'data': result}, status=201)
        return JsonResponse({'success': False, 'message': 'Entry Details not found!', 'data': []}, status=202)
