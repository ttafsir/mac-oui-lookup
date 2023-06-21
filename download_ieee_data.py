import json
import re
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional

IEEE_URL = "https://standards-oui.ieee.org/"
MAC_TO_COMPANY_RE = re.compile(r"([0-9A-F-]+)\s+\(hex\)\s+(.+?)\n", re.VERBOSE)


def download_ieee_data() -> Optional[str]:
    """Download MAC OUI data from IEEE site"""
    req = urllib.request.Request(IEEE_URL, method="GET")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


def parse(text_str: str) -> Dict:
    """Parse text data from IEEE"""
    matches = MAC_TO_COMPANY_RE.findall(text_str)
    return {match[0]: match[1].strip() for match in matches}


if __name__ == "__main__":
    ieee_data = download_ieee_data()
    if ieee_data:
        parsed_data = parse(ieee_data)
        sorted_data = dict(sorted(parsed_data.items(), key=lambda item: item[1]))
        Path("latest_oui_lookup.json").write_text(
            json.dumps(sorted_data, indent=4, ensure_ascii=False), encoding="utf-8"
        )
