import azure.functions as func

from api import Speaker


speaker = Speaker('confignenia.json', '365_epochs.pth')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return speaker.main(req)