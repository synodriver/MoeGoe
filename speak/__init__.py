import azure.functions as func

from io import BytesIO
from pathlib import Path
from torch import no_grad, LongTensor

import commons
from utils import load_checkpoint, get_hparams_from_file
from models import SynthesizerTrn
from text import text_to_sequence
from urllib.parse import unquote

from scipy.io.wavfile import write


hps_ms = get_hparams_from_file(str(Path(__file__).parent.parent/'config.json'))
net_g_ms = SynthesizerTrn(
    len(hps_ms.symbols),
    hps_ms.data.filter_length // 2 + 1,
    hps_ms.train.segment_size // hps_ms.data.hop_length,
    n_speakers=hps_ms.data.n_speakers,
    **hps_ms.model)
_ = net_g_ms.eval()
load_checkpoint(str(Path(__file__).parent.parent/'243_epochs.pth'), net_g_ms)


def get_text(text, hps, cleaned=False):
    if cleaned:
        text_norm = text_to_sequence(text, hps.symbols, [])
    else:
        text_norm = text_to_sequence(text, hps.symbols, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = LongTensor(text_norm)
    return text_norm


def main(req: func.HttpRequest) -> func.HttpResponse:
    text = req.params.get('text')
    cleantext = req.params.get('cleantext')
    if not text and not cleantext:
        return func.HttpResponse(
             "400 BAD REQUEST: null text",
             status_code=400
        )
    if text and cleantext:
        return func.HttpResponse(
             "400 BAD REQUEST: text and cleantext cannot be set both",
             status_code=400
        )
    cleaned = False
    if cleantext:
        cleaned = True
        text = cleantext
    speaker_id = req.params.get('id')
    if not speaker_id:
        return func.HttpResponse(
             "400 BAD REQUEST: null speaker id",
             status_code=400
        )
    try:
        speaker_id = int(speaker_id)
    except:
        return func.HttpResponse(
             "400 BAD REQUEST: invalid speaker id",
             status_code=400
        )
    try:
        stn_tst = get_text(unquote(text), hps_ms, cleaned)
    except:
        return func.HttpResponse(
            "400 BAD REQUEST: invalid text",
            status_code=400
        )
    try:
        with no_grad():
            x_tst = stn_tst.unsqueeze(0)
            x_tst_lengths = LongTensor([stn_tst.size(0)])
            sid = LongTensor([speaker_id])
            audio = net_g_ms.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][0,0].data.cpu().float().numpy()
        with BytesIO() as f:
            write(f, hps_ms.data.sampling_rate, audio)
            return func.HttpResponse(
                f.getvalue(),
                status_code=200,
                mimetype="audio/wav",
            )
    except Exception as e:
        return func.HttpResponse(
            "500 Internal Server Error\n"+e,
            status_code=500
        )
