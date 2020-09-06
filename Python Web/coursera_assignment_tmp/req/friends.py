import requests

def calc_age(uid):
    ACCESS_TOKEN = 'Your access token here'
    r = requests.get(f'https://api.vk.com/method/users.get?v=5.71&access_token={ACCESS_TOKEN}&user_ids={uid}')

    user_id = r.json().get('response')[0].get('id')

    r = requests.get(f'https://api.vk.com/method/friends.get?v=5.71&access_token={ACCESS_TOKEN}&user_id={user_id}&fields=bdate')

    dates = []
    for pers in r.json().get('response').get('items'):
        dates.append(pers.get('bdate'))

    good_dates = []
    dict = {}
    for date in dates:
        if (date != None):
            if (len(date.split('.')) == 3) :
                year = int(date.split('.')[2])
                nice_year = 2020 - year
                if (nice_year in dict):
                    dict[nice_year] += 1
                else:
                    dict[nice_year] = 1

    dict = {k : v for k, v in sorted(dict.items(), key=lambda item: item[0])}
    dict = {k : v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse = True)}
    ans = []
    for k, v in dict.items():
        ans.append((k, v))

    return ans



if __name__ == '__main__':
    res = calc_age('Your id name of person at vk.com')
    print(res)
