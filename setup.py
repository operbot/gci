# This file is placed in the Public Domain.


"Assembly. Court. Prosecutor. Reconsider OTP-CR-117/19."


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="gci",
    version="1",
    author="Bart Thate",
    author_email="operbot100@gmail.com",
    url="http://github.com/operbot/gci",
    description="Assembly. Court. Prosecutor. Reconsider OTP-CR-117/19.",
    long_description=read(),
    license="Public Domain",
    packages=["gci"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python",
        "Intended Audience :: System Administrators",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
