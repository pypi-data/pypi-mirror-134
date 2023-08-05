import setuptools

setuptools.setup(
    name="tunnelis_core",
    version="1.6.4",
    author="Pedro Melo, Rafael Arrais, Sergio Marinho",
    author_email="pedro.m.melo@inesctec.pt, rafael.l.arrais@inesctec.pt, sergio.d.marinho@inesctec.pt",
    description="Python package containing common classes and data structures required by Tunnelis.",
    packages=setuptools.find_packages(),
    install_requires=[
        "grpcio",
        "grpcio-tools",
        "tornado",
        "zmq"
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6'
)
