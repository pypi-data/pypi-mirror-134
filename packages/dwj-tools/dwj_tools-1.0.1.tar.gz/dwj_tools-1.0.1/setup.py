from setuptools import setup, find_packages

setup(
    name='dwj_tools', # 项目的名称,pip3 install get-time
    version='1.0.1', # 项目版本 
    author='丁文杰', # 项目作者 
    author_email='359582058@qq.com', # 作者email
    url='https://github.com/buwu-DWJ/strategy', # 项目代码仓库
    description='私人', # 项目描述
    packages=find_packages(), # 包名
    install_requires=[],
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.h5"],
    },
    entry_points={} # 重点
)

# 1.先更新版本号
# 2.生成新上传代码
# python setup.py sdist build
# 3.推送
# twine upload dist/*