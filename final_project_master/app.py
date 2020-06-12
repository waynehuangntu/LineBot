from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from datetime import datetime

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)

savinglist = []
restaurant = 0
# import random

"""透過google sheet api將我們建立的資料庫匯入"""
import gspread
gc = gspread.service_account(filename = 'python-course-279611-a46bd48963dd.json')

survey_key = '1y2zWIF_SKFx4Eld5W0P9aoj4a_AkX_OATKPWtWkoRRo'
sh = gc.open_by_key(survey_key)
worksheet = sh.sheet1

res = worksheet.get_all_records()


# class
class Restaurant:
    def __init__(self, name, weather, temp, mood, price, place, friend, foodtype,
                 timing, sandy, image, address, longitude, latitude):
        self.name = name
        self.weather = weather.split("、")
        self.temp = temp.split("、")
        self.mood = mood.split("、")
        self.price = price.split("、")
        self.place = place
        self.friend = friend
        self.foodtype = foodtype
        self.timing = timing.split("、")
        self.sandy = sandy
        self.image = image
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.Num_of_match = 0

Restaurantdict = {}

# 讀檔
for row in res:
    aRestaurant = Restaurant(row["店名"], row["天氣"], row["溫度"], row["心情"], row["價格"], row["地區"], row["聚餐"], row["食物類別I"], row["時段"], row["聖方推薦與否"], row["圖片網址"], row["地址"], row["經度"], row["緯度"])
    Restaurantdict[row["店名"]] = aRestaurant

# 去計算每個餐廳跟使用者的偏好有多少項符合
def update_Num_of_match():
    global Restaurantdict
    for Restaurant in Restaurantdict.values():
        Num_of_match = 0
        for weather in Restaurant.weather:
            if weather in savinglist:
                Num_of_match += 1
                break

        for temp in Restaurant.temp:
            if temp in savinglist:
                Num_of_match += 1
                break

        for mood in Restaurant.mood:
            if mood in savinglist:
                Num_of_match += 1
                break

        for price in Restaurant.price:
            if price in savinglist:
                Num_of_match += 1
                break

        if Restaurant.place in savinglist:
            Num_of_match += 1

        if Restaurant.friend in savinglist:
            Num_of_match += 1

        if Restaurant.foodtype in savinglist:
            Num_of_match += 1

        for timing in Restaurant.timing:
            if timing in savinglist:
                Num_of_match += 1
                break

        if Restaurant.sandy in savinglist:
            Num_of_match += 1

        Restaurant.Num_of_match = Num_of_match

# 找出符合最多的那幾個餐廳
def find_best():
    best_Num_of_match = 0
    best_Num_of_match_list = []
    for Restaurant in Restaurantdict.values():
        if Restaurant.Num_of_match > best_Num_of_match:
            best_Num_of_match = Restaurant.Num_of_match
            best_Num_of_match_list = []
            best_Num_of_match_list.append(Restaurant)
        elif Restaurant.Num_of_match == best_Num_of_match:
            best_Num_of_match_list.append(Restaurant)
    # random.shuffle(best_Num_of_match_list)
    now = datetime.now()
    second = now.strftime("%S")
    index = int(second) % len(best_Num_of_match_list)
    return best_Num_of_match_list[index]



# Channel Access Token
line_bot_api = LineBotApi('ILh4a91G2sR8bBbfAz9YOi6RvzfousZ+Q+G7PF5Gylx3Re5XaeOI65RH3JdtS/LUxrHx53yG73Nt3uMlry5mL4jqA3g1ajmL83dlrjq6NOIVjPe0FuYFFdOYstlZfntVHycjzMcNiOhyM64SO7GveAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler("9565a35e1afc821cbe78d714e2cd45c5")

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global savinglist
    global restaurant
    msg = event.message.text
    if 'start!' == msg:
        savinglist = []
        # savinglist.append("aaaaaa")
        message = buttons_weather_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'start' in msg:
        message = TextSendMessage(text="你是不是多輸入什麼或少輸入什麼？再試一次吧！")
        line_bot_api.reply_message(event.reply_token, message)

    elif '晴天' == msg or '雨天' == msg:  
        if '晴天' in savinglist or '雨天' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_temperature_message()
            line_bot_api.reply_message(event.reply_token, message)


    elif '冷' == msg or '熱' == msg:  
        if '冷' in savinglist or '熱' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_timing_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '剛睡醒吃早餐' == msg or '剛睡醒吃午餐' == msg or '都不是啦' == msg:  
        if '剛睡醒吃早餐' in savinglist or '剛睡醒吃午餐' in savinglist or '都不是啦' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        elif '都不是啦' == msg:
            message = buttons_timing2_message()
            savinglist.append(msg)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_mood_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '剛睡醒吃下午茶' == msg or '剛睡醒吃晚餐' == msg or '不知道捏，我剛睡醒。' == msg:  
        if '剛睡醒吃下午茶' in savinglist or '剛睡醒吃晚餐' in savinglist or '不知道捏，我剛睡醒。' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_mood_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '考100分' == msg or '考80分' == msg or '這都不是我的分數><' == msg:  
        if '考100分' in savinglist or '考80分' in savinglist or '這都不是我的分數><' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        elif '這都不是我的分數><' == msg:
            message = buttons_mood2_message()
            savinglist.append(msg)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_price_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '考60分' == msg or '不及格' == msg or '心情是不會影響我吃東西的啦！' == msg:  
        if '考60分' in savinglist or '不及格' in savinglist or '心情是不會影響我吃東西的啦！' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_price_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '100以下' == msg or '100~200' == msg or '太便宜了啦，給我更多選項' == msg:  
        if '100以下' in savinglist or '100~200' in savinglist or '太便宜了啦，給我更多選項' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        elif '太便宜了啦，給我更多選項' == msg:
            message = buttons_price2_message()
            savinglist.append(msg)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_TypeOfFood_message()
            line_bot_api.reply_message(event.reply_token, message)
 
    elif '200~300' == msg or '300以上' == msg or '我根本不精打細算！' == msg:  
        if '200~300' in savinglist or '300以上' in savinglist or '我根本不精打細算！' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_TypeOfFood_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '西式' == msg or '台、港、中' == msg or '這些都不是啦！' == msg:  
        if '西式' in savinglist or '台、港、中' in savinglist or '都不是啦！' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        elif '這些都不是啦！' == msg:
            message = buttons_TypeOfFood2_message()
            savinglist.append(msg)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_Place_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '日、韓' == msg or '東南亞' == msg or '咖啡（點心）' == msg or '我都行的啦><' == msg:  
        if '日、韓' in savinglist or '東南亞' in savinglist or '咖啡（點心）' in savinglist or '我都行的啦><' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_friend_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '公館商圈' == msg or '118' == msg or '再給我更多選擇QQ' == msg:  
        if '公館商圈' in savinglist or '118' in savinglist or '再給我更多選擇QQ' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        elif '再給我更多選擇QQ' == msg:
            message = buttons_Place2_message()
            savinglist.append(msg)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_friend_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '樂樂街&安居街' == msg or '溫州街' == msg or '其他' == msg:  
        if '樂樂街&安居街' in savinglist or '溫州街' in savinglist or '其他' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_friend_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '當然有，朋友王就是我' == msg or '我沒有朋友。' == msg or '有與沒有之間' == msg:  
        if '當然有，朋友王就是我' in savinglist or '我沒有朋友。' in savinglist or '有與沒有之間' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            message = buttons_sandy_message()
            line_bot_api.reply_message(event.reply_token, message)

    elif '我超級想知道的' == msg or '否，我根本不在乎' == msg:  
        if '我超級想知道的' in savinglist or '否，我根本不在乎' in savinglist:  
            message = TextSendMessage(text="還敢再按一次啊！給我重新開始吧！")
            line_bot_api.reply_message(event.reply_token, message)
        else:
            savinglist.append(msg)
            savinglist = simplify_savinglist(savinglist)
            update_Num_of_match()
            restaurant = find_best()
            message = buttons_recommendation_message(restaurant)
            line_bot_api.reply_message(event.reply_token, message)
    elif msg == "精選圖片":
        base_url = str(restaurant.image)
        message = ImagemapSendMessage(
        base_url= base_url,
        alt_text='美食上菜囉！', base_size=BaseSize(height=1280, width=1024))
        line_bot_api.reply_message(event.reply_token, message)
    elif msg == "怎麼走":
        
        """line not Location API 
        可以連結到google map"""
        address = str(restaurant.address)
        longitude = str(restaurant.longitude)
        latitude = str(restaurant.latitude)
        message = LocationSendMessage(
        title = restaurant.name,
        address = address,
        latitude = latitude,
        longitude = longitude
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif msg == "推薦其他家":
        message = TextSendMessage(text="不要。")
        line_bot_api.reply_message(event.reply_token, message)



    # for checking
    elif "list" == msg:
        strmessage = ""
        for i in range(len(savinglist)):
            strmessage += str(savinglist[i]) + "、"
        strmessage = strmessage[0:-1]
        message = TextSendMessage(text=strmessage)
        line_bot_api.reply_message(event.reply_token, message)

    elif "test" == msg:
        base_url = str(Restaurantdict["貓大福"].image)
        message = ImagemapSendMessage(
        base_url= base_url,
        alt_text='美食上菜囉！', base_size=BaseSize(height=1280, width=1024))
        line_bot_api.reply_message(event.reply_token, message)

    elif "test2" == msg:
        strmessage = str(Restaurantdict["貓大福"].address)
        message = TextSendMessage(text=strmessage)
        line_bot_api.reply_message(event.reply_token, message)
    elif "test21" == msg:
        strmessage = str(Restaurantdict["貓大福"].longitude)
        message = TextSendMessage(text=strmessage)
        line_bot_api.reply_message(event.reply_token, message)
    elif "test22" == msg:
        strmessage = str(Restaurantdict["貓大福"].latitude)
        message = TextSendMessage(text=strmessage)
        line_bot_api.reply_message(event.reply_token, message)

    elif "test3" == msg:
        address = str(Restaurantdict["貓大福"].address)
        longitude = str(Restaurantdict["貓大福"].longitude)
        latitude = str(Restaurantdict["貓大福"].latitude)
        message = LocationSendMessage(
        title = Restaurantdict["貓大福"].name,
        address = address,
        latitude = latitude,
        longitude = longitude
        )
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text="輸入start!以開始")
        line_bot_api.reply_message(event.reply_token, message)

# @handler.add(PostbackEvent)
# def handle_postback(event):
    # postBack = event.postback.data






import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
