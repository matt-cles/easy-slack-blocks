import setuptools

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name='easy-slack-blocks',
    version='1.0.1',
    author='Matthew Cles',
    author_email='matthew@cles.dev',
    description='An easy way to format Slack Blocks.',
    long_description=readme,
    long_description_content='text/markdown',
    url='https://github.com/matt-cles/easy-slack-blocks/',
    packages=setuptools.find_packages(),
    license="MIT",
)
