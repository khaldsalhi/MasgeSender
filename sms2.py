import os
import json
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

# اجرای فرمان و دریافت لیست مخاطبین به صورت JSON
contacts_json = os.popen('termux-contact-list').read()

# تبدیل رشته JSON به ساختار پایتون (لیست یا دیکشنری)
contacts = json.loads(contacts_json)

# لیستی برای ذخیره شماره‌ها
contacts_numbers = []
# پیمایش مخاطبین و اضافه کردن شماره‌ها
for contact in contacts:
    if "number" in contact:  # بعضی وقت‌ها مخاطب ممکنه شماره نداشته باشه
        contacts_numbers.append(contact["number"])
    elif "phone" in contact:  # ساختار بعضی گوشی‌ها
        contacts_numbers.append(contact["phone"])

# نمایش شماره‌ها
print(contacts_numbers)
contacts_numbers = [num.replace(" ", "") for num in contacts_numbers]
with open("contacts.txt", "w") as f:
    for num in contacts_numbers:
        f.write(num + "\n")

print(f"{len(contacts_numbers)} شماره ذخیره شد در contacts.txt")
