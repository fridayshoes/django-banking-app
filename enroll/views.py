from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#function for user to enroll in the bank
def enroll_user(request):
    return render(request, 'enroll/enroll.html')
 
def enrolled_user(request):
    return HttpResponse("enrolled_user function called")