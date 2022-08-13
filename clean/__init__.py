import azure.functions as func

from pathlib import Path

from utils import get_hparams_from_file
from text import _clean_text
from urllib.parse import unquote


cleanernames = get_hparams_from_file(str(Path(__file__).parent.parent/'config.json')).data.text_cleaners


def main(req: func.HttpRequest) -> func.HttpResponse:
    text = req.params.get('text')
    if not text:
        return func.HttpResponse(
             "400 BAD REQUEST: null text",
             status_code=400
        )
    try:
        return func.HttpResponse(
            _clean_text(unquote(text), cleanernames),
            status_code=200
        )
    except:
        return func.HttpResponse(
            "400 BAD REQUEST: invalid text",
            status_code=400
        )
