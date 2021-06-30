# corpus_Python-JPN
NMT モデル構築にあたって必要なデータ置き場

* 対訳コーパス
* SentencePiece モデル
* 学習済みNMT モデル (Terrier 実験用)

---
## 対訳コーパス一覧
---
### AOJ (JPN)
* AOJ から集めたソースコードをKotonoha で変換したもの

### conala (ENG)
* SOF を参考に人手でアノテーション付与したもの
* https://conala-corpus.github.io/)

### django (ENG)
* Web アプリケーションフレームワークDjango に対して擬似コードを付与したもの
* https://ahcweb01.naist.jp/pseudogen/
### DS (JPN)
* pandas/matplotlib/sklearn のソースコードに対して、人手で対訳を付与したもの
### euler (ENG)
* Project Euler4 の問題を解くためのPython コードに対して擬似コードを付与したもの
* https://ahcweb01.naist.jp/pseudogen/

---

## ディレクトリ構成 (抜粋)
---
```
.
├── AOJ-all2.pt (Terrier 実験用の仮NMT モデル)
├── Corpus-AOJ
│   ├── all.py (対訳コーパスの作成元のPython コード)
│   ├── line-by-line (行単位の対訳コーパス)
│   │   ├── AOJ.tsv (元ファイル)
│   │   ├── AOJ_all.tsv (変数名/リテラルの両方に特殊トークンを付与)
│   │   ├── AOJ_name.tsv (変数名のみに特殊トークンを付与)
│   │   └── AOJ_orig.tsv (特殊トークンの付与なし)
│   └── predict-result (PRO134 論文執筆時の翻訳結果 (仮置き))
│       └── JPN2Py
│           ├── all.tsv
│           └── orig.tsv
├── Corpus-DS
│   └── DS.tsv
├── Corpus-conala
│   ├── conala-json (row data)
│   │   ├── conala-test.json
│   │   └── conala-train.json
│   ├── conala.tsv (row data からtsv に変換したもの)
│   ├── conala_all.tsv
│   ├── conala_orig.tsv
│   └── make_conala_tsv.py (tsv 変換時のスクリプト)
├── Corpus-django
│   ├── django_orig.tsv
│   ├── en-django-all (row data)
│   │   ├── all.anno
│   │   └── all.code
│   └── make_django_tsv.py (tsv 変換時のスクリプト)
├── Corpus-euler
│   ├── block (ブロック単位の対訳コーパス)
│   │   ├── euler_all.tsv
│   │   ├── euler_before.tsv
│   │   ├── euler_name.tsv
│   │   └── euler_orig.tsv
│   ├── euler-before.tsv (?)
│   ├── euler-block.tsv (?)
│   ├── ja-euler (row data)
│   │   ├── euler02.py
│   │   ├── euler03.py
│   │   ├── ...
│   └── line-by-line (行単位の対訳コーパス)
│       ├── euler_all.tsv
│       ├── euler_before.tsv
│       ├── euler_name.tsv
│       └── euler_orig.tsv
│   ├── make_euler_tsv.py (tsv 変換時のスクリプト)
├── p3 (Python リファレンスから学習したSP モデル)
│   ├── p3.model
│   └── p3.vocab
└── prog8k (Wikiapedia のPL に関連のある記事から学習したSP モデル)
    ├── prog8k.model
    └── prog8k.vocab
```