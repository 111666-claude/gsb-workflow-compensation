"""按步骤执行并在失败时补偿。"""


class Counter:
    """记录本轮检查过的步骤条数。"""

    def __init__(self):
        self.scanned = 0


def run(steps, fail_at, tx_id, ledger, counter):
    if tx_id in ledger:
        return {"tx": tx_id, "done": [], "compensated": [],
                "scanned": counter.scanned}
    done = []
    for step in steps:
        counter.scanned += 1
        if step["id"] == fail_at:
            break
        done.append(step["id"])
    compensated = list(reversed(done))
    ledger.append(tx_id)
    return {"tx": tx_id, "done": done, "compensated": compensated,
            "scanned": counter.scanned}
