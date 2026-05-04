#!/usr/bin/env python3
"""
Generate self-contained HTML renderings of every report (DOCX) and runbook (MD)
in this repository, and a top-level index.html landing page.

Usage:
    python3 .html-tools/build-html.py

Re-run any time the underlying DOCX or MD changes.
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / ".html-tools"
CSS = TOOLS / "style.css"

DOCS_PAGES = [
    ("docs/about-csw",                 "Background — What is Cisco Secure Workload?"),
    ("docs/why-these-mappings-matter", "Why these mappings matter"),
    ("docs/audience-and-usage",        "Audience and usage guide"),
]

FRAMEWORKS = [
    ("HIPAA",         "HIPAA Security Rule",                        "HIPAA/CSW-HIPAA-Compliance-Report",          "HIPAA/CSW-HIPAA-Technical-Runbook"),
    ("SOC2",          "SOC 2 Type II",                              "SOC2/CSW-SOC2-Compliance-Report",            "SOC2/CSW-SOC2-Technical-Runbook"),
    ("PCI-DSS-v4",    "PCI DSS v4.0",                               "PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report",   "PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook"),
    ("NIST-800-53",   "NIST SP 800-53 Rev 5",                       "NIST-800-53/CSW-NIST-800-53-Compliance-Report","NIST-800-53/CSW-NIST-800-53-Technical-Runbook"),
    ("ISO-27001-2022","ISO/IEC 27001:2022",                         "ISO-27001-2022/CSW-ISO27001-Compliance-Report","ISO-27001-2022/CSW-ISO27001-Technical-Runbook"),
    ("CISA-ZeroTrust","CISA Zero Trust Maturity Model",             "CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report","CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook"),
    ("FIPS-140",      "FIPS 140",                                   "FIPS-140/CSW-FIPS-Compliance-Report",        "FIPS-140/CSW-FIPS-Technical-Runbook"),
    ("NIST-800-207",  "NIST SP 800-207 (ZTA Seven Tenets)",         "NIST-800-207/CSW-NIST-800-207-Compliance-Report","NIST-800-207/CSW-NIST-800-207-Technical-Runbook"),
    ("NIST-800-207A", "NIST SP 800-207A (PDP/PEP/PA/PIP)",          "NIST-800-207A/CSW-NIST-800-207A-Compliance-Report","NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook"),
    ("DORA",          "DORA (EU 2022/2554)",                        "DORA/CSW-DORA-Compliance-Report",            "DORA/CSW-DORA-Technical-Runbook"),
    ("NIS2",          "NIS2 (EU 2022/2555)",                        "NIS2/CSW-NIS2-Compliance-Report",            "NIS2/CSW-NIS2-Technical-Runbook"),
    ("NERC-CIP",      "NERC CIP (Bulk Electric System)",            "NERC-CIP/CSW-NERC-CIP-Compliance-Report",    "NERC-CIP/CSW-NERC-CIP-Technical-Runbook"),
    ("TSA-Pipeline",  "TSA Pipeline Security Directive",            "TSA-Pipeline/CSW-TSA-Pipeline-Compliance-Report","TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook"),
    ("CIS-Controls-v8","CIS Critical Security Controls v8.1",       "CIS-Controls-v8/CSW-CIS-Compliance-Report",  "CIS-Controls-v8/CSW-CIS-Technical-Runbook"),
    ("NIST-CSF-2",    "NIST Cybersecurity Framework 2.0",           "NIST-CSF-2/CSW-CSF-Compliance-Report",       "NIST-CSF-2/CSW-CSF-Technical-Runbook"),
    ("CMMC-2",        "CMMC 2.0",                                   "CMMC-2/CSW-CMMC-Compliance-Report",          "CMMC-2/CSW-CMMC-Technical-Runbook"),
]


def run_pandoc(input_path: Path, output_path: Path, title: str, source_label: str, source_href: str) -> None:
    """Render a single source (md or docx) to a self-contained HTML file."""
    header = TOOLS / "_inline-header.html"
    header.write_text(
        f'<style>\n{CSS.read_text()}\n</style>\n', encoding="utf-8"
    )
    before_body = TOOLS / "_before-body.html"
    before_body.write_text(
        f'<div class="doc-meta">'
        f'Source: <a href="{source_href}">{source_label}</a> &middot; '
        f'<a href="../index.html">repository index</a>'
        f'</div>\n',
        encoding="utf-8",
    )

    cmd = [
        "pandoc",
        "--standalone",
        "--embed-resources",
        "--from", "markdown" if input_path.suffix == ".md" else "docx",
        "--to", "html5",
        "--metadata", f"title={title}",
        "--metadata", "lang=en",
        "--include-in-header", str(header),
        "--include-before-body", str(before_body),
        "--toc",
        "--toc-depth=3",
        "-o", str(output_path),
        str(input_path),
    ]
    subprocess.run(cmd, check=True)
    header.unlink(missing_ok=True)
    before_body.unlink(missing_ok=True)


HREF_MD_RE = re.compile(r'(href="[^"]+?)\.md(["#])')
ABS_REPO_RE = re.compile(r'href="(?:\.\./)+(?:[^"/]+/)*?_csw-compliance-mapping-staging/')


def rewrite_links(html_path: Path) -> None:
    """Post-process pandoc HTML so cross-links work in the rendered tree.

    1. href="...something.md"  -> href="...something.html"
    2. Strip pandoc's absolute-filesystem leakage so links resolve inside the
       published site rather than the author's home directory.
    """
    text = html_path.read_text(encoding="utf-8")
    # Strip the absolute-filesystem prefix back to repo-root relative.
    new = ABS_REPO_RE.sub('href="', text)
    # Then rewrite .md -> .html on whatever's left.
    new = HREF_MD_RE.sub(r"\1.html\2", new)

    # If a link from inside framework/ now points to "framework/foo" (because
    # the absolute strip left the framework prefix in place), drop the
    # redundant prefix when current file is in the same framework folder.
    rel_dir = html_path.parent.name  # e.g. "DORA"
    if rel_dir and rel_dir != html_path.parent.parent.name:
        new = new.replace(f'href="{rel_dir}/', 'href="')

    if new != text:
        html_path.write_text(new, encoding="utf-8")


def build_index(report_html_paths: list[tuple[str, str, str]]) -> None:
    """Write top-level index.html linking to all rendered assets."""
    rows = []
    for fw_label, report_html, runbook_html in report_html_paths:
        rows.append(
            f'    <tr>'
            f'<td>{fw_label}</td>'
            f'<td><a href="{report_html}">Report</a></td>'
            f'<td><a href="{runbook_html}">Runbook</a></td>'
            f'</tr>'
        )

    index_template = (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>Cisco Secure Workload &mdash; Compliance Mapping</title>\n"
        f"<style>\n{CSS.read_text()}\n</style>\n"
        "</head>\n<body>\n"
        "<h1>Cisco Secure Workload &mdash; Compliance Mapping Assets</h1>\n"
        "<p>Browseable HTML renderings of the customer-facing reports and the matching "
        "technical runbooks for sixteen compliance, sector, and zero-trust frameworks. "
        "DOCX (editable master), PDF (review copy), and Markdown (runbook source) "
        "remain in the repository and on each framework's GitHub folder page.</p>\n"
        '<p><strong>Repository:</strong> '
        '<a href="https://github.com/chandrapati/CSW-Compliance-Mapping">'
        "chandrapati/CSW-Compliance-Mapping</a></p>\n"
        '<h2>Start here</h2>\n'
        '<ul>\n'
        '  <li><a href="README.html">Repository README</a> &mdash; '
        "compliance-mapping focus, asset library, scope notes, and disclaimer.</li>\n"
        '  <li><a href="docs/about-csw.html">Background &mdash; What is Cisco Secure Workload?</a>'
        " &mdash; one-page intro to the platform.</li>\n"
        '  <li><a href="docs/why-these-mappings-matter.html">Why these mappings matter</a>'
        " &mdash; conversation-starter questions to ask about your own environment.</li>\n"
        '  <li><a href="docs/audience-and-usage.html">Audience and usage guide</a>'
        " &mdash; who reads what, runbook-vs-report, file formats, and folder layout.</li>\n"
        '  <li><a href="INDEX.html">Control-ID Index</a> &mdash; '
        "lookup across all sixteen frameworks (PCI Req 1.2, HIPAA \u00a7164.312(a)(1), "
        "DORA Art. 9, NIS2 Art. 21(2)(d), NIST AC-4, NERC CIP-005 R1, "
        "TSA SD Section III.A, CIS Safeguard 13.4, CSF PR.IR-01, "
        "CMMC AC.L2-3.1.1, etc.).</li>\n"
        "</ul>\n"
        '<h2>Frameworks</h2>\n'
        '<table>\n'
        '<thead><tr><th>Framework</th><th>Customer report</th><th>Technical runbook</th></tr></thead>\n'
        '<tbody>\n'
        + "\n".join(rows)
        + "\n</tbody>\n</table>\n"
        "<hr>\n"
        '<p style="font-size:.85rem;color:var(--fg-muted);">Rendered with pandoc; '
        "see <code>.html-tools/build-html.py</code> in the repository to regenerate.</p>\n"
        "</body></html>\n"
    )
    (ROOT / "index.html").write_text(index_template, encoding="utf-8")


def main() -> int:
    if not shutil.which("pandoc"):
        print("ERROR: pandoc not found in PATH", file=sys.stderr)
        return 1

    rendered = []
    for fw_id, fw_label, report_stem, runbook_stem in FRAMEWORKS:
        report_docx = ROOT / f"{report_stem}.docx"
        report_html = ROOT / f"{report_stem}.html"
        runbook_md  = ROOT / f"{runbook_stem}.md"
        runbook_html = ROOT / f"{runbook_stem}.html"

        if not report_docx.exists():
            print(f"SKIP report (missing): {report_docx}")
        else:
            print(f"  report  -> {report_html.relative_to(ROOT)}")
            run_pandoc(report_docx, report_html, f"{fw_label} \u2014 Compliance Report",
                       report_docx.name, report_docx.name)
            rewrite_links(report_html)

        if not runbook_md.exists():
            print(f"SKIP runbook (missing): {runbook_md}")
        else:
            print(f"  runbook -> {runbook_html.relative_to(ROOT)}")
            run_pandoc(runbook_md, runbook_html, f"{fw_label} \u2014 Technical Runbook",
                       runbook_md.name, runbook_md.name)
            rewrite_links(runbook_html)

        rendered.append((
            fw_label,
            str(report_html.relative_to(ROOT)),
            str(runbook_html.relative_to(ROOT)),
        ))

    # docs/ background pages (rendered into docs/*.html alongside the source).
    # These live one folder deep so they reuse run_pandoc(), which already
    # writes a "../index.html" link in the doc-meta banner.
    for stem, title in DOCS_PAGES:
        src = ROOT / f"{stem}.md"
        out = ROOT / f"{stem}.html"
        if not src.exists():
            print(f"SKIP docs (missing): {src}")
            continue
        print(f"  docs    -> {out.relative_to(ROOT)}")
        run_pandoc(src, out, title, src.name, src.name)
        rewrite_links(out)

    # Top-level docs (INDEX.md, README.md)
    for src_name in ("INDEX.md", "README.md"):
        src = ROOT / src_name
        if not src.exists():
            continue
        out = ROOT / f"{src.stem}.html"
        title = "Control-ID Index" if src_name == "INDEX.md" else "Cisco Secure Workload \u2014 Compliance Mapping Assets"
        # For top-level files, "back to repo index" shouldn't escape one folder up.
        header = TOOLS / "_inline-header.html"
        header.write_text(f'<style>\n{CSS.read_text()}\n</style>\n', encoding="utf-8")
        before_body = TOOLS / "_before-body.html"
        before_body.write_text(
            f'<div class="doc-meta">'
            f'Source: <a href="{src_name}">{src_name}</a> &middot; '
            f'<a href="index.html">repository index</a>'
            f'</div>\n',
            encoding="utf-8",
        )
        cmd = [
            "pandoc",
            "--standalone",
            "--embed-resources",
            "--from", "markdown",
            "--to", "html5",
            "--metadata", f"title={title}",
            "--metadata", "lang=en",
            "--include-in-header", str(header),
            "--include-before-body", str(before_body),
            "-o", str(out),
            str(src),
        ]
        print(f"  toplvl  -> {out.relative_to(ROOT)}")
        subprocess.run(cmd, check=True)
        header.unlink(missing_ok=True)
        before_body.unlink(missing_ok=True)
        rewrite_links(out)

    # Landing page
    build_index(rendered)
    print(f"  landing -> index.html")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
