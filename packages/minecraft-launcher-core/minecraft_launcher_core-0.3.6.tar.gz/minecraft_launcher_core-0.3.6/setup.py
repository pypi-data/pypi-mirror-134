from setuptools import setup,find_packages
with open('README.md') as f:
    long_description = f.read()


setup(name = 'minecraft_launcher_core',     # 包名
      version = '0.3.6',  # 版本号
      description = 'a package for launch minecraft,start minecraft server',
      long_description = long_description,
      long_description_content_type="text/markdown",
      author = 'jack253.png',
      author_email = 'guoxiuchen20170402@163.com',
      url = 'https://github.com',
      license = 'MIT',
      install_requires = ['requests'],
      classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
      ],
      keywords = '',
      packages = ['launch','minecraft_server'],  # 必填，就是包的代码主目录
      include_package_data = True,
)