import azure.functions as func

from pathlib import Path

import utils
from text import _clean_text
from urllib.parse import unquote


config = str(Path(__file__).parent.parent/'config.json')
hps_ms = utils.get_hparams_from_file(config)

def main(req: func.HttpRequest) -> func.HttpResponse:
    text = req.params.get('text')
    if not text:
        return func.HttpResponse(
             "400 BAD REQUEST: null text",
             status_code=400
        )
    try:
        return func.HttpResponse(
            _clean_text(unquote(text), hps_ms.data.text_cleaners),
            status_code=200
        )
    except:
        return func.HttpResponse(
            "400 BAD REQUEST: invalid text",
            status_code=400
        )
