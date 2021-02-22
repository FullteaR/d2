FROM python:3.8.1

RUN apt update && apt install -y\
 sudo\
 wget\
 git\
 curl\
 graphviz\
 build-essential\
 aptitude\
 swig

RUN aptitude install mecab libmecab-dev mecab-ipadic-utf8 make xz-utils file -y

RUN pip install --upgrade\
 pip\
 setuptools\
 jupyter\
 pandas\
 mysqlclient\
 gensim\
 seaborn\
 matplotlib\
 tqdm\
 sklearn\
 timeout_decorator\
 sqlalchemy\
 tweepy\
 mecab-python3

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN echo yes | mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a

ADD credential.json /

RUN mkdir /root/.jupyter && touch /root/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.ip = '0.0.0.0'" >> /root/.jupyter/jupyter_notebook_config.py
RUN echo c.NotebookApp.open_browser = False >> /root/.jupyter/jupyter_notebook_config.py

WORKDIR /
CMD jupyter notebook --allow-root  --NotebookApp.token=''
