'''
Created on Jul 5, 2013

@author: netzsooc
'''
import simplejson
from urllib.request import urlopen
from urllib.parse import urlencode

lang = "en"
term = "rum"
target = "es"
decoder = simplejson.JSONDecoder()

parameters={"action": "query",
            "prop": "langlinks",
            "format": "json",
            "titles": term,
            "redirects": "",
            "lllimit": "500"}
query = urlencode(parameters)
api = "http://{0}.wikipedia.org/w/api.php?{1}".format(lang, query)

with urlopen(api) as wiki_json:
    temp = decoder.decode(wiki_json.read())
    
if len(temp) < 1:
    print("you must enter a term")
    quit()
    
pages_ids = list(temp["query"]["pages"])

langs = temp["query"]["pages"][pages_ids[0]]['langlinks']
out = None

for lang in langs:
    if lang["lang"] == target:
        out = lang["*"]
    
if not out:
    out = "{0} not found in target language({1})".format(term, target)
    
print(out)
