import requests
import webbrowser
from urllib import request
params={"order":"desc","sort":"relevance","site":"stackoverflow"}

#/2.3/search?order=desc&sort=activity&intitle=stack overflow api&site=stackoverflow
def searching(query):
    api_address =  "https://api.stackexchange.com/2.3/"
    type = "/search?"
    #response_json = requests.get("{0}{1}order={2}&sort={3}&intitle={4}&site={5}".format(api_address,type,params["order"],params["sort"],query,params["site"]))
    try:
        response_json = requests.get("https://api.stackexchange.com/2.3/search?order=desc&sort=relevance&intitle=python dict&site=stackoverflow")
    except requests.exceptions.RequestException:
        print("Vous n'avez pas de connection internet!!!")
        print("Vous n'avez pas de connection internet")
    result = response_json.json()
    #print(result.keys())
    all_result = []
    if "items" in result.keys():
        for item in result["items"]:
           all_result.append(item)
    else:
        print(result["error_message"])
        print("Nous n'avons pas pu trouver de reponse à votre question!")
        recherche = input("Voulez-vous essayer une recherche internet? Pressez 'o' pour Oui et 'n' pour non:")
        if recherche == 'o':
            openweb(query)
            return None

    return all_result
#https://www.google.com/search?q=python+dict

def getting_answer(id_Answer):
    #https://api.stackexchange.com/2.3/answers/1960546?order=desc&sort=activity&site=stackoverflow
    api_address = "https://api.stackechange.com/2.3/"
    type = "answers/"
    #requete_url ="{0}{1}{2}?order={3}&sort={4}&site={5}".format(api_address,type,id_Answer,params["order"],"activity",params["site"])
    requete_url = "https://api.stackexchange.com/2.3/answers/1960546?order=desc&sort=activity&site=stackoverflow"
    #print(requete_url)
    response = requests.get(requete_url)
    response_json = response.json()
    return response_json

def openweb(request):
    webbrowser.open_new("https://www.google.com/search?q={0}".format(request))

def internet_available():
    try:
        request.urlopen("https://www.google.com/",1)
        return True
    except request.URLError as err: 
        return False



again = "y"
while again == "y":
    if internet_available():
        query = input("What question do you have?")
        so_far = searching(query)
        num = 0
        if so_far is not None:
            for i in so_far:
                print("{0}....{1}".format(num,i["title"]))
                num+=1
            choice = input("Choose what the number associate with your question: ")
            if int(choice) in range(len(so_far)):
                print("Votre choix est {0}...{1}".format(choice,so_far[int(choice)]["title"]))
                if so_far[int(choice)]["is_answered"]==True:
                    print("Votre question a une reponse sur stackoverflow")
                    id_reponse = so_far[int(choice)]["accepted_answer_id"]
                    print(id_reponse)
                    answer= getting_answer(id_reponse)
                    webbrowser.open_new("https://stackoverflow.com/a/{0}".format(answer["items"][0]["answer_id"]))
                else:
                    print("Votre question n'a pas enconre été repondu, vous voudriez peut-être poursuivre votre recherche sur internet!")
                    mon_choix = input("Pressez 'o'pour Oui et 'n' pour Non:....")
                    if mon_choix == 'o':
                        openweb(query)
                #you maybe want to check the internet for an answer
        else:
            print("Votre choix n'est pas une option veuillez faire un autre choix...")
        pass
    else:
        print("Vous n'avez pas de connection internet disponible")
    
    again = input("Press 'y' to ask another question, press 'n' for closing the program: Press y or n:") 