"""固定场景，用来复现题面里的锚点。"""

import json

from . import core


def _line(obj):
    print(json.dumps(obj, ensure_ascii=False))


def _steps(*ids):
    return [{"id": i} for i in ids]


def run(name):
    if name == "order":
        out = core.run(_steps("s1", "s2", "s3"), "s3", "t1", [], core.Counter())
        _line({"compensated": out["compensated"]})
        return 0
    if name == "inclusive":
        out = core.run(_steps("s1", "s2"), "s2", "t1", [], core.Counter())
        _line({"compensated": out["compensated"]})
        return 0
    if name == "replay":
        ledger = []
        core.run(_steps("s1", "s2"), "s2", "t1", ledger, core.Counter())
        core.run(_steps("s1", "s2"), "s2", "t1", ledger, core.Counter())
        _line({"compensated": len(ledger)})
        return 0
    if name == "work":
        steps = _steps(*["s%04d" % i for i in range(2000)])
        counter = core.Counter()
        core.run(steps, "s1999", "t1", [], counter)
        _line({"steps": 2000, "scanned": counter.scanned})
        return 0
    raise SystemExit("未知场景：" + name)
