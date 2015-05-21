juicypipe
=======================
Pythonのジェネレータの糖衣構文ライブラリ[Pipe](https://github.com/JulienPalard/Pipe)を利用してログデータの処理を行う

```python
import juicypipe
[{"name": "Alice", "sex": "F", "score": 90},
 {"name": "Bob", "sex": "M", "score": 20},
 {"name": "Chris", "sex": "M", "score": 30}]
   | juicypipe.topivot(
       keycols=["sex"],
       sumcols=["score"],
       to_count=True
     )
   | juicypipe.csvprint(delim="¥t", to_yield_colname=True)
>>> 
sex	score	count
M	50	2
F	90	1
```

メリット
---------------
  * 省メモリ
  * 共通ライブラリ化の開発効率
  * 作業をローカルに寄せることで試行サイクルを早く出来る

インストール
---------------
```
python setup.py install
```

テスト
---------------
```shell
nosetests test
```

Dockerでお試し
---------------
```shell
docker build -t juicypipe .
docker run -t -i juicypipe /bin/bash
# テスト
docker run -t juicypipe nosetests -vs /home/juicypipe
```

利用例
---------------
TODO: 他のレポジトリのリンク
