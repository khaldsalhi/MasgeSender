import os
from colorama import Fore, Style, init
init(autoreset=True)

def show_logo():
    print(Fore.CYAN + r"""
   ███████╗███████╗███╗   ██╗██████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗  ██████╗ ███████╗
   ██╔════╝██╔════╝████╗  ██║██╔══██╗████╗ ████║██╔══██╗██╔════╝██╔═══██╗██╔═══██╗██╔════╝
   ███████╗█████╗  ██╔██╗ ██║██║  ██║██╔████╔██║███████║███████╗██║   ██║██║   ██║█████╗  
   ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██║╚██╔╝██║██╔══██║╚════██║██║   ██║██║   ██║██╔══╝  
   ███████║███████╗██║ ╚████║██████╔╝██║ ╚═╝ ██║██║  ██║███████║╚██████╔╝╚██████╔╝███████╗
   ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝
    """)
    print(Fore.YELLOW + "📢 SendMasge - ابزار ارسال تبلیغات پیامکی")
    print(Fore.GREEN + "👨‍💻 توسعه داده شده توسط خالد صالحی")
    print(Fore.MAGENTA + "=" * 90)

show_logo()
message=input("plase write your masage ? ")
# نام فایل متنی که شماره تلفن‌ها در آن ذخیره شده است
file_name = 'contacts.txt'

# خواندن شماره تلفن‌ها از فایل
with open(file_name, 'r') as file:
    phone_numbers = file.readlines()



for phone_number in phone_numbers:
    phone_number = phone_number.strip()  # حذف فاصله‌های اضافی
    if phone_number:  # بررسی اینکه شماره تلفن خالی نباشد
        command = f"termux-sms-send -n {phone_number} '{message}'"
        os.system(command)
        print(f"پیام به {phone_number} ارسال شد.")

