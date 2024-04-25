FROM python:3.9-slim

WORKDIR /app

COPY stopwords.py /app/
COPY paragraphs.txt /app/



RUN pip install nltk
RUN python -m nltk.downloader stopwords

CMD ["python","stopwords.py"]