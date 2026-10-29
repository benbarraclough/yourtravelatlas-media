"""Offline publication guards: every real brief must fit before photo downloads."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("renderer", ROOT / "scripts/render.py")
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class EditorialPublicationChecks(unittest.TestCase):
    def setUp(self):
        self.posts = [json.loads(p.read_text()) for p in sorted((ROOT / "content/posts").glob("*.json"))]
        self.post = next(p for p in self.posts if p.get("editorial_version", 0) >= 5)
        self.photo = Image.new("RGB", (2000, 1500), (105, 140, 150))

    def test_every_real_brief_passes_and_every_slide_fits(self):
        for post in self.posts:
            renderer.validate_editorial(post)
            for i, item in enumerate(post["slides"]):
                with self.subTest(issue=post["issue"], slide=i+1):
                    image = renderer.draw_slide(self.photo, post, item, i, len(post["slides"]))
                    self.assertEqual(image.size, (1080, 1350))

    def test_missing_or_misplaced_closing_card_stops_publication(self):
        for change in ("missing", "duplicate"):
            post = copy.deepcopy(self.post)
            if change == "missing":
                post["slides"][-1]["layout"] = "story"
            else:
                post["slides"][1]["layout"] = "cta"
            with self.assertRaisesRegex(ValueError, "closing card"):
                renderer.validate_editorial(post)

    def test_missing_research_and_review_stop_publication(self):
        for key in ("review", "fact_checks"):
            post = copy.deepcopy(self.post)
            del post["slides"][1][key]
            with self.assertRaises(ValueError):
                renderer.validate_editorial(post)

    def test_long_copy_is_rejected_instead_of_overlapping(self):
        item = copy.deepcopy(self.post["slides"][1])
        item["body"] = "This deliberately excessive body text must not cover a credit or footer. " * 20
        with self.assertRaises(ValueError):
            renderer.draw_slide(self.photo, self.post, item, 1, len(self.post["slides"]))

    def test_new_briefs_cannot_bypass_v5_and_caption_budget(self):
        post = copy.deepcopy(self.post)
        post.pop("editorial_version")
        with self.assertRaisesRegex(ValueError, "editorial_version"):
            renderer.validate_editorial(post)
        post = copy.deepcopy(self.post)
        post["caption"] = "x" * 2201
        with self.assertRaisesRegex(ValueError, "2200"):
            renderer.validate_editorial(post)


if __name__ == "__main__":
    unittest.main()
