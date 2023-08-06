import setuptools

setuptools.setup(
    name="s-ul.eu",
    version="0.0.1",
    author="Rukchad Wongprayoon",
    author_email="contact@biomooping.tk",
    short_description="s-ul.eu API wrapper",
    description=open("README.md").read(),
    url="https://s-ul.rukchadisa.live",
    packages=["suleu"],
    package_dir={"suleu": "src/suleu"},
    install_requires=open("./requirements.txt").readlines(),
    classifiers=[],
)
