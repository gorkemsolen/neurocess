from selenium import webdriver
from flask import *
import json

#selenium ve chrome driver ile gereken bağlantıyı sağlayarak verilerin elementine erişim ve ekranda yazdırma

browser = webdriver.Chrome(executable_path='C:/Users/admin/Downloads/chromedriver_win32/chromedriver.exe')

browser.get("https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4")

#veri ekleme ve çıktı

total=[]
for i in range(25):
    i+=6
    rowNo=str(i)
    try:
        newClue = {
        'name': browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div["+rowNo+"]/div/div/div/div/div[2]/div[1]/h2/a/span").text,
        'price': browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div["+rowNo+"]/div/div/div/div/div[2]/div[3]/div/a/span/span[2]").text,
        }
    except:
        rowNo=str(i+1)
        try:
            newClue = {
            'name': browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div["+rowNo+"]/div/div/div/div/div[2]/div[2]/h2/a/span").text,
            'price': browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div["+rowNo+"]/div/div/div/div/div[2]/div[4]/div/a/span/span[2]").text,
         }
        except:
            rowNo=str(i+1)
    
    print(newClue)
    total.append(newClue)
    

#localhost bağlantı kurumu ve çıktı

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():

    json_dump=json.dumps(total)
    
    return json_dump

if __name__== "__main__":
    app.run()
