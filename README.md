# MoeGoe Azure Cloud Function API
See [MoeGoe](https://github.com/CjangCjengh/MoeGoe)

## Japanese

> Nene + Meguru + Yoshino + Mako + Murasame + Koharu + Nanami

- GET https://moegoe.azurewebsites.net/api/speak?text=これは一つ簡単なテストです&id=0

return wav file in body

- GET https://moegoe.azurewebsites.net/api/clean?text=これは一つ簡単なテストです

return cleaned text in body

```
ko↑rewa hI↑to↓tsU ka↑NtaNna te↓sUtodesU.
```

- GET https://moegoe.azurewebsites.net/api/speak?cleantext=ko↑rewahI↑totsUka↑NtaNnate↓sUtodesU.&id=1

return wav file in body

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

return wav file in body

- GET https://moegoe.azurewebsites.net/api/cleankr?text=이것은%20간단한%20테스트이다

return cleaned text in body

```
ㅇㅣㄱㅓㅅㅇㅡㄴ ㄱㅏㄴㄷㅏㄴㅎㅏㄴ ㅌㅔㅅㅡㅌㅡㅇㅣㄷㅏ.
```

- GET https://moegoe.azurewebsites.net/api/speak?cleantext=ㅇㅣㄱㅓㅅㅇㅡㄴ%20ㄱㅏㄴㄷㅏㄴㅎㅏㄴ%20ㅌㅔㅅㅡㅌㅡㅇㅣㄷㅏ.&id=1

return wav file in body

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 수아 |
| 1 | 미미르 |
| 2 | 아린 |
| 3 | 연화 |
| 4 | 유화 |
| 5 | 선배 |
