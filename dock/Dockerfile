From atlasml/ml-base:debian

WORKDIR /dock
ADD . /dock

RUN pip install --user lz4
RUN pip install -r requirements.txt

CMD python3