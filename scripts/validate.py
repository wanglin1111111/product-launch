#!/usr/bin/env python3
"""product-launch 技能验证脚本。

断言"产出=合规成立"而非"动作已执行"：
- GOOD 样例：含全部合规要素，且无违规 → exit 0
- BAD 样例：命中任一违规模式 → exit 1

退出码契约：0=通过，1=存在错误，2=文件错误。
"""
import re
import sys
from pathlib import Path

EXIT_OK = 0
EXIT_FAIL = 1
EXIT_FILE_ERROR = 2


def read_sample(path: str) -> str:
    p = Path(path)
    if not p.is_file():
        print(f"文件不存在: {path}", file=sys.stderr)
        sys.exit(EXIT_FILE_ERROR)
    return p.read_text(encoding="utf-8")


GOOD_REQUIREMENTS = [
    ('(PH|Product ?Hunt).{0,20}(规则|反作弊|不.{0,4}索票|support)', '缺少 PH 规则核查（不索票）'),
    ('预发布|preview|提前.{0,6}(提交|审核)', '缺少预发布页提前提交'),
    ('时区|太平洋|PT|时间线', '缺少时区/时间线安排'),
    ('(社区|Reddit|HN).{0,10}(版规|规则|比例)', '缺少社区版规核查'),
    ('(真实|原创|水军|小号).{0,6}(互动|账号|禁止)', '缺少真实互动要求'),
]

BAD_VIOLATIONS = [
    ('(刷|买).{0,4}(票|赞|upvote|账号)', '命中违规：刷票/买票'),
    ('小号|马甲|fake account', '命中违规：小号互票'),
    ('(群发|让大家|让所有).{0,8}(upvote|投票|点赞)', '命中违规：群发索票'),
    ('(水军|批量账号).{0,4}(顶|发|评)', '命中违规：水军顶帖'),
]


def find_violations(text: str) -> list:
    hits = []
    for pattern, msg in BAD_VIOLATIONS:
        if re.search(pattern, text, re.IGNORECASE):
            hits.append(msg)
    return hits


def find_missing_good(text: str) -> list:
    missing = []
    for pattern, msg in GOOD_REQUIREMENTS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(msg)
    return missing


def main():
    if len(sys.argv) < 2:
        print("用法: validate.py <sample.md>", file=sys.stderr)
        sys.exit(EXIT_FILE_ERROR)

    sample_path = sys.argv[1]
    text = read_sample(sample_path)
    fname = Path(sample_path).name.lower()
    is_bad = "bad" in fname

    errors = []

    violations = find_violations(text)
    if is_bad:
        if not violations:
            errors.append("BAD 样例未命中任何已知违规模式（应至少命中一条）")
        else:
            errors.append(f"BAD 样例命中 {len(violations)} 条违规（预期失败）：{'; '.join(violations)}")
    else:
        if violations:
            errors.append(f"GOOD 样例命中违规（不应有）：{'; '.join(violations)}")
        missing = find_missing_good(text)
        errors.extend(missing)

    if errors:
        print(f"验证失败（{len(errors)} 项）：", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(EXIT_FAIL)

    print("验证通过")
    sys.exit(EXIT_OK)


if __name__ == "__main__":
    main()
