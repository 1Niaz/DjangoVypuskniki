from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import *


""" 
class graduateInfoView(View):
    def get(self,request,pk):
        graduate_info = GraduateInfoModel.objects.get(id=pk)
        return render(request, 'main/graduate.html', {"graduate_info":graduate_info})

"""


class IndexView(View):
    def get(self, request, *args, **kwargs):
        graduates = GraduateInfoModel.objects.all()
        spec_list = GraduateInfoModel.objects.values_list('spec__spec_name', flat=True).distinct()
        year_list = GraduateInfoModel.objects.values_list('year_of_issue__year', flat=True).distinct().order_by('year_of_issue__year')
        
        specialization = request.GET.get('specialization')
        year = request.GET.get('year')
        
        if specialization:
            graduates = graduates.filter(spec__spec_name=specialization)
        if year:
            graduates = graduates.filter(year_of_issue__year=year)
        if year and specialization:
            graduates = graduates.filter(spec__spec_name=specialization, year_of_issue__year=year)
        
        return render(request, 'main/index.html', {
            'graduates': graduates, 
            'spec_list': spec_list, 
            'year_list': year_list,
            'specialization': specialization,
            'year_param': year,
        })




class graduateInfoView(View):
    def get(self,request,slug):
        graduate_info = GraduateInfoModel.objects.get(slug=slug)
        social_partners = SocialPartnersModel.objects.all()

        context = {
            "graduate_info": graduate_info,
            "social_partners": social_partners,
        }

        return render(request, 'main/graduate.html', context)


def show_info(request, slug):
    graduate = get_object_or_404(GraduateInfoModel, slug = slug)

    context = {
        "graduate_info" : graduate,
    }

    return render(request, 'main/graduate.html', context=context)

"""     
class collegeInfoView(View):
    def get(self,request):
        college_info = CollegeInfoMoodel.objects.all()
        return render(request, 'main/include/footer.html', {"college_info":college_info}) """


def signin(request):
    return render(request, 'main/signin.html')


# def afterSigninPage(request):
#     return render(request, 'main/main.html')

class afterSigninPage(View):
    def get(self, request, *args, **kwargs):
        graduates = GraduateInfoModel.objects.all()
        spec_list = GraduateInfoModel.objects.values_list('spec__spec_name', flat=True).distinct()
        year_list = GraduateInfoModel.objects.values_list('year_of_issue__year', flat=True).distinct().order_by('year_of_issue__year')
        
        specialization = request.GET.get('specialization')
        year = request.GET.get('year')
        
        if specialization:
            graduates = graduates.filter(spec__spec_name=specialization)
        if year:
            graduates = graduates.filter(year_of_issue__year=year)
        if year and specialization:
            graduates = graduates.filter(spec__spec_name=specialization, year_of_issue__year=year)
        
        return render(request, 'main/main.html', {
            'graduates': graduates, 
            'spec_list': spec_list, 
            'year_list': year_list,
            'specialization': specialization,
            'year_param': year,
        })




