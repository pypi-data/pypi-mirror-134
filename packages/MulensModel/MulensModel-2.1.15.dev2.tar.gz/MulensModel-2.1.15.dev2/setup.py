from pathlib import Path

from setuptools import Extension, find_packages, setup

PROJECT_PATH = Path(__file__).resolve().parent
SOURCE_PATH = PROJECT_PATH / "source"
DATA_PATH = PROJECT_PATH / "data"

file_required = PROJECT_PATH / "requirements.txt"
with file_required.open() as file_:
    install_requires = file_.read().splitlines()

version = "unknown"
with Path(SOURCE_PATH / "MulensModel" / "version.py").open() as in_put:
    for line_ in in_put.readlines():
        if line_.startswith('__version__'):
            version = line_.split()[2][1:-1]

source_VBBL = SOURCE_PATH / "VBBL"
source_AC = SOURCE_PATH / "AdaptiveContouring"
source_MM = SOURCE_PATH / "MulensModel"
source_MMmo = source_MM / "mulensobjects"

# Read all files from data/ in format adequate for data_files option of setup.
files = [f.relative_to(PROJECT_PATH) for f in DATA_PATH.rglob("*") if f.is_file()]
data_files = {str(f): str(f) for f in files}

# C/C++ Extensions
ext_AC = Extension('MulensModel.AdaptiveContouring',
                   sources=[str(f) for f in source_AC.glob("*.c")],
                   libraries=["m"]
                )
ext_VBBL = Extension('MulensModel.VBBL',
                     sources=[str(f) for f in source_AC.glob("*.cpp")],
                     libraries=["m"]
                )

setup(
    name='MulensModel',
    version=version,
    url='https://github.com/rpoleski/MulensModel',
    project_urls={
        'documentation': 'https://github.com/rpoleski/MulensModel'},
    ext_modules=[ext_AC, ext_VBBL],
    author='Radek Poleski',
    author_email='radek.poleski@gmail.com',
    description='package for modeling gravitational microlensing events',
    packages=find_packages(where="source"),
    package_dir={"": "source"},
    data_files=data_files,
    python_requires=">=3.6",
    install_requires=install_requires,
)
