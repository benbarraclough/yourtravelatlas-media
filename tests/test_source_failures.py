"""A failed source must block its edition without losing independent ready editions."""
import importlib.util,json,tempfile,sys,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("batch_renderer",ROOT/"scripts/render.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class SourceIsolation(unittest.TestCase):
 def test_network_failure_is_recorded_and_next_edition_runs(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);inp=root/"posts";inp.mkdir()
   for i in (1,2):
    (inp/f"{i:03d}.json").write_text(json.dumps({"editorial_version":7,"issue":i,"slug":f"{i:03d}-test","slides":[]}))
   seen=[]
   def build(path):
    seen.append(path.name)
    if path.name=="001.json":raise m.requests.HTTPError("429 source unavailable")
   with patch.object(m,"ROOT",root),patch.object(m,"INPUT",inp),patch.object(m,"build",side_effect=build),patch.object(sys,"argv",["render.py"]):
    m.main()
   errors=json.loads((root/"review/render-errors.json").read_text())
   self.assertEqual(seen,["001.json","002.json"])
   self.assertEqual(len(errors),1)
   self.assertEqual(errors[0]["slug"],"001-test")
   self.assertEqual(errors[0]["status"],"blocked_source_download")
