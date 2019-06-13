import os
import re
from pyrogram import Client

# from https://my.telegram.org/apps
api_id = 12345
api_hash = "b1b1b1b1b1b1bb1b1b1b1b1bb1b1b1b1"
phone_number = '+79998887766'
DEBUG = 0


def phone_code_callback(x):
    return input('Enter code:').strip()


def get_code():
    app = Client(
        phone_number.strip('+'),
        api_id,
        api_hash,
        phone_number=phone_number,
        phone_code=phone_code_callback,
        workdir='tmp',
    )

    app.start()

    if DEBUG:
        for dialog in app.get_dialogs().dialogs:
            if dialog.chat.first_name == 'Telegram':
                print(dialog.chat.id, dialog.chat.type, [dialog.chat.title, dialog.chat.username, dialog.chat.first_name])
                print('\t', dialog.top_message.message_id, dialog.top_message.date, dialog.top_message.text)

    ret = app.get_history(777000, limit=10)

    for message in ret.messages:
        m = re.search(r'(?:Код подтверждения|Login code|Your login code): (\d+)', message.text)
        if m:
            code = m.group(1)
            ret = {
                'message_id': message.message_id,
                'date': message.date,
                'first_name': message.from_user.first_name,
                'text': message.text,
                'code': code,
            }
            print(str(ret))
            app.stop()

    print('---END---')
    os._exit(0)


if __name__ == "__main__":
    get_code()
