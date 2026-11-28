# Grand Challenge Labs — public institutional website

This repository publishes the GCL institutional homepage at the organization-root GitHub Pages site, and (once verified and DNS configured) at `https://grandchallenge.ai/`. The domain is a property of Grand Challenge Technologies Ltd.

Source of the initial front-end: `grandchallenge/gcl-public-web-preview` at commit `0bd6f274a85bd98f184eec07107a488b3a32f207`. The preview repository continues independently.

The site is built and deployed by `.github/workflows/pages.yml` after `python validate.py`. The mathematical documentary source and its Pages workflow remain entirely in `grandchallenge/MATH-PROGRAMME`; do not copy or modify those documents to publish this institutional homepage.

Pages custom domain is managed in the GitHub Pages repository settings. This is an Actions-based Pages build: a checked-in `CNAME` is unnecessary. Domain changes must preserve existing email forwarding DNS records.

## Live research console

The public live console defaults to research threads, with operations and diagnostics as a secondary view. It consumes the existing validated public feed, with no additional publisher, network request or release authority.

For source-designated ordinary public research, the existing first line is unchanged. Optional contiguous comments immediately after it give explicit context (one line per field):

```bash
# GCL_PUBLIC_RESEARCH grandchallenge/MATH-PROGRAMME EXACT_PUBLIC_COMMIT_SHA
# GCL_THREAD: SCC-001
# GCL_TITLE: Structural Capacity Calculus
# GCL_OBJECTIVE: State the actual objective.
# GCL_RESEARCH: State the actual question.
# GCL_EXECUTE: State the actual action.
```

Use a stable thread identifier within a repository, 1–80 ASCII letters, digits, dots, underscores or hyphens. Other fields are at most 600 characters. Follow with the actual research command. Where warranted, emit single-line `GCL_FINDING: ...`, `GCL_NEXT: ...` or `GCL_BLOCKER: ...` statements in its captured output, based on the observed result. Never emit speculative success as a finding or disclose private material; the existing public research designation and credential redaction rules apply unchanged. Do not add shell calls solely for narration. The viewer timestamps the statements at the observed request or result boundary, not at an invented intermediate instant. Findings are researcher-authored, not certification. Untagged public executions show their actual command and output without invented context. Evidence remains expandable, including full published commands, outputs, revisions, exit codes and redactions. This remains a bounded current-epoch view; missing history is not reconstructed.
