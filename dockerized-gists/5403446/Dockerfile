FROM python:2.7.13
ADD snippet.py snippet.py
RUN ["pip", "install", "AppKit"]
RUN ["pip", "install", "IPython"]
CMD ["python", "snippet.py"]