# import asyncio
# from telethon import TelegramClient

# # API ma'lumotlari (my.telegram.org saytidan oling)
# API_ID = 28904035  # O'zingizning API ID yozing
# API_HASH = "1c448c4a97970b435dac3c2466aedab1"  # O'zingizning API Hash yozing
# PHONE_NUMBER = "+998909280771"  # Telefon raqamingiz

# # Xabar yuboriladigan guruhlar ro‘yxati (username yoki ID lar)
# GROUPS = [
#     # "@dasturchilar_groupp",  # 1-guruh
#     -1922804886, #Uz garantni guruhi
#     # -2016923230, #Uz garantni 2-guruhi
#     # -1388131846, # Binance uzbekistan guruhi || https://t.me/tapswap_hamster_savdo_forum_chat
#     # -2203670917, #Istamov yaqinlari || Forum savdo
#     # -1916315162, #Ishonchi savdo
    
#     # #Tekin reklama ||
#     # -2288412718, #rek vz gr | rek
#     # -2463506982, #Reklama uz forum
#     # -2170188286. #Tekin reklama
#     # -2069351139,
#     # -4771228439,
#     # -4758155066,
# ]

# # Telethon sessiyasini yaratish
# client = TelegramClient("my_session", API_ID, API_HASH)

# async def send_messages():
#     await client.start(PHONE_NUMBER)  # Avtorizatsiya
#     print("Telegram akkauntga muvaffaqiyatli ulandik!")

#     while True:
#         for group in GROUPS:
#             try:
#                 await client.send_message(group, "Telegramda to'xtovsiz habar yuborish.\nSizning o'rningizga yozgan habaringizni dastur\naytgan guruhingizga yuboradi. \n\nBu habar ham avto habar yuborish orqali yuborilmoqda.\nRaqamingizni ulash narxi: 5 000 ming so'm.\nMurojat uchun: @Mr_XeaD",)
#                 print(f"Xabar yuborildi: {group}")
#             except Exception as e:
#                 print(f"Xatolik yuz berdi ({group}): {e}")

#         await asyncio.sleep(600)  # 600 soniya = 10 daqiqa

# # Klientni ishga tushirish
# with client:
#     client.loop.run_until_complete(send_messages())



# import asyncio
# from telethon import TelegramClient
# from telethon.tl.types import PeerChannel

# # API ma'lumotlari (my.telegram.org saytidan oling)
# API_ID = 28904035  # O'zingizning API ID yozing
# API_HASH = "1c448c4a97970b435dac3c2466aedab1"  # O'zingizning API Hash yozing
# PHONE_NUMBER = "+998909280771"  # Telefon raqamingiz

# # Xabar yuboriladigan guruhlar ro‘yxati (username yoki ID lar)
# GROUPS = [
#     -1922804886,  # Uz garant guruhi
#     -2016923230, #Uz garantni 2-guruhi
#     -2016923230, #Uz garantni 2-guruhi
#     -1388131846, # Binance uzbekistan guruhi || https://t.me/tapswap_hamster_savdo_forum_chat
#     -2203670917, #Istamov yaqinlari || Forum savdo
#     -1916315162, #Ishonchi savdo
    
#     #Tekin reklama ||
#     -2288412718, #rek vz gr | rek
#     -2463506982, #Reklama uz forum
#     -2170188286. #Tekin reklama
#     -2069351139,
#     -4771228439,
#     -4758155066,

# ]

# # Telethon sessiyasini yaratish
# client = TelegramClient("my_session", API_ID, API_HASH)

# async def send_messages():
#     await client.start(PHONE_NUMBER)  # Avtorizatsiya
#     print("Telegram akkauntga muvaffaqiyatli ulandik!")

#     while True:
#         for group in GROUPS:
#             try:
#                 if isinstance(group, int) and group < 0:
#                     group = PeerChannel(abs(group))  # Megaguruh uchun ID ni to‘g‘rilash

#                 entity = await client.get_entity(group)  # To‘g‘ri chat obyekti olish
#                 await client.send_message(entity, "Telegramda to'xtovsiz habar yuborish.\n"
#                                                    "Sizning o'rningizga yozgan habaringizni dastur\n"
#                                                    "aytgan guruhingizga yuboradi. \n\n"
#                                                    "Bu habar ham avto habar yuborish orqali yuborilmoqda.\n"
#                                                    "Raqamingizni ulash narxi: 5 000 ming so'm.\n"
#                                                    "Murojat uchun: @Mr_XeaD")
#                 print(f"✅ Xabar yuborildi: {group}")
#             except Exception as e:
#                 print(f"❌ Xatolik yuz berdi ({group}): {e}")

#         await asyncio.sleep(600)  # 10 daqiqa kutish

# # Klientni ishga tushirish
# with client:
#     client.loop.run_until_complete(send_messages())



# import asyncio
# from telethon import TelegramClient
# from telethon.tl.types import PeerChannel

# # API ma'lumotlari (my.telegram.org saytidan oling)
# API_ID = 28904035  # O'zingizning API ID yozing
# API_HASH = "1c448c4a97970b435dac3c2466aedab1"  # O'zingizning API Hash yozing
# PHONE_NUMBER = "+998909280771"  # Telefon raqamingiz

# # Xabar yuboriladigan guruhlar ro‘yxati (username yoki ID lar)
# GROUPS = [
#     -1922804886,  # Uz garant guruhi
#     -2016923230,  # Uz garant 2-guruhi
#     -2203670917,  # Istamov yaqinlari || Forum savdo
#     -1916315162,  # Ishonchi savdo
#     -2288412718,  # Reklama guruhi
#     -2463506982,  # Reklama uz forum
#     -2022831174,  # O'rtada turib berish guruhi 
#     -2394919330,  # Reklama 1,192 ta azo
#     -1517648590,  # Tekin reklama 15,750+ azo
# ]

# # Telethon sessiyasini yaratish
# client = TelegramClient("my_session", API_ID, API_HASH)

# async def send_messages():
#     await client.start(PHONE_NUMBER)  # Avtorizatsiya
#     print("✅ Telegram akkauntga muvaffaqiyatli ulandik!")

#     while True:
#         for group in GROUPS:
#             try:
#                 entity = await client.get_entity(PeerChannel(-group) if group < 0 else group)
#                 await client.send_message(entity, 
#                     "📢 Avtomatik habar yuborish!\n\n"
#                     "🔹 Bu habar avtomatik dastur orqali yuborildi. 🧑🏻‍💻\n"
#                     "🔹 O‘z xabarlaringizni kerakli guruhlarga yuborish imkoniyati bor.\n\n"
#                     "🔹 Open budjetga ovoz yeg'ayotganlar sizning o'rningizga dastur habar yuboradi\n"
#                     "🔹 Hattoki yopiq guruhlarga ham habar yuborish mumkin.\n"
#                     "🔹 Necha daqiqada habar yuborishni o'zingiz belgilaysiz 🕐\n"
#                     "🔹 Xabar yuborishga ketadigan vaqtingizni tejab qoling 🤫\n\n"


#                     "💰 Raqamingizni ulash narxi: 5 000 so'm.\n"
#                     "📩 Murojat uchun: @Mr_XeaD")
#                 print(f"✅ Xabar yuborildi: {group}")
#             except Exception as e:
#                 print(f"❌ Xatolik yuz berdi ({group}): {e}")

#         await asyncio.sleep(300)  # 3 daqiqa kutish

# # Klientni ishga tushirish
# with client:
#     client.loop.run_until_complete(send_messages())












import asyncio
import logging
from telethon import TelegramClient, errors
from telethon.tl.types import PeerChannel

# LOGGING - Xatolarni yozib borish
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Telegram API ma'lumotlari
API_ID = 25672276  # O'zingizning API ID yozing
API_HASH = "b41ebc93e68fb6a9909ca9f6d87ee696"  # O'zingizning API Hash yozing
PHONE_NUMBER = "+998939285758"  # Telefon raqamingiz

# Guruhlar ro‘yxati (ID yoki username)
GROUPS = [
   
          -1922804886, # uz garant | link yo'q
          -1535493404, # O'rtada turib berish gruppasi | link yo'q
        #   "@kanallar_savdosi3",
          "@uzgnet",
          "@uzbek_forum_vip",
          "@uzfor_garant_savdoi",
          "@uzbek_forum_pro",  #  Guruh username orqali
          "@garant_savdo_uzfor",
    -2203670917,  # Istamov yaqinlari || Forum savdo
    -1916315162,  # Ishonchi savdo
    -2288412718,  # Reklama guruhi
    -2463506982,  # Reklama uz forum
    # -2022831174,  # O'rtada turib berish guruhi 
    -2394919330,  # Reklama 1,192 ta azo
    -1517648590,  # Tekin reklama 15,750+ azo

]

# Xabar matni
MESSAGE_TEXT = """
📢 Avtomatik habar yuborish!\n\n"
🔹 Bu habar avtomatik dastur orqali yuborildi. 🧑🏻‍💻\n
🔹 O‘z xabarlaringizni kerakli guruhlarga yuborish imkoniyati bor.\n\n
🔹 Open budjetga ovoz yeg'ayotganlar sizning o'rningizga dastur habar yuboradi\n
🔹 Hattoki yopiq guruhlarga ham habar yuborish mumkin.\n
🔹 Necha daqiqada habar yuborishni o'zingiz belgilaysiz 🕐\n
🔹 Xabar yuborishga ketadigan vaqtingizni tejab qoling 🤫\n\n
💰 Raqamingizni ulash narxi: 5 000 so'm.\n
📩 Murojat uchun: @Mr_XeaD
"""

# Telethon sessiyasini yaratish
client = TelegramClient("my_session", API_ID, API_HASH)


async def check_and_join_group(group):
    """Guruhga a'zo bo‘lmagan bo‘lsa, avtomatik qo‘shiladi"""
    try:
        # Guruh ID yoki username orqali entity olish
        if isinstance(group, int):  # Agar ID bo‘lsa
            entity = await client.get_entity(PeerChannel(-group) if group < 0 else group)
        else:  # Agar username bo‘lsa
            entity = await client.get_entity(group)

        # Guruh a'zolarini tekshirish
        participant = await client.get_participants(entity)

        if participant:  # Agar a'zo bo'lsa
            logging.info(f"✅ Siz {group} guruhiga allaqachon a'zosiz.")
            return entity
        else:  # A'zo bo'lmasa, qo'shilish
            logging.info(f"🔄 {group} guruhiga qo‘shilmoqdamiz...")
            await client(JoinChannelRequest(entity))
            logging.info(f"✅ {group} guruhiga qo‘shildik!")
            return entity

    except errors.InviteRequestSentError:
        logging.error(f"⏳ {group} ga qo‘shilish uchun so‘rov yuborildi. Admin tasdiqlashi kerak.")
    except errors.ChatAdminRequiredError:
        logging.error(f"⛔ {group} ga qo‘shilish uchun admin ruxsati kerak!")
    except errors.FloodWaitError as e:
        logging.warning(f"⏳ FloodWaitError: {e.seconds} soniya kutish kerak!")
        await asyncio.sleep(e.seconds)
    except Exception as e:
        logging.error(f"❌ {group} ga qo‘shilishda xatolik: {e}")

    return None


async def send_messages():
    """Guruhga qo'shilish va xabar yuborish"""
    await client.start(PHONE_NUMBER)  # Avtorizatsiya
    logging.info("✅ Telegram akkauntga muvaffaqiyatli ulandik!")

    while True:
        for group in GROUPS:
            entity = await check_and_join_group(group)
            if entity:
                try:
                    await client.send_message(entity, MESSAGE_TEXT, parse_mode="md")
                    logging.info(f"✅ Xabar yuborildi: {group}")
                except Exception as e:
                    logging.error(f"❌ {group} ga xabar yuborishda xatolik: {e}")

        await asyncio.sleep(120)  # 3 daqiqa kutish


# Klientni ishga tushirish
with client:
    client.loop.run_until_complete(send_messages())
