from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from qrcode.image.svg import SvgImage
from django.http import HttpResponse
import io


# Create your views here.

def qr_gen(request):
    if request.method == 'POST': 
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(settings.MEDIA + '/' + img_name)
        print(img_name)
        return render(request, 'portfolio/portfolio.html', {'img_name': img_name})
    return render(request, 'core/home.html')

