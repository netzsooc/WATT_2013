'''
Created on Jul 8, 2013

@author: netzsooc
'''

from main.wikiObject import WikiObject

if __name__ == '__main__':
    term1 = WikiObject("perro callejero", "de")
    term2 = WikiObject("cat", "es", "en")
    term3 = WikiObject("Lehrstuhl", "en", "de")
    
    print(term1.term_in_t_lang, term1.abstract_in_t_lang(term1.t_lang))
    print()
    print()
    print()
    print(term2.term_in_t_lang, term2.abstract_in_t_lang(term2.t_lang))
    print()
    print()
    print()
    print(term3.term_in_t_lang, term3.abstract_in_t_lang(term3.t_lang))