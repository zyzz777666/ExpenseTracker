import json


class Convert:
    data = {}

    @staticmethod
    def record_files(file: str):
        with open(file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(Convert.data, ensure_ascii=False))

    @staticmethod
    def output_files(file):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                Convert.data = json.load(f)
        except json.JSONDecodeError:
            Convert.record_files('task.json')
