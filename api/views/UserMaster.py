""" API to create/get UserMaster records
"""
from django.http import JsonResponse, QueryDict
from rest_framework import views
from django.db.models import Max
from backend import models
from ..serializers import UserAccountSerializer

class UserMasterView(views.APIView):
    """ API view to get/add UserMasterView
    """
    def get(self, _):
        """ GET method handler to get UserMasterView
        """
        UserAccount_sel = models.UserAccount.objects.all()
        if UserAccount_sel.exists():
            result = []
            for UserAccount in UserAccount_sel:
                result.append({
                    'Cd': UserAccount.UserCode,
                    'Usernm' : UserAccount.FullName,
                    'Usertype' : UserAccount.UserType,
                    'Sts' : UserAccount.Status,
                })
            return JsonResponse({'success': True, 'data': result}, status=201)
        return JsonResponse({'success': False, 'message': 'UserAccount not found!', 'data': []}, status=202)