# coding: utf-8
import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')
PACKAGE_SITE_DIR = os.path.join(BASE_DIR, 'packages')

module_path = next(filter(lambda s: s.endswith('-main-base.yml'), os.listdir(BASE_DIR)))
module_path = os.path.join(BASE_DIR, module_path)

with open(module_path, 'rb') as f:
    file_content = f.read()
    try:
        module_data = yaml.safe_load(file_content.decode('utf-8'))
    except UnicodeDecodeError:
        module_data = yaml.safe_load(file_content.decode('gbk'))
    PRODUCT_ID = module_data['biz']['app']['lower-code']
    PRODUCT_NAME = module_data['biz']['module']['name']
    PORT = module_data['server']['port']


if __name__ == '__main__':
    import pprint
    data = globals()
    del data['module_data']
    pprint.pprint(data)
