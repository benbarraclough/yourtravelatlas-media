"""Offline checks for editorial omissions, text overflow and final-card layout."""
import copy
import json
import unittest
from pathlib import Path

from PIL import Image
import render


class EditorialRendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.posts = [json.loads(p.read_text()) for p in sorted(render.INPUT.glob("*.json")) if p.name != "001-faroe-islands.json"]
        cls.photo = Image.new("RGB", (2000, 1500), (65, 120, 135))

    def test_actual_current_briefs_fit_all_layouts(self):
        for post in self.posts:
            render.validate_editorial(post)
            for i, slide in enumerate(post["slides"]):
                with self.subTest(issue=post["issue"], slide=i+1):
                    self.assertEqual(render.draw_slide(self.photo, post, slide, i, len(post["slides"])).size, render.SIZE)

    def test_overflow_fails_instead_of_covering_footer(self):
        post = copy.deepcopy(self.posts[0])
        slide = next(s for s in post["slides"] if s.get("layout") == "photo")
        slide["body"] = "A detailed but impossibly long paragraph. " * 80
        with self.assertRaises(ValueError):
            render.draw_slide(self.photo, post, slide, 1, len(post["slides"]))

    def test_no_final_card_or_no_source_ledger_fails(self):
        for mutation in ("cta", "source", "review", "version", "caption"):
            post = copy.deepcopy(self.posts[0])
            if mutation == "cta": post["slides"][-1]["layout"] = "story"
            if mutation == "source": post["slides"][1]["fact_checks"] = []
            if mutation == "review": post["slides"][1]["review"] = {}
            if mutation == "version": post.pop("editorial_version")
            if mutation == "caption": post["caption"] = "x" * 2201
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                render.validate_editorial(post)


if __name__ == "__main__":
    unittest.main()
