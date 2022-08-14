# MoeGoe Azure Cloud Function API
See [MoeGoe](https://github.com/CjangCjengh/MoeGoe)

> GET https://moegoe.azurewebsites.net/api/speak?text=これは一つ簡単なテストです&id=0
> return wav file in body

> GET https://moegoe.azurewebsites.net/api/clean?text=これは一つ簡単なテストです
> return cleaned text in body

```
ko↑rewa hI↑to↓tsU ka↑NtaNna te↓sUtodesU.
```

> GET https://moegoe.azurewebsites.net/api/speak?cleantext=ko↑rewahIto↓tsU ka↑NtaNnate↓sUtode↓sU.&id=1
> return wav file in body

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 綾地寧々 |
| 1 | 因幡めぐる |
| 2 | 朝武芳乃 |
| 3 | 常陸茉子 |
| 4 | ムラサメ |
| 5 | 鞍馬小春 |
| 6 | 在原七海 |
