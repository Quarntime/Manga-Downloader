# Frame Height
FHEIGHT = 605
FWIDTH = 935

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
url_index = 0
button = []
domain_path = []
chapters = []
c_buttons = []
manga_domain = ''
genre_label = []
thumbnail = []
type_label = []
loading = ''

choice = 0
