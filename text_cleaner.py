#Preprocesses review text

import re
import nltk
from nltk.corpus import stopwords

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = list(stopwords.words('english'))
html = re.compile('<.*?>')
def clean(text):
  text = text.lower()
  text = re.sub(REPLACE_BY_SPACE_RE, ' ', text)
  text = re.sub(html, '', text)
  text = re.sub(BAD_SYMBOLS_RE, "", text)
  text = ' '.join(word for word in re.split(' ', text) if (word not in STOPWORDS))
  text = re.sub(' +', ' ', text)
  return text 