"""Test documentation quality and presence."""
import os
import re
from pathlib import Path

def test_readme_exists():
    """Verify README file exists and is not empty."""
    assert os.path.isfile("README.md"), "Missing README.md file"
    assert os.path.getsize("README.md") > 100, "README.md appears incomplete"

def test_readme_format():
    """Check README contains required sections."""
    readme = Path("README.md").read_text(encoding="utf-8")
    sections = {
        "installation": r"#+\s*installation",
        "usage": r"#+\s*usage",
        "features": r"#+\s*features",
        "development": r"#+\s*development",
        "contributing": r"#+\s*contributing"
    }
    
    for section, pattern in sections.items():
        assert re.search(pattern, readme, re.IGNORECASE), \
            f"Missing '{section}' section in README.md"
