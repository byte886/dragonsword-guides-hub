# 关卡4 学习复盘：SEO检查与代码上传

## 一、本关任务

1. 用 AITDK 插件检查网站 SEO：title、description、H1/H2 层级
2. 将网站代码上传到 GitHub

---

## 二、最大收获

### 1. 理解了 SEO 的核心检查维度

通过 AITDK 插件，第一次系统地了解了一个页面需要检查哪些 SEO 要素：

- **Title（标题）**：建议 ≤60 字符，是搜索引擎结果中显示的标题，也是浏览器标签页文字
- **Description（描述）**：建议 ≤160 字符，是搜索引擎结果中标题下方的摘要文字
- **Keywords（关键词）**：虽然现代搜索引擎权重降低，但仍需填写
- **Heading 层级**：H1 → H2 → H3 → H4 必须逐级递进，不能跳级（如 H1 直接到 H3）

AITDK 的两个核心面板：
- **Overview**：检查 title、description、keywords 的长度和内容
- **Headings**：检查 H1-H4 的数量和层级结构

### 2. 理解了多语言网站的 SEO 特殊要求

本项目是 5 种语言（英/中/韩/俄/日）的多语言网站，学到了多语言 SEO 的三个关键要素：

**（1）hreflang 标签**

每个页面的 `<head>` 中需要声明所有语言版本的 URL：
```html
<link rel="alternate" hreflang="en" href=".../en/review.html">
<link rel="alternate" hreflang="zh" href=".../zh/review.html">
<link rel="alternate" hreflang="ko" href=".../ko/review.html">
```
作用：告诉搜索引擎这个页面有其他语言版本，根据用户的语言和地区展示对应版本。

**（2）sitemap.xml**

列出网站所有页面的 URL，帮助搜索引擎爬虫发现和抓取所有页面。多语言网站的 sitemap 需要包含所有语言版本的页面。

**（3）robots.txt**

规定搜索引擎哪些页面可以抓取、哪些不可以。

### 3. 理解了语义化 HTML 的重要性

- 每个页面有且仅有一个 `<h1>`（页面主标题）
- `<h2>` 是大章节标题，`<h3>` 是子章节，`<h4>` 是更细的分类
- 正确的标题层级不仅利于 SEO，也利于屏幕阅读器等无障碍工具

抽查 `en/review.html` 的结果：H1=1、H2=7、H3=15、H4=3，层级递进正常。

### 4. 掌握了 GitHub 代码上传的完整流程

从本地代码到 GitHub 仓库的完整步骤：
1. `git init` 初始化本地仓库（项目已有）
2. 创建 `.gitignore` 排除不需要上传的文件（备份目录、.DS_Store 等）
3. `git add .` 暂存所有文件
4. `git commit -m "说明"` 提交到本地
5. 在 GitHub 创建空仓库（不初始化 README）
6. `git remote add origin 仓库地址` 关联远程仓库
7. `git push -u origin main` 推送到 GitHub

### 5. 理解了 .gitignore 的作用

不是所有文件都需要上传到 GitHub。本项目的 `.gitignore` 排除了：
- `_backup_root_pages/`：备份目录，不需要版本管理
- `.DS_Store`：macOS 系统自动生成的文件
- 编辑器临时文件

---

## 三、遇到的卡点与解决方案

### 卡点 1：创建 GitHub 仓库时不能初始化 README

**现象**：如果创建仓库时勾选了 "Add README"，推送本地代码时会报错冲突。

**原因**：本地已有完整的 git 历史和代码，远程仓库如果有初始化的 README 文件，两边的 commit 历史不一致，无法直接推送。

**解决**：创建仓库时保持 "Add README" 为 Off，创建完全空的仓库，推送本地代码后，再通过本地 `git add README.md` 的方式添加 README。

**学到的原则**：当本地已有代码时，远程仓库必须是空的，不能有任何初始化文件。

---

### 卡点 2：批量验证 115 个页面的 SEO 完整性

**现象**：项目有 115 个 HTML 页面，人工逐个用 AITDK 检查效率太低。

**解决**：用脚本批量检查每个页面是否包含 `<title>`、`<meta name="description">` 和 `<h1>` 标签，确保没有遗漏。抽查几个典型页面（如 review 页）用 AITDK 详细检查 heading 层级和字符长度。

**学到的思路**：批量检查用脚本保证覆盖率，抽样检查用工具保证质量。

---

### 卡点 3：理解 AITDK 中 Keywords 超过 100 字符的提示

**现象**：AITDK Overview 中 keywords 显示 111/100，超过了建议值。

**理解**：keywords 的建议长度是 100 字符，但这只是建议，不是硬性要求。现代搜索引擎对 keywords 的权重已经很低，超过一点不会有实质影响。title 和 description 才是最重要的。

---

## 四、最终成果

- ✅ 115 个页面全部包含 title、description、H1
- ✅ 抽查页面 H1-H4 层级正确，无跳级
- ✅ 多语言 hreflang 标签配置完整
- ✅ sitemap.xml 和 robots.txt 已配置
- ✅ 代码成功上传到 GitHub，包含 README 和 .gitignore

---

## 五、关键知识点总结

| 知识点 | 要点 |
|--------|------|
| Title | ≤60字符，每个页面唯一，包含核心关键词 |
| Description | ≤160字符，概括页面内容，吸引点击 |
| H1 | 每个页面仅一个，是页面主标题 |
| H2-H4 | 逐级递进，不能跳级，用于内容分块 |
| hreflang | 多语言网站必备，声明各语言版本URL |
| sitemap.xml | 列出所有页面，帮助爬虫发现 |
| robots.txt | 控制搜索引擎抓取范围 |
| .gitignore | 排除不需要版本管理的文件 |
| 空仓库推送 | 本地有代码时，远程仓库必须为空 |
