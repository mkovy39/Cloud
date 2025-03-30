```markdown
# CloudFront Configuration for S3 Static Website

This guide walks through setting up Amazon CloudFront as a CDN for your S3-hosted static website, enabling fast global delivery, HTTPS, and caching.

---

## Prerequisites

- A static website hosted on S3 with public access and static website hosting enabled.
- Optional: A custom domain name registered (e.g., `mkovy.com`).
- Optional: A valid SSL certificate from ACM if using HTTPS and a custom domain.

---

## Step-by-Step: Create CloudFront Distribution

1. Go to the [CloudFront Console](https://console.aws.amazon.com/cloudfront/).
2. Click **"Create Distribution"**.

### Origin Settings

- **Origin domain**: Paste your **S3 Website Endpoint** (not the bucket name).
  - Example: `mkovy.com.s3-website-us-east-1.amazonaws.com`
- **Origin name**: Auto-filled or set your own.
- **Origin access control**: Leave disabled for public websites.

### Default Cache Behavior

- **Viewer Protocol Policy**: Redirect HTTP to HTTPS (recommended).
- **Allowed HTTP Methods**: GET, HEAD
- **Cached HTTP Methods**: GET, HEAD
- **Cache policy**: Use the default or `CachingOptimized`.

### Distribution Settings

- **Price class**: Use `Price Class 100` to save cost (serves only US, Canada, Europe).
- **Alternate domain (CNAME)**: If using a custom domain, e.g., `www.mkovy.com`
- **SSL certificate**: Choose `Custom SSL Certificate` from ACM if using your domain.
- **Default root object**: `index.html`

3. Click **Create Distribution**.

---

## Step 2: Update DNS (if using custom domain)

If you're using Route 53 or another domain provider:

- Add a CNAME or A (Alias) record pointing your domain (e.g., `www.mkovy.com`) to the **CloudFront domain name**, which looks like:  
  `d1234abcd.cloudfront.net`

---

## Final Checks

- Wait for status to show **“Deployed”** (may take a few minutes).
- Visit your **CloudFront URL** or **custom domain** to see your website served with CDN + HTTPS.

---

## Optional: Add Security & Optimization

- Use **WAF (Web Application Firewall)** to block unwanted traffic.
- Set **custom error pages** (e.g., `404.html`).
- Enable **geo-restriction** to limit access by country.
- Customize cache behavior for different paths.
