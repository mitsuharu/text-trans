from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='texttrans', # パッケージ名(プロジェクト名)
    packages=['texttrans'], # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定

    version='1.0.0', # バージョン

    license='MIT', # ライセンス

    install_requires=[],

    author='Mitsuharu Emoto', # パッケージ作者の名前
    author_email='mthr1982+python@gmail.com', # パッケージ作者の連絡先メールアドレス

    url='https://github.com/mitsuharu/text-trans', # パッケージに関連するサイトのURL(GitHubなど)

    description='To computes transition probability of text', # パッケージの簡単な説明
    long_description=long_description, # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown' # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    keywords='texttrans text-trans', # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
