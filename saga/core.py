"""按步骤执行并在失败时补偿。"""


class Counter:
    """记录本轮检查过的步骤条数。"""

    def __init__(self):
        self.scanned = 0


def run(steps, fail_at, tx_id, ledger, counter):
    done = []
    for step in steps:
        for _ in steps:
            counter.scanned += 1
        if step["id"] == fail_at:
            break
        done.append(step["id"])
    compensated = []
    for step in steps:
        for _ in steps:
            counter.scanned += 1
        if step["id"] in done or step["id"] == fail_at:
            compensated.append(step["id"])
    ledger.append(tx_id)
    return {"tx": tx_id, "done": done, "compensated": compensated,
            "scanned": counter.scanned}
