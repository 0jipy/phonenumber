from django.views.generic import ListView, DetailView
from .models import Finder
# from django.shortcuts import render #필요없음

# Create your views here.

# CBV연습
class Finders(ListView):
    model = Finder
    ordering = '-pk'

class FinderDetail(DetailView):
    model = Finder

# FBV연습
# def index(request):
#     finders = Finder.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'finder/index.html',
#         {
#             'finders' : finders,
#         }
#     )

# # CBV로 구현시 필요없는 싱글페이지 함수.
# def single_page(request, pk):
#     finders = Finder.objects.get(pk=pk)
#
#     return  render(
#         request,
#         'finder/singel_page.html',
#         {
#             'finder' : finder,
#
#         }
#
#     )