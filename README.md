# Grand Challenge Labs — public institutional website

This repository publishes the GCL institutional homepage at the organization-root GitHub Pages site, and (once verified and DNS configured) at `https://grandchallenge.ai/`. The domain is a property of Grand Challenge Technologies Ltd.

Source of the initial front-end: `grandchallenge/gcl-public-web-preview` at commit `0bd6f274a85bd98f184eec07107a488b3a32f207`. The preview repository continues independently.

The site is built and deployed by `.github/workflows/pages.yml` after `python validate.py`. The mathematical documentary source and its Pages workflow remain entirely in `grandchallenge/MATH-PROGRAMME`; do not copy or modify those documents to publish this institutional homepage.

Pages custom domain is managed in the GitHub Pages repository settings. This is an Actions-based Pages build: a checked-in `CNAME` is unnecessary. Domain changes must preserve existing email forwarding DNS records.
