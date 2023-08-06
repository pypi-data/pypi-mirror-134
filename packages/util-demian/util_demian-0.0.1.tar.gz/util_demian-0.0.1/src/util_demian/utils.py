import os
import json

import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)


def get_json(path: str):
    # 치과의 json 파일을 불러온다.
    with open(os.path.join(path), 'r', encoding='UTF8') as f:
        json_data = json.load(f)
    logger.info(json_data)
    return json_data