import runpy
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
DB = SRC / 'banco.db'

if DB.exists():
    DB.unlink()

sys.path.insert(0, str(SRC))


class PruebaScriptTest(unittest.TestCase):
    def test_prueba_debe_ejecutarse_sin_crash_si_la_base_esta_vacia(self):
        runpy.run_path(str(SRC / 'prueba.py'), run_name='__main__')


if __name__ == '__main__':
    unittest.main()
