from setuptools import find_packages, setup


setup(
    name='eyja-redis',
    zip_safe=True,
    version='0.1.1',
    description='Redis Plugin for Eyja',
    url='https://gitlab.com/public.eyja.dev/eyja-redis',
    maintainer='Anton Berdnikov',
    maintainer_email='agratoth@yandex.ru',
    packages=find_packages(),
    package_dir={'eyja_redis': 'eyja_redis'},
    install_requires=[
        'eyja-internal>==0.3.14',
        'aioredis>=2.0.0',
        'python-slugify>=5.0.2',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.8',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
