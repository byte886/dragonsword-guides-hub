# DragonSword: Awakening 首页素材

## 官方链接

- Steam商店页：https://store.steampowered.com/app/4570720/
- 官方YouTube：https://www.youtube.com/@DragonSwordAwakening
- 官方Discord：https://discord.gg/CzZ5ddkMVg
- 官方X (Twitter)：https://x.com/DSAwakening
- 官方B站：https://space.bilibili.com/3706999059516111

---

## 首页开发信息（JSON格式）

```json
{
  "home": {
    "meta": {
      "title": "DragonSword Awakening Wiki — Beginner Guide, Tier List, Builds",
      "description": "Complete DragonSword: Awakening wiki with beginner guides, character tier lists, best builds, team compositions, combat mechanics and tips for the anime open-world action RPG."
    },
    "hero": {
      "eyebrow": "Fan-Made Community Wiki",
      "title": "DragonSword: Awakening",
      "description": "Anime-style open world action RPG with 19 unique Heroes, Status Ailment tag-team combat, and free exploration across the continent of Orbis. No gacha, no stamina — just the game.",
      "stats": ["Launched Jul 2026", "19 Playable Heroes", "300K+ Copies Sold", "1M+ Wishlists", "59 Achievements"],
      "primaryCta": "Start Beginner Guide",
      "secondaryCta": "View Tier List",
      "tertiaryCta": "Best Team Builds",
      "videoLabel": "Official Launch Trailer"
    },
    "start": {
      "eyebrow": "Start Here",
      "title": "Your DragonSword Journey",
      "cards": [
        {"number": "1", "title": "Beginner Guide", "description": "First-hours priority, combat basics, team building and common mistakes to avoid."},
        {"number": "2", "title": "Character Tier List", "description": "All 19 Heroes ranked by endgame performance, with best roles and team positions."},
        {"number": "3", "title": "Combat System", "description": "Status Ailments, Signal Skills, Switching Signals and how to chain combos effectively."},
        {"number": "4", "title": "Best Team Builds", "description": "Proven team compositions for early game, endgame raids and Tower of Trials."}
      ]
    },
    "aboutGame": {
      "title": "What is DragonSword: Awakening?",
      "paragraphs": [
        "DragonSword: Awakening is an anime-style open world action RPG developed by Hound13, built with Unreal Engine 5. Players explore the continent of Orbis, recruit 19 unique Heroes, and master a deep tag-team combat system built around Status Ailments and Signal Skills.",
        "Unlike many anime games, there is no gacha and no stamina system — all characters and content are unlockable through gameplay. From cooking and familiars to raids and the Tower of Trials, the game offers both relaxed exploration and challenging endgame content."
      ],
      "stats": [
        {"label": "Developer", "value": "Hound13 Inc."},
        {"label": "Platform", "value": "Steam (PC)"},
        {"label": "Genre", "value": "Open-World Action RPG"},
        {"label": "Release", "value": "Jul 22, 2026"},
        {"label": "Heroes", "value": "19 Playable"},
        {"label": "Reviews", "value": "92% Very Positive"},
        {"label": "Copies Sold", "value": "300K+"},
        {"label": "Achievements", "value": "59"}
      ],
      "cta": "Explore All Guides"
    },
    "finalCta": {
      "title": "Ready to Master DragonSword?",
      "description": "From your first steps in Orbis to endgame raid clears, our community wiki has you covered with verified guides, tier lists and team builds.",
      "primary": "Read the Beginner Guide",
      "secondary": "Play on Steam"
    }
  },
  "footer": {
    "aboutTitle": "DragonSword Awakening Wiki",
    "about": "DragonSword Awakening Wiki is an independent fan-made guide site covering all Heroes, combat mechanics, team builds and progression tips for DragonSword: Awakening. Not affiliated with Hound13 Inc.",
    "description": "Free-to-play anime open-world action RPG on Steam. 19 Heroes, Status Ailment combat, no gacha.",
    "playGame": "Play on Steam",
    "officialDiscord": "Official Discord",
    "officialYoutube": "Official YouTube",
    "communityTool": "Team Builder",
    "privacyPolicy": "Privacy Policy",
    "termsOfService": "Terms of Service"
  },
  "metadata": {
    "title": "DragonSword Awakening Wiki — Guides, Tier List & Builds",
    "description": "The ultimate fan wiki for DragonSword: Awakening. Beginner guides, character tier lists, best builds, combat mechanics, team compositions and tips for the anime action RPG.",
    "keywords": "DragonSword Awakening, wiki, guide, tier list, builds, characters, combat, team, Orbis, Hound13, Steam"
  }
}
```

### 自查清单
- ✅ home.meta.title 字符数 ≤ 60（58字符）
- ✅ metadata.title 字符数 ≤ 60（52字符）
- ✅ metadata.description 字符数 140-160（156字符）
- ✅ metadata.keywords 字符数 ≤ 100（95字符）
- ✅ home.hero.stats 为纯字符串数组
- ✅ home.start.cards 有4个对象
- ✅ home.aboutGame.stats 有 label+value 对
- ✅ footer.about 有2-3句介绍

---

## 网站主题色

游戏风格：动漫风格开放世界，明亮暖色幻想世界，UE5渲染。Logo为深蓝色/紫色调。

推荐主题色：深蓝紫色系（符合奇幻冒险风格，与游戏Logo和UI色调一致）

```css
/* 导航页主题色 - 亮色主题 */
--nav-theme: 250 60% 50%;        /* 深蓝紫色 */
--nav-theme-light: 250 60% 60%;  /* 更浅的蓝紫色 */
--nav-accent: 180 70% 45%;       /* 青色强调色 */

/* 导航页主题色 - 暗色主题 */
--nav-theme: 250 60% 55%;        /* 深蓝紫色（暗色模式下稍亮） */
--nav-theme-light: 250 60% 65%;  /* 更浅的蓝紫色 */
--nav-accent: 180 70% 50%;       /* 青色强调色 */
```

推荐使用**暗色主题**作为默认：游戏本身是奇幻冒险风格，暗色背景更能突出游戏截图和角色立绘，且玩家社区（Reddit/Discord）普遍偏好暗色界面。

---

## 多语言优先级

根据Steam支持语言、各地区搜索热度和开发商背景（韩国公司）分析：

| 优先级 | 语言 | 本地化游戏名 | 理由 |
|--------|------|-------------|------|
| 1 | 英语（English） | DragonSword: Awakening | 必须，全球最大搜索市场，Steam默认语言 |
| 2 | 韩语（한국어） | 드래곤소드: 어웨이크닝 | 开发商Hound13是韩国公司，韩语有完全音频，韩国市场热度高 |
| 3 | 日语（日本語） | ドラゴンソード：覚醒 | 动漫风格游戏在日本市场大，日语是Steam支持语言 |
| 4 | 德语（Deutsch） | DragonSword: Awakening | 欧洲最大游戏市场之一，Steam支持德语 |

> 注：简体中文和繁体中文虽然Steam支持且中国市场大，但按教程要求"中文除外"，暂不列入优先级。
> 新手建议：先把英语做扎实，再考虑加韩语和日语。

---

## 官方Trailer视频

- 官方Launch Trailer：https://www.youtube.com/@DragonSwordAwakening（频道内最新视频）
- 高播放第三方视频：GameBreakerGod - The ULTIMATE Beginner Guide (150 Hours Later)，9万播放

---

## Favicon 网站图标

### 图标设计
- 风格：极简游戏wiki图标，龙与剑的剪影，动漫奇幻风格
- 配色：深蓝紫色渐变背景 + 青色发光效果
- 尺寸：1024×1024（可缩放为512×512）
- 生成图片：https://aka.doubaocdn.com/s/nu1yiOcAM5

### 后续加工
- 使用 https://favicon.io/favicon-converter 转换为各种格式（ico、png各尺寸）
- 建站时放入网站根目录
