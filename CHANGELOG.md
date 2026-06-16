# 修改记录

本文件用于记录本仓库中较重要的文字、LaTeX 类文件和公式格式修改。后续修改时，请在最新日期下追加条目，尽量写清楚修改动机、涉及文件和验证方式。

## 2026-06-12

### README 读者定位调整

- 调整 `README.md` 中对本书读者对象的表述，保持“计算机专业学生”的限定，但是不强调低年级本科生。
- 已将该 README 修改提交并推送到远端仓库。

### `thinking`、`property` 环境增加计数器

- 修改 `elegantbook.cls`，为 `thinking` 和 `property` 增加按章重置的计数器。
- 将两个环境改为 `\NewDocumentEnvironment{...}{g}`，兼容已有写法，如 `\begin{property}{...}`。
- 在环境内部使用 `\refstepcounter`，使 `\label` 能正确引用到“思考”或“性质”本身。
- 为 `cleveref` 增加 `thinking`、`property` 的中文引用名称。

### `remark` 环境增加计数器

- 统计正文中 `remark` 使用较多，且已有 `rem:` 标签，因此修改 `elegantbook.cls` 为 `remark` 增加按章重置的计数器。
- 将 `remark` 改为支持可选标题参数的编号环境。
- 为 `cleveref` 增加 `remark` 的中文引用名称。

### 将 `eqnarray*` 改为 `align*`

- 将当前目录 `.tex` 文档中的所有 `eqnarray*` 公式环境改为 `align*`。
- 同步整理常见旧式对齐写法：
  - `&=&` 改为 `&=`
  - `&\equiv&` 改为 `&\equiv`
  - `&\mapsto&` 改为 `&\mapsto`
- 对矩阵展示、同余式、等式链等缺少对齐点的公式补充必要的 `&`。
- 保留未带星号的 `eqnarray`，本次只处理 `eqnarray*`。

### `mcs-07-rings-fields` 关系总结页

- 修改 `Slides/mcs-07-rings-fields.tex`，在课程结束页前增加极大理想、素理想、域与整环之间的关系图表。
- 用等价关系和蕴含链串联：
  - `M` 极大当且仅当 `R/M` 是域。
  - `M` 素当且仅当 `R/M` 是整环。
  - 域一定是整环，因此交换环中极大理想必为素理想。
- 将总结链中的长箭头改为普通箭头，避免 `\Longrightarrow` 在 PDF 渲染时出现接缝。

### `01-integers` 习题区 `\mbox` 清理

- 修改 `sessions/01-integers.tex` 的 `problemset` 部分，去除不规范的 `\mbox{...}` 用法。
- 程序语言名改为正文写法，如 `C`、`Python`。
- 函数名和布尔返回值改为 `\texttt{...}`，如 `\texttt{is\_even}`、`\texttt{True}`。
- 数学集合名 `GF` 改为 `\mathrm{GF}`；数学函数调用改为 `\operatorname{GF\_mul}(x, \cdot)`。

### `01-integers` 公式代码整理

- 修改 `sessions/01-integers.tex` 中的二进制和十六进制字面量，将 `\text{0b}`、`\text{0x}` 改为 `\mathtt{...}`。
- 将二进制累加示例中的 `flalign*` 和手写 `\quad` 对齐改为 `array` 对齐。
- 将递归乘法公式由 `\left\{...\begin{array}` 改为 `cases` 环境。
- 将映射写法 `\phi: A \mapsto B` 改为 `\phi\colon A \to B`。
- 统一大 O 记号为 `\mathcal{O}(\cdot)`，并将 `\not =` 改为 `\ne`。
- 将 C 风格移位和按位与符号放入 `\text{\ttfamily ...}`，避免裸符号在数学模式中产生不合适的间距。

### 验证

- 使用 `latexmk -pdfxe -interaction=nonstopmode -halt-on-error -outdir=/tmp/cinta-latex-check CINTA-cn.tex` 验证主文档可编译。
- 使用 `rg --no-ignore --hidden -F "eqnarray*" --glob "*.tex"` 确认无 `eqnarray*` 残留。
- 使用 `git diff --check` 检查空白问题。
- 使用 `xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/cinta-slides-check Slides/mcs-07-rings-fields.tex` 验证环与域幻灯片可编译。
- 使用 `rg -n -F "\\mbox" sessions/01-integers.tex` 确认 `01-integers` 中无 `\mbox` 残留。

## 2026-06-13
对sessions中所有latex文档进行以下修改
### 修改latex表达的规范
- 修改不规范的\mbox{...}用法。
- 程序语言名改为正文写法，如 `C`、`Python`。
- 函数名和布尔返回值改为 `\texttt{...}`，如 `\texttt{is\_even}`、`\texttt{True}`。
- 数学集合名 `GF` 改为 `\mathrm{GF}`；数学函数调用改为 `\operatorname{GF\_mul}(x, \cdot)`。类似的数学集合与数学函数调用也相应修改。

### 将 `eqnarray*` 改为 `align*`
- 将当前sessions子目录中 `.tex` 文档中的所有 `eqnarray*` 和`eqnarray`公式环境改为 `align*`和`align`。
- 同步整理常见旧式对齐写法：
  - `&=&` 改为 `&=`
  - `&\equiv&` 改为 `&\equiv`
  - `&\mapsto&` 改为 `&\mapsto`
- 对矩阵展示、同余式、等式链等缺少对齐点的公式补充必要的 `&`。

### 术语英文标注、索引表、术语表和中英混排原则

- 英文术语是否大写，由术语本身的英文规则决定，不由其出现位置决定；正文括注、索引表和术语表应保持同一写法。
- 正文中标注英文术语时，统一使用中文术语后接括号英文的形式，如 `最大公因数（greatest common divisor）`。
- 索引表和术语表中也使用普通英文短语写法，如 `最大公因数 greatest common divisor, gcd`，不因列入表格而改成标题式大小写。
- 中英混排时，拉丁字母、英文单词、英文缩写与相邻中文之间留一个半角空格，如 `C 语言`、`Python 程序`、`RSA 密码系统`、`LaTeX 文档`；中文标点与相邻内容之间不额外加空格。
- 普通数学术语的英文标注使用小写短语，不采用标题式首字母大写，如 `prime number`、`modular inverse`、`greatest common divisor`。
- 专有名词、人名、地名、专有形容词和固定缩写按英语本身规则大写，如 `Euclidean algorithm`、`Bézout's identity`、`Fermat's little theorem`、`Chinese remainder theorem`、`RSA cryptosystem`。
- `gcd`、`lcm` 等常见数学缩写可保持小写；`RSA`、`AES` 等标准大写缩写保持大写。
- 章节标题、小节标题可按标题自身风格处理；正文括注、索引表和术语表中的英文术语以自然英文写法为准。

### 实施记录

- 已清理 `sessions` 子目录中 `.tex` 文档的 `\mbox{...}` 用法。
- 已将 `sessions` 子目录中的 `eqnarray` 环境改为 `align` 环境，并整理旧式对齐点。
- 已确认 `sessions` 子目录中无 `\mbox{...}`、`eqnarray`、`&=&`、`&\equiv&`、`&\mapsto&` 残留。
- 已使用 `latexmk -pdfxe -interaction=nonstopmode -halt-on-error -outdir=/tmp/cinta-latex-check CINTA-cn.tex` 验证主文档可编译。

### 引用之前的空格
- 统一对所有的的引用都改成 ~\ref 这种格式。
- 正文中 \cite{...} 与前面的中文词语之间使用不可断空格 ~；若前面是中文标点或左括号，则不额外加空格。例如：相关背景可参考如下文献：\cite{Ros11ENTA} 。

## 2026-06-14

### mod 运算的改写 (To do)
- 直观图需要改；
- 增加一些新的表述。
- 不一定在第二章改，再思考思考。

### 02-gcd.tex push 到了远端

### 尝试mod运算直观的作图
- codex先给出矢量图
- codex改写为卡通图
- 尚未完成. Todo tomorrow.

## 2026-06-15

### mod与同余的直观改写
- 完成改写。提交03-congruence.tex到远端
- 作图完成，增加mod-congruence-buckets.png，并已经引入正文
- 所有\bmod{x}都已经改写为\bmod x

## 2026-06-16

### 分离本项目对 `elegantbook.cls` 的本地修改

- 将当前使用的 `elegantbook.cls` 替换为新下载的上游版本 `elegantbook-origin.cls`，并确认两个文件内容一致，便于以后继续跟进 ElegantBook 的更新版本。
- 新增 `cinta.sty`，用于保存本项目自己的扩展，不再把这些内容直接写入上游 class 文件。
- `CINTA-cn.tex` 只做最小改动：
  - `\documentclass` 增加 `nofont` 选项；
  - 增加 `\usepackage{cinta}`。

### 已移入 `cinta.sty` 的项目扩展

- 保留并独立定义 `thinking` 环境，按章编号，并支持原有正文中的无标题写法。
- 保留编号版 `property` 环境，继续使用 `property` 计数器，避免改变旧的 `\label` 和 `cleveref` 语义。
- 保留编号版 `remark` 环境，继续使用 `remark` 计数器，并兼容正文中带标题的写法。
- 补回 `conjecture` 定理环境，兼容正文中的 `\begin{conjecture}{标题}{label}` 写法。
- 将 `CINTA-cn.tex` 中的通用导言区配置迁入 `cinta.sty`，包括 `tikz-cd`、`diagbox`、`makeidx`、`array`、`cleveref`、目录深度、`\ccr` 和 `\lcm`、`\egcd`、`\Ker`。
- 把旧 class 中的数学简写 `\Q`、`\Z`、`\F`、`\N`、`\R`、`\qed` 移入独立扩展包。
- 把旧 class 中的 listings 配置移入独立扩展包，保留“算法”标题、Python 风格、行号和边框设置。
- 把旧 class 中对 `polynom` 多项式长除法的补丁移入独立扩展包。
- 由于新版 ElegantBook 改用 `biblatex`，在扩展包中加入 `\addbibresource{reference.bib}`，并兼容正文末尾旧的 `\bibliography{reference}` 写法。
- 使用 Fandol 字体设置配合 `nofont` 选项，避免新版 class 默认查找本机不存在的中文字体。

### 检查到的额外兼容问题

- 新版 `elegantbook.cls` 中已经不再内置旧项目添加的 `conjecture` 环境，因此需要在扩展包中补回。
- 新版 class 的 `\elegantnewtheorem` 会重定义 `\conjecturename`，直接传入 `\conjecturename` 会形成自引用；已改为先保存标题宏再创建 `conjecture`。
- 新版 class 改用 `biblatex` 后，正文中的 `\bibliography{reference}` 会被判定为只能在导言区使用；已通过较晚的 `begindocument/end` hook 将其转为 `\printbibliography`。

### 验证

- 使用最小烟测文档分别验证 `thinking`、`property`、`remark`、`conjecture`、listings 和旧式 `\bibliography{reference}` 兼容入口。
- 使用 `latexmk -pdfxe -interaction=nonstopmode -halt-on-error -g -outdir=/tmp/cinta-class-check-final CINTA-cn.tex` 验证主文档完整编译成功。
- 编译生成 `/tmp/cinta-class-check-final/CINTA-cn.pdf`，日志中未发现致命错误、未定义引用或需要继续重跑的警告；仅剩 overfull/underfull hbox 和 JPEG 分辨率提示等排版警告。
