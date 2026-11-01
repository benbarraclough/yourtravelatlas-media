"""Full landscape context and source size guards for archival transport images."""
import importlib.util,unittest
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("landscape_renderer",root/"scripts/render.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class LandscapeContext(unittest.TestCase):
 def test_wide_source_retains_all_four_edges(self):
  source=Image.new("RGB",(1024,768),"red")
  item={"heading":"The coastal train","body":"Use Nice as a base for coastal rail outings.","date_label":"ARCHIVE · 2016","layout":"landscape"}
  image=m.draw_landscape(source,{},item)
  self.assertEqual(image.size,(1080,1350))
  self.assertEqual(image.getpixel((0,0)),(255,0,0))
  self.assertEqual(image.getpixel((1079,809)),(255,0,0))
 def test_inappropriate_tall_frame_and_overlong_copy_fail(self):
  item={"heading":"Train","body":"word "*31,"layout":"landscape"}
  with self.assertRaises(ValueError):m.draw_landscape(Image.new("RGB",(1024,768)),{},item)
  item["body"]="A short description."
  with self.assertRaises(ValueError):m.draw_landscape(Image.new("RGB",(1024,1500)),{},item)
