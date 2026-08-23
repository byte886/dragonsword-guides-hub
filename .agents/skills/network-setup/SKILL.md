---
name: network-setup
description: "项目网络环境配置：ClashX 代理、GitHub SSH、飞书 API 连通性。遇到网络超时、DNS 解析失败、git push 失败时查阅。"
---

# 网络环境与代理配置

本项目运行在 macOS 上，ClashX 始终开启（HTTP 代理端口 7890）。

## 核心原则

1. **国内资源直连**：飞书 API（open.feishu.cn）、百度、国内镜像源不需要代理
2. **国外资源走代理**：GitHub、Google、GA/GSC、npm、Homebrew bottles
3. **先检测后决策**：连接失败时先测试直连和代理，再决定
4. **代理按需设置**：只在需要的命令前设置环境变量，不全局持久化

## 快速检测

```bash
# 直连测试
curl -s --connect-timeout 3 -o /dev/null -w "%{http_code}" https://www.baidu.com
# 代理测试
curl -s --connect-timeout 3 -x http://127.0.0.1:7890 -o /dev/null -w "%{http_code}" https://www.google.com
```

## 各场景代理配置

### GitHub（SSH 推送）

已配置 `~/.ssh/config`，通过 ssh.github.com:443 + ClashX 代理：

```
Host github.com
  HostName ssh.github.com
  Port 443
  User git
  IdentityFile ~/.ssh/id_rsa_softwawrecheng
  ProxyCommand nc -X connect -x 127.0.0.1:7890 %h %p
```

直接 `git push origin main` 即可，不需要额外设置环境变量。

### 飞书 API（lark-cli）

飞书是国内服务，默认直连。如果遇到 DNS 超时（`lookup www.doubao.com: i/o timeout`），设置代理后重试：

```bash
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890
lark-cli wiki +space-list --as user
```

### Playwright 连接 Chrome

不需要代理设置，连接的是本地 Chrome（127.0.0.1）。

### npm / npx

```bash
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890
npx playwright cli --version
```

### Google 搜索 / GA / GSC（通过 Playwright）

Chrome 浏览器本身走 ClashX 系统代理，不需要额外配置。

## 常见问题

| 症状 | 原因 | 解决 |
|------|------|------|
| git push 超时 / 22 端口失败 | SSH 22 被代理节点关闭 | 已配置 443 端口，确认 ~/.ssh/config 正确 |
| lark-cli 报 DNS 超时 | 终端 DNS 直连失败 | 设置 https_proxy 环境变量后重试 |
| npx playwright 下载慢 | npm 官方源慢 | 设置代理或切换 npmmirror 镜像 |
| ClashX 增强模式导致异常 | TUN 模式接管所有流量 | 在 ClashX 菜单中关闭增强模式 |
| sandbox 残留导致 Playwright 失败 | 未 detach 的会话 | playwright cli kill-all 或重启豆包 |

## 取消代理

```bash
unset https_proxy http_proxy all_proxy
```
