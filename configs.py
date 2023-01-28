from dotenv import load_dotenv
from os import path, getenv, mkdir


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

if not path.exists("search"):
    mkdir("search")


class Configs:
    API_ID = '7166549'
    API_HASH = '9a3151e9f5815a26b9fd7f447a1040a6'
    BOT_TOKEN = '5951640980:AAFJz7Y8A2KZnpnbvdao4lEIGvwyWSVSuNg'
    OWNER_ID = 1179359966
    SESSION = 'BQB_tmX39Zy47B9eyH0hvG1JuDDj0_vkfNThT_XWRQ1DK5dWbVj0KYTfj1j2Ep8nJQmFKN_sw93hXffh_nn9yNb8ZnxG0alAx28Vg9pinyZb6t7yi5MVm0ULbU3swqNTO5XJkckanocoFBRW_TN-DYwe0OOAqwYjjAjwhYXDecI5CPHxG14-Xpq7icEj8k8_qNIrkAI70Pott15IiS4WKOeaZIJGAPv8PNrMlg1F7FKDjIXtkYQuSbEUocVnhHtrw5vAOnZyQIkzZ9Cn5HGlhM2a-I2FyuztSxpPFzp2Lau74OadRPcbK8O1BN48WvjHjghlb5QCpb_G9NZpObNEgy6ERskxzQA'
    CHANNEL_LINK = 'https://t.me/C_DanaInstantPay'
    GROUP_LINK = 'https://t.me/G_DanaInstantPay'
    UPSTREAM_REPO = 'https://github.com/CryptoHunter299/CodingMusicBot'
    AUTO_LEAVE = '1800'


config = Configs()
