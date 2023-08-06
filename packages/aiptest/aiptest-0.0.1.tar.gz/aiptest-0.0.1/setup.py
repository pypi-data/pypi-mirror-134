from setuptools import setup, find_packages 
import codecs
import os 

name='aiptest'

def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), "r",encoding='utf-8').read()


def get_version(): 
    version_file = name + '/version.py'
    with open(version_file, 'r', encoding='utf-8') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']
    '''
    return '0.0.1'
    ''' 

setup(
    name=name,
    version=get_version(),
    description="pytest接口测试",
    author='zrr',#作者
    author_email="781103544@qq.com",
    url="https://gitee.com/zrr/apitest",
    packages=find_packages(exclude=[]), # 排除不生效？
    # 任何包如果包含 *.txt or *.rst 文件都加进去，可以处理多层package目录结构 
    package_data={'': ['*.js','*.css','*.map'],},
    install_requires=['requests'], # 未添加依赖
    python_requires='>=3.7', 
)

