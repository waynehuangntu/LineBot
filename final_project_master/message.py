#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


# =========================================琛琛琛琛
def buttons_weather_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="今天天氣如何呢？",
            text="點選以下最符合的天氣",
            actions=[
                MessageTemplateAction(
                    label="晴天",
                    text="晴天"
                ),
                MessageTemplateAction(
                    label="雨天",
                    text="雨天"
                )
            ]
        )
    )
    return message

def buttons_temperature_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="今天天氣如何呢？",
            text="點選以下最符合的天氣",
            actions=[
                MessageTemplateAction(
                    label="冷",
                    text="冷"
                ),
                MessageTemplateAction(
                    label="熱",
                    text="熱"
                )
            ]
        )
    )
    return message

def buttons_timing_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您想吃哪一餐呢？",
            text="我們認為使用者大概都是剛睡醒！",
            actions=[
                MessageTemplateAction(
                    label="剛睡醒吃早餐",
                    text="剛睡醒吃早餐"
                ),
                MessageTemplateAction(
                    label="剛睡醒吃午餐",
                    text="剛睡醒吃午餐"
                ),
               MessageTemplateAction(
                    label="都不是啦",
                    text="都不是啦"
                )
            ]
        )
    )
    return message

def buttons_timing2_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您想吃哪一餐呢？",
            text="只有這些選項了！",
            actions=[
                MessageTemplateAction(
                    label="剛睡醒吃下午茶",
                    text="剛睡醒吃下午茶"
                ),
                MessageTemplateAction(
                    label="剛睡醒吃晚餐",
                    text="剛睡醒吃晚餐"
                ),
               MessageTemplateAction(
                    label="不知道捏，我剛睡醒。",
                    text="不知道捏，我剛睡醒。"
                )
            ]
        )
    )
    return message

def buttons_mood_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您今天的心情如何呢？",
            text="心情，用考試分數呈現應該最為理想。",
            actions=[
                MessageTemplateAction(
                    label="考100分",
                    text="考100分"
                ),
                MessageTemplateAction(
                    label="考80分",
                    text="考80分"
                ),
                MessageTemplateAction(
                    label="這都不是我的分數><",
                    text="這都不是我的分數><")
            ]
        )
    )
    return message

def buttons_mood2_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您今天的心情如何呢？",
            text="QQ，考爛也沒關係啦，來吃點好吃的吧！",
            actions=[
                MessageTemplateAction(
                    label="考60分",
                    text="考60分"
                ),
                MessageTemplateAction(
                    label="不及格",
                    text="不及格"
                ),
                MessageTemplateAction(
                    label="心情是不會影響我吃東西的啦！",
                    text="心情是不會影響我吃東西的啦！")
            ]
        )
    )
    return message

def buttons_price_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您偏好怎麼樣的價格呢？",
            text="身為精打細算的學生，價格是必須掌控的！",
            actions=[
                MessageTemplateAction(
                    label="100以下",
                    text="100以下"
                ),
                MessageTemplateAction(
                    label="100~200",
                    text="100~200"
                ),
                MessageTemplateAction(
                    label="太便宜了啦，給我更多選項",
                    text="太便宜了啦，給我更多選項")
            ]
        )
    )
    return message

def buttons_price2_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您偏好怎麼樣的價格呢？",
            text="身為精打細算的學生，價格是必須掌控的！",
            actions=[
                MessageTemplateAction(
                    label="200~300",
                    text="200~300"
                ),
                MessageTemplateAction(
                    label="300以上",
                    text="300以上"
                ),
                MessageTemplateAction(
                    label="我根本不精打細算！",
                    text="我根本不精打細算！")
            ]
        )
    )
    return message

def buttons_TypeOfFood_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您比較偏好哪種風味的料理呢？",
            text="本機器人最喜歡台式料理了！",
            actions=[
                MessageTemplateAction(
                    label="西式",
                    text="西式"
                ),
                MessageTemplateAction(
                    label="台、港、中",
                    text="台、港、中"
                ),
               MessageTemplateAction(
                    label="這些都不是啦！",
                    text="這些都不是啦！"
                )
            ]
        )
    )
    return message

def buttons_TypeOfFood2_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您比較偏好哪種風味的料理呢？",
            text="居然不選台式料理qq！",
            actions=[
                MessageTemplateAction(
                    label="日、韓",
                    text="日、韓"
                ),
                MessageTemplateAction(
                    label="東南亞",
                    text="東南亞"
                ),
                MessageTemplateAction(
                    label="咖啡（點心）",
                    text="咖啡（點心）"
                ),
               MessageTemplateAction(
                    label="我都行的啦><",
                    text="我都行的啦><"
                )
            ]
        )
    )
    return message

def buttons_Place_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您比較偏好去哪個地方吃東西呢？",
            text="即便選了118，還是有可能推薦你去公館商圈喔:)",
            actions=[
                MessageTemplateAction(
                    label="公館商圈",
                    text="公館商圈"
                ),
                MessageTemplateAction(
                    label="118",
                    text="118"
                ),
               MessageTemplateAction(
                    label="再給我更多選擇QQ",
                    text="再給我更多選擇QQ"
                )
            ]
        )
    )
    return message

def buttons_Place2_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您比較偏好去哪個地方吃東西呢？",
            text="究竟比較想去哪兒呀～",
            actions=[
                MessageTemplateAction(
                    label="樂樂街&安居街",
                    text="樂樂街&安居街"
                ),
                MessageTemplateAction(
                    label="溫州街",
                    text="溫州街"
                ),
               MessageTemplateAction(
                    label="其他",
                    text="其他"
                )
            ]
        )
    )
    return message

def buttons_friend_message():
    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您是否有與朋友同行？",
            text="如果是約會的話，就請離開程式吧。",
            actions=[
                MessageTemplateAction(
                    label="當然有，朋友王就是我",
                    text="當然有，朋友王就是我"
                ),
                MessageTemplateAction(
                    label="我沒有朋友。",
                    text="我沒有朋友。"
                ),
               MessageTemplateAction(
                    label="有與沒有之間",
                    text="有與沒有之間"
                )
            ]
        )
    )
    return message




def buttons_sandy_message():
    message = TemplateSendMessage(
        alt_text='您已獲得成為美食家的機會',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="您想接受美食大師聖芳的推薦嗎？",
            text="財金一，黃聖芳，隱藏在台大的美食家。",
            actions=[
                MessageTemplateAction(
                    label="我超級想知道的",
                    text="我超級想知道的"
                ),
                MessageTemplateAction(
                    label="否，我根本不在乎",
                    text="否，我根本不在乎"
                )
            ]
        )
    )
    return message

def buttons_recommendation_message(restaurant):

    message = TemplateSendMessage(
        alt_text='重要訊息！請立即點開！',
        template=ButtonsTemplate(
            thumbnail_image_url=str(restaurant.image),
            title="我們想推薦您的餐廳是" + str(restaurant.name),
            text="請選擇查看以下資訊",
            actions=[
                MessageTemplateAction(
                    label="精選圖片",
                    text="精選圖片"
                ),
                MessageTemplateAction(
                    label="怎麼走",
                    text="怎麼走"
                ),
                MessageTemplateAction(
                    label="推薦其他家",
                    text="推薦其他家"
                )
            ]
        )
    )
    return message

def simplify_savinglist(savinglist):
    if '都不是啦' in savinglist:
        savinglist.remove('都不是啦')
    if '不知道捏，我剛睡醒。' in savinglist:
        savinglist.remove('不知道捏，我剛睡醒。')
    if '這都不是我的分數><' in savinglist:
        savinglist.remove('這都不是我的分數><')
    if '心情是不會影響我吃東西的啦！' in savinglist:
        savinglist.remove('心情是不會影響我吃東西的啦！')
    if '太便宜了啦，給我更多選項' in savinglist:
        savinglist.remove('太便宜了啦，給我更多選項')
    if '我根本不精打細算！' in savinglist:
        savinglist.remove('我根本不精打細算！')
    if '這些都不是啦！' in savinglist:
        savinglist.remove('這些都不是啦！')
    if '我都行的啦><' in savinglist:
        savinglist.remove('我都行的啦><')
    if '再給我更多選擇QQ' in savinglist:
        savinglist.remove('再給我更多選擇QQ')
    if '否，我根本不在乎' in savinglist:
        savinglist.remove('否，我根本不在乎')
    return savinglist
    
