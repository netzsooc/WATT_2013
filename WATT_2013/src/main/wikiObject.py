'''
Created on Jul 5, 2013

@author: netzsooc
'''


import simplejson
from urllib.parse import urlencode
from urllib.request import urlopen


class WikiObject(object):
    '''
    The class contains an object that wraps Wikipedia language links, and an
    abstract
    '''


    api = "http://{0}.wikipedia.org/w/api.php?{1}"
    decoder = simplejson.JSONDecoder()


    def __init__(self, term, t_lang, source_lang="es"):
        '''
        Constructor
        '''
        self.term = term
        self.source_lang = source_lang
        self._all_langs = self._get_all_langs()

        self.t_lang = t_lang
        self.term_in_t_lang = self.get_in_t_lang(self.t_lang)


    def get_in_t_lang(self, target):
        langs = self._all_langs
        return langs[target]
    
    
    def _get_all_langs(self, lllimit="500"):
        '''Uses GET method to get json containing language links 
        from Wikipedia. Returns a dictionary containing lang:term pairs.'''
        
        parameters={"action": "query",
            "prop": "langlinks",
            "format": "json",
            "titles": self.term,
            "redirects": "",
            "lllimit": lllimit}
        
        api = WikiObject.api.format(self.source_lang, urlencode(parameters))
        with urlopen(api) as wiki_json:
            temp = WikiObject.decoder.decode(wiki_json.read())

        try:
            l_links = list(temp["query"]["pages"].values())[0]["langlinks"]
            return {l_link['lang']: l_link['*'] for l_link in l_links}
        except KeyError:
            return dict()


    def abstract_in_t_lang(self, t_lang):
        try:
            title = self.get_in_t_lang(t_lang)
        except KeyError:
            return ''
            
        parameters={"action": "query",
            "prop": "extracts",
            "format": "json",
            "titles": title,
            "exsectionformat":"plain",
            "redirects": "",
            "exintro":"",
            "explaintext":""}
        
        api = WikiObject.api.format(self.t_lang, urlencode(parameters))
        with urlopen(api) as wiki_json:
            temp = WikiObject.decoder.decode(wiki_json.read())

        try:
            return list(temp["query"]["pages"].values())[0]["extract"]
        except KeyError:
            return ''


    def _get_abstracts(self):
        pass
    



