---
name: data-review
description: "Periodic website data review using GA, GSC, and SimilarWeb. Use when the user asks for a data review, traffic analysis, performance check, SEO review, or periodic (weekly/monthly) analytics report. Produces an evaluation report with action items."
---

# Website Data Review Skill

Systematic data review for ds-guides.wiki. Combines GA (on-site behavior), GSC (search performance), and SimilarWeb (competitive intelligence) into an actionable report.

## When to Use

- Weekly GSC quick check (every 7 days)
- Bi-weekly full GA+GSC review (every 14 days)
- Monthly comprehensive review with SimilarWeb
- After major content updates or deployments
- When user asks "how is the site doing" or "check analytics"

## Prerequisites

1. Read `05-operation-guides/07-ga-gsc-guide.md` for report navigation
2. Connect to user Chrome via Playwright (read `.agents/skills/playwright-extension/SKILL.md`)
3. Confirm GA property: ds-guides.wiki (G-6XQCHB1YYV)
4. Confirm GSC property: sc-domain:ds-guides.wiki

## Review Checklist

### Step 1: GA Reports (via Playwright)

Navigate to https://analytics.google.com/ and collect ALL of the following:

| Report | Path | What to collect |
|--------|------|-----------------|
| **Realtime** | Reports > Realtime | Current active users, top pages, countries |
| **Traffic Acquisition** | Reports > Acquisition > Traffic acquisition | Sessions by channel (Organic/Direct/Referral/Social), users, engagement rate |
| **Pages & Screens** | Reports > Engagement > Pages and screens | Top 10 pages: views, users, avg engagement time, views per user |
| **Countries** | Reports > User > Demographics > Country/Region | Top 10 countries: users, engagement rate, avg time |
| **Tech Details** | Reports > Tech > Tech details | Browsers (switch dimension to Device category for desktop/mobile split) |
| **Events** | Reports > Engagement > Events | Event counts: page_view, scroll, click, user_engagement; % of users per event |
| **Retention** | Reports > Retention | New vs returning users, cohort retention curve |

**Important**:
- Set date range to match the review period (last 7/14/30 days)
- Take screenshots of each report, save to `07-homework/`
- Note any anomalies (spikes, drops, unexpected countries)

### Step 2: GSC Reports (via Playwright)

Navigate to https://search.google.com/search-console/ and collect:

| Report | Path | What to collect |
|--------|------|-----------------|
| **Performance** | Performance > Search results | Clicks, impressions, CTR, avg position; switch to Queries/Pages/Countries/Devices tabs |
| **Pages (Indexing)** | Indexing > Pages | Indexed vs not indexed count, top issues |
| **Sitemaps** | Indexing > Sitemaps | Status, last read, discovered URLs |
| **URL Inspection** | Top search bar | Spot-check 2-3 important pages for indexing status |

**For Performance report, collect all 4 dimensions:**
1. Queries: top 10 by clicks, top 10 by impressions (look for high-impression low-CTR)
2. Pages: top 10 by clicks
3. Countries: top 5
4. Devices: desktop/mobile/tablet split

### Step 3: SimilarWeb (monthly only)

Navigate to https://www.similarweb.com/ and check:

1. **Our site** (ds-guides.wiki): May show "No data" if traffic is too low (<10K monthly visits)
2. **Competitors**: Check 2-3 competitor guide sites (e.g., games.gg, destructoid.com, thegameswiki.com) for:
   - Total monthly visits trend
   - Traffic sources breakdown
   - Top referral sites (potential backlink opportunities)
   - Top organic keywords (keyword gap analysis)
   - Audience interests

**Note**: SimilarWeb requires login (user has PRO). If site is too new, skip and note "revisit when monthly traffic >10K".

### Step 4: Cross-Reference & Analysis

Compare data sources to find insights:

| Question | GA | GSC | SimilarWeb |
|----------|----|----|------------|
| Which pages get traffic? | Top pages by views | Top pages by clicks | — |
| Where does traffic come from? | Channels | Queries | Referral sites |
| Which countries? | Country report | Country dimension | Geo distribution |
| Mobile vs desktop? | Tech report | Device dimension | — |
| Do users engage? | Events, retention, time on page | CTR (search appeal) | Bounce rate, pages/visit |
| Competitor benchmarks | — | — | Traffic, keywords, referrals |

**Red flags to look for:**
- High US traffic with <15% engagement → possible bot traffic
- High impressions but CTR <3% → title/description needs optimization
- Page views but no scroll events → content doesn't match intent
- Sudden traffic drop → check indexing, algorithm updates, site errors
- Referral traffic = 0 after 30+ days → need backlink building

### Step 5: Produce Report

Save report to `07-homework/level{N}-data-review.md` using this structure:

```markdown
# Level {N} Data Review: GA + GSC Analysis

> Period: {start} - {end} ({days} days)
> Date reviewed: {date}

## 1. Executive Summary
{2-3 sentence overview with grade (A/B/C/D) and key finding}

## 2. GA Metrics
### 2.1 Traffic Acquisition (table)
### 2.2 Top Pages (table with views, users, time)
### 2.3 Countries (table with engagement rate)
### 2.4 Devices & Browsers
### 2.5 Events (engagement rate, scroll rate)
### 2.6 Retention (new vs returning)

## 3. GSC Metrics
### 3.1 Performance summary
### 3.2 Top Queries (high-CTR and high-impression-low-CTR)
### 3.3 Indexing status

## 4. Problems Identified
### P0 Critical / P1 Important / P2 Monitor

## 5. Action Plan
### This Week / Next 2 Weeks / Next 30 Days
- [ ] Specific, measurable actions with owners

## 6. Next Review Date
```

### Step 6: Update Project Documents

After each review:
1. Update `06-project-continuity/01-项目背景与决策日志.md` with key decisions
2. Update AGENTS.md if review cadence or thresholds change
3. Commit screenshots to `07-homework/`
4. If new content gaps found, create follow-up tasks

## Review Cadence

| Frequency | Scope | Tools |
|-----------|-------|-------|
| Every 7 days | GSC quick check (clicks, impressions, indexing) | GSC only |
| Every 14 days | Full GA + GSC review | GA + GSC |
| Every 30 days | Comprehensive + competitors | GA + GSC + SimilarWeb |

## Key Thresholds (for ds-guides.wiki)

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Engagement rate | >40% | 25-40% | <25% |
| Scroll rate | >40% | 20-40% | <20% |
| CTR (GSC) | >5% | 3-5% | <3% |
| Avg position | <5 | 5-10 | >10 |
| Return rate (30d) | >15% | 8-15% | <8% |
| Indexed pages | >90% | 70-90% | <70% |
| Organic traffic trend | Growing | Flat | Declining |
| Referral traffic | >10% | 1-10% | 0% after 30 days |

## Common Pitfalls

- GA data has 24-48 hour delay; GSC has 2-3 day delay
- New sites show inflated US/bot traffic in first weeks
- Don't compare GA and GSC numbers directly (different measurement methods)
- SimilarWeb estimates are directional, not exact
- Always check date ranges are consistent across reports
- Screenshots should capture the full report table, not just charts
