import json, requests
import sendgrid
import MySQLdb
import mysql.connector
from sendgrid.helpers.mail import *

url="https://developers.zomato.com/api/v2.1/"
headers= {'user-key': ''}

def get_reviews(resId):
    url1= url+"reviews?res_id="+resId
    request = requests.get(url1,headers=headers)
    data = request.json()
    reviews = data['user_reviews']
    for x in reviews:
        sentimentanalysis(x['review']['review_text'])


def sendemail(text, sentiment):
    sg = sendgrid.SendGridAPIClient(apikey='')
    from_email = Email("")
    to_email = Email("")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "Review ->\n"+text+"  \n the sentiment analysis\n"+sentiment )
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.body)
    print(response.headers)
    return

def sentimentanalysis(text):
    request = requests.post("http://text-processing.com/api/sentiment/",data={"text":text})
    data = request.json()
    print text+"\n the sentiment analysis   "+ data['label']
    sendemail(text,data['label'])
    return

def get_res_id(name):
    request = requests.get(url+"search?q="+name,headers=headers)
    data=request.json()
    restaurants=data['restaurants']
    for x in restaurants:
        restaurant=x['restaurant']
        print restaurant['id'],restaurant['location']['address'],restaurant['location']['city']
    res_id=raw_input("enter the res id from above\n")
    get_reviews(res_id)


def main():
    search_res=raw_input("enter the returants name\n")
    get_res_id(search_res)

main()


