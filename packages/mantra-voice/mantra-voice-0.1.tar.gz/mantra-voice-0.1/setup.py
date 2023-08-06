from distutils.core import setup
install_requires = []
with open("./requirements.txt") as f:
    install_requires.extend([x.strip("\n") for x in f.readlines()])

setup(
    name="mantra-voice",
    packages=["mantra_voice"],
    version="0.1",
    license="MIT",
    description="A speech to text library that builds on top of gTTS and pyttsx3.",
    author="Philippe Mathew",
    author_email="philmattdev@gmail.com",
    url="https://github.com/bossauh/mantra-voice",
    download_url="https://github.com/bossauh/mantra-voice/archive/refs/tags/v_01.tar.gz",
    keywords=["speech", "synthesizer"],
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
