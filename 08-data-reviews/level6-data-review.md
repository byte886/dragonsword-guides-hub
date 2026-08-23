# Level 6 Data Review: GA + GSC Analysis

> Period: Aug 15-22, 2026 (first 8 days since launch)
> Date reviewed: Aug 23, 2026
> Tools: Google Analytics (G-6XQCHB1YYV), Google Search Console (sc-domain:ds-guides.wiki)

---

## 1. Executive Summary

The site gained **305 users** and **135 search clicks** in its first 8 days. Organic search already accounts for 50% of traffic, confirming SEO is working. However, **49% of users leave without engaging** and the homepage averages only 11 seconds. Korean and Russian users show the strongest engagement; US traffic is high-volume but low-quality (likely bots/casual).

**Grade: B-** — Solid start for SEO, but engagement and content depth need improvement.

---

## 2. GA Metrics

### 2.1 Traffic Acquisition

| Channel | Users | Share |
|---------|-------|-------|
| Organic Search | 153 | 50.2% |
| Direct | 152 | 49.8% |
| Referral | 0 | 0% |
| Social | 0 | 0% |

**Insight**: 50% organic in 8 days is strong. Zero referral/social means no backlink or social promotion yet — this is the biggest growth lever.

### 2.2 Top Pages

| # | Page | Views | Users | Avg Time | Notes |
|---|------|-------|-------|----------|-------|
| 1 | / (homepage) | 101 | 90 | 11s | High traffic, low engagement |
| 2 | /en/classes.html | 21 | 17 | 10s | Matches GSC top query |
| 3 | /ko/gear.html | 20 | 8 | 1m34s | Deep engagement (2.5 pages/user) |
| 4 | /en/characters.html | 18 | 15 | 15s | |
| 5 | /ru/build.html | 16 | 7 | 12s | |
| 6 | /zh/characters.html | 13 | 12 | 3s | Very high bounce |
| 7 | /en/build.html | 12 | 8 | 22s | |
| 8 | /ru/gear.html | 12 | 7 | 39s | |
| 9 | /ko/build.html | 11 | 4 | 2m | Highest engagement |
| 10 | /en/best-team.html | 10 | 6 | 1m05s | |

### 2.3 Countries

| # | Country | Users | Share | Engagement Rate | Avg Time |
|---|---------|-------|-------|-----------------|----------|
| 1 | United States | 115 | 38.1% | 13.45% | 9s |
| 2 | South Korea | 32 | 10.6% | 65.91% | 1m50s |
| 3 | Russia | 25 | 8.3% | 33.33% | 1m16s |
| 4 | Japan | 21 | 7.0% | 48.57% | 1m31s |
| 5 | China | 11 | 3.6% | 50.00% | 1m30s |
| 6 | United Kingdom | 10 | 3.3% | — | — |

**Key finding**: US traffic is 38% of users but only 13% engage and stay 9 seconds. This pattern (high volume, low engagement, short duration) suggests a significant portion may be bot traffic or accidental clicks. Korean users are the highest-quality segment by far.

### 2.4 Devices & Browsers

| Device (GSC) | Clicks | Share |
|--------------|--------|-------|
| Desktop | 89 | 65.9% |
| Mobile | 46 | 34.1% |
| Tablet | 0 | 0% |

| Browser (GA) | Users | Share |
|-------------|-------|-------|
| Chrome | 209 | 69.2% |
| Edge | 34 | 11.3% |
| Safari | 30 | 9.9% |

**Insight**: Desktop dominates (66%), but mobile is 34% — mobile experience must remain solid.

### 2.5 Events

| Event | Count | Users | User % |
|-------|-------|-------|--------|
| page_view | 497 | 302 | 100% |
| session_start | 382 | 301 | 99.7% |
| first_visit | 305 | 301 | 99.7% |
| user_engagement | 298 | 155 | 51.3% |
| scroll | 92 | 63 | 20.9% |
| click | 6 | 5 | 1.7% |

**Critical finding**: Only **51.3%** of users trigger an engagement event (stay >10s or interact). Only **20.9%** scroll. This means roughly half of visitors bounce immediately. The click count (6) is suspiciously low — GA's enhanced measurement may not be tracking all clicks properly, or users genuinely aren't clicking navigation.

### 2.6 Retention

| Metric | Value |
|--------|-------|
| New users | 305 |
| Returning users | 27 |
| Return rate | 8.9% |

For an 8-day-old site, 8.9% return rate is acceptable but not strong. Game guide sites typically see higher return rates as players come back for updates.

---

## 3. GSC Metrics

### 3.1 Performance (Aug 13-20)

| Metric | Value |
|--------|-------|
| Clicks | 135 |
| Impressions | 2,870 |
| CTR | 4.7% |
| Avg Position | 7.8 |

### 3.2 Top Queries

| Query | Clicks | Impressions | CTR | Position |
|-------|--------|-------------|-----|----------|
| dragonsword classes | 11 | 78 | 14.1% | — |
| kalien team | 3 | 9 | 33.3% | — |
| 드래곤소드 어웨이크닝 전용 카르마 | 7 | 132 | 5.3% | — |
| 시련의 탑 | — | — | — | — |
| lute ornette sion | — | 10 | — | — |

### 3.3 Indexing

| Status | Count |
|--------|-------|
| Indexed | 89 |
| Not indexed | 43 |
| — Redirect | 11 |
| — Canonical alternate | 1 |
| — Crawled, not indexed | 1 |
| — Discovered, not indexed | 30 |

43 unindexed pages is normal for a new site. The 30 "discovered, not indexed" pages will be crawled over time.

---

## 4. Problems Identified

### P0 — Critical

1. **High bounce rate (49%)**: Half of users leave without engaging. Homepage is the worst offender (11s avg).
2. **Low scroll rate (21%)**: Only 1 in 5 users scroll, suggesting content doesn't capture attention above the fold.

### P1 — Important

3. **US traffic quality mismatch**: 38% of users but 13% engagement. Need to determine if this is bots or content mismatch.
4. **Chinese pages bounce**: /zh/characters.html averages 3 seconds. Chinese content may not match user expectations.
5. **Zero referral/social traffic**: No backlinks or social promotion — missing growth channels.
6. **Click events extremely low (6)**: May indicate GA click tracking issue or poor navigation engagement.

### P2 — Monitor

7. **43 pages not indexed**: Normal for new site, but monitor weekly.
8. **ja/ru/zh new pages have English body content**: Metadata translated but body still English.
9. **SimilarWeb has no data**: Site too new; revisit at 3 months.

---

## 5. Action Plan

### This Week (Aug 23-29)

- [ ] Request indexing in GSC for 20 new pages (kalien, ornette, sion, tower-of-trials × 5 languages)
- [ ] Verify GA click tracking is working (check enhanced measurement settings)
- [ ] Improve homepage above-the-fold: add "Popular Guides" section with links to top pages
- [ ] Investigate US traffic: check GA Bot Filtering setting, compare US vs Korea behavior flow

### Next 2 Weeks (Aug 30 - Sep 12)

- [ ] Optimize titles/descriptions for high-impression low-CTR pages (target CTR >6%)
- [ ] Add internal links from high-traffic pages (classes, gear, build) to new pages
- [ ] Promote on Reddit (r/DragonSwordAwakening), Discord, and game forums to build referral traffic
- [ ] Translate ja/ru/zh new page body content (priority: Korean is done, Japanese next)
- [ ] Set up GA conversion event: "viewed_3_pages" as engagement milestone

### Next 30 Days (by Sep 22)

- [ ] Second GSC/GA data review (Sep 6, then Sep 20)
- [ ] Monitor new pages' ranking and impressions
- [ ] Evaluate if daily traffic reaches 500+ (threshold for Adsterra)
- [ ] Check SimilarWeb for competitor traffic data
- [ ] Build 3-5 backlinks from game wiki/guide sites

### Next Review

- **Next GSC review**: Aug 29 (7 days)
- **Next full GA+GSC review**: Sep 6 (14 days)
- **SimilarWeb check**: Sep 22 (30 days, when site may have enough traffic)

---

## 6. Screenshots

- GA Traffic Acquisition: `ga-traffic-level6.png`
- GA Top Pages: `ga-pages-level6.png`
- GA Countries: `ga-countries-level6.png`
- GA Retention: `ga-retention-level6.png`
- GSC Performance: `gsc-performance-level6.png`
