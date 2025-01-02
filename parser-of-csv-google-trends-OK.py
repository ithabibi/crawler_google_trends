import sys  # for utf8
import csv
import locale
import pandas as pd
from io import StringIO
import pandas as pd
from datetime import datetime
import os

sys.stdout.reconfigure(encoding='utf-8')
print("به عنوان کدینگ پیش فرض فعال شد", sys.getdefaultencoding())

directory_path = r"C:\related-dir"  # مسیر دایرکتوری که فایل‌ها در آن قرار دارند

# لیست کردن فایل‌ها در دایرکتوری
for filename in os.listdir(directory_path):
    # بررسی اینکه آیا نام فایل با عبارت 'relatedQueries' شروع می‌شود
    if filename.startswith('relatedQueries'):
        file_path = os.path.join(directory_path, filename)
        # خواندن فایل
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) < 5:
                print(filename + " is empty")
                continue
        # elif  # len(lines) > 40:  # تشخیص پر بودن فایل
        date_line = lines[1].strip()  # استخراج تاریخ از خط دوم
        # استخراج قسمت تاریخ از داخل پرانتز و حذف بخش های اضافی
        date_string = date_line.split('(')[1].split('-')[0].strip()
        # تبدیل رشته تاریخ به شیء تاریخ با فرمت مشخص
        date_obj = datetime.strptime(date_string, '%d/%m/%y')
        # تبدیل شیء تاریخ به رشته با فرمت yyyy-mm-dd
        scrape_date = date_obj.strftime('%Y-%m-%d')

        results = []  # لیست برای ذخیره نتایج
        # متغیر برای پیگیری اینکه در بخش TOP یا RISING هستیم
        current_section = None
        # پردازش هر خط
        for line in lines:
            line = line.strip()  # حذف فضاهای اضافی
            if line == "":
                continue
            # شناسایی بخش‌های TOP و RISING
            if line == "TOP":
                current_section = "TOP"
                continue
            elif line == "RISING":
                current_section = "RISING"
                continue
            # ذخیره نتایج بر اساس بخش فعلی
            if current_section == "TOP":
                results.append(f"{line},{scrape_date}, TOP")
            elif current_section == "RISING":
                results.append(f"{line},{scrape_date}, RISING")

            # نوشتن نتایج در یک فایل جدید یا چاپ آنها
            output_filename = scrape_date + '.csv'
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                for result in results:
                    output_file.write(result + '\n')
        print(filename + " to " + scrape_date + ".csv successfully save ")
# ##############################################################
