# GCL institutional domain migration — tracked safeguards

**Target domain:** `grandchallenge.ai`, owned by Grand Challenge Technologies Ltd.
**Root hosting:** `grandchallenge/grandchallenge.github.io` (GitHub Actions Pages).
**Existing mathematics authority:** `grandchallenge/MATH-PROGRAMME`, at `https://grandchallenge.github.io/MATH-PROGRAMME/`.

## Preserve
- The existing MATH-PROGRAMME repository, workflow, exact document routes and archive remain untouched.
- The preview remains at `grandchallenge/gcl-public-web-preview`.
- Namecheap DNS MX and SPF records for email forwarding remain intact.
- No wildcard records.

## Migration gates
1. Build and verify this organization-root Pages site without any custom-domain or DNS changes.
2. Verify `grandchallenge.ai` ownership in GitHub organization Pages settings by adding the returned TXT challenge to Namecheap DNS.
3. Set root Pages custom domain to `grandchallenge.ai` in GitHub; change only web DNS: apex parking A to the four GitHub Pages IPv4 addresses and `www` parking CNAME to `grandchallenge.github.io`.
4. Wait for DNS resolution, HTTPS issuance, redirect checks, and verify `grandchallenge.ai/MATH-PROGRAMME/` serves the authoritative mathematics site.
5. Confirm the old `grandchallenge.github.io/MATH-PROGRAMME/` route redirects or remains navigable, with no internal broken asset paths.

**Rollback:** Remove the custom domain from root Pages and restore the original apex and `www` DNS records from the registrar backup. Preserve MX/SPF unchanged. Restore the original project Pages configuration only if an unexpected change is independently observed; do not modify it as a generic rollback step.
