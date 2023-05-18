""" API to create/get Register records
"""
from django.http import JsonResponse, QueryDict
from rest_framework import views
from django.db.models import Max
from backend import models
from ..serializers import LoginSerializer

class LoginView(views.APIView):
    """ API view to add Register Data """
    
    # def post(self, request):
    #     """ POST method handler to add LoginView
    #     """
    #     data = request.data.dict() if isinstance(request.data, QueryDict) else request.data
    #     CategoryMaster_qs = models.UserAccount.objects.filter(EmailId=data['EmailId'],UserPass=data['UserPass'])
    #     if CategoryMaster_qs.exists():
    #         return JsonResponse({'success': True, 'message': 'Login Information successfully.'}, status=201)
    #     return JsonResponse({'success': False, 'message': 'Login not found!'}, status=202)
    
    def post(self, request):
        """ PUT method handler to update Employee and MyConn data
        """
        data = request.data.dict() if isinstance(request.data, QueryDict) else request.data
        UserAccount_qs = models.UserAccount.objects.filter(EmailId=data['EmailId'],UserPass=data['UserPass'])
        if not UserAccount_qs.exists():
            return JsonResponse({'success': False, 'message': 'Invalid User Account'}, status=202)
        v_UserCode = UserAccount_qs.get(UserCode = UserAccount_qs.last().UserCode)
        if v_UserCode.UserCode > 0 :
            result =[]
            result.append({
                'UserCode':v_UserCode.UserCode,
                'UserName':v_UserCode.UserName,
                'FullName':v_UserCode.FullName,
                'ContactNo':v_UserCode.ContactNo,
                'EmailId':v_UserCode.EmailId,
                'UserPass':v_UserCode.UserPass,
                'UserType':v_UserCode.UserType,
                'UserTypeName':v_UserCode.UserTypeName,
                'Status':v_UserCode.Status
                })
            return JsonResponse({'success': True, 'message': 'UserAccount validation is successfull!', 'data':result}, status=201)
        
        return JsonResponse({'success': False, 'message': 'Invalid User Account'}, status=202)