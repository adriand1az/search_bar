import re

names_file = open("random.txt", encoding="UTF-8")
data = names_file.read()
names_file.close()


class Search:

    def __init__(self):
        pass

    def search_letter(self):  # Searches document for a str
        user_search = input("search: ")
        searching_letter = re.findall(user_search, data, re.I)
        if user_search in searching_letter:
            for i, name in enumerate(searching_letter):
                print(i, searching_letter[0])
        else:
            print("Not in text file")

    def search_email(self):  # Searches for all emails
        searching_email = re.findall(r'[\wd.-]+@[\wd.]+', data, re.I)
        if searching_email:
            print(sorted(searching_email))

    def search_nums(self):  # searches for all numbers
        searching_nums = re.findall(r'\d', data)
        print(searching_nums)


phrase = Search()

