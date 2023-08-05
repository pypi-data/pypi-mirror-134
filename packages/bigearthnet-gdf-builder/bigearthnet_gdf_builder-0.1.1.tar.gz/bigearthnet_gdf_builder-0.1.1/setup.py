# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bigearthnet_gdf_builder']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4,<2.0',
 'bigearthnet-common>=1.0.0,<2.0.0',
 'fastcore>=1.3,<2.0',
 'geopandas>=0.10,<0.11',
 'natsort>=8,<9',
 'pyarrow>=6,<7',
 'pydantic>=1.8,<2.0',
 'pygeos>=0.12,<0.13',
 'rich>=10,<12',
 'typer>=0.4,<0.5']

entry_points = \
{'console_scripts': ['ben_gdf_builder = '
                     'bigearthnet_gdf_builder.builder:_run_gdf_cli']}

setup_kwargs = {
    'name': 'bigearthnet-gdf-builder',
    'version': '0.1.1',
    'description': "A package to generate and extend BigEarthNet GeoDataFrame's.",
    'long_description': "# BigEarthNet GeoDataFrame Builder\n> A package to generate and extend BigEarthNet GeoDataFrame's.\n\n\n<!-- [![Tests](https://img.shields.io/github/workflow/status/kai-tub/bigearthnet_common/CI?color=dark-green&label=%20Tests)](https://github.com/kai-tub/bigearthnet_common/actions/workflows/main.yml)\n[![License](https://img.shields.io/pypi/l/bigearthnet_common?color=dark-green)](https://github.com/kai-tub/bigearthnet_common/blob/main/LICENSE)\n[![PyPI version](https://badge.fury.io/py/bigearthnet-common.svg)](https://pypi.org/project/bigearthnet-common/)\n[![Conda Version](https://img.shields.io/conda/vn/conda-forge/bigearthnet-common?color=dark-green)](https://anaconda.org/conda-forge/bigearthnet-common)\n[![Auto Release](https://img.shields.io/badge/release-auto.svg?colorA=888888&colorB=9B065A&label=auto&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAACzElEQVR4AYXBW2iVBQAA4O+/nLlLO9NM7JSXasko2ASZMaKyhRKEDH2ohxHVWy6EiIiiLOgiZG9CtdgG0VNQoJEXRogVgZYylI1skiKVITPTTtnv3M7+v8UvnG3M+r7APLIRxStn69qzqeBBrMYyBDiL4SD0VeFmRwtrkrI5IjP0F7rjzrSjvbTqwubiLZffySrhRrSghBJa8EBYY0NyLJt8bDBOtzbEY72TldQ1kRm6otana8JK3/kzN/3V/NBPU6HsNnNlZAz/ukOalb0RBJKeQnykd7LiX5Fp/YXuQlfUuhXbg8Di5GL9jbXFq/tLa86PpxPhAPrwCYaiorS8L/uuPJh1hZFbcR8mewrx0d7JShr3F7pNW4vX0GRakKWVk7taDq7uPvFWw8YkMcPVb+vfvfRZ1i7zqFwjtmFouL72y6C/0L0Ie3GvaQXRyYVB3YZNE32/+A/D9bVLcRB3yw3hkRCdaDUtFl6Ykr20aaLvKoqIXUdbMj6GFzAmdxfWx9iIRrkDr1f27cFONGMUo/gRI/jNbIMYxJOoR1cY0OGaVPb5z9mlKbyJP/EsdmIXvsFmM7Ql42nEblX3xI1BbYbTkXCqRnxUbgzPo4T7sQBNeBG7zbAiDI8nWfZDhQWYCG4PFr+HMBQ6l5VPJybeRyJXwsdYJ/cRnlJV0yB4ZlUYtFQIkMZnst8fRrPcKezHCblz2IInMIkPzbbyb9mW42nWInc2xmE0y61AJ06oGsXL5rcOK1UdCbEXiVwNXsEy/6+EbaiVG8eeEAfxvaoSBnCH61uOD7BS1Ul8ESHBKWxCrdyd6EYNKihgEVrwOAbQruoytuBYIFfAc3gVN6iawhjKyNCEpYhVJXgbOzARyaU4hCtYizq5EI1YgiUoIlT1B7ZjByqmRWYbwtdYjoWoN7+LOIQefIqKawLzK6ID69GGpQgwhhEcwGGUzfEPAiPqsCXadFsAAAAASUVORK5CYII=)](https://github.com/intuit/auto) -->\n\nThis library provides a collection of functions to generate and extend GeoDataFrames for the [BigEarthNet](bigearth.net) dataset.\n\n`bigearthnet_gdf_builder` tries to accomplish two goals:\n\n1. Easily generate [geopandas](https://geopandas.org/en/stable/) [GeoDataFrame](https://geopandas.org/en/stable/getting_started/introduction.html) by passing a BigEarthNet archive directory.\n   - Allow for easy top-level statistical analysis of the data in a familiar _pandas_-style\n   - Provide functions to enrich GeoDataFrames with often required BigEarthNet metadata (like the season or country of the patch)\n2. Simplify the building procedure by providing a command-line interface with reproducible results\n\n## Installation\n<!-- I strongly recommend to use [mamba](https://github.com/mamba-org/mamba) or `conda` with [miniforge](https://github.com/conda-forge/miniforge) to install the package with:\n- `mamba/conda install bigearthnet-common -c conda-forge`\n\nAs the `bigearthnet_common` tool is built on top of `geopandas` the same restrictions apply.\nFor more details please review the [geopandas installation documentation](https://geopandas.org/en/stable/getting_started/install.html).\n\nThe package is also available via PyPI and could be installed with:\n- `pip install bigearthnet_common` (not recommended) -->\n\n## TL;DR\nThe most relevant functions are exposed as CLI entry points.\n\nTo build the tabular data, use:\n- `ben_gdf_builder --help` or\n- `python -m bigearthnet_gdf_builder.builder --help`\n\n\n## Deep Learning\n\nOne of the primary purposes of the dataset is to allow deep learning researchers and practitioners to train their models on multi-spectral satellite data.\nIn that regard, there is a general recommendation to drop patches that are covered by seasonal snow or clouds.\nAlso, the novel 19-class nomenclature should be preferred over the original 43-class nomenclature.\nAs a result of these recommendations, some patches have to be _excluded_ from the original raw BigEarthNet dataset that is provided at [BigEarthNet](bigearth.net).\n\nTo simplify the procedure of pre-converting the JSON metadata files, the library provides a single command that will generate a recommended GeoDataFrame with extra metadata (country/season data of each patch) while dropping all patches that are not recommended for deep learning research.\nFunctions for both archives, BEN-S1 and BEN-S2, are provided.\n\nTo generate such a GeoDataFrame and store it as an `parquet` file, use:\n\n- `ben_gdf_builder build-recommended-s2-parquet` (available after installing package) or\n- `python -m bigearthnet_gdf_builder.builder build-recommended-s2-parquet`\n- `ben_gdf_builder build-recommended-s1-parquet` (available after installing package) or\n- `python -m bigearthnet_gdf_builder.builder build-recommended-s1-parquet`\n\nIf you want to read the raw JSON files and convert those to a GeoDataFrame file without dropping any patches or adding any metadata, use:\n\n- `ben_gdf_builder build-raw-ben-s2-parquet` (available after installing package) or\n- `python -m bigearthnet_gdf_builder.builder build-raw-ben-s2-parquet`\n- `ben_gdf_builder build-raw-ben-s1-parquet` (available after installing package) or\n- `python -m bigearthnet_gdf_builder.builder build-raw-ben-s1-parquet`\n\n## Contributing\n\nContributions are always welcome!\n\nPlease look at the corresponding `ipynb` notebook from the `nbs` folder to review the source code.\nThese notebooks include extensive documentation, visualizations, and tests.\nThe automatically generated Python files are available in the `bigearthnet_gdf_builder` module.\n\nMore information is available in the [contributing guidelines](https://github.com/kai-tub/bigearthnet_common/blob/main/.github/CONTRIBUTING.md) document.\n",
    'author': 'Kai Norman Clasen',
    'author_email': 'snakemap_navigation@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kai-tub/bigearthnet_gdf_builder',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
