
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ForgetPassword

class ForgotPasswordView(APIView):
    """ Unauthorized User Forgot Password View """

    def post(self, request): 

        try:
            user = User.objects.get(email=request.data['email'])
            
        except Exception as err:
            return Response({
                "message": f"User account with email {request.data['email']} not found.",
                "status_code": status.HTTP_404_NOT_FOUND,
                "error": str(err)
            })

        forgot_password_obj = ForgotPassword.objects.filter(user=user).first()
        forgot_password_obj.is_user_password_updated = True
        forgot_password_obj.save()
        return Response({
            "Message": "Success. Check your email for the otp.",
            "Status_Code": status.HTTP_201_CREATED
         })