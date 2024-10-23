from dotenv import load_dotenv
import os

load_dotenv()


def pega(asd):
    for item in asd:
        print(os.getenv(item))

pega(("BD_USER", "BD_PASSWORD", 'BD_PORT', 'BD_HOST'))