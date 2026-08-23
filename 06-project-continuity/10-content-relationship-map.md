# Content Relationship Map

> When updating one page, check this map to see which other pages may need adjustment.
> Last updated: 2026-08-23 (Level 6 — added Kalien, Ornette, Sion, Tower of Trials)

## How to Use This Map

1. Find the page you're editing in the left column
2. Check "Links to this page" — these pages reference your page and may need updates if you change URLs, titles, or key facts
3. Check "This page links to" — if you remove or rename a section, verify these linked pages still make sense
4. All relationships exist across 5 languages (en/ko/ja/ru/zh) — changes must be applied to all language versions

---

## Character Pages

| Page | Links to this page (incoming) | This page links to (outgoing) |
|------|-------------------------------|-------------------------------|
| **characters.html** | All 129 pages (navbar/footer) | All 7 character pages |
| **lute.html** | 54 files: characters, tier-list, build, karma, all character sidebars | All characters, beginner-guide, best-team, tier-list, build, gear, karma, tower-of-trials |
| **theresia.html** | 54 files: characters, tier-list, build, karma, all character sidebars | All characters, beginner-guide, best-team, tier-list, build, gear, karma, recipes |
| **charlotte.html** | 44 files: characters, tier-list, build, all character sidebars | All characters, beginner-guide, best-team, tier-list, build, gear, karma, recipes |
| **reina.html** | 44 files: characters, tier-list, build, karma, all character sidebars | All characters, beginner-guide, best-team, tier-list, build, gear, karma, recipes |
| **kalien.html** (NEW) | 39 files: characters, best-team, tier-list, all character sidebars, tower-of-trials | All characters, best-team, tier-list, build, gear, karma, tower-of-trials |
| **ornette.html** (NEW) | 30 files: characters, best-team, tier-list, all character sidebars, tower-of-trials | All characters, best-team, tier-list, build, gear, karma, tower-of-trials |
| **sion.html** (NEW) | 30 files: characters, best-team, tier-list, all character sidebars, tower-of-trials | All characters, best-team, tier-list, build, gear, karma, tower-of-trials |

### Character Page Maintenance Rules

- **When adding a new character page**: Update ALL existing character pages' "Other Heroes" sidebar (5 languages each), update characters.html card to `<a>` link, add to sitemap
- **When updating a character's tier/rank**: Update tier-list.html, characters.html, and the character's own page (5 languages each)
- **When updating build/gear info**: Update the character page + build.html + gear.html if the info appears there
- **When updating team compositions**: Update best-team.html + all character pages that mention the team

## Game System Pages

| Page | Incoming links | Key outgoing links | Maintenance notes |
|------|---------------|-------------------|-------------------|
| **tower-of-trials.html** (NEW) | 20 files: endgame, kalien, ornette, sion (×5 langs) | endgame, kalien, ornette, sion, build, gear, karma, best-team | When tower mechanics/rewards change, update endgame.html too |
| **endgame.html** | 34 files | tower-of-trials, raid, boss, build, gear, karma | Tower of Trials section should stay in sync with tower-of-trials.html |
| **combat.html** | 129 files (global nav) | classes, build, gear, karma, boss, raid | Core combat mechanics reference |
| **gear.html** | 129 files (global nav) | build, combat, karma, boss, raid | Gear set names must match character pages |
| **karma.html** | 129 files (global nav) | build, combat, gear, classes, raid | Exclusive Karma names must match character pages |
| **classes.html** | 35 files | combat, build, gear, karma, endgame, raid | Hero Trait descriptions must match character pages |
| **build.html** | 129 files (global nav) | classes, combat, gear, karma, boss, raid | Build recommendations reference character pages |
| **boss.html** | 89 files | build, combat, gear, karma, raid | |
| **raid.html** | 94 files | boss, build, combat, endgame, gear, karma | |

## Getting Started Pages

| Page | Incoming links | Notes |
|------|---------------|-------|
| **beginner-guide.html** | 129 files (global nav) | Entry point for new visitors |
| **tier-list.html** | 129 files (global nav) | Tier rankings must match character pages |
| **best-team.html** | 129 files (global nav) | Team comps must match character pages |
| **map.html** | 129 files (global nav) | |

## Other Pages

| Page | Incoming links | Notes |
|------|---------------|-------|
| **roadmap.html** | 129 files (global nav/footer) | Update when new content drops |
| **recipes.html** | 109 files | |
| **review.html** | 109 files | |
| **coop.html** | 89 files | |
| **faq.html** | 0 (orphaned) | Needs incoming links or should be removed |

## Global Elements (appear on every page)

When these change, update ALL 135 HTML files across 5 languages:

| Element | Location | What to update |
|---------|----------|---------------|
| Navbar | `<nav class="navbar">` | Navigation links, Steam CTA |
| Footer | `<footer class="footer">` | Footer links, copyright year, disclaimer |
| GA code | `js/analytics.js` | Single file — no HTML changes needed |
| CSS | `css/style.css` | Single file — cache-bust with `?v=N` |
| JS | `js/main.js` | Single file — cache-bust with `?v=N` |
| Sitemap | `sitemap.xml` | Add new pages, update lastmod |
| robots.txt | `robots.txt` | Sitemap reference |

## Content Update Checklist

When adding or modifying content:

1. [ ] Identify all affected pages using this map
2. [ ] Make changes in English first (`en/`)
3. [ ] Apply same changes to ko/ja/ru/zh versions
4. [ ] Update internal links (sidebar "Other Heroes", related guides)
5. [ ] Update sitemap.xml if pages added/removed
6. [ ] Run validation: `python3 scripts/validate-pages.py`
7. [ ] Commit with descriptive message
8. [ ] Push to GitHub (Vercel auto-deploys)
9. [ ] Verify on live site after deployment
10. [ ] Request indexing in GSC for new pages
