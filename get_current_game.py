import cassiopeia as cass
from cassiopeia import Summoner

def getAPI_key():
    #Create a txt file w/ the API key in the same folder as the script
    f = open("./api_key.txt", "r")
    return f.read()

def get_result(summoner):
    
    cass.set_riot_api_key(getAPI_key())
    last_match = summoner.match_history[0]
    champion_id_to_name_mapping = {
        champion.id: champion.name for champion in cass.get_champions(region='NA')
    }
    champ_played_id = last_match.participants[summoner].champion.id
    champ_played_name = champion_id_to_name_mapping[champ_played_id]
    win = last_match.participants[summoner].stats.win

    return win, champ_played_name

def throw_flame(summoner_name):

    summoner = Summoner(name=summoner_name, region="NA")
    win, champ = get_result(summoner)

    if win:
        pass
    else:
        print("\n" + f"{summoner_name}" + ', you fuckin scrub, you lost your last game as ' + f"{champ}" + '.')

if __name__ == "__main__":
    throw_flame("YodelYaddle")
