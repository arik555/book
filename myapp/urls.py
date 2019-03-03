from django.urls import path
from .views import home, display, edit, add, erase, power

# VAR = ['category', 'book']

urlpatterns = [
	path('', home, name='home'),
	path('<int:cat_id>/', home, name='home'),
	path('read/<int:id>/', display, name='display'),
	path('add/<slug:typ>/', add, name='add'),
	path('edit/<slug:typ>/<int:id>/', edit, name='edit'),
	path('delete/<slug:typ>/<int:id>/', erase, name='delete'),
	path('power/', power, name='power'),
]