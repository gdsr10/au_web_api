""" API to create/get CenterMaster records
"""
from django.http import JsonResponse, QueryDict
from rest_framework import views
from django.db.models import Max
from backend import models
from ..serializers import CenterMasterSerializer

class CenterMasterView(views.APIView):
    """ API view to get/add CenterMasterView
    """
    def get(self, _):
        """ GET method handler to get CenterMasterView
        """
        CenterMaster_sel = models.MedicalCenterMaster.objects.all()
        if CenterMaster_sel.exists():
            result = []
            for CenterMaster in CenterMaster_sel:
                result.append({
                    'Cd': CenterMaster.MedicalCenterCode,
                    'Centernm' : CenterMaster.MedicalCenterName,
                    'Centertypecd' : CenterMaster.MedicalCenterTypeCode,
                    'Sts' : CenterMaster.Status,
                })
            return JsonResponse({'success': True, 'data': result}, status=201)
        return JsonResponse({'success': False, 'message': 'CenterMaster not found!', 'data': []}, status=202)