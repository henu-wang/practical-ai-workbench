# 公开收录与搜索基线审计

审计日期：2026-10-07。对象：[Practical AI Workbench](https://henu-wang.github.io/practical-ai-workbench/) 与 [TokRepo Guides](https://henu-wang.github.io/tokrepo-guides/)。本记录是新版搜索落地指南发布前的基线，不是新内容验收。

**结论：现有 15 个 sitemap URL 都公开可访问、自身 canonical、未观察到 noindex；Google/Bing 真实收录和排名仍 UNVERIFIED。** 具体时间、每 URL response/hash、SERP 请求参数和限制保存在 `indexing-baseline.json`。这个 agent 没有读取或修改 GSC 账户，没有提交 sitemap、请求 indexing、改站点、发布或改自动任务。

## 技术抓取基线

| 项目 | Workbench | TokRepo Guides |
| --- | --- | --- |
| 首页 HTTP | 200 | 200 |
| sitemap.xml | 200、有效 namespace、8 URLs | 200、有效 namespace、7 URLs |
| sitemap 所有 URL | 8/8 HTTP 200 | 7/7 HTTP 200 |
| canonical | 8/8 与访问 URL 完全一致 | 7/7 与访问 URL 完全一致 |
| meta robots / X-Robots-Tag | 未观察 noindex；首页 index,follow | 未观察 noindex；首页 index,follow |
| 项目目录 robots.txt | 200，但位置不具有 host robots 权威性 | 200，但位置不具有 host robots 权威性 |
| Search Console property | 此 agent 不查，交 root 确认 | 此 agent 不查，交 root 确认 |
| Google index / position | 未获 URL Inspection 或 Performance 证据 | 未获 URL Inspection 或 Performance 证据 |

两个 sitemap 都使用绝对 HTTPS URL，全部位于自身项目 prefix；没有把 URL 交叉写到 TokRepo。静态页面提供标题、canonical 和内容，不需要先登录取得 HTML。HTTP 抓取成功是公开访问证据，不等于 Googlebot 已访问或 Google 已采用该 canonical。

### robots.txt 的实际位置

两站同属 `henu-wang.github.io`。搜索爬虫的 robots URL 是 [host root robots.txt](https://henu-wang.github.io/robots.txt)，此次返回 **404**。两份项目目录里的 robots.txt 各自有 Allow 和 Sitemap 行，但爬虫不从子目录读取 robots 规则，不能以这两份文件作为 sitemap 已被发现的证据。Google 对 robots 的 404 按不存在处理，通常视为没有该文件施加的抓取限制，而非拒绝抓取。[Google 官方规范](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec)

因此不需要为了“允许抓取”再加一个根 robots 才能收录。若未来维护用户级根站，可在真正根 robots 指明两个 sitemap；当前更直接的发现路径是经已验证 prefix property 提交各自 sitemap，以及保持可抓取导航链接。这里只给方案，未修改配置。

## Google 与 Bing 搜索采样

采样窗口 UTC `2026-10-07 05:48:30.963–05:48:31.648`，北京时间约 13:48。每个引擎四个 query：

- `site:henu-wang.github.io/practical-ai-workbench/`
- `site:henu-wang.github.io/tokrepo-guides/`
- `"Practical AI Workbench" "merge PDF"`
- `"henu-wang.github.io/tokrepo-guides/ollama-rag-python-chroma/"`

请求为无登录 HTTP、桌面 Chrome 155 User-Agent，设置 US/en；Google 加 `pws=0`。请求参数不是实际地区保证，网络出口位置未被控制。

| 引擎 | 实际观察 | 允许的结论 |
| --- | --- | --- |
| Google | 4/4 请求在取得 HTTP response 前 `fetch failed` | 没有取得 Google SERP；不能说无结果、未收录或排名 0 |
| Bing | 4/4 HTTP 200，但重定向 `cn.bing.com`；各解析出 10 个 organic-like blocks，未在这些 block 观察到目标域 | 此地区不受控的有限采样未命中；不能称为 US 排名或未收录证明 |

原始 HTML 中出现查询目标可能只是搜索输入或页面导航，不把它算为被收录结果。Bing 的 block 解析也不是账户级 position。没有把页面从这次有限采样中消失解释为技术抓取失败。

Google 官方明确 `site:` 返回不穷尽已收录 URL，且无 query 的 site 搜索不是排序列表。实际收录应看对应 URL Inspection；表现应看 property 的 Performance，而不是给 site 搜索排一个名次。[Google site operator 官方说明](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site?hl=en)

## GitHub Pages 与 GSC 验证路径

GitHub Pages 项目站公开在 `<owner>.github.io/<repo>/`，不是每个 repo 一个独立 hostname。可为两个 HTTPS 项目 prefix 分别建立 URL-prefix property，按 GSC 显示的验证位置放置其原样 HTML file，或采用其支持的 meta 验证。不要对共享 `github.io` hostname 猜测 DNS 控制权；Domain property 的 DNS 验证不由普通项目仓库中的 HTML file 完成。[GitHub Pages 站型](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)、[GSC property 类型](https://support.google.com/webmasters/answer/34592?hl=en)

URL-prefix 候选应精确包括 HTTPS 与尾斜杠：

1. `https://henu-wang.github.io/practical-ai-workbench/`
2. `https://henu-wang.github.io/tokrepo-guides/`

HTML file 方法要保存 GSC 给出的文件名和内容，不要用自己造的文件替代。文件应进入实际 Pages publish output：例如 publishing source 是 `main:/docs`，则源文件放 `docs/<provided-file>.html`，上线 URL 在项目 prefix 下；若 source 是 `/` 则放根 publishing output。最后以 GSC 页面提供的**具体 URL**为准，公开无登录 GET 确认后再点 Verify。[Google 验证说明](https://support.google.com/webmasters/answer/9008080?hl=en-GB)、[GitHub publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

此次首页未见 `google-site-verification` meta，不能据此判 property 未验证：file、权限继承等其他方式可能成立。账户状态和 verification token 留 root 的私有上下文；公开审计不记录邮箱、token 或账号截图。

## 新版指南的 canonical 与质量边界

新版主站落地页应保持自身 canonical，并用准确正文、步骤、成果示例和相关资产链接支持搜索意图。TokRepo CTA 是读者继续完成任务的链接，**不是**跨域 canonical。若把 guide canonical 指到不同内容的 TokRepo 资产，会发出偏向另一 URL 的合并信号，可能削弱 guide 自身被选为搜索结果的机会；canonical 也不是 Google 一定采纳的指令。[Google canonical 官方说明](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

多个页面可以组合 TokRepo 资产，但每个页面必须提供独立任务成果，不能只替换 query、堆关键词或全部把用户导向同一个目的页。原网页有工具不代表满足新的指南目标；新版质量应另作独立内容审查，不把此技术 baseline 的 200/indexable 当作内容 PASS。[Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies)

## 后续监测计划

这是一份监测方案，没有创建或修改任何计划任务。root 可纳入已授权搜索复盘：

| 时点 | 实际检查 | 必须记录 | 失败/不足时的动作 |
| --- | --- | --- | --- |
| 每次发布 | 公网状态、canonical/noindex、sitemap、正文/CTA 与发布 source 一致 | published URL、commit、时间、实际响应 | 修复公开版本；不要用 push 成功替代上线 |
| 已验证 property 后 | sitemap 读取/提交状态；代表性 URL Inspection | property prefix、sitemap 状态、inspection coverage、last crawl、Google canonical | 按实际错误处理；未验证或无数据写 unknown，不猜已收录 |
| 发布后约 3/7/14 天 | 新页是否 discovered/crawled/indexed，有无 exclusion 与 canonical 异常 | 每 URL 状态和时间；不要把预设日期当 Google SLA | 与 sitemap、访问和内容质量对照；不要重复无差别请求 indexing |
| 每周 | Performance 的 page/query、country、device，取真实可用完整日期 | impressions、clicks、CTR、average position、日期范围和当前延迟 | 有曝光少点击再查标题/意图；无曝光先查收录与相关性 |
| 每周辅助 | 固定 query 的少量公开 SERP 采样 | engine、时间、country 实际可控性、device、target observed | bot/network 错误标失败；没看到结果标采样未见，不写未收录 |
| 内容复盘 | 落地指南到 TokRepo 资产的后续访问/使用，使用实际可获得数据 | metric 定义、来源、时间、缺失字段 | 区分 page 发布、search click 和 asset conversion，不以互链数代替效果 |

月搜索量此轮仍 unknown；不能由网页存在、老问题浏览数、autocomplete 或当前 SERP 数量换算。更通用关键词的竞争和真实流量要之后的数据验证。当前 baseline 的作用是让新版可以与真实起点比较，不承诺收录时间、排名或流量。
