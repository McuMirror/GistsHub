FROM python:2.7.13
ADD snippet.py snippet.py
RUN ["pip", "install", "pytest"]
RUN ["pip", "install", "elasticsearch"]
CMD ["python", "snippet.py"]