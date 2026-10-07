import hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def source_hash():
 paths=[]
 for name in ['content','docs/assets','docs/vendor']:
  paths.extend(p for p in (ROOT/name).rglob('*') if p.is_file())
 paths.append(ROOT/'scripts/build.py')
 digest=hashlib.sha256()
 for path in sorted(paths,key=lambda p:p.relative_to(ROOT).as_posix()):
  digest.update(path.relative_to(ROOT).as_posix().encode()+b'\0'+path.read_bytes()+b'\0')
 return digest.hexdigest()
if __name__=='__main__':print(source_hash())
