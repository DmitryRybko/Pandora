from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

import account.views as account

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(next_page='/'), name='login'),
    path('update/<int:pk>/', account.AccountUpdateView.as_view(), name='update'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', account.RegistrationView.as_view(), name='registration'),
    path('<int:pk>/', account.AccountPersonalData.as_view(), name='personal_data'),
    path('<int:pk>/my_articles/<str:type>/', account.AccountArticles.as_view(), name='my_articles'),
    path('adminaccount/<int:pk>/', account.AdminAccountView.as_view(), name='admin_account'),
    path('moderatoraccount/<int:pk>/', account.ModeratorAccountView.as_view(), name='moder_account'),
    path('give_rights/<int:pk>/', account.give_rights_moderator, name='give_rights'),
    path('approve/<str:type>/<int:pk>/', account.approve_moder_article, name='approve_moder'),
]
