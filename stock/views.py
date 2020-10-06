from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')
def addblog(request):
    NumberAlbum=request.GET['NumberAlbum']
    YourContact=request.GET['YourContact']
    Deliverly=request.GET['Deliverly']
    SelectCard=request.GET['SelectCard']
    Main=request.GET['Main']
    city=request.GET['city']
    zip=request.GET['zip']

    return render(request, 'frontend/result.html',{'NumberAlbum':NumberAlbum, 'YourContact':YourContact, 
 'Deliverly':Deliverly, 'SelectCard':SelectCard, 'Main':Main, 'city':city, 'zip':zip})
