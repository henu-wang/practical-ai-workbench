import hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def source_hash():
 paths=[]
 for name in ['recipes','templates']:
  paths.extend(p for p in (ROOT/name).rglob('*') if p.is_file())
 paths.extend(ROOT/name for name in ['scripts/build.py','recipes.json','docs/assets/style.css'])
 digest=hashlib.sha256()
 for path in sorted(paths,key=lambda p:p.relative_to(ROOT).as_posix()):
  digest.update(path.relative_to(ROOT).as_posix().encode()+b'\0'+path.read_bytes()+b'\0')
 return digest.hexdigest()
if __name__=='__main__':print(source_hash())
