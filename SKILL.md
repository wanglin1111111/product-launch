---
name: product-launch
version: 2.0.0
description: |
  Product Launch 产品发布技能集合（Product Hunt 发布指南、Playbook 等）。当产品准备在 Product Hunt/科技社区首发、制定发布日 SOP 与发布后转化策略时使用。不适用于：应用商店 ASO、广告投放、GTM 整体战略（用 ai-native-gtm）。
---

# SKILL.md - product-launch

## 任务边界

**做什么**：PH 发布时间线（4 周准备/上线日 SOP/发布后转化）、社区发布节奏（Reddit/HN/X）、素材与团队动员。
**不做什么**：ASO、付费投放、产品定价。
**红线**：禁止刷票/小号/群发索票——PH 反作弊系统会降权封禁；社区发布遵守各平台自我推销规则。

## Gotchas 速查（详见 references/gotchas.md）

1. PH 明令禁止直接求 upvote（'support us'可以，'upvote us'违规），小号互票会被反作弊系统识别并取消资格
2. 发布须在上线日前约 24-48 小时提交预发布页（Preview）过审，不是上线当天才提交
3. Reddit 各 sub 版规对自我推销严格（常见 9:1 内容比例），直接发广告链接会被秒删+封号
4. Hacker Hacker News 文化反营销：Show HN 须真实参与讨论，水军顶帖会被 detect 并沉帖
5. PH 时间线按太平洋时间 00:01 开始，评论回复高峰在前 4 小时——时区算错等于弃掉半天流量

> Merged from 7 skills

## Skill: product-hunt-launch-guide

---
name: product-launch
description: |
  The complete first-timer's guide to launching on Product Hunt. Covers timing, hunter selection, asset prep, launch-day engagement, and post-launch follow-up.
---

# Product Hunt Launch Guide — First-Timer's Step-by-Step SOP

> 🌍 **Language / 语言**: [中文](#中文版) | [English](references/en/README.md) | [日本語](references/ja/README.md) | [한국어](references/ko/README.md)

Everything you need to know for your first Product Hunt launch, distilled into an actionable checklist.

- **Timeline**: 4-week prep schedule with daily tasks
- **Hunter strategy**: How to find and pitch top hunters
- **Asset checklist**: Thumbnails, taglines, first comment, demo video
- **Launch-day SOP**: Hour-by-hour engagement plan for top 5 ranking
- **Post-launch**: Converting PH traffic into retained users

## Related Gingiris Skills
- Full version: https://clawhub.ai/skill/gingiris-launch
- All skills: https://clawhub.ai/user/gingiris
- Follow: [@WeiYipei on X](https://x.com/WeiYipei)

---

## Skill: product-hunt-playbook

---
name: product-hunt-playbook
description: |
  Product Hunt Launch Playbook — Win #1 Daily. Hour-by-hour operations manual from someone who's coached 30+ #1 finishes. Covers ranking algorithm deep-dive, launch day minute-by-minute checklists, and post-launch conversion.
---

## 📦 Install

```bash
clawhub install product-hunt-playbook
```

**What you get after installing:**
- Ranking algorithm deep-dive (it's not just upvotes — weighted factors decoded)
- Launch day minute-by-minute checklist
- Post-launch conversion playbook turning PH traffic into retained users

---

## 许可证

MIT License


---

## 输出规范（validate.py 断言）

本技能产出的分析/方案文档，必须同时满足：
- **应含**：本文件输出规范所列合规要素
- **不应含**：红线违规模式（详见 scripts/validate.py BAD_VIOLATIONS）

校验命令：`python scripts/validate.py <文档路径>`（exit 0=通过，1=违规或缺失，2=文件错误）
双样例：`tests/sample_good.md` → 0；`tests/sample_bad.md` → 1。两者必须同时验证通过才视为技能可用。
