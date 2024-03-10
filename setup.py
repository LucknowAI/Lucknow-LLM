from setuptools import setup, find_packages

setup(
    name='lucknowllm',
    version='0.1',
    packages=find_packages(),
    description='llm for lucknow',
    long_description=open('README.md').read(),
    author='Lucknow AI Labs Team',
    url='https://github.com/LucknowAI/Lucknow-LLM',
    package_data={
        '': ['*.txt', '*.md', '*.json'],  # Add other file types as needed.
        'lucknowllm': ['data/*', 'data/*/*', 'data/*/*/*'],  # Assuming 'data' is directly inside the 'lucknowllm' package.
    },
    include_package_data=True,
)
