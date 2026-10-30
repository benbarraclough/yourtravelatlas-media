"""Regression tests for format routing, identity and footage gates."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module
render, reel = load('render'), load('render_reel')

class FormatChecks(unittest.TestCase):
    def setUp(self):
        self.post=json.loads((ROOT/'content/posts/002-porto-slow-weekend.json').read_text())
        self.post.update(editorial_version=7, content_type='discovery')
        self.photo=Image.new('RGB',(2000,1500),(50,100,130))
    def test_both_formats_fit_every_page(self):
        for kind in ('discovery','collection'):
            post=copy.deepcopy(self.post);post['content_type']=kind
            if kind=='collection':post['collection_number']=2
            render.validate_editorial(post)
            for i,s in enumerate(post['slides']):
                self.assertEqual(render.draw_slide(self.photo,post,s,i,len(post['slides'])).size,(1080,1350))
    def test_public_numbers_and_tagline(self):
        original=render.ImageDraw.ImageDraw.text
        for kind in ('collection','discovery'):
            post=copy.deepcopy(self.post);post['content_type']=kind
            if kind=='collection':post['collection_number']=2
            words=[]
            def capture(obj, xy, text, *args, **kwargs):
                words.append(str(text));return original(obj,xy,text,*args,**kwargs)
            with patch.object(render.ImageDraw.ImageDraw,'text',capture):
                render.draw_slide(self.photo,post,post['slides'][0],0,len(post['slides']))
            joined=' '.join(words)
            self.assertNotIn('WANDER FURTHER',joined)
            self.assertEqual('COLLECTION  /  002' in joined,kind=='collection')
            self.assertNotIn('ISSUE',joined)
    def test_bad_format_or_number_rejected(self):
        for updates in ({'content_type':'unknown'}, {'content_type':'collection'}, {'content_type':'collection','collection_number':1}, {'collection_number':2}):
            post=copy.deepcopy(self.post);post.update(updates)
            with self.assertRaises(ValueError):render.validate_editorial(post)
    def test_legacy_routing_remains_discovery(self):
        # Legacy routing remains covered by existing real-brief tests.
        post=copy.deepcopy(self.post);post['editorial_version']=6
        for i,s in enumerate(post['slides']):
            self.assertEqual(render.draw_slide(self.photo,post,s,i,len(post['slides'])).tobytes(),render.draw_discovery(self.photo,post,s,i,len(post['slides'])).tobytes())

class ReelChecks(unittest.TestCase):
    def test_four_shot_exception_fails(self):
        brief=json.loads((ROOT/'content/reels/004-behind-the-waterfall.json').read_text())
        with self.assertRaisesRegex(ValueError,'5-8'):reel.validate_shots(brief)
    def test_repeated_download_does_not_count_as_new_shot(self):
        brief={'clips':[{'page_url':str(i),'download_url':'same'} for i in range(5)]}
        with self.assertRaisesRegex(ValueError,'Duplicate'):reel.validate_shots(brief)
    def test_distinct_five_pass_and_missing_v7_context_fails(self):
        brief={'clips':[{'page_url':str(i),'download_url':str(i)} for i in range(5)]}
        reel.validate_shots(brief)
        brief['editorial_version']=7
        with self.assertRaisesRegex(ValueError,'location_evidence'):reel.validate_shots(brief)
