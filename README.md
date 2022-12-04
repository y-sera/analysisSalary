# analysisSalary
## 概要
 毎月の給与明細の情報を分析・可視化するためのプログラム.
 事前(自力で)作成したにyamlファイルを読み込ませ, 毎月の給与額や控除, 残業時間等をグラフによって可視化する(予定).

## 入力テンプレート
```
period:
  year:
  month:
kind:
payment:
  items:
  - name:
    amount:
  total:
deduction:
  items:
  - name:
    amount:
  total:
netpayment:
overtime:
```

### period
 月を入力
- `period.yaer`: 年
- `period.month`: 月
 #### sample
```
period:
  year: 2022
  month: 4
```   

### kind
 種別を入力. 
-  `monthly`: 月給
-  `bonus`: 賞与(ボーナス)

#### sample
```
kind: monthly
```

### payment
支給項目, 支給合計額を入力.
- `payment.items`: 支給項目を入力. 
  - `payment.items.name`: 項目名. 
  - `payment.items.amount`: 項目の金額.
- `payment.total`: 支給合計額.

#### sample
```
payment:
  items:
  - name: "職能給"
    amount: 200000
  - name: "非課税交通費"
    amount: 10000
  - name: "超過勤務手当"
    amount: 33000
 total: 243000
```

### deduction
控除項目, 控除合計額を入力
- `deduction.items`: 控除項目を入力.
  - `deduction.items.name`: 項目名.
  - `deduction.items.amount`: 項目の金額. 
- `deduction.total`: 控除合計額.

#### sample
```
deduction:
  items:
  - name: "健康保険"
    amount: 12000
  - name: "厚生年金"
    amount: 1300
  - name: "雇用保険"
    amount: 1400
  - name: "所得税"
    amount: 5000
  - name: "住民税"
    amount: 14000
  total: 33700
```

### netpayment
純支給額. 
#### sample
```
netpayment: 209300
```

### (optional) overtime
月の超過勤務時間(h). `kind: monthly`の場合のみ必要.

#### sample
```
overtime: 33
```
