
from bs4 import BeautifulSoup
import pandas as pd
import requests

def get_html(page):
    response = requests.get('http://www.haitibusiness.com/11/category?page='+str(page))
    return response.text

def get_content(page):
    text = get_html(page)
    soup = BeautifulSoup(text,'html.parser')
    content = soup.find(id='content')
    content = content.div.find_all(class_="box-business")
    return content
    pass
def get_phone(content):
    a=[]
    phones =content.find("div",class_="phone").find_all("a")
    for phone in phones:
        a.append(phone.text)
    return a
    pass

def get_address(content):
    address = content.find("div",class_="address")
    address = {"ville":address["data-city"],"address":address.text}
    return address
    pass

def content_to_dic():
    dict = []
    for i in range(1,30):
        contents = get_content(i)
        for content in contents:
            myad = get_address(content)
            dict.append({"email" : content.find("a",class_="email").text,"phone":get_phone(content), "ville": myad["ville"], "address":myad["address"] })
    return dict
    pass
def run():
    dict = content_to_dic()
    print(dict)
    print("len of dict"+str(len(dict)))
    df = pd.DataFrame(dict)
    df.to_csv("./business.csv")
pass
