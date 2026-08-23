---
name: data-review
description: "Periodic website data review using GA, GSC, and SimilarWeb. Use when the user asks for a data review, traffic analysis, performance check, SEO review, or periodic (weekly/monthly) analytics report. Produces an evaluation report with action items."
---

# Website Data Review Skill

Systematic data review for ds-guides.wiki. Combines GA (on-site behavior), GSC (search performance), and SimilarWeb (competitive intelligence) into an actionable report.

**Detailed interpretation guide**: `05-operation-guides/08-ga-gsc-practice-handbook.md`

## When to Use

- Weekly GSC quick check (every 7 days)
- Bi-weekly full GA+GSC review (every 14 days)
- Monthly comprehensive review with SimilarWeb
- After major content updates or deployments
- When user asks "how is the site doing" or "check analytics"

## Prerequisites

1. Read `05-operation-guides/07-ga-gsc-guide.md` for report navigation
2. Read `05-operation-guides/08-ga-gsc-practice-handbook.md` for interpretation logic
3. Connect to user Chrome via Playwright (read `.agents/skills/playwright-extension/SKILL.md`)
4. Confirm GA property: ds-guides.wiki (G-6XQCHB1YYV)
5. Confirm GSC property: sc-domain:ds-guides.wiki

## Review Checklist

### Step 1: GA Reports (via Playwright)

Navigate to https://analytics.google.com/ and collect ALL of the following:

| Report | Path | What to collect | Why it matters |
|--------|------|-----------------|----------------|
| **Realtime** | Reports > Realtime | Active users, top pages, countries | Confirm tracking works; spot traffic spikes |
| **Traffic Acquisition** | Reports > Acquisition > Traffic acquisition | Channel breakdown (Organic/Direct/Referral/Social), users, engagement rate per channel | Is SEO working? Are backlinks/social driving traffic? |
| **Pages & Screens** | Reports > Engagement > Pages and screens | Top 10 pages: views, users, avg engagement time, views per user | Which content is popular? Is content quality good (time on page)? |
| **Countries** | Reports > User > Demographics > Country/Region | Top 10 countries: users, engagement rate, avg time | Does traffic match 5 target languages? Which markets are high-quality? |
| **Tech Details** | Reports > Tech > Tech details | Browsers; switch dimension to Device category for desktop/mobile | Browser compatibility; mobile vs desktop optimization priority |
| **Events** | Reports > Engagement > Events | page_view, user_engagement, scroll, click counts and user % | Engagement depth: bounce rate, scroll rate, navigation usage |
| **Retention** | Reports > Retention | New vs returning users, cohort curve | Do users come back? Content stickiness |

**Important**:
- Set date range to match the review period (last 7/14/30 days)
- Take screenshots of each report, save to `08-data-reviews/`
- Note any anomalies (spikes, drops, unexpected countries)

### Step 2: GSC Reports (via Playwright)

Navigate to https://search.google.com/search-console/ and collect:

| Report | Path | What to collect | Why it matters |
|--------|------|-----------------|----------------|
| **Performance** | Performance > Search results | Clicks, impressions, CTR, avg position across 4 dimensions | Is SEO working? Which queries/pages drive traffic? |
| **Pages (Indexing)** | Indexing > Pages | Indexed vs not indexed count, top issue reasons | Are pages being found by Google? Technical SEO issues? |
| **Sitemaps** | Indexing > Sitemaps | Status, last read, discovered URL count | Is Google reading our sitemap? |
| **URL Inspection** | Top search bar | Spot-check 2-3 important pages | Are new pages indexed? Request indexing if not |

**For Performance report, collect all 4 dimensions:**
1. **Queries**: Top 10 by clicks (what works), top 10 by impressions (high-impression low-CTR = optimize titles), queries with no landing page (content gaps)
2. **Pages**: Top 10 by clicks; high-impression low-click pages need title/description optimization
3. **Countries**: Top 5; compare with GA country data to assess traffic quality
4. **Devices**: Desktop/mobile/tablet split; if mobile ranks worse, check mobile experience

### Step 3: SimilarWeb (monthly only, after day 30)

Navigate to https://www.similarweb.com/ (login required, user has PRO):

1. **Our site** (ds-guides.wiki): May show "No data" if <10K monthly visits — skip if so
2. **Competitors**: Check 2-3 competitor guide sites (games.gg, destructoid.com, thegameswiki.com):
   - Monthly visits trend (benchmark against our traffic)
   - Traffic sources (organic vs referral vs social percentages)
   - Top referral sites (backlink opportunities)
   - Top organic keywords (keyword gap analysis)
   - Audience interests (content direction)

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

### Step 5: Interpretation — Apply Action Logic

For each metric, compare against thresholds and project history. **Do not just report numbers — interpret them.**

#### Traffic Acquisition
- Organic share rising → SEO working, continue
- Organic share <20% → critical, SEO not effective
- Referral = 0 after 30 days → start backlink building (Reddit, Discord, forums)
- Direct >70% with low engagement → possible tracking issue or bot traffic

#### Pages & Screens
- Guide page avg time >1 min → good content quality
- Guide page avg time <10 sec → content doesn't match search intent; check title vs content
- Homepage avg time <15 sec → improve above-the-fold, add "Popular Guides" section
- New page has 0 views after 7 days → check indexing and internal links
- High views but low scroll → content below fold not reached, improve intro/navigation

#### Countries
- US traffic >30% but engagement <15% → likely bot traffic; check GA bot filtering
- Korea/Japan/Russia high engagement → prioritize translating/supplementing those languages
- A language's target country has 0 traffic → check if that language version is indexed

#### Events
- Engagement rate <25% → critical, half of users bounce immediately
- Scroll rate <20% → users don't see content below fold; improve first screen
- Click count abnormally low → check if GA enhanced measurement is enabled; check navigation usability

#### Retention
- Return rate >15% → healthy for a guide site
- Return rate <8% after 30 days → add "recent updates" section, consider newsletter
- New sites: low return rate is normal in first 30 days, track trend not absolute

#### GSC Performance
- CTR >5% → titles/descriptions are effective
- CTR <3% with high impressions → optimize title and meta description
- Position 5-10 with impressions → on the cusp of page 1; optimize content to break through
- Position >10 → needs more content depth or backlinks
- High-impression queries with no landing page → create new content (content gap)

#### GSC Indexing
- Indexed >90% → healthy
- "Discovered - not indexed" → normal for new sites, wait; if persists >30 days, improve internal linking
- "Crawled - not indexed" → content quality may be too thin or duplicate
- 404 errors → fix links or add redirects
- New pages not indexed after 14 days → request indexing via URL Inspection

### Step 6: Produce Report

Save report to `08-data-reviews/level{N}-data-review.md` using this structure:

```markdown
# Level {N} Data Review: GA + GSC Analysis

> Period: {start} - {end} ({days} days)
> Date reviewed: {date}
> Tools: GA (G-6XQCHB1YYV), GSC (sc-domain:ds-guides.wiki)

## 1. Executive Summary
{2-3 sentence overview with grade (A/B/C/D) and key finding}

## 2. GA Metrics
### 2.1 Traffic Acquisition
{table + interpretation: is SEO working? any new channels?}
### 2.2 Top Pages
{table + interpretation: which content performs? which pages have issues?}
### 2.3 Countries
{table + interpretation: traffic quality by market, language alignment}
### 2.4 Devices & Browsers
{data + interpretation: optimization priority}
### 2.5 Events
{engagement rate, scroll rate, click rate + interpretation}
### 2.6 Retention
{new vs returning + interpretation}

## 3. GSC Metrics
### 3.1 Performance Summary
{clicks, impressions, CTR, position + trend vs previous period}
### 3.2 Top Queries
{high performers + high-impression low-CTR + content gaps}
### 3.3 Top Pages
{best performing pages + pages needing optimization}
### 3.4 Indexing Status
{indexed count, not indexed breakdown, action needed}

## 4. Reports Not Checked (and why)
{List any GA/GSC reports skipped and the reason — e.g., "Conversions: no key events configured yet"}

## 5. Problems Identified
### P0 Critical (immediate action)
### P1 Important (this sprint)
### P2 Monitor (watch trend)

## 6. Action Plan
### This Week
- [ ] {specific, measurable actions}
### Next 2 Weeks
- [ ] {specific actions}
### Next 30 Days
- [ ] {specific actions}

## 7. Next Review Date
{date}

## 8. Screenshots
{list of screenshot files}
```

### Step 7: Update Project Documents

After each review:
1. Update `06-project-continuity/01-项目背景与决策日志.md` with key decisions
2. Update AGENTS.md if review cadence or thresholds change
3. Commit screenshots to `08-data-reviews/`
4. If new content gaps found, create follow-up tasks
5. Commit and push both repos (website + hub)

## Review Cadence

| Frequency | Scope | Tools | Duration |
|-----------|-------|-------|----------|
| Every 7 days | GSC: performance + indexing | GSC only | 10 min |
| Every 14 days | Full GA + GSC review | GA + GSC | 30 min |
| Every 30 days | Comprehensive + competitors | GA + GSC + SimilarWeb | 60 min |

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
| Guide page avg time | >1 min | 30-60 sec | <10 sec |

## Project Benchmarks (first 8 days, Aug 15-22 2026)

Use these as baseline for future comparisons:

| Metric | Value |
|--------|-------|
| Total users | 305 |
| Organic search share | 50% |
| Top country | US (38%, but low engagement — likely bots) |
| Highest engagement | South Korea (66% engagement, 1m50s avg) |
| Engagement rate | 51% |
| Scroll rate | 21% |
| Return rate | 8.9% |
| GSC clicks | 135 |
| GSC impressions | 2,870 |
| GSC CTR | 4.7% |
| GSC avg position | 7.8 |
| Indexed pages | 89 of 135 |

## Reports Not Routinely Checked (and when to check them)

| Report | Tool | Skip reason | Check when |
|--------|------|-------------|------------|
| User Acquisition | GA | Nearly identical to Traffic Acquisition for new sites | Running paid ads or UTM campaigns |
| Conversions | GA | No key events configured | After setting up conversion events |
| Advertising | GA | No ads running | After AdSense/Adsterra integration |
| Explorations | GA | Custom analysis not needed for routine review | Funnel/path/cohort analysis needed |
| Landing Pages | GA | Covered by Pages report | Page count >50 or running campaign landing pages |
| Ecommerce/Monetization | GA | Content site, no products | Never (unless selling products) |
| User Lifetime Value | GA | Needs long-term data | After 90 days |
| Core Web Vitals | GSC | Insufficient data for new site | After 30 days, monthly |
| Mobile Usability | GSC | Responsive CSS already implemented | Mobile traffic anomalies |
| Links report | GSC | Minimal backlinks; internal links tracked in content map | After starting backlink building |
| Security/Manual Actions | GSC | Should be empty; quick weekly scan | If traffic suddenly drops |
| International Targeting | GSC | hreflang validated via code | Multi-language ranking issues |

## Common Pitfalls

- GA data has 24-48 hour delay; GSC has 2-3 day delay
- New sites show inflated US/bot traffic in first weeks — compare engagement rate, not just user count
- Don't compare GA and GSC numbers directly (different measurement methods)
- SimilarWeb estimates are directional, not exact
- Always check date ranges are consistent across reports
- Screenshots should capture the full report table, not just charts
- GA device category dimension may be hard to switch in UI; GSC device data is an acceptable substitute
- When GA navigation is difficult, use JavaScript evaluation to click buttons: `document.querySelectorAll('button')` and match by textContent
