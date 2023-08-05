# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tbcp_devops',
 'tbcp_devops.pkgmgmt',
 'tbcp_devops.pkgmgmt.examples.python',
 'tbcp_devops.pkgmgmt.py',
 'tbcp_devops.scmgmt',
 'tbcp_devops.scmgmt.utils']

package_data = \
{'': ['*'],
 'tbcp_devops.pkgmgmt': ['examples/default/*',
                         'examples/git/*',
                         'examples/gitlab/*',
                         'examples/nodejs/*',
                         'examples/poetry/*',
                         'examples/typescript/*']}

install_requires = \
['GitPython>=3.1.24,<4.0.0',
 'Jinja2>=3.0.3,<4.0.0',
 'semver>=2.13.0,<3.0.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'tbcp-devops',
    'version': '1.4.0',
    'description': 'DevOps stuff for working with files, folders, project structures, sementic versioning, Git management and so on',
    'long_description': '<!--\nMIT License\n\nCopyright (c) 2021 Bootcamp contributors\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n-->\n<a href="https://bootcamp-project.com/" target="_blank"><img src="https://bootcamp-project.com/tbcp.svg" align="right" height="200" /></a>\n\n# TBCP - DevOps Python Module\n\n## ready-2-use and user-friendly\n\n<img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" />\n<img src="https://img.shields.io/badge/Bootcamp-Project-blue?style=for-the-badge" />\n\n## 🦄 About 🦄\n\n**Minimum Viable Product**: *What is what we want?*\n\n> DevOps stuff for working with files, folders, project structures, sementic versioning, Git management and so on\n\n## 🚀 Getting Started 🚀\n\n**Project Links**\n\n- [Homepage][Project_Homepage]\n- [Documentation][Project_Docs]\n- [Repository][Repo_URL]\n- [Issues][Repo_Issues]\n\n### ✋ Prerequisites ✋\n\n### 💪 Installation 💪\n\n### 😏 Development 😏\n\n### 🤓 Linting 🤓\n\n### 🧐 Testing 🧐\n\n### 🤩 Building 🤩\n\n### 🥳 Publishing 🥳\n\n### 😅 Support 😅\n\n*Don\'t be shy!* You are also welcome to open a [post in the issue registar][Repo_Issues] for simple questions.\n\n## ⭐️ Features ⭐️\n\n- [**Smoke** and **Unit-tested**][Repo_Tests] modules\n- Security-first production-ready [**configurations**][TBCP_Configurations] by default\n- Extensive [**documentation**][Project_Docs]\n\n### 😎 Built With 😎\n\n<table>\n<tr>\n<td><a href="https://www.python.org/" target="_blank"><img src="https://cdr.bootcamp-project.com/logos/programming/python.svg" alt="Python" width="200"/></a></td>\n<td><a href="https://bootcamp-project.com/" target="_blank"><img src="https://bootcamp-project.com/tbcp.svg" alt="tbcp" width="200"/></a></td>\n</tr>\n</table>\n\n### 🏆 Acknowledgements 🏆\n\nThanks for these awesome resources that were used during the development of the **Bootcamp: DevOps Python Module**:\n\n## 📑 Changelog 📑\n\nSee [CHANGELOG][Repo_Changelog] for more information.\n\n## 📋 Roadmap 📋\n\n- [ ] In the Initialization section\n  - [ ] Create Nodejs and Python Projects\n  - [ ] Automatic creation of Gitlab Projects\n- [ ] Automate Versioning\n  - [ ] in Python Projects\n  - [ ] in Node.js Projects\n    - [ ] with NPM\n    - [ ] with Yarn\n- [ ] Secret Management\n- [ ] Log Messenger\n- [ ] Parse Error messages and search on SE\n  - [ ] Bash History\n\nSee the [open issues][Repo_Issues] for a list of proposed features (and known issues).\n\n## 🤝 Contribute 🤝\n\nContributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.\n\nPlease read the [contribution guidelines][TBCP_Contribution] first.\n\n0. [Give us a star][Repo_Stars], it\'s really important! 😅\n1. Fork the Project: (`git clone https://gitlab.com/the-bootcamp-project/packages/workdirpy.git`)\n2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some AmazingFeature\'`)\n4. Push to the Branch (`git push origin feature/AmazingFeature`)\n5. Open a Pull Request\n\n## 📜 License 📜\n\nSee [LICENSE][Repo_License] for more information.\n\n## 💌 Contact 💌\n\n[Bootcamp contributors][TBCP_Homepage] - `contributors` @ `bootcamp-project` .com\n\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n[Project_Homepage]: https://packages.bootcamp-project.com\n[Project_Docs]: https://packages.bootcamp-project.com\n[Project_Install_Docs]: https://packages.bootcamp-project.com/#/install\n[Project_Develop_Docs]: https://packages.bootcamp-project.com/#/develop\n[Project_Linting_Docs]: https://packages.bootcamp-project.com/#/linting\n[Project_esting_Docs]: https://packages.bootcamp-project.com/#/testing\n[Project_Building_Docs]: https://packages.bootcamp-project.com/#/building\n[Project_Publishing_Docs]: https://packages.bootcamp-project.com/#/publishing\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n[Repo_URL]: https://gitlab.com/the-bootcamp-project/packages/workdirpy\n[Repo_Issues]: https://gitlab.com/the-bootcamp-project/packages/workdirpy/-/issues\n[Repo_Forks]: https://gitlab.com/the-bootcamp-project/packages/workdirpy/-/forks\n[Repo_Stars]: https://gitlab.com/the-bootcamp-project/packages/workdirpy/-/starrers\n[Repo_Tests]: https://gitlab.com/the-bootcamp-project/packages/workdirpy/-/tree/main/tests\n[Repo_License]: https://gitlab.com/the-bootcamp-project/packages/workdirpy/-/blob/main/LICENSE\n[Repo_Changelog]: https://gitlab.com/the-bootcamp-project/packages/workdirpy/-/blob/main/CHANGELOG\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n[TBCP_Homepage]: https://bootcamp-project.com\n[TBCP_Configurations]: https://configurations.bootcamp-project.com\n[TBCP_Contribution]: https://bootcamp-project.com/#code_of_conduct\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n[RTFM_GitwithPython]: https://dev.rtfm.page/#/working_with/git/interaction/with_python\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n[URL_Python]: https://wiki.python.org/moin/BeginnersGuide/Download\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n<!-- ---------------------------------------------------------------------------------------------------------------------------------- -->\n',
    'author': 'Bootcamp contributors',
    'author_email': 'contributors@bootcamp-project.com',
    'maintainer': 'Bootcamp contributors',
    'maintainer_email': 'contributors@bootcamp-project.com',
    'url': 'https://gitlab.com/the-bootcamp-project/packages/workdirpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
