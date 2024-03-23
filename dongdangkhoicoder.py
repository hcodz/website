from flask import Flask, request
import hashlib,time,datetime,string,requests,json
from datetime import datetime,date
def rutgonlink (url):
    try:
        link = requests.get('https://yeumoney.com/api.php?token=5c6ca45f8786a484731a8b800d2c76a248129c10060f3a1e5b42365da7f5dbdc&url='+url).json()["url"]
        x=requests.get(f'https://link4m.co/api-shorten/v2?api=6506c585b96a684478636b84&url='+link).text
        x=json.loads(x)
        linkvuot=x["shortenedUrl"]
        return linkvuot
    except :
        x=requests.get(f'https://link4m.co/api-shorten/v2?api=6506c585b96a684478636b84&url='+url).text

        x=json.loads(x)

        linkvuot=x["shortenedUrl"]
        return linkvuot
app = Flask(__name__)


@app.route('/')
def get_key():
  # Lấy giá trị của tham số key
  key = request.args.get('key')
  keyduphong = request.args.get('keyduphong')
  datetao = request.args.get('datetao')
  datehethan = request.args.get('datehethan')

  # Gộp lại thành một chuỗi thông tin với xuống dòng sử dụng thẻ HTML <br/>
  info = f"Key: {key}<br/>Key Dự Phòng: {keyduphong}<br/>Ngày Tạo: {datetao}<br/>Ngày Hết Hạn: {datehethan}"
  return info
@app.route('/getlink/')
def get_code_enc():
  # Lấy giá trị của tham số key
  key = request.args.get('enccode')
  today = date.today()
  d1 = (key) + (today.strftime("%Y/%m/%d")) +'fcdsdf3'
  str = hashlib.md5(d1.encode('utf-8')).hexdigest() + "493f"
  stro = ''
  for i in range (len(str) ):
        if i ==0 :
            stro += str[i]
        elif i > 0 and i <5:
            stro += str[i+2]
        elif i>5:
            stro += str[i+-3]
  # Gộp lại thành một chuỗi thông tin với xuống dòng sử dụng thẻ HTML <br/>
  info = 'KKtool' + stro + '93f'
  link = rutgonlink ('https://khoido.pythonanywhere.com/?key='+info+'&keyduphong='+info+'&')
  return link
if __name__ == '__main__':
  app.run(port=5000, debug=False)
