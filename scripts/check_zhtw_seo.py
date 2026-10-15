# -*- coding: utf-8 -*-
import os
import re

zhtw_dir = r"F:\Ramana\pages\zh-TW"
canonical_errors = []
missing_hreflang = []
missing_canonical = []
total_pages = 0

for root, dirs, files in os.walk(zhtw_dir):
    for f in files:
        if f.lower().endswith(".html"):
            total_pages += 1
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8") as file:
                c = file.read()
            
            canon_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', c)
            if canon_match:
                url = canon_match.group(1)
                if "/zh-TW" not in url:
                    canonical_errors.append((fp, url))
            else:
                missing_canonical.append(fp)

            has_zhtw = ('hreflang="zh-TW"' in c) or ('hreflang="zh-Hant"' in c)
            if not has_zhtw:
                missing_hreflang.append(fp)

print("=" * 60)
print(f"zh-TW HTML files: {total_pages}")
print(f"Canonical pointing to non-zh-TW: {len(canonical_errors)}")
print(f"Missing canonical: {len(missing_canonical)}")
if missing_canonical:
    print("Missing canonical files:")
    for fp in missing_canonical:
        print(f"  {fp}")
print(f"Missing zh-TW hreflang: {len(missing_hreflang)}")
if canonical_errors:
    print("Sample canonical errors:")
    for fp, url in canonical_errors[:5]:
        print(f"  {os.path.basename(fp)} -> {url}")
print("=" * 60)
