# TokRepo 资产解决方案需求 brief — 2026-10-07

唯一目标：**英文指南/模板搜索需求 → 公共解决方案页 → TokRepo 对应资产访问/获取/使用**。GitHub项目承载原创教程、示例、模板和编辑框架；不做独立文件工具产品，不把读者留在另一个转换器网站。完整可复用资产出处和获取入口是TokRepo。

本次只做需求编辑研究；不发布、不改自动化、不实现或运行教程程序。源证据保存在 `redirect-demand.json`：`recipes` 是供编辑直接消费的统一数组，包含 slug、title、primary_query、assets、autocomplete、questions、deliverables、claim_boundaries。六项已通过定性需求门槛；文章和产物是否真实可用由实施/质量编辑另验。

## 六项决定

|slug|标题/匹配主查询|用户拿到什么|TokRepo完整资产入口|
|---|---|---|---|
|transcribe-audio-to-text|How to transcribe audio to text for free；`how to transcribe audio to text for free`|本地转录步骤、音频准备方式、TXT/SRT结果检查清单；真实短样例或明确未运行的预期结构|Whisper识别音频+FFmpeg准备输入|
|meeting-minutes-template|Meeting minutes template with decisions and action items；`meeting minutes template word`|原创可编辑Word/Markdown模板、虚构填好示例、决策和待办出处核对|原创会议笔记prompt+action register prompt+DOCX生成skill|
|extract-tables-from-pdf-to-excel|How to extract tables from a PDF to Excel；`extract tables from pdf to excel`|逐表提取到CSV/Excel的步骤、原样例/输出、表格质量检查|Docling解析+pandas核对和导出|
|presentation-from-notes|How to make a presentation from notes；`make presentation from notes`|受众/目标brief、原创6页大纲、可编辑PPTX仅在真正生成验证后提供|原创写作prompt确定内容+PPTX skill生成文档|
|clean-csv-remove-duplicate-rows|How to clean a CSV file and remove duplicate rows；`remove duplicate rows pandas`|小型脏CSV、规则和清理步骤、实际执行后提供cleaned及duplicate-audit文件|pandas处理+Papa Parse作为JS解析替代路径|
|flashcards-from-lecture-notes|How to make flashcards from lecture notes and transcripts；`make flashcards from notes`|原讲义片段→3–8张来源可查问答卡、TSV结构、检查和复习清单|TokRepo原讲座study-card prompt；音频笔记才可选Whisper|

所有primary_query都原样出现在今天 US/en Google联想返回里。模板/步骤页面匹配这些意图；没有拿 `online converter` 或 `free generator` 为代码文章充依据。CSV的主query包含pandas，是Python指南意图，标题和正文必须明确其安装/代码前提，不能伪装成无设置在线工具。

## 需求证据：每项两个真实独立问题

**音频转录**：Google种子 `how to transcribe audio` 返回完整 `how to transcribe audio to text for free`。[三小时音频求免费方法](https://www.reddit.com/r/audiovisual/comments/1uf7epb/can_you_transcribe_a_3hour_audio_for_free/)；[超过一小时的免费转录问题](https://www.reddit.com/r/software/comments/1mr7kl9/free_transcription_over_an_hour/)。用户痛点是免费额度、长文件和实际结果。指南说明本地开源软件与限额云服务的区别，先试短样本再全量，不虚构处理速度和准确率。

**会议纪要模板**：种子 `meeting minutes template` 返回 `meeting minutes template word`；另有 `how to write meeting minutes template`。[什么样的meeting template好用](https://www.reddit.com/r/ObsidianMD/comments/1jzx88n/anyone_have_a_good_meeting_template/)；[会议笔记与正式纪要的处理困惑](https://www.reddit.com/r/ExecutiveAssistants/comments/1w5e7p2/meeting_notes_formal_minutes/)。模板应包含讨论、决策、动作、责任人、期限和原文出处。未知值保留UNKNOWN；正式治理纪要要求因机构而异，普通模板不承诺普适合规。

**PDF表格到Excel**：种子 `extract tables from pdf` 返回 `extract tables from pdf to excel`。[只拿到部分表头/内容](https://stackoverflow.com/questions/56017702/how-to-extract-table-from-pdf-in-python)；[只提取第一页第一表](https://stackoverflow.com/questions/62044535/how-to-extract-tables-from-pdf-using-camelot)。示例必须覆盖多个检测表，并核对行列/首尾；扫描件先OCR，复杂表格不能保证识别完整。问题使用Camelot/Tabula不等于要求指南用那些库；对应的是同一提取结果及具体失败现象。

**笔记到演示文稿**：种子 `presentation from notes` 返回 `make presentation from notes`。[不逐页复制，如何由笔记创建销售deck](https://www.reddit.com/r/powerpoint/comments/1vkzaae/whats_the_easiest_way_to_create_a_sales/)；[Word大纲无法插入PowerPoint模板](https://answers.microsoft.com/en-us/msoffice/forum/all/word-outline-into-powerpoint/7cb6ec23-17a6-44ef-98b9-85d1d8bcea23)。教程先给审过的大纲再给制作路径。销售场景不得编造客户、收益或数字；保留输入出处。第二问题验证导入障碍，不应声称新方案修复了所有历史Mac导入问题。

**CSV去重**：种子 `remove duplicate rows pandas` 返回主query、`drop duplicate rows pandas based on column`等。[合并CSV后去重复记录](https://stackoverflow.com/questions/52428342/pandas-drop-duplicates-in-csv)；[按指定列去除重复行](https://stackoverflow.com/questions/50885093/how-do-i-remove-rows-with-duplicate-values-of-columns-in-pandas-data-frame)。讲明整行/键列、保留第一/最后/全部删除；输出审计文件；缺失键和前导零不能默默破坏。Papa Parse负责正确解析，去重规则另实现。

**讲义转记忆卡**：种子 `flashcards from notes` 返回 `make flashcards from notes`。[如何把笔记自动做卡](https://www.reddit.com/r/Anki/comments/19c0u1e/converting_notes_into_flashcards_automatically/)；[大量笔记怎样快速做Anki卡](https://www.reddit.com/r/GetStudying/comments/kw9a77/how_do_you_guys_make_anki_flash_cards_from_a_lot/)。给一节短笔记、原子问题、能回查出处的答案；不要自动堆巨大题库。对应原创TokRepo prompt原本基于讲座transcript，适配文字笔记需说清并测试；音频才用Whisper。

## 精确资产地址与关系

以下13个资产在本次重新查了当前detail API和公开页面，均HTTP200且页面含slug。完整原始API快照仅保留在仓库外的private-monitoring目录；公共JSON只保留资产元数据和需求证据，不代表允许复制完整内容到公共指南，也不证明本项目运行已经通过。

|ID|资产|TokRepo精确地址|用途|
|---|---|---|---|
|105|Whisper|https://tokrepo.com/en/workflows/whisper-openai-speech-text-eb0f9dd6|转录本地音频；学习卡可选前处理|
|1157|FFmpeg|https://tokrepo.com/en/workflows/ffmpeg-universal-multimedia-processing-toolkit-353248b1|准备或从视频提取音频|
|6826|Meeting Notes to Decisions and Action Items|https://tokrepo.com/en/workflows/meeting-notes-decisions-action-items-e0ccfa90|原创会议笔记prompt，完整prompt在TokRepo获取|
|6946|Meeting Minutes to Action Register Prompt|https://tokrepo.com/en/workflows/meeting-minutes-action-register-prompt-a7cdc10d|未确认责任人/期限不编造的动作表|
|66|DOCX skill|https://tokrepo.com/en/workflows/claude-official-skill-docx-word-document-creation-6236da40|可选Word格式制作与核验|
|173|Docling|https://tokrepo.com/en/workflows/docling-document-parsing-ai-443e86c2|结构化文档/表格提取|
|1144|pandas|https://tokrepo.com/en/workflows/pandas-powerful-data-analysis-manipulation-python-1005b785|表格检查、Excel导出、CSV去重|
|4980|Papa Parse|https://tokrepo.com/en/workflows/papa-parse-fast-browser-csv-parser-javascript-ed9fd7fc|JS替代路径解析CSV；本身不去重|
|6825|Reusable Draft-to-Final Writing Prompt|https://tokrepo.com/en/workflows/reusable-draft-final-writing-prompt-3128c956|确认目标/受众/约束，做忠于来源的大纲|
|67|PPTX skill|https://tokrepo.com/en/workflows/claude-official-skill-pptx-powerpoint-presentations-01b1713e|依审过的大纲制作编辑型演示文档|
|6935|Turn a Lecture Transcript into Study Cards|https://tokrepo.com/en/workflows/turn-lecture-transcript-into-study-cards-585e76f2|原始学习卡prompt的完整获取入口|
|4456|Se Technical Writer agent|https://tokrepo.com/en/workflows/claude-code-agent-se-technical-writer-adb34fbc|已核验备选写作资产；首批未硬塞|
|3677|yt-fts|https://tokrepo.com/en/workflows/yt-fts-youtube-full-text-search-cli|已核验，仅用于pending视频转文章题；不冒充单视频即时文章生成器|

DOCX/PPTX资产的快捷安装命令未在本次执行，不能直接把页面中旧式 `claude skill install ...` 当成现时有效命令。编辑需要沿源仓库检查正确获取/使用方式，并分清普通复制prompt与技能执行前提。浏览资产页200只证明链接可访问。

## YouTube→blog 暂不批准

`how to convert youtube video to blog post`种子直接返回 `how to turn a youtube video into a blog post`，所以搜索意图有证据。但本次找出的若干“问题”其实是作者推广自己的转写产品，或同一问题跨subreddit重复投递；不能算两条独立用户需求。`r/Blogging/1fqthjc`正文后面自称拥有同类app；`1pou2pb`与blogspot `1pou4kl`为近乎同题crosspost。公开营销教程也不算用户问题。JSON中明确pending，不发布凑数。更强的flashcards需求用于首批第六。

## 竞争与边界

所有月搜索量、关键词难度、排名概率与预计流量都是unknown，不能拿用户帖子浏览量或Google联想换算。参数US/en验证英美查询措辞，不证明真实来访国家。

市场已有转录服务、微软/Notion模板、PDF转换与pandas教程、Gamma/PlusAI演示生成、Anki/Quizlet记忆卡工具。我们不能声称唯一、最快、最准确。可交付差异是一个具体任务的资产组合、原创可下载样例/模板、逐项来源核对，以及清楚的TokRepo获取入口。广告式堆工具名字和完整复制资产都不符合这一目标。

每篇核心CTA应准确说明读者下一步，例如“Get the full meeting-note prompt on TokRepo”“Open the Docling asset and source setup”。如果资产是外部软件目录，不能声称它是一键可安装skill；如果是原创prompt，不能把普通paste使用假装API自动化。支持组合按真实角色分步骤即可，不要求每个读者全部安装。

发布前仍必须确认：模板/附件存在且可打开，代码用当前官方源检查，实际结果与示例标注一致，未运行的流程不能写tested，完整原创TokRepo资产不镜像，links到对应资产而非只到首页。六篇是这次六项合格选题；日6依旧上限，缺需求/产物/证据时少发。
