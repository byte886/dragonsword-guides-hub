# Deployment Guide: Vercel + Cloudflare + Spaceship

> This guide covers how the ds-guides.wiki site is deployed across three platforms, plus GA/GSC setup.
> Official docs: [Vercel custom domains](https://vercel.com/docs/domains/set-up-custom-domain) | [Cloudflare full setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup) | [Spaceship nameservers](https://www.spaceship.com/knowledgebase/connect-domain-to-spaceship-hosting/) | [GA4 setup](https://support.google.com/analytics/answer/9304153) | [GSC domain verification](https://support.google.com/webmasters/answer/9008080)

---

## 1. Architecture Overview

```
User types ds-guides.wiki
        │
        ▼
   DNS resolver asks: "Who manages ds-guides.wiki DNS?"
        │
        ▼
   Cloudflare nameservers (celeste/thaddeus.ns.cloudflare.com)
        │
        ├── A record:     @      → 216.198.79.1        (Vercel IP)
        └── CNAME record: www    → df9ecd0750052516.vercel-dns-017.com (Vercel CDN)
        │
        ▼
   Vercel edge network → serves static files from GitHub repo
```

| Platform | Role | What it does |
|----------|------|-------------|
| **Spaceship** | Domain registrar | Holds the domain registration; only stores nameserver pointers |
| **Cloudflare** | DNS manager | Stores DNS records (A/CNAME); proxy status = DNS only (gray cloud) |
| **Vercel** | Hosting | Serves the static site; auto-deploys on git push to main |

### Why DNS only (gray cloud), not Proxied (orange cloud)?

- Vercel already provides global CDN and automatic SSL
- Orange cloud + Vercel can cause redirect loops and SSL conflicts
- Cloudflare proxy can be enabled later if DDoS protection is needed
- Reference: Vercel recommends DNS-only when using external DNS [docs](https://vercel.com/docs/domains/set-up-custom-domain)

---

## 2. Prerequisites

- Domain purchased (ds-guides.wiki at Spaceship)
- GitHub repo with website code (byte886/dragonsword-guides)
- Vercel account connected to GitHub
- Cloudflare account
- All accounts logged in before starting

---

## 3. Step-by-Step Deployment

### Step 1: Deploy to Vercel

1. Go to https://vercel.com/new
2. Import the GitHub repository `byte886/dragonsword-guides`
3. Configure:
   - Framework Preset: **Other** (static site, no build step)
   - Root Directory: `./`
   - Build Command: leave empty
   - Output Directory: leave empty
4. Click **Deploy**
5. Wait for deployment to complete; site is live at `https://dragonsword-guides.vercel.app`

**Reference**: https://vercel.com/docs/deployments

### Step 2: Add Custom Domain in Vercel

1. Go to Project Settings → Domains
2. Enter `ds-guides.wiki` and click Add
3. Vercel automatically adds both:
   - `ds-guides.wiki` (apex, Production — primary domain)
   - `www.ds-guides.wiki` (initially Production; change to 308 redirect to apex)
4. **Set apex as primary domain**:
   - Click Edit on `ds-guides.wiki` → select "Connect to an environment" → Production → Save
   - Click Edit on `www.ds-guides.wiki` → select "Redirect to Another Domain" → 308 Permanent Redirect → target `ds-guides.wiki` → Save
5. Note the DNS records Vercel requires (click "View DNS configuration"):
   - **A record**: `@` → `216.198.79.1`
   - **CNAME**: `www` → `df9ecd0750052516.vercel-dns-017.com` (Vercel recommended value; old `cname.vercel-dns.com` also works)

**Domain redirect logic**: apex (`ds-guides.wiki`) serves the site directly; www 308-redirects to apex. All canonical URLs use `https://ds-guides.wiki/` (no www).

**Important**: Vercel's displayed IP may change. Always copy the exact value from Vercel's "View DNS configuration" panel, not from this guide.

**Reference**: https://vercel.com/docs/domains/set-up-custom-domain

### Step 3: Add Site in Cloudflare

1. Go to https://dash.cloudflare.com → **Add a site**
2. Enter `ds-guides.wiki` → Continue
3. Select **Free** plan → Continue
4. Cloudflare scans existing DNS records (imports registrar parking records — see Step 4)

### Step 4: Configure DNS Records in Cloudflare

After the scan, review and edit records:

1. **Delete all imported parking records** (e.g., A records pointing to Spaceship/AWS IPs like 54.149.79.189 or 34.216.117.25)
   - These are registrar default records, not yours
   - Spaceship's Advanced DNS shows "0 custom records" because these are system-generated
2. **Add A record**:
   - Type: A
   - Name: `@` (or `ds-guides.wiki`)
   - IPv4 address: `216.198.79.1`
   - Proxy status: **DNS only** (gray cloud)
   - TTL: Auto
3. **Add CNAME record**:
   - Type: CNAME
   - Name: `www`
   - Target: `df9ecd0750052516.vercel-dns-017.com`
   - Proxy status: **DNS only** (gray cloud)
   - TTL: Auto
4. Click **Continue to activation**

**Why delete parking records?** Cloudflare scans the current DNS (via Spaceship nameservers) and imports whatever it finds, including the registrar's default parking page IPs. These must be replaced with Vercel's records.

**Reference**: https://developers.cloudflare.com/dns/zone-setups/full-setup/setup

### Step 5: Update Nameservers at Spaceship

1. Go to Spaceship Launchpad → Domain Manager → click `ds-guides.wiki`
2. Click **Nameservers and DNS** (名称服务器和DNS)
3. Click **Change** (更改)
4. Select **Custom nameservers** (自定义名称服务器)
5. Enter the two nameservers assigned by Cloudflare (e.g., `celeste.ns.cloudflare.com`, `thaddeus.ns.cloudflare.com`)
6. Click **Save nameserver settings**
7. Verify DNSSEC is disabled:
   - Go to Advanced DNS → DNSSEC tab
   - Should show "0 records"
   - If DNSSEC is enabled, disable it (it will break resolution after nameserver change)

**Direct URL**: https://www.spaceship.com/zh/application/domain-list-application/

**Reference**: https://www.spaceship.com/knowledgebase/connect-domain-to-spaceship-hosting/

### Step 6: Wait for Activation

1. Cloudflare automatically checks nameserver propagation
2. Typical time: 1-2 hours, up to 24 hours
3. You can manually trigger a check: Cloudflare Overview → "Check nameservers now"
4. Once active, Cloudflare sends a confirmation email

### Step 7: Set Up Google Analytics (GA4)

1. Go to https://analytics.google.com/
2. Create account (e.g., `byte886`) → create property (e.g., `ds-guides.wiki`)
3. Business details: industry category, reporting time zone
4. Data collection: choose **Web** → enter `https://www.ds-guides.wiki`
5. Copy the **Measurement ID** (format: `G-XXXXXXXXXX`)
6. Add the tracking code to `js/analytics.js` in the website repo (single file, all pages reference it)
7. Push to GitHub → Vercel auto-deploys
8. Verify: GA → Reports → Realtime → visit the site → should show 1 active user

**Key settings**:
- Enhanced measurement: enable/disable based on needs (page views is the default)
- Data retention: set to 14 months (default is 2 months)
- Account structure: one account per owner, one property per website

**Reference**: https://support.google.com/analytics/answer/9304153

### Step 8: Set Up Google Search Console (GSC)

1. Go to https://search.google.com/search-console
2. Click **Add property** → choose **Domain** (not URL prefix)
3. Enter `ds-guides.wiki` → Continue
4. GSC auto-detects Cloudflare as DNS provider → click **Start verification**
5. Cloudflare authorization page opens → click **Authorize**
   - This is a one-time authorization via Domain Connect protocol
   - Google adds a TXT record to Cloudflare DNS automatically
   - No ongoing permission is granted
6. Verification completes instantly → click **Go to property**
7. Submit sitemap:
   - Left sidebar → Indexing → Sitemaps
   - Enter `https://www.ds-guides.wiki/sitemap.xml` → Submit
   - Status initially shows "Couldn't fetch" — this is normal, Google processes it within hours
8. After a few days, check:
   - Pages → indexing status
   - Performance → search queries, impressions, clicks, position

**Why Domain type over URL prefix?**
- Covers all subdomains (www, m, blog) and both http/https
- Cloudflare one-click verification is only available for Domain type
- Future subdomains don't need re-verification

**Reference**: https://support.google.com/webmasters/answer/9008080

---

## 4. Verification

After Cloudflare shows "Active":

```bash
# Check nameservers
dig NS ds-guides.wiki +short
# Should return: celeste.ns.cloudflare.com / thaddeus.ns.cloudflare.com

# Check A record
dig A ds-guides.wiki +short
# Should return: 216.198.79.1

# Check CNAME
dig CNAME www.ds-guides.wiki +short
# Should return: df9ecd0750052516.vercel-dns-017.com

# Check HTTPS
curl -I https://ds-guides.wiki
# Should return: 200 OK (or 308 to www)
```

Then verify in browser:
- https://ds-guides.wiki → should load the site (200 OK, primary domain)
- https://www.ds-guides.wiki → should 308 redirect to https://ds-guides.wiki/
- Check SSL certificate is valid
- Check GA is receiving data (GA → Reports → Realtime)
- Check GSC verification is complete (GSC → Settings → Ownership verification)
- Check sitemap submitted (GSC → Sitemaps → status should eventually show "Success")
- SEO basics: title, meta description, canonical, H1/H2 hierarchy, viewport meta tag

---

## 5. Maintenance Operations

### Add a subdomain (e.g., blog.ds-guides.wiki)

1. Cloudflare → DNS → Records → Add record
2. Type: CNAME, Name: `blog`, Target: `df9ecd0750052516.vercel-dns-017.com`, Proxy: DNS only
3. Vercel → Project Settings → Domains → add `blog.ds-guides.wiki`

### Change Vercel IP

If Vercel changes their A record IP:
1. Vercel → Domains → "View DNS configuration" to get new IP
2. Cloudflare → DNS → edit the A record with new IP

### Revert to Spaceship nameservers

1. Spaceship → Nameservers and DNS → Change → select "Spaceship nameservers"
2. Wait for propagation
3. DNS management returns to Spaceship; Cloudflare records become inactive

### Check DNS propagation

- Spaceship: Advanced DNS → "Check servers" button
- External tool: https://dnschecker.org/

---

## 6. Troubleshooting

### Domain shows "Invalid Configuration" in Vercel

- DNS records not yet propagated; wait 1-24 hours
- Verify records in Cloudflare match Vercel's "View DNS configuration" exactly
- Check for duplicate/conflicting DNS records

### Redirect loop (ERR_TOO_MANY_REDIRECTS)

- Usually caused by Cloudflare orange cloud + Vercel SSL
- Fix: set proxy status to DNS only (gray cloud) in Cloudflare
- If orange cloud is required, set Cloudflare SSL mode to "Full (Strict)"

### Nameservers not updating after 24 hours

- Verify nameservers entered correctly at Spaceship (no typos)
- Check DNSSEC is disabled at Spaceship
- Reference: https://developers.cloudflare.com/dns/zone-setups/troubleshooting/pending-nameservers/

### Site works on www but not apex (or vice versa)

- Check both A and CNAME records exist in Cloudflare
- Verify Vercel has both domains added in project settings

---

## 7. Platform Account Reference

| Platform | Account/ID | Notes |
|----------|-----------|-------|
| Spaceship | ds-guides.wiki, expires 2027-08-15 | Registrar only |
| Cloudflare | Account ID: 62adf960343b448a7e52838e68808b21 | Free plan, DNS only |
| Cloudflare | Zone ID: 96aa94883c28ef6b8c872d5c35f9841a | ds-guides.wiki zone |
| Cloudflare nameservers | celeste.ns.cloudflare.com / thaddeus.ns.cloudflare.com | Assigned by Cloudflare |
| Vercel | Team: dragonsword-guides (Hobby) | Auto-deploy from GitHub main |
| GitHub | byte886/dragonsword-guides | Website code repo |
| GA | Account ID: 404676857, Property ID: 549932655 | Measurement ID: G-6XQCHB1YYV |
| GA | Tracking code in `js/analytics.js` | Single file, all pages reference it |
| GSC | Property: sc-domain:ds-guides.wiki | Verified via Cloudflare Domain Connect |
| GSC | Sitemap: https://www.ds-guides.wiki/sitemap.xml | Submitted 2026-08-15 |
