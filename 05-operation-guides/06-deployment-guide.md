# Deployment Guide: Vercel + Cloudflare + Spaceship

> This guide covers how the ds-guides.wiki site is deployed across three platforms.
> Official docs: [Vercel custom domains](https://vercel.com/docs/domains/set-up-custom-domain) | [Cloudflare full setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup) | [Spaceship nameservers](https://www.spaceship.com/knowledgebase/connect-domain-to-spaceship-hosting/)

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
        └── CNAME record: www    → cname.vercel-dns.com (Vercel CDN)
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
   - `ds-guides.wiki` (apex, with 308 redirect to www by default)
   - `www.ds-guides.wiki` (production)
4. Note the DNS records Vercel requires (click "View DNS configuration"):
   - **A record**: `@` → `216.198.79.1`
   - **CNAME**: `www` → `cname.vercel-dns.com` (legacy but still works)

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
   - Target: `cname.vercel-dns.com`
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
# Should return: cname.vercel-dns.com

# Check HTTPS
curl -I https://ds-guides.wiki
# Should return: 200 OK (or 308 to www)
```

Then verify in browser:
- https://ds-guides.wiki → should load the site
- https://www.ds-guides.wiki → should load the site
- Check SSL certificate is valid
- Check GA is receiving data (GA Realtime report)

---

## 5. Maintenance Operations

### Add a subdomain (e.g., blog.ds-guides.wiki)

1. Cloudflare → DNS → Records → Add record
2. Type: CNAME, Name: `blog`, Target: `cname.vercel-dns.com`, Proxy: DNS only
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
| Cloudflare nameservers | celeste.ns.cloudflare.com / thaddeus.ns.cloudflare.com | Assigned by Cloudflare |
| Vercel | Team: dragonsword-guides (Hobby) | Auto-deploy from GitHub main |
| GitHub | byte886/dragonsword-guides | Website code repo |
| GA | Measurement ID: G-6XQCHB1YYV | In js/analytics.js |
