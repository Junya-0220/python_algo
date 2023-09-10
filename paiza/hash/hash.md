# ハッシュ関数

ハッシュ関数は、データに対して特定の計算を行い、特定の範囲に収まる値(固定長の出力)を得る関数のことを指します。
この時、入力のことを`キー`と呼び、出力のことを`値・ハッシュ値、ダイジェスト`などと呼びます。

ハッシュ関数は、以下の性質を持っている事が期待されます。

- 同じ入力に対して、常に同じ出力を返す
- 出力から入力を推測する事が難しい
- 出力が一様に分布している(出力値に偏りがない)

ハッシュ関数は、例えば以下の用途で使われています。

・ハッシュテーブル
連想配列の内部で用いられているデータ構造で、最もシンプルな