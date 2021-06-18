import json
import os
import datetime
import random
person = {}
people = ["vinit@tribes.ai", "guilermo@tribes.ai", "christian@tribes.ai", "elly@tribes.ai",
"akash@tribes.ai"]
u_index = ["a1", "a2", "a3", "a4", "a5"]
n_list = []
def rand_func():  
        for i in range(0,6):
            n1 = random.randint(0, 180)
            n_list.append(n1)

date_obj = str(datetime.date.today())

for i in range (0, len(people)):

    while True:
        rand_func()
        if sum(n_list) <= 480:
            break
        else:
            n_list = []

    person[u_index[i]] = {
        'user_id' : people[i],
        'usages_date' : date_obj,
        'device' : {
            'os' : 'ios',
            'brand': 'apple'
    },
        'usages' : [
            {
                'app_name': 'slack',
                'minutes_used': n_list[0],
                'app_category': 'communication'
            },
            {
                'app_name': 'gmail',
                'minutes_used': n_list[1],
                'app_category': 'communication'
            },
            {
                'app_name': 'jira',
                'minutes_used': n_list[2],
                'app_category': 'task_management'
            },
            {
                'app_name': 'google_drive',
                'minutes_used': n_list[3],
                'app_category': 'file_management'
            },
            {
                'app_name': 'chrome',
                'minutes_used': n_list[4],
                'app_category': 'web_browser'
            },
            {
                'app_name': 'spotify',
                'minutes_used': n_list[5],
                'app_category': 'entertainment_music'
            }

        ]
    }

    print(n_list)
    n_list.clear()

#s= json.dumps(person)
#print(s)

with open('user_data.json', 'w') as json_file:
    json.dump(person, json_file, indent=4)