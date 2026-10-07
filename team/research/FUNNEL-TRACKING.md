# TokRepo 导流漏斗与实际 GA 能力审计

日期：2026-10-07。只读范围：当前 TokRepo 仓库 `frontend-nuxt` 的配置、详情页面、公共 clipboard helper、PostHog plugin、hosted MCP funnel emitter，并只读核对自有 backend funnel 定义。源码 HEAD：`05a0cbe6d14c3b727bfbdba296d8008e1b05227b`；本报告是当前文件行为审计，不能证明同一版本已部署或线上事件实际收到。

**结论：没有发现向 GA 发送资产取得/复制/安装完成的自定义业务事件。** 现有 GA 配置能启动标准 Google tag；PostHog 和自有 funnel 的事件属于不同接收方，不能当成 GA conversion。root 观察 GA connector `connected=false`、缺 Analytics scope，因此这轮没有读取真实 GA property/event 报表，也没有登录、调整设置或触发生产 QA。

## 配置与代码依据

| 代码位置 | 实际行为 | 可作的结论 |
| --- | --- | --- |
| `frontend-nuxt/nuxt.config.ts:112–113` | 载入 `gtag/js?id=G-SJEZGZ3RCW`；调用 `gtag('js',...)` 和 `gtag('config',...)` | 配置了 Google tag，未关闭默认 pageview；不等于真实 GA receipt 已验证 |
| `frontend-nuxt/plugins/posthog.client.ts:4–9,16–46` | PostHog 开启 pageview/pageleave/performance；有 public key，且已同意 analytics 或调用 consent function 才初始化 | PostHog 页浏览及后续事件取决于配置和同意，独立于 GA |
| `frontend-nuxt/composables/useClipboard.ts:13–46` | Clipboard API 或 textarea fallback，返回成功/失败 | helper 自身不发送 GA/PostHog 业务事件 |
| `frontend-nuxt/pages/workflows/[id].vue:2132–2137` | 复制当前页面 URL并 toast | 没有显式业务事件 |
| 同页 `2314–2330` | copyAssetPrompt / copySkillInstallText / copyApiFetchLink 成功后 toast | 没有显式 GA，且这些方法没有 PostHog capture |
| 同页 `2332–2338` | 复制 agent install prompt 成功才 capture `asset_agent_install_prompt_copied`，含 asset UUID、target、status | **PostHog** 事件；复制成功不是完成安装 |
| 同页 `2341–2352` | 创建 Markdown Blob，临时 `<a>` 点击，revoke URL | 没有显式业务事件；创建下载不证明安装或使用成功 |
| 同页 `2244–2266`、`components/SaveButton.vue:87–105` | 收藏 API 成功后 capture `saved_added` / `saved_removed` | **PostHog** 收藏事件，非 GA conversion |
| `pages/@[username]/index.vue:915–920` | 复制 saved install-all prompt 成功，capture `saved_install_all_copied` | **PostHog** 复制批量指令，非完成安装 |

在 Nuxt plugin/composables/components/pages/server/utils 中针对 `gtag`、`dataLayer`、`capture`、analytics/funnel 的代码检索没有发现自定义 `gtag('event', ...)` 或 GA Measurement Protocol 转发。无明确 event call 是源码结论，不是“GA 后台一定没有其他自动事件”的结论。

## GA 自动事件的范围

Google 官方说明，标准 `config` 默认发送 pageview；GA 的自动事件和 web stream 的 enhanced measurement 可带来 session/user engagement、历史导航页浏览、outbound clicks、常见文件下载等。是否开了哪些 enhanced measurement 选项必须读实际 stream 配置和事件记录，不能从当前 repo 推断。[GA pageview 说明](https://developers.google.com/analytics/devguides/collection/ga4/views?hl=en)、[自动与 enhanced measurement](https://support.google.com/analytics/answer/9216061?hl=en)

因此不能把此次结论写成“只有 page_view”。更准确的是：**只有标准 GA 初始化在源码中得到确认，资产业务漏斗的显式 GA 事件未实现/未发现，自动事件真实覆盖未知。**

详情页 Markdown 下载使用 Blob URL。不能仅凭 GA 的 file_download 功能就说这种下载一定被记录；官方常见扩展名列表不含 `.md`，Blob URL 也不是正常后缀资源链接。需要实际 DebugView/network 确认。即便观察到 download event，也不代表用户成功保存、导入或运行资产。

## 自有安装漏斗不是 GA

`frontend-nuxt/server/routes/mcp.post.ts:761–791` 构造 `search | install_plan | completed_install` 并发送到 `https://api.tokrepo.com/api/v1/tokenboard/analytics/funnel`。它有 event UUID、entry_point、tool_name、asset UUID、outcome、source/version 和 request hashes。`requestFunnelHashes` 在同文件 `586–595` 用 salt 后的 IP/UA 及 caller hash；不是 GA 的 client_id/session_id。

`install_plan` 在 `2152–2161` 记录 blocked/returned；`completed_install` 的 hosted lifecycle 分支在 `1931–1948` 记录 completed/updated。但 hosted MCP 无法读取调用者磁盘，代码说明成功报告须在本地成功和 post_verify 之后使用。收到该报告是契约级 completion receipt，不自动证明每个调用者遵守了本地验证；也不是在网站上复制按钮就完成安装。

代码本轮未见从 guide CTA 的 UTM 自动传给 hosted MCP emitter，亦未见把 UTM/session 持久化为浏览器→CLI 的链路。自有 funnel 可能衡量 MCP 内部 search→plan→completion，但不能未经 bridge 证明某篇 GitHub guide 带来了这次安装。该 endpoint 的线上接收、表数据和实际使用量未在此审计读取。

## 当前能衡量到哪一步

| 目标步骤 | 当前证据/可用能力 | 尚缺什么 |
| --- | --- | --- |
| 搜索者发现 guide | 公共页面与技术 indexability；root 另处理 GSC | GSC 实际 page/query impressions、clicks、country/device |
| guide 访问 | 无 GA 追踪的原静态站不可凭其代码给 visit counts；改版须另核验 | 实际可用访问数据来源及其定义 |
| guide → 对应 TokRepo 资产 | 正确带 UTM 的链接可让接收站标准 attribution 有机会区分 source/campaign/content | root 验证接收站 GA session source / campaign / landing page；页面看到链接不等于点击 |
| TokRepo 资产详情阅读 | 标准 tag 可生成 page_view；route/SPA 实际 receipt 未验证 | 线上 page path/location 与 UTM归因、过滤内部QA/机器人规则 |
| 复制/取得资产 | 部分 PostHog复制/收藏；普通复制和 Markdown 下载无明确业务事件 | 一致的成功 event、asset stable ID、CTA context；实际 receipt |
| 实际安装/使用 | MCP/CLI自有 completion reporting 体系 | guide context→本地 receipt 的可验证 bridge；不能把 plan/copy 算 completion |

UTM 能标注一次入口，但不自动让每个后续动作变成 conversion，不保证跨浏览器/设备/CLI join，也不保证 GA 把新 UTM 当成新 session。应优先按接收站实际可用 attribution dimensions 报告，不从参数存在倒推出访问量或成功量。

## 建议的最小指标合同（尚未实施）

后续如用户授权主站 instrumentation，可使用一致的事件表，而不是把所有按钮点按叫“安装”：

- `asset_detail_view`：带 stable asset UUID、来源 recipe slug/UTM context；仅详情真实显示时。
- `asset_copy_success`：Clipboard 确认成功才发，区分 payload 类型；不发具体 prompt/私有文本。
- `asset_download_started`：记录启动意图，明确不能证明保存成功。
- `asset_install_plan`：记录取得 plan 与 gate 状态，不当完成。
- `asset_install_completed`：本地命令退出成功、post_verify 通过的结构化 receipt；保留 target/version 和来源桥接标识。

事件名是方案，**当前未写入源码、未部署、未创建 GA event 或 key event**。是否采用 GA/PostHog/自有 funnel 作为事实来源要明确，不把三个计数相加当用户数。

## 实际复盘路径

root 当前优先把 GSC/GA 只读权限连接与精确 property 核实；本 agent 不重复连接。已有 GA 数据能读后，先按 source/medium、campaign、landing page 对统一 UTM入口做小规模核对，再看它真正有哪些 event names。针对 event 的一次受控、标记 QA 验证应检查浏览器 collect/request 与后台 receipt，并区分 source、动作和成功条件。

没有完成业务事件或 bridge 前，公开复盘应停留在“搜索点击、带UTM进入资产页的访问、已观测的复制”等相应层级。缺 conversion 数据写 unknown，不填 0，不宣称 GitHub guide 已推动安装。此轮未修改 TokRepo 主站、埋点、部署、账户或 automation。
