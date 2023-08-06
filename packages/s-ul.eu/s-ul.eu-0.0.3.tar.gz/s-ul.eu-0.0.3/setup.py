import setuptools

setuptools.setup(
    name="s-ul.eu",
    version="0.0.3",
    author="Rukchad Wongprayoon",
    author_email="contact@biomooping.tk",
    description="s-ul.eu API wrapper.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://s-ul.rukchadisa.live",
    packages=["suleu"],
    package_dir={"suleu": "src/suleu"},
    install_requires=open("./requirements.txt").readlines(),
    classifiers=[],
)
