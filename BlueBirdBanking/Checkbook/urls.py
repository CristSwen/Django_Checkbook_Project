from django.urls import path
from . import views


urlpatterns = [
    #Sets the url path to the home page index.html
    path('', views.home, name='index'),
    #Sets the url path to reate new account page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    #Sets the url path to balacne sheet page BalanceSheet.html
    path('balance/', views.balance, name='balance'),
    #Sets the url path to add new transaction page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction'),
    path('<int:pk/balance/', views.balance, name='balance'),
]