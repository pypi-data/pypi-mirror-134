
from pathlib import Path
import oyaml as yaml
from typing import OrderedDict

GLOBAL_CONFIG_PATH = Path().home() / ".devcontainer_manager" / "global_config.yaml"

def default_global_config():
    return OrderedDict(
        defaults=OrderedDict(
            devcontainer=OrderedDict(),
            dockerfile=OrderedDict()
        ),
    )

def get_global_config():
    if GLOBAL_CONFIG_PATH.exists():
        return yaml.load(GLOBAL_CONFIG_PATH.read_text())
    else:
        GLOBAL_CONFIG_PATH.parent.mkdir()
        GLOBAL_CONFIG_PATH.write_text(default_global_config())
        return default_global_config()