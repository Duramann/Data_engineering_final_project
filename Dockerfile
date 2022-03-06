FROM python:3.6
WORKDIR /app
ENV FLASK_APP web_app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY * /app
COPY templates /app/templates
COPY static /app/static
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]