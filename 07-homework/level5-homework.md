# 关卡5 学习复盘：网站部署上线

## 一、本关任务

1. 将网站部署到 Vercel
2. 购买域名 ds-guides.wiki（Spaceship），通过 Cloudflare 配置 DNS
3. 接入 Google Analytics 并验证数据
4. 接入 Google Search Console 并提交 sitemap
5. 电脑+手机访问验证，SEO 基础检查

---

## 二、最大收获

### 1. 理解了域名、DNS、部署平台三者的关系

之前对"网站上线"的理解是模糊的，通过本关实际操作，理清了三个平台各自的角色：

- **Spaceship（域名注册商）**：你"买"了 ds-guides.wiki 这个名字，但它只是个名字，不指向任何服务器
- **Cloudflare（DNS 管理）**：维护一张"电话簿"，告诉全世界 ds-guides.wiki 对应哪个 IP（A 记录）、www 对应哪个域名（CNAME 记录）
- **Vercel（托管平台）**：真正存放网站文件的服务器，当用户访问域名时，Vercel 返回 HTML 文件

三者配合的流程：用户输入 ds-guides.wiki → 查 Cloudflare DNS → 得到 Vercel 的 IP → 请求 Vercel → 返回网页。

**关键概念：nameserver（域名服务器）**
在 Spaceship 把 nameserver 改成 Cloudflare 的（celeste/thaddeus.ns.cloudflare.com），等于告诉全世界"关于这个域名的地址，请去问 Cloudflare"。这一步是 DNS 生效的前提。

### 2. 理解了 308 重定向和 canonical 的关系

本关遇到一个决策：apex 域名（ds-guides.wiki）和 www 域名（www.ds-guides.wiki），哪个做主域名？

- **308 Permanent Redirect**：告诉浏览器和搜索引擎"这个页面永久搬到另一个地址了"，权重会转移到目标地址
- **canonical 标签**：告诉搜索引擎"如果多个 URL 能访问同一内容，请以我声明的这个为准"

两者必须方向一致。最终选择 apex 做主域名（更短更好记），www 308 重定向到 apex，canonical 统一为 https://ds-guides.wiki/。

**踩坑**：22 个英文子页面的 canonical 缺少 /en/ 前缀，指向了不存在的 404 页面。通过 curl 检查发现并修复。教训：canonical 必须与实际 URL 完全一致，新增页面后要验证。

### 3. 学会了 GA 和 GSC 的分工

- **GA（Google Analytics）**：管"用户来了之后做了什么"——多少人访问、看了哪些页面、来自哪个国家、用什么设备
- **GSC（Google Search Console）**：管"Google 怎么看你的网站"——有没有收录、搜索展示了多少次、排第几名、有没有抓取错误

两者互补：GA 看用户行为，GSC 看搜索引擎视角。

**GA 验证方法**：安装代码后，打开 GA → Reports → Realtime，自己访问网站，能看到实时活跃用户就说明代码生效。

**GSC 验证方法**：选择"网域"（Domain）类型，通过 Cloudflare Domain Connect 一键授权，无需手动复制 TXT 记录。提交 sitemap 后状态从"无法抓取"变为"成功"，发现 115 个页面。

### 4. 理解了 Cloudflare 代理状态（橙色云 vs 灰色云）

- **橙色云（Proxied）**：流量经过 Cloudflare 服务器，Cloudflare 提供 CDN、DDoS 防护、SSL
- **灰色云（DNS only）**：DNS 只做解析，流量直接到 Vercel

本项目选择灰色云，因为 Vercel 已自带全球 CDN 和自动 SSL，橙色云会造成双重 CDN，可能引发重定向循环。以后需要防护时可随时开启。

### 5. 掌握了用 curl 做 SEO 基础检查

不需要浏览器插件，用命令行就能快速检查：

```bash
# 检查 title/description/canonical/viewport
curl -s https://ds-guides.wiki/ | grep -o '<title>[^<]*</title>'
curl -s https://ds-guides.wiki/ | grep -o '<meta name="description"[^>]*>'
curl -s https://ds-guides.wiki/ | grep -o '<link rel="canonical"[^>]*>'

# 检查重定向
curl -sI https://www.ds-guides.wiki | grep -i location

# 检查 robots.txt 和 sitemap
curl -sI https://ds-guides.wiki/robots.txt
curl -sI https://ds-guides.wiki/sitemap.xml
```

---

## 三、遇到的卡点及解决

### 卡点1：Playwright sandbox 池耗尽

**现象**：Playwright 命令报 SandboxPoolExhaustedError，所有 Bash 命令无法执行。

**原因**：之前的 Playwright 进程未正确 detach，残留进程占满 sandbox 池。

**解决**：`pkill -9 -f playwright` 清理残留进程，或重启豆包。后续操作完必须 detach。

### 卡点2：GA 账户命名混乱

**现象**：GA 中有 3 个旧账户（deweb.me、softwarecheng、www.s187.com），用网站名命名账户，不符合 GA 层级结构。

**解决**：清空所有旧账户，按正确层级重建：
- Account（账户）：byte886（个人/组织名）
- Property（媒体资源）：ds-guides.wiki（域名）
- Data Stream（数据流）：网站数据流

### 卡点3：GSC sitemap 提交失败

**现象**：第一次只填 `sitemap.xml`，报"站点地图地址无效"。

**原因**：Domain 资源类型需要完整 URL。

**解决**：改为 `https://www.ds-guides.wiki/sitemap.xml`，提交成功。

### 卡点4：Vercel 域名重定向方向

**现象**：Vercel 默认 apex 308 重定向到 www，但 canonical URL 不带 www，方向不一致。

**解决**：在 Vercel Domains 设置中手动调整：apex 设为 Production，www 设为 308 重定向到 apex。

---

## 四、部署架构总结

```
用户浏览器
    │
    ▼
ds-guides.wiki（Spaceship 注册）
    │ nameserver → Cloudflare
    ▼
Cloudflare DNS（灰色云，DNS only）
    │ A 记录 @ → 216.198.79.1
    │ CNAME www → df9ecd0750052516.vercel-dns-017.com
    ▼
Vercel（Hobby 免费计划）
    │ 项目：dragonsword-guides
    │ apex = Production（200）
    │ www → 308 → apex
    ▼
静态 HTML/CSS/JS（115 个页面，5 语言）
    │
    ├── js/analytics.js → GA（G-6XQCHB1YYV）
    └── sitemap.xml → GSC（sc-domain:ds-guides.wiki）
```

---

## 五、账号信息速查

| 平台 | 关键信息 |
|------|---------|
| 域名 | ds-guides.wiki（Spaceship，到期 2027-08-15） |
| Vercel | 团队 dragonsword-guides，项目 dragonsword-guides |
| Cloudflare | Account ID 62adf960343b448a7e52838e68808b21，Zone ID 96aa94883c28ef6b8c872d5c35f9841a |
| GA | Account byte886（404676857），Property ds-guides.wiki（549932655），G-6XQCHB1YYV |
| GSC | sc-domain:ds-guides.wiki，sitemap 已提交（115 URLs discovered） |
| GitHub | byte886/dragonsword-guides（代码）、byte886/dragonsword-guides-hub（完整项目） |
