# from indic_transliteration import sanscript
# import time
# start_time=time.time()
# def translate_to_telugu(text):
#
#     translated = sanscript.transliterate(text, sanscript.ITRANS,sanscript.TELUGU)
#     return translated
#
# name = "shruthi"
#
#
# telugu_translation = translate_to_telugu(name)
#
# print("Telugu Translation:", telugu_translation)
# end_time=time.time()
# print(end_time-start_time)
#99.xlsx
# fn="99.xlsx"
# fn=fn.split('.')
# print(fn)
# fn=fn[0]+"_result"+fn[1]
# print(fn)
import pandas as pd
# mobile=input("enter a phone number:")
# mobile=str(mobile)
# if 'e' in str(mobile):
#     mobile = "{:.0f}".format(mobile)
#     if len(mobile)==10 and mobile.startswith(('6','7','8','9')):
#         print(mobile)
#     elif len(mobile)==12 and mobile.startswith("91"):
#         print(mobile)
# elif len(mobile)==10 and mobile.startswith(('6','7','8','9')):
#     print(mobile)
# elif len(mobile)==12 and mobile.startswith("91"):
#     print(mobile[2:])
# from googletrans import Translator
# df="ravi"
# def eng_to_tel(data):
#     translator=Translator()
#     result=translator.translate(data,src="en",dest="hi")
#     return result
# df1=eng_to_tel(df)
# print(df1)
# phone_number_str = "99891524 8  0"
#
# # Remove non-numeric characters from the string
# cleaned_phone_number_str = ''.join(filter(str.isdigit, phone_number_str))
#
# # Convert the cleaned string to an integer
# phone_number_int = int(cleaned_phone_number_str)
#
# print(phone_number_int)  # Output: 1234567890

# import requests
# def translate_to_telugu(english_text):
#     api_key = 'YOUR_API_KEY'
#     url = 'https://inputtools.google.com/request'
#
#     data = {
#         "app": "translate",
#         "ie": "UTF-8",
#         "oe": "UTF-8",
#         "text": english_text,
#         "tk": "null",
#         "sl": "en",
#         "tl": "te",  # Telugu language code
#     }
#
#     response = requests.get(url, data=data)
#     translated_text = response.json()[0][1][0][0]
#     return translated_text
#
#
# english_text = "Hello, how are you?"
# telugu_translation = translate_to_telugu(english_text)
# print(telugu_translation)
# import requests
#
#
# def fetch_google_search_results(query):
#     url = "https://www.google.com/search"
#     params = {"q": query}
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
#
#     response = requests.get(url, params=params, headers=headers)
#     if response.status_code == 200:
#         return response.text
#     else:
#         print("Failed to fetch search results.")
#         return None
#
#
# search_query = "Python programming"
# google_search_results = fetch_google_search_results(search_query)
# if google_search_results:
#     print(google_search_results)  # This will print the HTML content of the Google search results page


# condition = (
#     df['Mobile_Numbers'].str.isdigit() &  # Check if the value is in digits only
#     df['Mobile_Numbers'].str.match(r'^[6-9]\d{9}$')  # Check if it starts with 6, 7, 8, or 9 and has 10 digits
# )
#
# # Keep only the rows that meet the specified conditions
# filtered_df = df[condition]
# def replace_char_not_adjacent_to_space(string, char_to_replace, new_char):
#     modified_string = ""
#     for i in range(len(string)):
#         # Check if the character is not at either end of the string
#         if i != 0 and i != len(string) - 1:
#             # Check if the character is not adjacent to a space
#             if string[i] != " " and string[i - 1] != " " and string[i + 1] != " ":
#                 # Replace the character
#                 if string[i]=="M":
#                     modified_string += new_char
#                     continue
#         modified_string += string[i]  # Keep the character as it is
#     return modified_string
#
# # Example usage
# original_string = "allaM aMjamma"
# # char_to_replace = "c"
# new_char = "n"
#
# modified_string = replace_char_not_adjacent_to_space(original_string, char_to_replace, new_char)
# print("Modified string:", modified_string)

# name="AllaM saMdya"
# name1=""
# for i in range(0,len(name)):
#     if i !=0 and i!=len(name)-1:
#         # print(name[i])
#         if name[i] != " " and name[i+1] != " " and name[i-1] != " " :
#             if name[i]=="M":
#                 name1+="n"
#                 continue
#     name1+=name[i]
# print(name1)
# num1=[1,3,5]
# num2=[2,4,6,7]
# num3 = []
# sum = 0
# for i in num1:
#     num3.append(i)
# for i in num2:
#     num3.append(i)
# num3 = sorted(num3)
# if len(num3) % 2 == 0:
#     n = len(num3) // 2
#     print((num3[n - 1] + num3[n]) / 2)
#     # print(num3)
# else:
#     n = len(num3) // 2
#     print(num3[n])
"""string="cbbd"
string1=string
l1=0
out=""


for j in range(len(string1)):
    ss1 = ""
    ss = ""
    for i in range(len(string1)):
        ss+=string1[i]
        rev=ss[::-1]
        if i!=0:
            ss1+=string1[i]

        if ss == rev:
            l2 =len(rev)

        if l2 >l1:
            l1=l2
            out=ss
    string1=ss1
    # print(string1)
    print(ss)
print(out,l1)"""
# s="PAYPALISHIRING"
# n=3
# #PAHNAPLSIIGYIR
# for i in range(n):
# Initialize an empty list to store the lists
'''x=int(input("enter a number:"))
if x>(-2**31) and x<(2**31-1):
    if x<0:
        x=x*(-1)
        rev=0
        while x!=0:
            rev=rev*10+x%10
            x=x//10
        print(rev*(-1))
    else:
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
        print(rev)
else:
    print("your number was not in our limits.enter a number in range of [-231, 231 - 1]")'''
'''n=input("enter a value:")
n1=0
n=n.strip()
if not n:
    print(0)
l=n.split(" ")
for i in l:
    if  i.isdigit():
        n1=n1+int(i)

    elif i[0]=="-" and i[1:].isdigit():
        n1 = n1 + int(i)

if n1>(-2**31) and n1<(2**31-1):
    print(n1)
else:
    print("your number was not in our limits.enter a number in range of [-231, 231 - 1]")'''


class Solution:
    def isPalindrome(x):
        if x > (-2 ** 31) and x < (2 ** 31 - 1):
            return str(x)==str(x)[::-1]
s=Solution
a=s.isPalindrome(10)
print(a)















