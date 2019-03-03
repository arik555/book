from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import Ebook, Category
from .forms import CategoryForm, EbookForm
from .utils import custom_pagination
# Create your views here.

def display(request, id):
	instance = Ebook.objects.get(id=id)
	context = {'instance': instance, }
	return render(request, 'display.html', context=context)

def home(request, cat_id=None):
	if cat_id is None:
		instance = Ebook.objects.all()
		instance, page_range = custom_pagination(request, instance)
		print(page_range)
		if request.method == 'GET':
			keyword = request.GET.get('qs')
			if keyword:
				instance = Ebook.objects.filter(Q(title__icontains=keyword)| Q(author__icontains=keyword))
		context = {'instance': instance, 'categories': Category.objects.all(), 'page_range': page_range,}
		return render(request, 'index.html', context=context)
	cat_obj = Category.objects.get(id=cat_id)
	instance = Ebook.objects.filter(category=cat_obj)
	context = {'instance': instance, 'categories': Category.objects.all(), }
	return render(request, 'index.html', context=context)

##### ADMIN SECTION #####
VAR = ['category', 'book']

def edit(request, typ, id):
	if typ in VAR and request.user.is_superuser:
		if typ == 'category':
			instance = Category.objects.get(id=id)
			form = CategoryForm(request.POST or None, instance=instance)
		elif typ == 'book':
			instance = Ebook.objects.get(id=id)
			form = EbookForm(request.POST or None, instance=instance)
		if request.method == 'POST':
			if form.is_valid():
				form.save()
		context = {'form': form, 'btn_val': 'Update', 'instance': instance}
		return render(request, 'add_edit.html', context=context)
	else:
		return HttpResponse('<h3>Invlid Request</h3>')

def add(request, typ):
	if typ in VAR and request.user.is_superuser:
		if typ == 'category':
			form = CategoryForm(request.POST or None)
		elif typ == 'book':
			form = EbookForm(request.POST or None)
		if request.method == 'POST':
			if form.is_valid():
				form.save()
		context = {'form': form, 'btn_val': 'Append'}
		return render(request, 'add_edit.html', context=context)
	else:
		return HttpResponse('<h3>Invlid Request</h3>')

def erase(request, typ, id):
	if typ in VAR and request.user.is_superuser:
		if typ == 'category':
			instance = Category.objects.get(id=id)
		elif typ == 'book':
			instance = Ebook.objects.get(id=id)
		instance.delete()
		return HttpResponse('<h3>Deletion Success : {}</h3>'.format(typ))
	else:
		return HttpResponse('<h3>Invlid Request</h3>')

def power(request):
	if request.user.is_superuser:
		instance = Category.objects.all()
		context = {'instance': instance, }
		return render(request, 'power.html', context=context)
	else:
		return HttpResponse('<h3>Invlid Request</h3>')