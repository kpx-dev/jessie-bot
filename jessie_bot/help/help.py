import json
import logging
from pathlib import Path
from hermes.common.lex_utils import success, error

logger = logging.getLogger(__name__)

script_path = Path.cwd().joinpath('hermes/help/script.json')
with script_path.open() as f: script = json.load(f)


def handler(event, context):
    help_text = '\n'.join(script['help_text'])

    return success(message=help_text)


if __name__ == '__main__':
    res = handler(event={}, context={})

    print(json.dumps(res, indent=3))