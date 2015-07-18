# rpi-led-lastip
IPアドレス末尾をオンボードのLチカで表示

## 解説

* https://www.youtube.com/watch?v=EHFepy2fkIc

IPアドレスが 192.168.0.156 の場合、末尾の156を取得。
156を1文字づつLEDで以下のように表現。

* 赤点灯しながら、緑1回点滅
* 赤点灯しながら、緑5回点滅
* 赤点灯しながら、緑6回点滅

## Usage

```
sudo lastip.py
```

* rootユーザのcronに登録しておけばよさ気
