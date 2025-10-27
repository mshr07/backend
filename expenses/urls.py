from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # Authentication
    path('auth/register/', views.UserRegistrationView.as_view(), name='user_register'),
    path('auth/login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/profile/', views.user_profile, name='user_profile'),
    
    # Categories
    path('categories/', views.ExpenseCategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', views.ExpenseCategoryDetailView.as_view(), name='category_detail'),
    
    # Expenses
    path('expenses/', views.ExpenseListCreateView.as_view(), name='expense_list_create'),
    path('expenses/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense_detail'),
    path('expenses/history/', views.expense_history, name='expense_history'),
    path('expenses/stats/', views.expense_stats, name='expense_stats'),
]