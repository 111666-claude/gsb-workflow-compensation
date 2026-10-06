# workflow-compensation

按步骤执行，失败时逆序补偿。只用 Python 标准库。

```
python3 -m unittest discover -s tests
python3 -m saga --sample=order
python3 -m saga --sample=inclusive
python3 -m saga --sample=replay
python3 -m saga --sample=work
```

## 口径

- **执行**：按顺序执行到失败那一步为止，失败步本身不算完成。
- **补偿**：只补偿已经成功的步骤，且**逆序**补偿。
- **幂等**：同一个 `tx_id` 只结算一次，重复请求不再补偿。
- **台账**：每次生效的结算在台账里留一条记录。

## 不变量

- 补偿列表只含成功过的步骤，且顺序与执行顺序相反。
- 失败步不出现在完成列表也不需要补偿。
- `scanned` 不随步骤数平方级放大：两千步的 `scanned` 不超过 6000。

## 输出契约

每个场景打印一行 JSON；`--sample=work` 只打印 `{"steps": N, "scanned": N}`。
