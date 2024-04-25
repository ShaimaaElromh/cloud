import sys
import nltk
from collections import Counter
from nltk.corpus import stopwords

nltk.download('stopwords')
stopwords=set(stopwords.words('english'))
try:
    with open('/app/paragraphs.txt','r') as file:
        words=file.read().lower().split()
    processed_file=[word for word in words if word not in stopwords]
    count=Counter(processed_file)
    for word,count in count.items():
        print(f'{word}: {count}')
except Exception as e:
    print(f'An error ocurred: {e}')
        