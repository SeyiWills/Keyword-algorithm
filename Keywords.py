from requests_html import HTMLSession
from rake_nltk import Rake

def extract_text():
    s = HTMLSession() # creates the html session
    url = 'https://bluevoyant.applytojob.com/apply/1p8vHHwOvO' # uses any url that you want. I used Job board url
    response = s.get(url) 
    return response.html.find('div#job-description', first=True).text # finds where the job section starts and and will print out the text

r = Rake() # calls the rake algorithm 
r.extract_keywords_from_text(extract_text()) # find the keywords, extracts it and then it prints it to the screen

for rating, keyword in r.get_ranked_phrases_with_scores(): # create a forloop to pring out the keywords along with the ratings
    if rating > 5:
        print(rating, keyword)

