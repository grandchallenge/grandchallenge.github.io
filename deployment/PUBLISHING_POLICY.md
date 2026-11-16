# Public website release and documentation migration policy

## Roles and deployment boundaries

- `grandchallenge/gcl-public-web-preview`: independent design staging at `/gcl-public-web-preview/`; never owns the production domain.
- `grandchallenge/grandchallenge.github.io`: production homepage source; custom domain `grandchallenge.ai` is set in repository Pages settings, not via a checked-in CNAME.
- `grandchallenge/MATH-PROGRAMME`: mathematical documentation and source of authority; its build and deployment remain independent.

Preview source is **not automatically promoted** to production. For each release, compare the exact preview commit with the current production head; transfer only reviewed changes on a production PR; validate that PR; follow protected merge policy; then check the deployed page and record its final source SHA. Do not copy the preview's Pages settings, workflow, or DNS records.

## Production artifact

`python validate.py && python scripts/build_publication.py` validates the homepage and assembles `dist/` containing only `index.html` and `assets/`. `publication-manifest.json` (not deployed) contains SHA-256 hashes for every published file. The workflow publishes `dist/`, never the repository root. No repository metadata, source scripts, or deployment instructions are eligible for upload.

## Domain cutover acceptance

1. Verify ownership TXT challenge, apex and www records and GitHub Pages settings. Do not modify MX/SPF email-forwarding records.
2. Check HTTPS and the root site, including redirects from www.
3. Check `/MATH-PROGRAMME/` and the old Pages path independently, including CSS/JS/search assets and mathematical rendering.
4. Reconcile MkDocs `site_url`, canonicals and sitemap only once the actual custom-domain route works.
5. Verify all institutional links and publish a source-revision-bound deployment receipt.
6. Roll back only the root custom-domain assignment/web DNS, if necessary; leave the mathematics source and deploy workflow untouched.

## MkDocs Material retirement

Material for MkDocs is in maintenance mode, with upstream critical maintenance through 2027-05-05. Zensical is the preferred migration candidate but must pass parallel builds, generated-documentation hook compatibility, mathematics rendering, search, links, and exact-head publication controls before production switch. Keep the current working generator until evidence supports replacement.
