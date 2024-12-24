FROM python:latest

ENV VIRTUAL_ENV=/backend/.env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /backend

COPY pyproject.toml poetry.lock /backend/

RUN python -m venv "$VIRTUAL_ENV" \
    source "$VIRTUAL_ENV/activate" && \
    pip install --upgrade pip &&\
    pip install poetry &&\
    poetry install --without dev

COPY . /backend/

EXPOSE 8000

WORKDIR /backend/src/anime

CMD [ "fastapi", "run", "run.py" ]