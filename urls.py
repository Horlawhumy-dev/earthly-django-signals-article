from .  import views

path('user/account/forgot-password', views.ForgotPasswordView.as_view(), name="forgot-password")