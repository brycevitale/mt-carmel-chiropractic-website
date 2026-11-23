# Mt Carmel Chiropractic & Acupuncture

**Live website: [hamdenchiropracticandacupuncture.com](https://hamdenchiropracticandacupuncture.com)**

## Overview

I developed this website for Mt Carmel Chiropractic & Acupuncture, a chiropractic and acupuncture clinic in Hamden, Connecticut, and handled its hosting, domain configuration, and production deployment. The site launched in November 2026.

This repository is a public portfolio copy of the website. The production site is maintained and deployed from a separate private repository.

## Technologies

- HTML5, CSS3, and vanilla JavaScript
- Cloudflare Workers and the Wrangler CLI
- Git and GitHub
- ChiroTouch (online appointment booking)
- Python 3 (local preview server)

## Features

- 12 pages plus a custom 404 page: home, services overview, six service pages, Meet the Team, Booking, Insurance & Payment, and Contact
- Responsive layout with a mobile navigation menu
- Online appointment booking through the clinic's ChiroTouch patient portal
- Tap-to-call phone links, office hours, and map directions
- Expandable service summaries
- Accessibility features, including a skip link, keyboard-friendly navigation, descriptive alt text, and support for reduced motion and high-contrast mode

## Architecture

- **Static site:** plain HTML pages with one stylesheet and one small script, with no framework or build step.
- **Responsive design:** a mobile-first stylesheet that uses CSS custom properties for the clinic's colors and adapts the layout for tablet and desktop screens.
- **Appointment booking:** "Book an Appointment" buttons link to the clinic's existing ChiroTouch patient portal in a new tab. The website has no forms and does not collect patient information.
- **SEO:** unique page titles and descriptions, canonical tags, a sitemap, `robots.txt`, structured data for the clinic, and clean URLs such as `/team` and `/services/chiropractic`.

## Project Structure

```
mt-carmel-chiro-showcase/
├── public/
│   ├── index.html
│   ├── booking.html
│   ├── contact.html
│   ├── insurance.html
│   ├── team.html
│   ├── 404.html
│   ├── services/
│   │   ├── index.html
│   │   └── ... (six service pages)
│   ├── assets/
│   │   ├── css/styles.css
│   │   ├── js/main.js
│   │   └── images/
│   ├── favicon.ico
│   ├── apple-touch-icon.png
│   ├── robots.txt
│   └── sitemap.xml
├── examples/
│   └── wrangler.example.jsonc
├── scripts/
│   └── preview_server.py
└── README.md
```

## Hosting and Deployment

- **Cloudflare Workers:** the site is served as static assets from Cloudflare Workers and deployed with the Wrangler CLI. `examples/wrangler.example.jsonc` shows the configuration with placeholder names and domains.
- **DNS:** both of the clinic's domains use Cloudflare DNS.
- **HTTPS:** Cloudflare manages the TLS certificates, and all HTTP requests redirect to HTTPS.
- **Redirects:** `hamdenhealthandwellness.com` permanently redirects to the primary domain, `www` addresses redirect to the non-`www` domain, and old `.html` addresses redirect to clean URLs.
- **Google Search Console:** both domains are verified through DNS records, and Search Console is used to monitor indexing.
- **Staging:** a separate staging address is protected with Cloudflare Access.

## Local Development

Requires Python 3. From the project folder:

```bash
python3 scripts/preview_server.py
```

Then open http://localhost:8123. The preview server handles clean URLs and the custom 404 page the same way the live site does. To use a different port:

```bash
python3 scripts/preview_server.py 8000
```

## Usage

The clinic's name, branding, photographs, and content belong to Mt Carmel Chiropractic & Acupuncture and are shared here with the clinic's permission. They are not licensed for reuse.
