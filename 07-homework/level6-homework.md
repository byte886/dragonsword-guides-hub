# Level 6 Review: First Data Retrospective

## Data Review Table (Required Submission)

```
My site: https://ds-guides.wiki
GSC total impressions: 2,870
GSC total clicks: 135
Average CTR: 4.7%
Average position: 7.8
Period: 2026-08-13 to 2026-08-20 (8 days since launch on 2026-08-15)

New search queries that appeared:
1. dragonsword classes — 4 clicks / 11 impressions
2. 드래곤소드 어웨이크닝 전용 카르마 — 2 clicks / 25 impressions
3. dragonsword awakening classes — 2 clicks / 16 impressions
4. kalien team — 2 clicks / 6 impressions (CTR 33%)
5. dragonsword awakening roadmap — 1 click / 34 impressions
6. lute ornette sion — 1 click / 10 impressions
7. dragonsword awakening tier list — 1 click / 10 impressions
8. 드래곤소드 어웨이크닝 시련의 탑 — 1 click / 4 impressions
9. ドラゴンソード アウェイクニング 専用カルマ — 1 click / 4 impressions
10. 龙之剑觉醒wiki — 1 click / 4 impressions

Next step decision: Continue adding pages
Reason: 135 clicks and 2,870 impressions in 8 days, average position 7.8 (page 1 of Google).
Data is growing, multi-language traffic confirmed (KR/RU/JP/US/TW).
Specific actions:
1. Create Kalien character guide page (high CTR 33% on "kalien team")
2. Create Tower of Trials dedicated page (multi-language KR/CN/JP search demand)
3. Create Ornette & Sion character pages ("lute ornette sion" 10 impressions)
```

---

## 1. Task Summary

First GSC data review after launch. Check impressions, clicks, search queries, page performance; identify content gaps from real user search signals; plan 2-3 new pages; understand ad monetization paths (AdSense/Adsterra); decide next step.

---

## 2. Key Findings

### Core Metrics (8 days)

| Metric | Value | Benchmark |
|--------|-------|-----------|
| Total clicks | 135 | Strong for a new site |
| Total impressions | 2,870 | Growing |
| Average CTR | 4.7% | Normal for position 7-8 |
| Average position | 7.8 | Page 1 of Google |

### Top Pages by Clicks

| Page | Clicks | Impressions |
|------|--------|-------------|
| /en/classes.html | 11 | 78 |
| /ru/gear.html | 11 | 63 |
| /ko/karma.html | 7 | 132 |
| /en/best-team.html | 6 | 132 |
| /en/boss.html | 6 | 107 |
| /ko/gear.html | 6 | 66 |
| /en/raid.html | 5 | 152 |

### Geographic Distribution

| Country | Clicks | Impressions | CTR |
|---------|--------|-------------|-----|
| Russia | 35 | 226 | 15.5% |
| Korea | 32 | 525 | 6.1% |
| Japan | 16 | 131 | 12.2% |
| USA | 15 | 544 | 2.8% |
| Taiwan | 6 | 118 | 5.1% |

### Devices

- Desktop: 89 clicks (66%), 2,114 impressions
- Mobile: 46 clicks (34%), 740 impressions
- Tablet: 0 clicks, 14 impressions

### Indexing Status

- Indexed: 89 pages
- Not indexed: 43 pages
  - 11 redirects (expected: www -> apex, language redirects)
  - 1 alternate page with canonical (expected: en/index.html -> /)
  - 1 crawled - not indexed
  - 30 discovered - not indexed (Google still queuing, normal for new site)

---

## 3. Content Gap Analysis

### Pages that already exist (not gaps)

- `roadmap.html` exists in all 5 languages (25KB content). 34 impressions but only 1 click (2.9% CTR) — likely a ranking issue, not a content gap. Monitor and check position.
- `tier-list.html` exists in all 5 languages (25KB content). 10 impressions, 1 click — page is new, ranking may improve.

### Confirmed gaps (3 new pages planned)

1. **Kalien character guide** — "kalien team" has 33% CTR (2 clicks / 6 impressions). Kalien is a Stacker hero with fox clones, Burn/Stun mechanics. Currently only mentioned in best-team.html, no dedicated page.
2. **Tower of Trials (시련의 탑)** — Multiple Korean/Chinese/Japanese search variants (11+ total impressions). Content is buried in endgame.html; a dedicated page would concentrate ranking signals.
3. **Ornette & Sion character pages** — "lute ornette sion" has 10 impressions. Both are characters with team synergy with Lute but have no dedicated pages.

---

## 4. Ad Monetization Learning

### AdSense (Google)

- Google's ad system; place ad slots, Google auto-matches ads, earn per view/click
- Best to join after daily visits > 500 (earnings are very low before that)
- Requirements: enough content, privacy page, about page, contact page
- Approval: days to weeks (sometimes 1-2 months)
- Common rejection reasons: too little content, low quality, missing privacy page
- Payment: wire transfer (high fixed fee) or cryptocurrency (~2% fee)

### Adsterra

- Lower threshold, faster approval (1-3 minutes)
- Recommended for new sites: Native Banner or Banner format
- Avoid Popunder (too aggressive, hurts UX)
- Each ad unit gets a unique 32-char hex key
- Script can reference key via environment variable

### Recommended path

New site -> Adsterra first (quick start) -> daily visits > 1000 and AdSense approved -> switch to AdSense or use both (AdSense for main slots, Adsterra for secondary).

### Current status

Site has 135 clicks in 8 days but daily visits are likely still in the tens. Not ready for ads yet. Revisit after more content is added and traffic grows.

---

## 5. Key Learnings

### 1. GSC search queries are the most valuable signal

The tutorial says "search query report is the most important — you'll discover words you never thought of." This proved true immediately:

- "kalien team" — a specific character team composition we hadn't prioritized
- "시련의 탑" — Korean users searching for a game mode we had buried in endgame
- "lute ornette sion" — character synergy searches showing demand for individual character pages

These are not guesses — they are real user intents captured by Google.

### 2. CTR is a diagnostic, not a direct action item

CTR is influenced by ranking position (higher position naturally gets more clicks). A low CTR with high impressions (like roadmap: 2.9%) first requires checking the ranking position before optimizing titles. A high CTR (like kalien team: 33%) is a strong signal to double down on that topic.

### 3. Multi-language traffic is real and differentiated

- Russia has the highest CTR (15.5%) — Russian pages are performing well
- Korea has the most impressions (525) but lower CTR — Korean content may need optimization
- USA has 544 impressions but only 2.8% CTR — English titles/descriptions may need improvement for US search intent
- Japanese CTR is strong (12.2%) — Japanese content is resonating

### 4. "Discovered - not indexed" is normal for new sites

30 pages in this state is not an error. Google discovered them via sitemap but hasn't crawled/indexed them yet. This resolves naturally as the site gains authority. No action needed except continuing to add content and internal links.

### 5. The "continue or switch" decision should be data-driven, not emotional

The decision framework:
- Data growing, impressions + clicks, ranking on page 1 -> continue
- Impressions but no clicks after weeks, single-digit daily visits -> consider switching
- Traffic but content can't rank -> consider upgrading to tool site

Our data clearly supports "continue": 135 clicks, position 7.8, multi-language traffic, and clear content gap signals.

---

## 6. Next Actions

| Action | Priority | Status |
|--------|----------|--------|
| Create Kalien character guide (5 languages) | High | Planned |
| Create Tower of Trials guide (5 languages) | High | Planned |
| Create Ornette & Sion character pages (5 languages) | Medium | Planned |
| Monitor roadmap page ranking position | Medium | Next review (day 14) |
| Revisit Adsterra after traffic grows | Low | When daily visits > 100 |
| Day 14 GSC review | Scheduled | 2026-08-29 |

---

## 7. Screenshot

GSC performance report saved as `gsc-performance-level6.png`.
