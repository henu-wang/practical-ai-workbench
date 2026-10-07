# 英语任务需求与第一批公开工具：2026-10-07

责任：需求编辑。这里只报告搜索/公开问题/资产研究；没有运行文件转换、部署或修改自动化。原始记录见同目录 `demand.json`。时间以 JSON 中 UTC `retrieved_at` 为准，市场参数 US，语言 en。

## 决定

第一批选择六种可以打开就完成的结果：合并 PDF、提取 PDF 页、压缩图片、调整图片尺寸、CSV 行去重、CSV 转 JSON。不是六篇安装不同软件的教程，也不是六个相同关键词换标题的页面。它们共用三类处理引擎，发布为有实际工具、示例和结果下载的开源项目。

推荐优先顺序：PDF 合并 → 图片尺寸调整 → CSV 去重。前两项的通用意图明确；CSV 去重的受众较窄，但指定列、保留第一条、避免误删等问题让产物更容易做出实际价值。余下三项是相邻但不同结果，既能扩展项目，也能共用处理能力。

六项均有今天抓取的直接 Google 联想词，加两个题意匹配的独立真实用户问题。问题大多是历史提问，证明具体痛点，不证明今天的提问频率。所有六项的月搜索量、搜索排名难度和预计流量都是 **unknown**。网页上线后还需检查索引、展示、点击和使用，不能把需求证据写成流量保证。

## 方法和证据强度

1. 现场请求 Google 联想接口，参数 `client=firefox&hl=en&gl=us`；保存 URL、原始返回、抓取时间，共 28 个种子。其中 20 个为任务候选，8 个为首批细分验证。
2. 搜索并读取公开原始用户问题；先核实正文是否真在提问，再计数。官方教程、作者推广自己的工具、两个 URL 指向同一原问题，不计作两个独立问题。
3. 查看官方已有产品/开源项目，了解用户已经能得到什么。已有产品证明供给和竞争方式，不能替代用户需求证据。
4. 查 TokRepo 当前公开 list/detail API。首批所需 pdf-lib、Papa Parse、Sharp、Jimp 的资产详情返回成功，公共页面 HTTP 200 且正文包含对应 slug。资产页可用不代表依赖功能已经测试。

特别纠错：Adobe 社区 `how-to-save-one-single-page-of-a-pdf-document-1246764` 打开后发现是官方操作说明，已从用户问题清单剔除。压图问题 `/questions/64110528/...` 跳转到 `/questions/48632459/...`，只计后者一次。

## 首批六项比较

|任务/主意图|现场直接联想|竞争已有满足方式|本项目应实际交付|真实资产关系|缺口/上线门槛|
|---|---|---|---|---|---|
|Merge PDF|`merge pdf free`、`merge pdf files`；`merge pdf offline free`|Adobe 在线工具；BentoPDF 已本地开源合并|选文件→展示合并顺序/页数→下载新 PDF；示例文件可一键试用|pdf-lib 是实际依赖|检查每份文件全部页数、顺序；加密/损坏文件报清楚，不假称保留全部表单、书签、签名|
|Extract PDF pages|`extract pages from pdf into new pdf`、`extract pages from pdf online free`|Adobe 有提取页；BentoPDF 有拆分/提取|输入 `1,3-5`，展示有效选择及输出页数→下载一份新 PDF|pdf-lib 是实际依赖|清楚一基页码；越界/反向/重复/非数字处理；没有逐页多个文件导出就别称完整“Split into individual pages”|
|Compress image|`compress image to 100kb`、`compress image online free`|Squoosh 已本地压图；多种成熟转换工具|原/输出字节数、格式/质量选项、预览和下载；输出变大明确提示|首发为浏览器 Canvas；Sharp 为可选批量扩展资产|首版没有迭代目标大小算法，就不能标题承诺100 KB；有损格式不能承诺 without losing quality；透明 PNG 转 JPEG 需解释背景|
|Resize image|`resize image for instagram without cropping`、`resize image to 20kb`|Canva/Adobe 图片尺寸工具|宽高/锁定比例、实际导出尺寸、前后对照；像素结果与文件大小分开|首发 Canvas；Jimp/Sharp 是可选脚本扩展资产|不做 padding/crop 就不能声称无裁切变成任意比例；20 KB是压缩意图，不应拿像素调整冒充|
|Remove CSV duplicates|`remove duplicate rows in csv file online`、`csv duplicate remover tool`|Excel 指定列去重；各类 CSV 清理器|选整行/指定列、明确保留第一条、原行数/去除/剩余计数、下载新CSV|Papa Parse 实际解析依赖；去重规则为本项目代码|原文件不改；处理引用逗号、换行、空值、大小写；未经用户选项不自动 trim/lowercase；坏行不能静默丢弃|
|CSV to JSON|`csv to json converter`、`csv to json array`、`csv to json online`|ConvertCSV 已丰富转换；Papa Parse demo也能转换|文件输入→对象数组预览→下载JSON，示例覆盖逗号/换行/前导零|Papa Parse 实际解析依赖；下载/对象映射为本项目代码|ID保留字符串；重复/空表头不能静默覆盖；不声称支持复杂嵌套JSON或所有Excel格式|

“本地、免费、开源”是首批基本条件，**不是独特卖点**。Squoosh 和 BentoPDF 已做到这些。本项目的差别需要从可核验样例、清晰结果、失败说明和可继续扩展的 TokRepo 能力路径做出来。没有证据，不声称比它们更快、更小、更准确。

## 每项两条独立真实问题及编辑含义

### 1. 合并 PDF

- [Merge PDF with PDF-LIB](https://stackoverflow.com/questions/65567732/merge-pdf-with-pdf-lib)：用户从硬编码示例改成自选两个本地文件后无法合并。页面不能只贴代码；真正接收文件并给下载结果才满足问题。
- [How to Merge Two PDF Files Using jsPDF?](https://stackoverflow.com/questions/60234692/how-to-merge-two-pdf-files-using-jspdf)：需求是两份或更多 PDF 变成一个并在浏览器查看。合并顺序和全部页保留是验证点。

标题建议：**Merge PDF files online — free, in your browser**。开头直接说选两份或多份PDF、确认顺序、下载；后面才解释依赖和更复杂批处理方案。不要写“PDF-LIB + AI + MCP Ultimate Workflow”。

### 2. 提取 PDF 页

- [Extract specific pages of PDF and save it with Python](https://stackoverflow.com/questions/51567750/extract-specific-pages-of-pdf-and-save-it-with-python)：用户指定起止页，却得到空文件或一页文件。范围端点及页码要用示例和输出计数讲清。
- [How do I separate pages in a PDF?](https://community.adobe.com/questions-9/how-do-i-separate-pages-in-a-pdf-1242074)：JoyceU问多页文件怎么拆开；后续另一人问多个不同页段。页面允许单页和离散页段，但不能声称暂未实现的逐页ZIP或批量自动拆分。

标题建议：**Extract pages from a PDF into a new PDF**。示例 `1,3-5` 代表4页，下载后用实际文件验收。

### 3. 压缩图片

- [How to compress an image via Javascript in the browser?](https://stackoverflow.com/questions/14672746/how-to-compress-an-image-via-javascript-in-the-browser)：用户要浏览器压图。工作文件本地处理、可下载文件是对应结果。
- [Downsizing image dimensions … leads to image size inflation in bytes](https://stackoverflow.com/questions/48632459/downsizing-image-dimensions-via-pure-js-leads-to-image-size-inflation-in-bytes)：减像素后字节反而变大。页面必须显示真实文件大小，不能把缩小像素直接包装成压缩成功。

标题建议：**Compress an image and see the new file size**。100KB是需求证据，不是未经实现的产品承诺；发布时按实际能力写。

### 4. 调整图片尺寸

- [How to proportionally resize an image in canvas?](https://stackoverflow.com/questions/14087483/how-to-proportionally-resize-an-image-in-canvas)：用户硬设宽高造成比例问题。锁比例及导出尺寸可直接解决。
- [Resize image with javascript canvas (smoothly)](https://stackoverflow.com/questions/19262141/resize-image-with-javascript-canvas-smoothly)：用户缩小后边缘效果不好。提供预览和真实样例；图片变小会丢失像素信息，不宣传“无损任意放大”。

标题建议：**Resize an image to exact dimensions**。正文讲宽高、比例、像素与KB差别。未实现留白/裁切模式就不把Instagram无裁切写成工具功能。

### 5. CSV 去重

- [How to remove duplicate rows of csv file using nodejs](https://stackoverflow.com/questions/68980588/how-to-remove-duplicate-rows-of-csv-file-using-nodejs)：存在不同列数及重复整行。不能按文本逗号直接split，坏行应报告。
- [Remove CSV rows with duplicate values](https://www.reddit.com/r/shortcuts/comments/1ger647/)：用户要按某一列的相同值删整行。指定键与全行匹配须明确区分，默认保留第一条。

标题建议：**Remove duplicate rows from a CSV**。示例可包含同一email的不同备注，说明选email会保留哪条、选整行会得到什么。不要假称Excel直接导入也支持。

### 6. CSV 转 JSON

- [Can not convert correctly formatted CSV to JSON](https://stackoverflow.com/questions/47638814/can-not-convert-correctly-formatted-csv-to-json)：用户把本地文件路径当CSV内容，输出错误。一个真正接收 File 并展示结果的工具可省去配置障碍。
- [JavaScript, Papaparse, return array of objects](https://stackoverflow.com/questions/59652049/javascript-papaparse-return-array-of-objects)：用户需要表头映射的对象数组，得到的却是数组数组。示例输出必须表明结果结构。

标题建议：**Convert CSV to JSON without uploading your file**。示例应包含ID `0017` 和被引用的逗号，证明其不会被擅自变成数字或两列。

## 经核验的首批 TokRepo 路径

|资产|现时公开路径|真实角色|
|---|---|---|
|pdf-lib，id5690|https://tokrepo.com/en/workflows/asset-51d0242d|浏览器PDF工具实际依赖|
|Papa Parse，id4980|https://tokrepo.com/en/workflows/papa-parse-fast-browser-csv-parser-javascript-ed9fd7fc|CSV解析实际依赖|
|Sharp，id2073|https://tokrepo.com/en/workflows/sharp-high-performance-image-processing-node-js-f5801cab|可选Node批量/服务端扩展，不声称首发使用|
|Jimp，id4054|https://tokrepo.com/en/workflows/jimp-pure-javascript-image-processing-node-js-0b52787e|可选可编程图片扩展，不声称首发使用|
|BentoPDF，id1805|https://tokrepo.com/en/workflows/bentopdf-privacy-first-self-hosted-pdf-toolkit-03c80967|若有更完整PDF需求，可选开源替代；不是首发依赖|

PDF.js也核验到可用资产，但首发没有渲染预览功能就不应说已集成。每页一个真实使用的资产连接足够；强塞第二个只是营销。图片页的浏览器Canvas是Web原生API，应诚实说明，再给批量扩展资产链接。

## 20候选池：首批6项加后续14项

下面14项的**直接Google联想已经核验**；但未达到首批的“两条独立问题+实际产物QA”门槛。因此全部标为后续候选，不能自动发布。资产“详情/公共页已核验”和“仅list存在”分开。

|后续任务|现场直接联想/需求变化|资产配对及核验层级|有用产物/阻止立即上线的缺口|
|---|---|---|---|
|Extract tables from PDF to Excel|`extract tables from pdf to excel`、`…python`|Docling id173 + pandas id1144，详情及公共页已核验|原表格→CSV+行列/缺失审核；OCR和跨页表格准确性不能未经测试保证|
|Compress video to a target size|`compress video for discord`、`compress video to 10mb`|FFmpeg id1157已核验；HandBrake id1718仅list|目标大小计算/样例对照；WASM性能与浏览器内存缺口，服务限制先官方查证|
|Add subtitles to video|`add subtitles to video free without watermark`|Whisper id105 + FFmpeg id1157已核验；VideoCaptioner id110仅list|字幕编辑、SRT+带字幕视频；真正语音推理、模型下载、导出需要运行证据|
|Transcribe audio to text|`transcribe audio to text free no sign up`|Whisper+FFmpeg已核验|本地音频→可编辑文本；不能用手填示例假称自动转录|
|Convert video to MP3|`convert video to mp3 file`、`…free`|FFmpeg已核验；LosslessCut id5110仅list|本地视频取音轨、播放/时长核对；编码/大文件资源限制未验证|
|Convert HEIC to JPG|`convert heic to jpg windows 11`、`…free`|ImageMagick id2348已核验；Sharp已核验|真实HEIC解码及方向/色彩样例；普通canvas不保证HEIC支持，不能改扩展名冒充转换|
|Compress PDF|`compress pdf on mac`、`compress pdf free`|BentoPDF+StirlingPDF id905已核验|字节变化及画质前后；不把合并或重保存误称压缩，签名/文字层风险未测试|
|PDF to Word|`pdf to word converter free no sign up`|ConvertX id1799仅list；Docling已核验但其并非直接Word保真转换承诺|可编辑DOCX与阅读顺序检查；当前资产链功能对应不足，暂不批准|
|Convert Markdown to PDF|`convert markdown to pdf pandoc`、`…command line`|Pandoc id2436 + Quarto id5213仅list|模板及带表格/代码示例PDF；浏览器与本地CLI模式须区分|
|Translate subtitles|`translate subtitles to english`、`translate subtitles srt`|VideoCaptioner id110、VideoLingo id6073仅list|保留时间轴的双语SRT；需要翻译模型/费用及质量验证，不宣传自动完美翻译|
|Resume builder / factual bullet editor|`resume builder free download`、`resume builder template`|ReactiveResume id866、Resume Bullet Editor id6922详情存在；公共页检查失败，原因未分类|可导出简历模板+真实事实约束；不得编学历/成绩，不把模板下载称完整builder|
|Batch rename files|`batch rename files windows 11`、`…mac`|Dry-Run File Rename Plan id6936详情存在；公共页检查失败|可审核重命名计划和冲突清单；网页下载命名不等于操作用户整个文件夹|
|Remove background from image|`remove background from image free`|SAM id2505仅list；rembg关键词list没找到记录|透明PNG+边缘检查；SAM记录不等于已实现一键去背景，模型/掩码编辑缺口|
|Summarize PDF for study|`summarize pdf for study`、`summarize pdf to notes`|Docling已核验；Ollama此前同日记录可用但此池未重新查细节|页码引用的学习笔记；不能用无引用随机摘要做产物，需模型或API配置与事实核查|

表中“已核验”仅指API详情和公开资产地址，不指软件质量、兼容性、许可证再分发许可或本项目运行通过。另五个公共资产页面探测失败无分类原因，不将它们称为TokRepo服务器故障；发布前再做定点核验。

## 竞争来源与质量门槛

- [BentoPDF Getting Started](https://www.bentopdf.com/docs/getting-started)：已有开源浏览器PDF处理。我们的PDF入口需至少同样真实可用，不能靠长文章遮住只有下载链接的页面。
- [Squoosh原项目](https://github.com/GoogleChromeLabs/squoosh)：已有本地压图和多格式。我们的单图版本不能宣传是全新、唯一隐私工具。
- [Canva Image Resizer](https://www.canva.com/features/image-resizer/)：已有普通用户尺寸工具；教程应用结果、比例和文件大小的具体区别。
- [ConvertCSV CSV to JSON](https://www.convertcsv.com/csv-to-json.htm)：已有完整转换入口。我们的优势只能从简单可核查默认规则、样例和开源实现建立。
- [Papa Parse官方文档](https://www.papaparse.com/docs)、[pdf-lib官方API](https://pdf-lib.js.org/docs/api/classes/pdfdocument)：验证实际接口；原问题中的代码不作为最新库用法依据。

发布门槛：直接搜索意图有证据；两条真问题且去重；有可使用的结果；清晰输入/输出/失败边界；样例实际验证；资产链接真实且关系不伪造。搜索量unknown不用凑数字。六个是本次六个结果，不是固定每天必须新造六个页面。没有新的结果意图或显著改善，就修正文档/工具，避免复制标题制造薄页。
