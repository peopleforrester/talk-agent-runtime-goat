# ABOUTME: Checks the submitted abstract files against the Sessionize limits and each other.
# ABOUTME: Run with `python3 -m unittest discover -s tests` from the repo root; stdlib only.

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SESSION = ROOT / "abstract" / "kubecon-eu-2027-session.md"
FIELDS = ROOT / "abstract" / "sessionize-fields.md"
README = ROOT / "README.md"

DESCRIPTION_LIMIT = 1000


def section(path, heading):
    """Return the stripped body under a level-2 heading, up to the next level-2 heading."""
    text = path.read_text(encoding="utf-8")
    marker = f"\n## {heading}\n"
    if marker not in text:
        raise AssertionError(f"{path.name} has no '## {heading}' section")
    return text.split(marker, 1)[1].split("\n## ", 1)[0].strip()


def h1(path):
    first = path.read_text(encoding="utf-8").splitlines()[0]
    if not first.startswith("# "):
        raise AssertionError(f"{path.name} does not open with a level-1 heading")
    return first[2:].strip()


def stated_count(path):
    """The character count the file's status line claims for the description."""
    match = re.search(r"\b(\d{3,4}) characters against|this text is (\d{3,4})\)",
                      path.read_text(encoding="utf-8"))
    if not match:
        raise AssertionError(f"{path.name} does not state the description length")
    return int(match.group(1) or match.group(2))


class DescriptionTest(unittest.TestCase):
    def setUp(self):
        self.session = section(SESSION, "Description (Sessionize field, max 1,000 characters)")
        self.fields = section(FIELDS, "Description")

    def test_within_sessionize_limit(self):
        for name, text in (("session", self.session), ("fields", self.fields)):
            with self.subTest(file=name):
                self.assertLessEqual(len(text), DESCRIPTION_LIMIT)

    def test_both_files_carry_the_same_text(self):
        self.assertEqual(self.session, self.fields)

    def test_stated_length_matches_actual(self):
        for path, text in ((SESSION, self.session), (FIELDS, self.fields)):
            with self.subTest(file=path.name):
                self.assertEqual(stated_count(path), len(text))


class TitleTest(unittest.TestCase):
    def test_titles_agree(self):
        title = section(FIELDS, "Session Title")
        self.assertEqual(section(SESSION, "Title"), title)
        self.assertEqual(h1(README), title)
        self.assertTrue(h1(SESSION).endswith(": " + title))
        self.assertTrue(h1(FIELDS).startswith(h1(SESSION) + " "))


class LayoutTest(unittest.TestCase):
    def test_readme_layout_paths_exist(self):
        rows = re.findall(r"^\| `([^`]+)` \|", section(README, "Layout"), re.MULTILINE)
        self.assertTrue(rows, "README Layout table lists no paths")
        for rel in rows:
            with self.subTest(path=rel):
                self.assertTrue((ROOT / rel).is_file(), f"{rel} is listed but missing")


class IdentityTest(unittest.TestCase):
    def test_agents_md_says_where_things_live(self):
        where = section(ROOT / "AGENTS.md", "Where things live")
        self.assertIn("talks-knowledge", where)
        self.assertIn("talks/register.md", where)
        self.assertIn("conference-knowledge", where)

    def test_readme_points_at_talks_knowledge(self):
        self.assertIn("talks-knowledge", README.read_text(encoding="utf-8"))

    def test_claude_md_links_to_agents_md(self):
        self.assertEqual((ROOT / "CLAUDE.md").readlink(), Path("AGENTS.md"))


class GateTest(unittest.TestCase):
    def test_agents_md_declares_or_explains_the_e2e_command(self):
        lines = (ROOT / "AGENTS.md").read_text(encoding="utf-8").splitlines()
        declared = [l for l in lines if re.fullmatch(r"E2E command: `[^`]+`", l)]
        explained = [l for l in lines if l.startswith("No E2E command yet: ")]
        self.assertEqual(len(declared) + len(explained), 1,
                         "AGENTS.md must declare one E2E command or say why it has none")


if __name__ == "__main__":
    unittest.main()
