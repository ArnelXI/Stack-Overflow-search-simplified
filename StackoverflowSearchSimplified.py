import requests
import webbrowser
#/2.3/search?order=desc&sort=activity&intitle=stack overflow api&site=stackoverflow
def searching():
    api_address =  "https://api.stackexchange.com/2.3/"
    type = "/search?"
    params={"order":"desc","sort":"relevance","site":"stackoverflow"}
    query = input("What question do you have?")
    #response_json = requests.get("{0}{1}order={2}&sort={3}&intitle={4}&site={5}".format(api_address,type,params["order"],params["sort"],query,params["site"]))
    response_json = requests.get("https://api.stackexchange.com/2.3/search?order=desc&sort=relevance&intitle=python dict&site=stackoverflow")
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
            webbrowser.open_new("https://www.google.com/search?q={0}".format(query))
            return None

    return all_result
#https://www.google.com/search?q=python+dict

def getting_answer(data,choice):
    #https://api.stackexchange.com/2.3/answers/%7Bids%7D?order=desc&sort=activity&site=stackoverflow
    api_address = "https://api.stackechange.com/2.3/"
    type = "/answer/"
    params = {"order":"desc","sort":"desc","site":"stackoverflow"}
    query = input("Do you want to see another answer....")#id_Answer = data["answerd-id"]
    response_json = requests.get("{0}{1}".format(api_address,))





again = "y"
while again=="y":
    so_far = searching()
    num = 0
    if so_far is not None:
        for i in so_far:
            print("{0}....{1}".format(num,i["title"]))
            num+=1
        choice = input("Choose what the number associate with your question")
        if int(choice) in range(len(so_far)):
            print("Votre choix est {0}...{1}".format(choice,so_far[int(choice)]["title"]))
            if so_far[int(choice)]["is_answered"]==True:
                pass
            else:
                #you maybe want to check the internet for an answer
                pass
        else:
            print("Votre choix n'est pas une options veuillez faire un autre choix...")
    again = input("Press 'y' to ask another question, press 'n' for closing the program: Press y or n:") 
