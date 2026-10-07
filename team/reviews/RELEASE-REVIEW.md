# 独立发布验收

日期：2026-10-07。审稿人：managing_editor。**Release verdict：PASS**。范围是本次已上线的六个文件工具，未观察到需要阻止发布的实际缺陷。

- 公开站：[Practical AI Workbench](https://henu-wang.github.io/practical-ai-workbench/)
- 发布 commit：`a89619ebb35e28749842f6ba6eccdc464a0f04e3`
- 产品 source hash：`63940d48a640fc5cbf5c510bf460aa43676a5b6a979def50a09a8dc01e3af94e`
- 完整机器证据与时间：`release-review.json`

## 独立核验结果

1. 重新用 Node 按 `scripts/source_hash.py` 相同路径排序与 NUL 分隔算法计算，hash 与独立内容审查、browser-local、browser-public 三份记录一致。未用旧版 PASS 批准修改后的源码。
2. 独立读取两份实际 Chrome 记录：本地与公网站都为六页 PASS。每页有非空下载、实际产物 hash、empty input、有效变体、reset/error recovery、390px mobile viewport。external requests 和 page errors 都为空。没有重复运行整套已通过的浏览器测试。
3. 独立 GET 并逐字节比对首页、privacy、六个工具 HTML、core.js、app.js、style.css 和三个小样本，共 **14 个公开文件**，HTTP 200 且与当前 `docs` 相同。另读取 root 的 12 文件比对记录，其中包括两份 vendor。不是仅从 Git commit 推断上线。
4. 独立访问四个具体 TokRepo 资产地址。程序客户端重定向 `/raw/<slug>`，返回实际资产正文；从 heading 和能力描述确认 pdf-lib、Papa Parse、Sharp、Jimp 身份，未仅以 HTTP 200 判正确。pdf-lib/Papa Parse 是实际依赖，Sharp/Jimp 是可选批量处理延伸，页面没有虚构集成。
5. 独立内容阶段已运行当前源码 `npm test`，9/9 PASS。source 此后未变，未无意义重复。root 已报告 machine editorial gate PASS；本次读了该脚本并核对 source/records/demand 与 cases，不伪称重新执行了它。

## 功能证据覆盖

| 页面 | 公共 Chrome 实际检查 |
| --- | --- |
| Merge PDF | 两个样本得到三页；file order 变体；页面宽度对应所需序列 |
| Extract PDF pages | 2,1 顺序；有效单页变体；无效页码后恢复；真实 PDF 下载 |
| Compress image | 实际 JPEG 下载及原始/结果 bytes；WebP 变体；无效尺寸提示 |
| Resize image | 样本 1200×800 → 600×400；JPEG/WebP；边界错误和下载 |
| Remove CSV duplicates | 四记录 → 三记录；引号逗号、多行；单 key 大小写/keep last 变体 |
| CSV to JSON | 四对象；leading-zero 字符串；重复 header 错误；下载完整 JSON |

所有六页还通过空输入、重置、错误恢复和移动视口检查。移动视口不代表真实手机或所有浏览器覆盖；当前证据为 Chrome 155.0.8059.39 与自有合成样本。

PDF 的两次下载 hash 不同，不是页顺序失败证据；浏览器脚本按结构和几何核对输出。页面没有承诺签名、可编辑 form、metadata、OCR 或 redaction 等未实现能力。图片没有 target bytes、animation preservation 或任意 exact shape 保证。CSV 说明 all values strings、header trim 和可选 formula protection。

## GitHub Actions 的实际状态

独立查询 API：`enabled=true`，run 列表为空，`total_count=0`。状态是 **UNOBSERVED**，不能记 PASS 或 FAIL。该可选 remote CI 未被观察到执行，不阻断已被本地测试和真实公网站交互验证的这次产品发布。后续有 run 后按其真实结果记录。

## 验证的边界

额外独立下载约 2.6 MiB 的 `sample-image.png` 时，在 20 秒及 45 秒请求预算内均超时，因此没有声称完成该样本的独立字节比对。这是补充传输检查的限制；root 的公开 Chrome 记录实际成功载入该样本，并验证两页编码产物及下载，未观察到工具任务失败。首屏和用户自选文件处理不依赖下载这个示例文件。没有据此把站点称为全时段性能通过。

产品 source hash 不等于整仓库 hash；生成 HTML、小样本及发布 commit 分别提供额外绑定。实时网络与后来发布可能改变状态；此记录仅对应时间戳内的当前上线版本。

## 搜索与结果表述

六任务的搜索需求证据是 US English 的 D2 定性支持，monthly search volume 为 **unknown**。本次确认公开工具上线与可用，不代表搜索已收录、已有曝光或点击，也不保证排名或流量。页面没有宣称数字搜索量、100 KB 必达或 100% 准确。

**当前 release blockers：无。** 通过范围仅为以上实际记录与独立检查；不把未观测 CI、跨浏览器或搜索业绩加入 PASS 范围。
