'''
 The URLHIERARCHY is a dictionary for the importance of each site in the
 dictionary. Sites that comes earlier have higher importance. Sites with higher
 importance are the ones the script looks through first before proceeding to
 the next site.
'''

import config as cf

urls = ['mangareader']

url_search_list = {
'mangareader': 'https://www.mangareader.net/search/?nsearch=&msearch=',

}

url_domains = {
'mangareader': 'https://www.mangareader.net'
}
