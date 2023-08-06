import os
import hashlib
from typing import Any, Dict
import pandas as pd


def is_member_variable(obj, identifier):
    return not callable(getattr(obj, identifier)) and \
        not identifier.startswith("__")


def hash_config(config):
    config_pairs = list(config.items())
    string = str(sorted(config_pairs))
    return hashlib.sha512(string.encode()).hexdigest()


def config_from_args(args, file=None) -> Dict[str, Any]:
    config = {} if file is None else {'file': file}
    for ident in dir(args):
        if is_member_variable(args, ident):
            config[ident] = getattr(args, ident)
    return config


# FUTURE: add testing, writing reading files in test cases?
def write_results(config: Dict[str, Any], results: Dict[str, Any]) -> None:
    identifier = hash_config(config)

    combined = {'id': identifier, **config, **results}

    frame = pd.DataFrame([combined], columns=list(combined.keys()))
    frame = frame.set_index('id')

    os.makedirs('args_to_db_cache', exist_ok=True)

    frame.to_pickle(f'args_to_db_cache/{identifier}.pkl')
    # frame.to_csv(f'args_to_db_cache/{id}.csv')
