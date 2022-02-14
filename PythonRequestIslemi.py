import requests 

req = requests.get("http://musana.net", params={'par':'value'})
print(req.url) #çıktı=par=value


req=requests.get("http://musana.net",params={'par1':'value1','par2':'value2'})
print(req.url)

req=requests.get("http://musana.net",params={'par1':'value1','par2':['var1','var2','var3']})
print(req.url)

req=requests.post("http://musana.net",params={'kullanıcı':'beri','meslek':'mühendis'})

#diger metod isimlerini kullanrak request göndermek

req=requests.head("http://musana.net")
req=requests.delete("http://musana.net")
#req=requests.option("http://musana.net")
req=requests.head("http://musana.net")


#dönen cevabı işleme
"""req = requests.get("http://musana.net", params={'par1':'value1', 'par2':'value2'})
print(req.text) 

"""

#yapılan işleme göre dönen http reponse kodu
req=requests.post("http://musana.net")
print(req.status_code)

#Sunucudan dönen cevabın başlık bilgilerine erişebilmek
# için ise request nesnemize headers nesne değişkeni üzerinden erişebiliriz.
#başlık degeri yoksa sonuç none döner.

#req=requests("http://musana.net")
print(req.headers)

#karşı sunucuya dosya göndermek,flles parametresi kullanılır.

dosya={"dosyam":open("python.txt","rb")}
req=requests.post("http://musana.net",files=dosya)

#gönderdigimiz içergiin zaman aşımını kontrol etmek
req=requests.get('http://github.com',timeout=0.099)
 #cevap dönmezse timeout meydana gelir










