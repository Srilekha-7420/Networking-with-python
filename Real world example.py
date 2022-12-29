#Before Threadind
import requests
import time
img_urls=["https://www.pexels.com/photo/pink-red-yellow-petaled-flower-in-close-up-shot-85773/",
         "https://www.istockphoto.com/photo/morning-visitor-gm1336193639-417545877"]
t1=time.perf_counter()
for img_url in img_urls:
    img_bytes=requests.get(img_url).content
    img_name=img_url.split('/')[4]
    img_name=f'{img_name}.jpg'
    with open(img_name,'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded')
finish=time.perf_counter()
print(f'Finshed in {finish-t1}seconds')