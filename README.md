# DBLP Spider

A spider tool for downloading the DBLP search results into local BibTeX files.

## Install

```bash
pip3 install -i https://pypi.org/simple/ dblp-spider
```

## Usage

```bash
# Get result from all of the ccf recommandation venues
dblp-spider --keywords "DNS Security" --output result
# Get result from all of the ccf class A recommandation venues
dblp-spider --keywords "DNS Security" --output result --ccf-a
# Get result from all of the ccf class A/B recommandation venues 
dblp-spider --keywords "DNS Security" --output result --ccf-a --ccf-b
# Get result of multiple research keywords
dblp-spider --keywords "DNS Security" "BGP Security" --output result
```

## Output

```bash
├── TCP Security
│   ├── ACSAC
│   │   ├── conf-acsac-Bellovin04.bib
│   │   ├── conf-acsac-HsuC04.bib
│   │   └── conf-acsac-RitcheyON02.bib
│   ├── INFOCOM
│   │   └── conf-infocom-GuhaM96.bib
│   ├── USENIX
│   │   ├── conf-uss-CaoQWDKM16.bib
│   │   ├── conf-uss-ChenQ18.bib
│   │   ├── conf-uss-DharmapurikarP05.bib
│   │   ├── conf-uss-Joncheray95.bib
│   │   ├── conf-uss-ReardonG09.bib
│   │   └── conf-uss-SmartMJ00.bib
│   └── summary.bib
```

## Zotero

1. File->Import
2. Select `summary.bib`

## Acknowledgement

* [DBLP](https://dblp.uni-trier.de/)
* [默小西](https://github.com/mo-xiaoxi)

## References

* [如何建立独属于你自己的论文数据库 - 默小西](https://moxiaoxi.info/papers/2020/10/18/Papers/)
* [How to use the dblp search? - DBLP](https://dblp.org/faq/How+to+use+the+dblp+search)