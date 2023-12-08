From python:3.9.18



RUN mkdir -p /opt/webscraper
WORKDIR /opt/webscraper
COPY requirements.txt /opt/webscraper/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY webscraper.py /opt/webscraper/webscraper.py

CMD python webscraper.py https://realpython.github.io/fake-jobs/
