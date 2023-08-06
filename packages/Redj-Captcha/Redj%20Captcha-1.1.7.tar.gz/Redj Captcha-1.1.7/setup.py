import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    version='1.1.7',
    author='redj_ai',
    name='Redj Captcha',
    url='https://redj.ai/',
    author_email='info@redj.ai',
    long_description=long_description,
    install_requires=['Pillow==9.0.0'],
    long_description_content_type="text/markdown",
    description='Django / Rest Framework Captcha',
    project_urls={
        "Bug Tracker": "https://redj.ai/",
    },
    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires=">=3",
    package_dir={"": "src"},
    package_data= {'redjcaptcha.management.fonts': ['*','*/*','*/*/*']},
    packages=setuptools.find_packages(where="src"),
)
