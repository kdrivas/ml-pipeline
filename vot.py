import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '2008994569:AAFP6UTqxYbRif5QntR5t2hwnWG-ZeyvvKg'
    bot_chatID = '1236029712'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

test = telegram_bot_sendtext("Auto refresh enabled...")
print(test)