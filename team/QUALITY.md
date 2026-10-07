# 编辑质量合同与发布门禁

本合同服务于可用的开源搜索项目。多发、排版漂亮、写满字数、GitHub commit 成功都不是完成任务。选题与发布之间至少有独立审稿角色；作者不能将自己的声明填成验证证据。

## 编辑职责与可否决权

| 角色 | 必须提供 | 可以独立阻止的原因 |
| --- | --- | --- |
| 选题编辑 | intent、受众、市场/语言、带日期的需求证据、已有页面去重 | 无可核验需求、标题误匹配产品、只是已有意图换词 |
| 实用编辑 | 固定样例、答案靠前、下载产物、失败处理、TokRepo 作用 | 读者拿不到结果、安装压过任务、无意义拼组件 |
| 验证编辑 | 实际运行与浏览器行为记录、fixture 输出、源和资产链接 | 核心行为不工作、伪造测试、数据损失被隐藏、链接失效 |
| 执行主编 | 综合记录、遗留问题、明确 verdict 和发布范围 | 独立 blocker 未解决、宣称范围超过验证、同日重复发布 |

每个角色可判 **PASS / REVISE / REJECT**。PASS 只能针对记录明确的对象、commit/source hash、时间和范围；文件改动后受影响项重新检查。REVISE 是能用具体修复解决的缺口。REJECT 是没有可成立的意图/价值、重复页面或无法诚实兑现的产品承诺。作者不应抹掉 reviewer verdict；修复后新增一次审查。

## 搜索需求证据等级

| 等级 | 条件 | 可作的结论 |
| --- | --- | --- |
| D0 | 仅 AI 生成词、资产名、猜测、站内词 | 不可入发布队列 |
| D1 | 可复查的市场/语言联想、相关 SERP 或单个真实任务提问 | 有定性意图线索；可做候选 |
| D2 | 两种独立类型证据一致指向同一任务；例如市场联想 + 有上下文的公开反复提问，或市场联想 + SERP 页面明确工具意图 | 可发小规模试点；搜索量未知时必须明确未知 |
| D3 | 有可信关键词量化字段，并保留提供者、国家、语言、时段、单位和日期，同时意图适配 | 可按实测量级排序；不能保证流量/排名 |

两次相同 autocomplete 返回不是两种证据。无关社区提问、某个仓库 star、工具用户数、Google 结果数和 YouTube 搜索量都不能替代网页关键词搜索量。英语地区目标要记录国家；只看 US en 不能声称全部英语地区已验证。

首次上线的工具页需 D2 或 D3。没有可靠数字就写 unknown；不能把 D2 包装为“高搜索量”。审核时也要问：读者要转换、检查、学习还是购买？现有页是文章、工具还是下载？是否满足核心意图？

## 评分与硬阻断

每项 0–5，总分 30。0 为缺失/错误；3 为具体可用但有非核心缺口；5 为用户可立即完成并有证据。**至少 24 分且六项都至少 3 分** 才可 PASS。

| 项目 | 达到 3 分的最低条件 |
| --- | --- |
| 需求与意图 | D2+；明确目标读者；标题覆盖实际能力；有独立意图去重 |
| 即时实用性 | 页面有直接使用/下载的结果；第一屏入口清楚；非技术用户路径匹配任务 |
| 证据与复现 | 固定 fixture + 真实运行输出；浏览器工具有实际交互；所有 tested 声明有记录 |
| 内容具体性 | 一组输入输出；具体适用条件；关键错误能解释和修复 |
| TokRepo 相关性 | 准确资产 URL 已核验；参与或延伸关系明确；CTA 帮助下一步 |
| 开源与可维护性 | 完整源和许可；下载可复现；验证能重跑；错误和贡献入口可用 |

即使总分够，以下任何一项仍硬阻断：核心输出错误；不可用按钮或下载；标题过度承诺；隐瞒信息丢失；伪造/推断为实测；无具体资产链接；公开凭证/未经授权内容；已存在相同意图的近似页；关键独立审稿项为 REVISE/REJECT。有效 HTTP 200 只证明 URL 可访问，不证明功能正常。

## 机器可读取的 review 记录

推荐每个页面一个 JSON，以下是 schema 的字段合同；值仅为说明，不是某页面已通过的记录。不要填假 PASS 让脚本通过。

```json
{
  "schema_version": 1,
  "page_slug": "unique-task-slug",
  "reviewed_source_sha256": "actual-source-hash",
  "reviewed_at": "ISO-8601 timestamp",
  "target": {"language": "en", "countries": ["US"], "audience": "specific audience"},
  "intent": {"primary_query": "task query", "job": "input to desired output", "dedupe_key": "normalized-intent", "title_matches_capability": true},
  "demand": {
    "grade": "D2",
    "monthly_volume": null,
    "evidence": [
      {"type": "autocomplete", "url": "source URL", "retrieved_at": "ISO-8601", "market": "US", "language": "en", "observed_text": "exact relevant phrase"},
      {"type": "public_question", "url": "source URL", "retrieved_at": "ISO-8601", "observed_intent": "specific task and obstacle"}
    ]
  },
  "deliverable": {"kind": "browser_tool", "input_fixture": "path", "expected_output_fixture": "path", "download_paths": ["path"], "limitations": ["specific limitation"]},
  "verification": {
    "runtime": {"status": "PASS", "record": "path", "environment": "actual version"},
    "browser": {"status": "PASS", "record": "path", "cases": ["sample to output", "invalid input", "copy", "download", "mobile viewport"]},
    "links": {"status": "PASS", "record": "path"},
    "claims": {"status": "PASS", "record": "path"},
    "privacy": {"status": "PASS", "record": "path"}
  },
  "tokrepo_assets": [{"url": "verified asset URL", "relationship": "used or optional_next_step", "reason": "concrete contribution", "checked_at": "ISO-8601"}],
  "scores": {"demand_intent": 0, "immediate_utility": 0, "evidence": 0, "specificity": 0, "asset_fit": 0, "open_source": 0},
  "roles": {"topic_editor": "REVISE", "practical_editor": "REVISE", "verification_editor": "REVISE", "managing_editor": "REVISE"},
  "blockers": ["specific unresolved issue"],
  "verdict": "REVISE"
}
```

门禁脚本必须检查：字段存在；D2+；至少两种独立证据类型；真实 source hash 匹配；fixture 和 record 文件存在且非空；验证 status 不接受 pending/unknown 当 PASS；分数最低值及总分；各角色 PASS；blockers 空；同日 dedupe_key 不重复。脚本不能只检查 JSON 上写了 PASS；运行可执行校验、比对输出，并检查完整 artifact。没有运行记录的内容只能留草稿。

模板/纯下载页的 browser 可用明确 `N/A` 理由替代，但网页下载和复制实际路径仍要检查。浏览器工具不可把 `node --check`、单元测试或代码审读替代浏览器交互。无法取得真实浏览器验证时，状态必须是 REVISE；不要将此类页计入“已发布可用工具”。

## 浏览器工具的最低功能案例

- 载入样例后输入可见，执行后输出与 fixture 一致。
- 粘贴一个有效变体；结果不得仅对默认样例硬编码。
- 空输入、错误格式、边界数据给具体错误，不抛无提示异常，不覆盖原输入。
- 下载产物（以及工具实际提供复制功能时的复制内容）的实际内容和编码正确，下载名称/扩展名与能力相符。
- 移动视口可操作；标签、键盘、焦点和状态消息可理解。
- 多次运行不会使用旧结果；有 clear/reset 路径。
- 内容和网络行为支持页面的数据处理/隐私声明。

验证记录应含一次成功和至少一次失败输入。支持范围较复杂时增加真实边界，不追求固定测试数量。动态模型或第三方调用不能只跑 mock 后写真实服务正常。

## 发布与完成定义

发布前：独立审稿 PASS、构建成功、实际功能通过、资产核验、源与许可、无私有信息。发布后：确认公开 HTML 与审核 commit 对应、页面交互、下载和 TokRepo 目标可达。仅 GitHub 仓库 commit 成功不能记为站点已上线。

搜索收录、曝光、点击和资产后续使用分别计量；刚上线只汇报上线事实。日量是最多 6 个合格独立意图，不是必须填满 6 个。优先修复现有缺陷，再扩张；不足就不发，拒绝廉价换标题和不相干链接组合。
