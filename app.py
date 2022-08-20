from io import BytesIO
from typing import Optional
from urllib.parse import unquote

from fastapi import FastAPI, File, Form, Query
from fastapi.responses import StreamingResponse, UJSONResponse
from scipy.io.wavfile import write
from torch import LongTensor, no_grad

from api import Cleaner, Speaker
from text import _clean_text, text_to_sequence
from utils import get_hparams_from_file, load_checkpoint, wav2

speaker = Speaker("configsuae.json", "417_epochs.pth")

app = FastAPI(title="MoeGoe")


@app.post("/speak")
def handle_speak(
    text: Optional[bytes] = Form(None, description=""),
    cleantext: Optional[bytes] = Form(None, description=""),
    id: int = Form(0, description=""),
    format: str = Form("wav", description=""),
):
    if not text and not cleantext:
        return UJSONResponse({"msg": "null text"}, 400)
    if text and cleantext:
        return UJSONResponse({"msg": "text and cleantext cannot be set both"}, 400)
    cleaned: bool = False
    if cleantext:
        cleaned = True
        text = cleantext
    if id not in range(speaker.hps_ms.data.n_speakers):
        return UJSONResponse({"msg": "speaker id out of range"}, 400)
    if format not in ("ogg", "mp3", "wav"):
        return UJSONResponse({"msg": "invalid format"}, 400)
    try:
        stn_tst = speaker.get_text(unquote(text), cleaned)
    except:
        return UJSONResponse({"msg": "invalid text"}, 400)
    try:
        with no_grad():
            x_tst = stn_tst.unsqueeze(0)
            x_tst_lengths = LongTensor([stn_tst.size(0)])
            sid = LongTensor([id])
            audio = (
                speaker.net_g_ms.infer(
                    x_tst,
                    x_tst_lengths,
                    sid=sid,
                    noise_scale=0.667,
                    noise_scale_w=0.8,
                    length_scale=1,
                )[0][0, 0]
                .data.cpu()
                .float()
                .numpy()
            )
            f = BytesIO()
            write(f, speaker.hps_ms.data.sampling_rate, audio)
            f.seek(0, 0)
            if format == "wav":
                return StreamingResponse(f, 200, media_type="audio/wav")
            else:
                ofp = BytesIO()
                wav2(f, ofp, format)
                ofp.seek(0, 0)
                return StreamingResponse(
                    ofp,
                    200,
                    media_type="audio/mpeg" if format == "mp3" else "audio/ogg",
                )
    except Exception as e:
        return UJSONResponse({"msg": f"Internal Server Error {e}"}, 500)


@app.post("/clean")
async def handle_clean(text: str = Form(...), config: str = Form(...)):
    cleaner = Cleaner(config)  # 'configsuae.json'
    try:
        t = _clean_text(unquote(text), cleaner.cleanernames)
        return UJSONResponse({"msg": t}, 200)
    except:
        return UJSONResponse({"msg": "invalid text"}, 400)
