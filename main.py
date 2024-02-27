
# 11

# with open('data.yaml', 'w') as f:
#     yaml.dump(input('soz yoz : '), f)


# 12


# import openpyxl
#
# workbook = openpyxl.Workbook()
#
# sheet = workbook.active
#
# sheet['A1'] = 'Name'
# sheet['B1'] = 'age'
# sheet['C1'] = 'address'
# sheet['D1'] = 'phone_number'
#
# sheet['A2'] = 'Diyorbek' # noqa
# sheet['B2'] = 15 # noqa
# sheet['C2'] = 'Mirzo ulugbek' # noqa
# sheet['D2'] = '0987654321' # noqa
#
# workbook.save("data.xlsx")





# 10 - misol

# import json
#
# text = {
#     'word':'hello world'
# }
#
# with open('Torabekov_08.json', 'w') as f:
#     json.dump(text, f)


# 2 - misol

# import asyncio
# import logging
# from aiogram import Bot, Dispatcher
# from aiogram.filters import CommandStart
# from aiogram.types import Message
#
# TOKEN = ""
#
# dp = Dispatcher()
#
#
# @dp.message(CommandStart())
# async def start(message: Message):
#     name = message.from_user.full_name
#     user = message.from_user.username
#     number = message.from_user.id
#     data = {"name": name, "username": user, "id": number}
#     with open("users.yaml", 'w') as f:
#         yaml.dump(data, f)
#     await message.answer("Salom bot ishlayabdi !")
#
#     @dp.message()
#     async def echo(message: Message):
#         await message.reply(message.text)
#
#
# async def main() -> None:
#     bot = Bot(token=TOKEN)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     asyncio.run(main())



# 1 - misol

# import base64

# data = input("so'z yoz: ")
# encoode = base64.b64encode(data.encode('utf-8'))
# print(f"encode text --> {encoode}")
# decoode = base64.b64decode(encoode).decode('utf-8')
# print(f"decode text --> {decoode}")

