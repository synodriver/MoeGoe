# GUI
See [MoeGoe_GUI](https://github.com/CjangCjengh/MoeGoe_GUI)
# Online demo
- Integrated into [Huggingface Spaces 🤗](https://huggingface.co/spaces) using [Gradio](https://github.com/gradio-app/gradio). Try it out [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/skytnt/moe-japanese-tts)
- Integrated into Azure Cloud Function by [fumiama](https://github.com/fumiama), see API [here](https://github.com/fumiama/MoeGoe).
- Integrated into Android APP using Azure Cloud Function API by [fumiama](https://github.com/fumiama) [![MoeGoe-Android](https://img.shields.io/badge/MoeGoe-Android-orange)](https://github.com/fumiama/MoeGoe-Android)

# Models
## Nene + Meguru + Yoshino + Mako + Murasame + Koharu + Nanami
Download [Config File](https://sjtueducn-my.sharepoint.com/:u:/g/personal/cjang_cjengh_sjtu_edu_cn/Ed7PXqaBdllAki0TPpeZorgBFdnxirbX_AYGUIiIcWAYNg?e=avxkWs)

Download [Model](https://sjtueducn-my.sharepoint.com/:u:/g/personal/cjang_cjengh_sjtu_edu_cn/EXTQrTj-UJpItH3BmgIUvhgBNZk88P1tT_7GPNr4yegNyw?e=93bbpR) (365 epochs)

Download [Model](https://sjtueducn-my.sharepoint.com/:u:/g/personal/cjang_cjengh_sjtu_edu_cn/EYH0aVcuLbVAgdTVRjmNNDgB8xSSBINAIHByWL1tp97hWg?e=jYshj1) (H excluded)
## Sua + Mimiru + Arin + Yeonhwa + Yuhwa + Seonbae
Download [Config File](https://sjtueducn-my.sharepoint.com/:u:/g/personal/cjang_cjengh_sjtu_edu_cn/EYXC9IqILZFJqe0kyFjb9XwBuLldZnQBEMGJxI3h_iYX3w?e=Q4GrVH)

Download [Model](https://sjtueducn-my.sharepoint.com/:u:/g/personal/cjang_cjengh_sjtu_edu_cn/ESfLsfGbqbJJkC6NmZ5R1TkBbVLvTLeLG3u8jB2UfA4jtQ?e=cpw40v) (417 epochs)
# How to use
Run MoeGoe.exe

# MoeGoe Azure Cloud Function API
See [MoeGoe](https://github.com/CjangCjengh/MoeGoe)

## Japanese

> Nene + Meguru + Yoshino + Mako + Murasame + Koharu + Nanami

- GET https://moegoe.azurewebsites.net/api/speak?text=これは一つ簡単なテストです&id=0

return ogg file in body

- GET https://moegoe.azurewebsites.net/api/clean?text=これは一つ簡単なテストです

return cleaned text in body

```
ko↑rewa hI↑to↓tsU ka↑NtaNna te↓sUtodesU.
```

- GET https://moegoe.azurewebsites.net/api/speak?cleantext=ko↑rewahI↑totsUka↑NtaNnate↓sUtodesU.&id=1

return ogg file in body

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 綾地寧々 |
| 1 | 因幡めぐる |
| 2 | 朝武芳乃 |
| 3 | 常陸茉子 |
| 4 | ムラサメ |
| 5 | 鞍馬小春 |
| 6 | 在原七海 |

## Korean

> Sua + Mimiru + Arin + Yeonhwa + Yuhwa + Seonbae

- GET https://moegoe.azurewebsites.net/api/speakkr?text=이것은%20간단한%20테스트이다&id=0

return ogg file in body

- GET https://moegoe.azurewebsites.net/api/cleankr?text=이것은%20간단한%20테스트이다

return cleaned text in body

```
ㅇㅣㄱㅓㅅㅇㅡㄴ ㄱㅏㄴㄷㅏㄴㅎㅏㄴ ㅌㅔㅅㅡㅌㅡㅇㅣㄷㅏ.
```

- GET https://moegoe.azurewebsites.net/api/speakkr?cleantext=ㅇㅣㄱㅓㅅㅇㅡㄴ%20ㄱㅏㄴㄷㅏㄴㅎㅏㄴ%20ㅌㅔㅅㅡㅌㅡㅇㅣㄷㅏ.&id=1

return ogg file in body

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 수아 |
| 1 | 미미르 |
| 2 | 아린 |
| 3 | 연화 |
| 4 | 유화 |
| 5 | 선배 |

## Optional Parameters

### speak
- **format**: ogg(default), mp3 or wav
