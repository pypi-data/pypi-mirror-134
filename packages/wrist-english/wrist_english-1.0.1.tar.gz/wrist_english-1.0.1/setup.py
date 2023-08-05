from setuptools import setup, find_packages

setup(
    name='wrist_english',
    version='1.0.1',
    keywords='english',
    description='Lightweight online translation tool created for learners.',
    license='MIT License',
    url='https://github.com/wristwaking/python',
    author='唤醒手腕',
    author_email='1620444902@qq.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'requests>=2.26.0',
        'pypiwin32'
    ],
)
