import berserk
import math

from pprint import pprint

session = berserk.TokenSession("lip_YoSUJI8ZXAB3kc4GkUwU")
client = berserk.Client(session=session)
perfEnum = berserk.enums.PerfType

try:
    userName = 'kelpiii'
    userRating = client.users.get_by_id(userName)[0].get("perfs")
    gameUFPerfs = ['atomic', 'chess960', 'crazyhouse', 'horde', 'racingkings', 'storm', 'threecheck']
    gameOFPerfs = ['blitz', 'bullet', 'classical', 'correspondence', 'puzzle', 'racingkings', 'rapid', 'ultrabullet']
    # pprint(userRating)

    ratingList = str()

    for k, v in userRating.items():
        try:
            if str(k) in gameOFPerfs:
                if v.get('games') > 0:
                    ratingList += f'{k} rating: {v.get("rating")}\n'
        except Exception as e:
            continue
        # print(k, " - ", v.get('games'))
    
    print(ratingList)
    # pprint(type(userRating))
except Exception as e:
    
    print(f'You got an error!\n {e}')

def getUser(lilaName):

    try:
        userPerf = client.users.get_user_performance(lilaName, perfEnum.BULLET)
        userRating = math.floor(userPerf.get('perf').get('glicko').get('rating'))

        for x in userRating:
            print(x)

    except Exception as e:
        print(f'You got an error!\n {e}')
    
    # return f'User {lilaName} has a rating of {userRating} in bullet'

# print(getUser('nsedler'))



