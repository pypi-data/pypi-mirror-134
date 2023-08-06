# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastq_downloader',
 'fastq_downloader.helper',
 'fastq_downloader.snakemake',
 'fastq_downloader.tests']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4', 'click', 'httpx', 'lxml']

entry_points = \
{'console_scripts': ['fastq-downloader = fastq_downloader.__main__:main']}

setup_kwargs = {
    'name': 'fastq-downloader',
    'version': '0.3.3',
    'description': '',
    'long_description': "# Fastq Downloader (WIP)\n\nThis python package let you download fastq files from ena.\nIt can automatic merge and rename fastq files based on the input file provided.\nIf you have trouble downloading this repo's release, please go to [fastgit](https://fastgit.org)\n\n## How to use\nauto merge multiple files of paired end reads are not tested now, but should be usable\n```bash\nconda create --name fastq-downloader -c conda-forge -c hcc -c bioconda aspera-cli snakemake httpx lxml click beautifulsoup4 python=3.9\n## use what ever you want to download the gist mentioned above to thisname.smk\n## download whl file from github release of this project to thisname.whl\nconda activate fastq-downloader\npip install fastq-downloader==0.3.1\n## make sure to create an infotsv before, you can just copy from the geo website,\n## then go to vim, type :set paste to get into paste mode, paste the table into vim,\n## save the file as whatever name you want, then exit vim\n## the white space will be auto convert to underscore\n## refresh_acc need to be False if you don't want to query again the accesion number,\n## or due to the recreation of the link file(default set to false), all files are to be downloaded.\nfastq-downloader smk --info thisname.tsv --out thisname --refresh_acc False\n```\n\nIt will automatically try to download the file, check md5, retry if file integrity check failed, and merge the files if the number of files is more than 2, finally rename the files to the description you provided.\n\nprepare the info.tsv like this:\nnote the file must be tab delimited (tsv file), you can simply achieve this by paste it from the Excel or GEO website. Or from SRA Run Selector downloaded csv file.\n```\nGSM12345  h3k9me3_rep1\nGSM12345  h3k9me3_rep2\n```\n\n\n## todo\n  - [ ] test for paired-end reads run merge\n  - [ ] publish to bioconda\n  - [x] if fail, retry\n  - [x] use dag to run the pipeline (sort of, implemented by using snakemake)\n  - [x] option to resume download when md5 not match\n  - [x] option to continue from last time download\n  - [x] implement second level parallelization\n\n## update content\n  - 0.3.2:\n     - add filter for library layout (some sra entry has content mismatches its library layout)",
    'author': 'tpob',
    'author_email': 'tpob@tpob.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
