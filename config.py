# Frame Height
FHEIGHT = 390
FWIDTH = 530

# Background Color
BGCOLOR = 'grey'

# URLHIERARCHY

'''
 The URLHIERARCHY is a dictionary for the importance of each site in the
 dictionary. Sites that comes earlier have higher importance. Sites with higher
 importance are the ones the script looks through first before proceeding to
 the next site.
'''


urls = ['mangareader']

url_search_list = {
'mangareader': 'https://www.mangareader.net/search/?nsearch=&msearch=',

}

url_domains = {
'mangareader': 'https://www.mangareader.net'
}

# global vars; do not change
IMGLIST = {}
url_index = 0
button = []

choice = 0
Runtime = True
domain_path = []
