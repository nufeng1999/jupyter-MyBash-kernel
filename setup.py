from setuptools import setup

setup(name='jupyter_MyBash_kernel',
      version='0.0.1',
      description='Minimalistic shellscript kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyBash-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyBash-kernel/tarball/0.0.1',
      packages=['jupyter_MyBash_kernel'],
      scripts=['jupyter_MyBash_kernel/install_MyBash_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'shell','shellscript','Bash','sh'],
      include_package_data=True
      )
