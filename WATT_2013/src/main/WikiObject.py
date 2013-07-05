'''
Created on Jul 5, 2013

@author: netzsooc
'''

class WikiObject(object):
    '''
    The class contains an object that wraps Wikipedia language links, and an
    abstract
    '''


    def __init__(self, term):
        '''
        Constructor
        '''


    def term_in_lang(self, target):
        return self._get_all_langs()[target]


    def abstract_in_lang(self, target):
        pass


    def _get_all_langs(self):
        pass


    def _get_abstracts(self):
        pass