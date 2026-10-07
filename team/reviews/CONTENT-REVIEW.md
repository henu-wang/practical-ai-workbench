# 新项目独立内容审查

日期：2026-10-07。审稿人：独立 managing_editor agent。作者：project_editor + root。

结论：**内容审查 PASS；发布就绪 PENDING**。准确时间、完整 source hash、逐文件 manifest 和六页记录见同目录 `content-review.json`。

## 范围与证据

读了六篇正文、页面生成器、浏览器 UI glue 与 core 实现，核对 US English 需求记录中的真实返回联想和每题两条公开用户问题。需求判为 D2 定性支持：monthly search volume = unknown，不代表全部英语市场已验证，更不代表已有排名或流量。审查核对已有证据 packet，未重复抓取全部外站问题。

独立运行当前 `npm test`：**9 / 9 PASS**，包括 PDF 顺序/几何、选页、损坏样本、CSV 引用逗号/多行/BOM/leading zeros、header 和宽度错误、dedup first/last、formula protection、image fit，以及有效单列 CSV。这个测试没有运行浏览器 Canvas、网页下载或 GitHub Actions。浏览器、下载、网络和公开部署由单独 release 记录证明。

## 页面评分

评分顺序：需求意图、即时实用、证据复现、内容具体、资产关联、开源维护；每项 0–5。本表是内容与源码审查评分，证据项 3 分明确保留执行范围；并非六工具的浏览器验收结果。

| 页面 | 六项分数 | 总分 | 内容 verdict | 检查结论 |
| --- | --- | --- | --- | --- |
| merge-pdf | 4 / 4 / 3 / 5 / 4 / 4 | 24 / 30 | PASS | 顺序、页内排列、10 文件/40 MiB 限制符合实现；不称压缩/OCR；不以输出替代签名和表单原件 |
| extract-pdf-pages | 4 / 4 / 3 / 5 / 4 / 4 | 24 / 30 | PASS | 页码从 1 开始，支持指定顺序、重复页去除；不称 redaction 或文本找页 |
| compress-image | 4 / 4 / 3 / 5 / 4 / 4 | 24 / 30 | PASS | 用真实字节比较；可更大；100 KB 不保证；JPEG 白底；Sharp 是可选批量延伸 |
| resize-image | 4 / 4 / 3 / 5 / 4 / 4 | 24 / 30 | PASS | fit bounds、不裁切/拉伸/放大；600×400 只对相同比例样例成立；Jimp 是可选后续 |
| remove-duplicate-csv-rows | 4 / 4 / 3 / 5 / 4 / 4 | 24 / 30 | PASS | 全字段或一个 key；first/last；header trim 与比较 normalization 不同；公式保护可改 export |
| csv-to-json | 4 / 4 / 3 / 5 / 4 / 4 | 24 / 30 | PASS | 全部字段保持字符串；leading zeros、多行保持；header 规范、8 条预览与全量下载准确 |

## 阻断问题与修复核对

1. 去重正文原来承诺选择多个 key，现已明确一个 key，blank 为全部字段。不强行增加不存在的能力。
2. 去重正文现在披露 header whitespace 会 trim；comparison normalization 不改保留字段。可选公式保护可能改导出数据。
3. 有效单列 CSV 原来因自动 delimiter 警告被拒绝，现只忽略 `UndetectableDelimiter` 并继续正常字段校验。独立第 9 项测试通过。
4. 图片错误文案明确 HEIC/SVG/GIF 不支持、animation 不保留，符合 PNG/WebP 经 Canvas 变成静帧的范围。没有暗示检测并拒绝所有动画。
5. demand primary query 改为真实返回的 `compress image online free` / `resize image online free`。100 KB 和 Instagram 不作为此版能力承诺；页面不承诺任意 exact shape 或 target bytes。
6. merge 页原建议删列表条目，但 UI 没有 Remove；现改为重选正确文件，操作相符。

**当前内容 blockers：无。** 上述修复均从当前文件重读确认。透明度真实输出、下载及 mobile/network 检查仍属独立发布验收，不能根据代码推断为已经实测。

## 页面体验判断

首屏是真正任务表单，后面才有教程和 TokRepo；没有安装门槛。六个意图按不同输出划分，区别于同一文章换库名。实例提供自有 PDF、图片与 CSV 下载，用顺序、尺寸、记录数指导检查。资产说明把 pdf-lib/PapaParse 实际依赖与 Sharp/Jimp 可选批量延伸分开，不虚构后者参与浏览器引擎。

限制说清了 PDF 不做 OCR/压缩/redaction、不保留 functional signatures/forms；JPEG 透明区域变白、动画/metadata 丢失；CSV 字段仍是字符串、header 规范和预览范围。无需给这些内容硬添字数或组件链接。

## 尚未获得的发布证明

- 本次审查落盘时未读到已完成的 Chrome record，content PASS 不替代它。
- GitHub Actions 未在此审查确认运行通过。本地 npm PASS 不等于 remote CI PASS。
- 仓库、公开 HTML、实际外链 identity 与当前部署结果须由 release 记录验证。
- 此审查不声称 100% 准确、目标字节保证、数字月搜索量或已获得搜索流量。

## Hash 复算与失效规则

运行 `python3 scripts/source_hash.py`。取 `content/`、`docs/assets/`、`docs/vendor/` 的所有递归文件，加上 `scripts/build.py`；按相对 POSIX 路径排序，把每个 UTF-8 路径、NUL、原始 file bytes、NUL 依次送入 SHA256。JSON 保留每个输入文件的 hash，以及 demand evidence 的独立 hash。

源码、CSS、正文、vendor 或 build 变动使 source 绑定失效，应复查受影响项后重新生成记录。编译 HTML、样本、templates、tests 和 CI 文件不在此产品 hash 中，必须由 runtime/release 记录另行绑定并检查；不能把这个 hash 当作整仓库或线上版本证明。
