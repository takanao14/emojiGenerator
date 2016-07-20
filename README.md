# emojiGenerator
slackのemojiを自動生成する

## 実行環境
- python 3.5.1
- Pillow 3.3.0

## 使い方
    slackEmojiGenerator.py だが 断る

![test.png](test.png)

## オプション
    -h ヘルプ
    -f (--font) ttf or otfのフォントファイルを指定する(指定しない場合はNotoSanssJP-Bold.otf)
    -o (--out)  出力ファイル名を指定する(指定しない場合はtest.png)
    -c (--color) 文字色をRRGGBBで指定する(指定しない場合は000000)
