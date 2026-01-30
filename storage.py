import json
from pathlib import Path

class Storage:
    def __init__(self, path: str):
        self.path = Path(path)
        
    def load(self):
        if not self.path.exists():
            return []
        
        try:
            with open(self.path, "r", encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
        
    def save(self, data: list):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
