from asyncio.tasks import sleep, wait
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ParselVerileri,SehirMerkezi
from django.views import View
from django.utils.decorators import method_decorator
from django.template.response import TemplateResponse
import math
from decimal import Decimal,ROUND_HALF_EVEN
import asyncio


@method_decorator(csrf_exempt, name='dispatch')
##Burası POST GET ve HESAPLAMA metodlarının olduğu Class
class ParselFind(View):
    ## Kurucu method
    def __init__(self):
        self.sehiler = SehirMerkezi.objects.all().values()
     ## GET
    def get(self,request):
        return render(request, 'home.html')
    #POST
    def post(self,request):
        #birinci POST
        data=list()
        if request.POST.dict()['type'] == 'parselbul':
            min_value = int(request.POST.dict()['min'])
            max_value = int(request.POST.dict()['max'])
            __mesafe = request.POST.dict()['mesafe']
            sehir_id = request.POST.dict()['sehir']
            for parsel in ParselVerileri.objects.filter(alan__gte=min_value).filter(alan__lte=max_value).values():
                mesafe =  self.hesapla(parsel['ada'],__mesafe,sehir_id)
                
                if mesafe is not None: ### mesdafe değeri geliyorsa
                    veriler = {}
                    veriler['mesafe'] = mesafe
                    veriler['ada'] = parsel['ada']
                    veriler['parsel'] = parsel['parsel']
                    data.append(veriler)
        return JsonResponse(list(data),safe=False)


            #return JsonResponse(list(ParselVerileri.objects.filter(alan__gte=min_value).filter(alan__lte=max_value).values()),safe=False)
        #İkinci POST Bu
        # elif request.POST.dict()['type'] == 'mesafebul':
        #     ada_number=request.POST.dict()['ada']
        #     if ParselVerileri.objects.filter(ada=ada_number).count():
        #         print(self.hesapla(ada_number))
        #         return JsonResponse({'status':200,'mesafe':self.hesapla(ada_number) }) 
        #     else:
        #         return JsonResponse({'status':400}) 

    #Hesaplama
    def hesapla(self,ada,mesafe,sehir):
        __mesafe=mesafe
        try:
            x = ParselVerileri.objects.filter(ada=ada).values_list('kordinatx',flat=True).first()
            y = ParselVerileri.objects.filter(ada=ada).values_list('kordinatx',flat=True).first()  
            x1=SehirMerkezi.objects.filter(parselid=sehir).values_list('kordinatx',flat=True).first()
            y1=SehirMerkezi.objects.filter(parselid=sehir).values_list('kordinaty',flat=True).first()
            #print(x,x1,y,y1)
            
            mesafe_fark=self.formul(x1,x,y1,y)
            #print(mesafe_fark)
            sonuc=self.mesafe_farkı_uygun_mu(__mesafe,mesafe_fark)
            if sonuc is not None:
                return sonuc
        except Exception as err:
            #HATAYA uğrarsa boş döndür amksat kod kırılmasın
            #print("-",err)
            return None
    
    def formul(self,x1,x2,y1,y2):
       return   math.sqrt(abs((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))
    
    def mesafe_farkı_uygun_mu(self,mesafe,mesafe_farkı):
        #print(mesafe,mesafe_farkı)
        try:
            if float(mesafe) > mesafe_farkı:
                return mesafe_farkı
            else:
                return None
        except Exception as err:
            print(err)
            pass

         