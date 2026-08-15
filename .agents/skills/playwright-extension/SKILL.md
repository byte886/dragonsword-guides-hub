---
name: playwright-extension
description: "通过 Playwright Extension 连接用户已打开的 Chrome/Edge 浏览器，实现可视化浏览器自动化。用户可实时观察页面操作。适用于需要登录态、用户想观察操作过程、或需要复用浏览器已有会话的场景。"
---

# Playwright Extension 浏览器自动化

通过 Playwright 官方的 Chrome Extension + `playwright-cli` 命令行工具，连接到用户**已经打开并登录好的 Chrome 浏览器**进行自动化操作。用户可以在自己的浏览器中实时看到所有页面变化。

## 前置条件

1. 用户已在 Chrome/Edge 中安装 **Playwright Extension**（Chrome Web Store 搜索 "Playwright Extension"）
2. 点击扩展图标，获取 `PLAYWRIGHT_MCP_EXTENSION_TOKEN`（token 可能会过期，需要用户刷新提供）
3. 本地有 Node.js 和 npx

## 核心概念

- **attach（附加）**：连接到用户已打开的浏览器，而不是启动新的浏览器实例
- **named session（命名会话）**：用 `-s=<name>` 创建持久会话，后续命令复用同一连接，**不会每次打开新窗口**
- **snapshot（快照）**：获取页面的 accessibility tree（YAML 格式），每个元素有 `ref`（如 `e15`），用 ref 来点击/输入
- **highlight（高亮）**：在页面上用虚线框标记元素，让用户看到要操作哪里

## 快速开始

```bash
# 1. 一次性附加到用户的 Chrome（创建名为 ga 的持久会话）
PLAYWRIGHT_MCP_EXTENSION_TOKEN=<token> npx playwright cli -s=ga attach --extension=chrome

# 2. 后续所有操作复用会话（不需要再传 token）
npx playwright cli -s=ga goto https://example.com
npx playwright cli -s=ga snapshot
npx playwright cli -s=ga click e15
npx playwright cli -s=ga type "hello"
npx playwright cli -s=ga fill e5 "user@example.com" --submit
npx playwright cli -s=ga press Enter
npx playwright cli -s=ga screenshot --filename=page.png

# 3. 操作完成后断开（浏览器保持打开）
npx playwright cli -s=ga detach
```

## 常用命令

### 导航
```bash
npx playwright cli -s=<session> goto <url>
npx playwright cli -s=<session> go-back
npx playwright cli -s=<session> reload
```

### 获取元素引用
```bash
npx playwright cli -s=<session> snapshot
npx playwright cli -s=<session> snapshot --filename=page.yml
npx playwright cli -s=<session> find "Sign in"
npx playwright cli -s=<session> find --regex "/sign (in|up)/i"
```

### 交互
```bash
npx playwright cli -s=<session> click <ref>
npx playwright cli -s=<session> fill <ref> "text"
npx playwright cli -s=<session> type "text"
npx playwright cli -s=<session> press Enter
npx playwright cli -s=<session> select <ref> "value"
npx playwright cli -s=<session> hover <ref>
npx playwright cli -s=<session> check <ref>
```

### 可视化辅助
```bash
npx playwright cli -s=<session> highlight <ref>
npx playwright cli -s=<session> highlight --hide
```

### 标签页
```bash
npx playwright cli -s=<session> tab-list
npx playwright cli -s=<session> tab-new [url]
npx playwright cli -s=<session> tab-select <index>
npx playwright cli -s=<session> tab-close [index]
```

### 截图
```bash
npx playwright cli -s=<session> screenshot --filename=shot.png
npx playwright cli -s=<session> screenshot --hires
```

### 等待
```bash
npx playwright cli -s=<session> wait-for "Welcome"
npx playwright cli -s=<session> wait-for 3000
```

### 执行 JS
```bash
npx playwright cli -s=<session> eval "document.title"
npx playwright cli -s=<session> eval "el => el.textContent" e5
```

### 会话管理
```bash
npx playwright cli list
npx playwright cli -s=<name> detach
npx playwright cli -s=<name> close
npx playwright cli kill-all
```

## 操作流程（每步确认模式）

1. **attach**：用 token 创建命名会话
2. **goto**：导航到目标页面
3. **snapshot/find**：获取页面结构，找到目标元素的 ref
4. **highlight**：高亮要操作的元素，告诉用户"下一步要点击 XXX"
5. **等用户确认**（如果用户要求每步确认）
6. **执行操作**：click/fill/type 等
7. **snapshot**：确认操作结果
8. 重复 3-7 直到完成
9. **detach**：断开连接

## 注意事项

- **token 会过期**：如果连接报 "Invalid token"，让用户点击扩展图标刷新 token
- **第一次连接**：Chrome 可能弹出标签页选择页面，设置了 token 后会自动跳过
- **snapshot 是主要的"看"方式**：它返回页面的 accessibility tree（YAML），比截图更精确，包含元素 ref
- **ref 是动态的**：每次页面变化后 ref 可能改变，操作前要重新 snapshot/find
- **不要每次都启动新进程**：用命名会话 `-s=<name>` 复用连接，避免反复打开 connect.html 页面
- **命令路径**：用 `npx playwright cli`（不是 `npx playwright-cli`，也不是 `npx @playwright/mcp`）
- **用户能看到页面变化**：导航、点击、输入都会在用户浏览器中实时发生，但看不到鼠标光标移动轨迹
- **macOS 上 daemon 会自动脱离**：attach 启动的后台 daemon 在 macOS 上会正确 `detach + unref`，Bash 命令会正常返回，不会卡住
- **禁止用 Python 脚本直连 MCP server**：之前用 Python subprocess 启动 `@playwright/mcp` 进程，那些进程不会自动退出，会占满 sandbox 池导致所有工具不可用。必须用 `npx playwright cli` 命令
- **SPA 页面导航**：Google Analytics 等单页应用直接 goto 子页面 URL（如 `#/admin`）可能被重定向到首页，需要用 `find` 找到导航按钮再 `click` 进入
- **attach 后当前页是 connect.html**：需要先 `goto` 目标 URL 才能操作
- **进程清理**：操作完成后执行 `npx playwright cli -s=<name> detach` 断开连接；如果会话异常用 `npx playwright cli kill-all` 强制清理
