import requests
#/2.3/search?order=desc&sort=activity&intitle=stack overflow api&site=stackoverflow
api_address =  "https://api.stackexchange.com/2.3/"
type = "/search?"
params={"order":"desc","sort":"activity","site":"stackoverflow"}
query = input("What question do you have?")
response_json = requests.get("{0}{1}order={2}&sort={3}&intitle={4}&site={5}".format(api_address,type,params["order"],params["sort"],query,params["site"]))
data = response_json.json()

again = "y"
while again==y:
    print(data) 
