import berserk

from pprint import pprint

class Chila():

    def __init__(self, token: str) -> None:
        self.token = token
        self.session = berserk.TokenSession(self.token)
        self.client = berserk.Client(session=self.session)
        
    async def getUserCrossTable(self, usrID1: str, usrID2: str):
        """
            Gets the crosstable (score) of 2 players

            usrID1 -- ID of the first player
            usrID2 -- ID of the second player

            returns -- The score between 2 players
        """

        crossTable = self.client.users.get_crosstable(usrID1, usrID2, True)
        usrScore = "{} has won {} games and {} has won {} games"
        

        return usrScore.format(usrID1, crossTable.get('users').get(usrID1.lower()), usrID2, crossTable.get('users').get(usrID2.lower()))

    async def getUserRating(self, usrID: str, ofPerf: bool):
        """
            Gets the rating for a player in all game types

            usrID -- The username of the player
        """

        usrRating = self.client.users.get_by_id(usrID)[0].get("perfs")
        ratingList = dict()

        # lists 
        gameUFPerfs = ['atomic', 'chess960', 'crazyhouse', 'horde', 'racingkings', 'storm', 'threecheck']
        gameOFPerfs = ['blitz', 'bullet', 'classical', 'correspondence', 'puzzle', 'racingkings', 'rapid', 'ultrabullet']

        if ofPerf:
            for k, v in usrRating.items():
                try:
                    if str(k) in gameOFPerfs:
                        if v.get('games') > 0:
                            ratingList[k] = v.get("rating")
                except Exception as e:
                    continue
            return ratingList
        else:
            for k, v in usrRating.items():
                try:
                    if v.get('games') > 0:
                        ratingList += f'{k} rating: {v.get("rating")}\n'
                except Exception as e:
                    continue
            return ratingList
            
        

    async def isUser(self, usrID: str) -> bool:
        """
            Checks if the user exists on lichess.org

            usrID -- ID to be checked
        """
        usrData = self.client.users.get_by_id(usrID)
        if usrData == []:
            return False
        return True