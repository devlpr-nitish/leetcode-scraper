
from db import store_data
from scraper import get_profile_info
from generate_csv import get_csv



username = input("Enter your leetcode username: ")

profile = get_profile_info(username)

print("Enter 1 for profile details \nEnter 2 for profile details in csv file \nEnter 3 to save profile info to database")

option = input("your choice : ")

match int(option):
    case 1:
        print(f"your username is {profile["username"]}")
        print(f"your current ranking is {profile["ranking"]}")
        print(f"you have solve {profile["easy"]} easy problems")
        print(f"you have solve {profile["medium"]} medium problems")
        print(f"you have solve {profile["hard"]} hard problems")

        print(f"Total problems your have solved is ${profile["total"]}")

               
    case 2:
        get_csv(profile)
        print("CSV file is generated successfully, check your file name called ""leetcode_profile.csv""")
    case 3:
        store_data(profile)
        print("Your data is successfully saved in database")
    case _:
        print("Please enter the valid option")
    




