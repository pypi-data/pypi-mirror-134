# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['centralcli', 'centralcli.boilerplate', 'centralcli.boilerplate.2.5.3']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6,<7',
 'Pygments>=2,<3',
 'aiohttp>=3,<4',
 'asyncio>=3,<4',
 'cchardet',
 'certifi',
 'colorama',
 'halo',
 'idna>=3,<4',
 'pendulum>=2,<3',
 'pycentral>=0.0.3,<0.0.4',
 'pylibyaml>=0.1.0,<0.2.0',
 'rich>=10,<11',
 'shellingham>=1,<2',
 'tablib>=3,<4',
 'tabulate',
 'tinydb>=4,<5',
 'typer>=0.4,<0.5',
 'urllib3>=1,<2']

extras_require = \
{'hook_proxy': ['fastapi', 'uvicorn']}

entry_points = \
{'console_scripts': ['cencli = centralcli.cli:app']}

setup_kwargs = {
    'name': 'centralcli',
    'version': '0.18.0',
    'description': 'A CLI for interacting with Aruba Central (Cloud Management Platform).  Facilitates bulk imports, exports, reporting.  A handy tool if you have devices managed by Aruba Central.',
    'long_description': "# Aruba Central API CLI\n\n[![Documentation Status](https://readthedocs.org/projects/central-api-cli/badge/?version=latest)](https://central-api-cli.readthedocs.io/en/latest/?badge=latest)\n\nA CLI app for interacting with Aruba Central Cloud Management Platform. With cross-platform shell support. Auto Completion, easy device/site/group/template identification (fuzzy match), support for batch import, and a lot more.\n\n  > As commands are built out the CLI hierarchy may evolve.  Refer to the [documentation](https://central-api-cli.readthedocs.org) or help text for CLI structure/syntax.\n\n![centralcli Animated Demo](https://raw.githubusercontent.com/Pack3tL0ss/central-api-cli/master/docs/img/cencli-demo.gif)\n\n## Features\n\n- Cross Platform Support\n- Auto/TAB Completion\n- Specify device, site, etc. by fuzzy match of multiple fields (i.e. name, mac, serial#, ip address)\n- Multiple output formats\n- Output to file\n- Numerous import formats (csv, yaml, json, xls, etc.)\n- Multiple account support (easily switch between different central accounts `--account myotheraccount`)\n- Batch Operation based on data from input file.  i.e. Add sites in batch based on data from a csv.\n- Automatic Token refresh.  With prompt to paste in a new token if it becomes invalid.\n  > If using Tokens, dedicate the token to the CLI alone, using it in swagger or on another system, will eventually lead to a refresh that invalidates the tokens on the other systems using it.\n- You can also use username/Password Auth. which will facilitate automatic retrieval of new Tokens even if they do become invalid.\n\n## Installation\n\nRequires python 3.7+ and pip\n\n`pip3 install centralcli`\n\n> You can also install in a virtual environment (venv), but you'll lose auto-completion, unless you activate the venv.\n\n### Upgrading the CLI\n\n`pip3 install -U centralcli`\n\n### if you don't have python\n\n- You can get it for any platform @ [https://www.python.org](https://www.python.org)\n- On Windows 10 it's also available in the Windows store.\n\n## Configuration\n\nRefer to [config.yaml.example](https://github.com/Pack3tL0ss/central-api-cli/blob/master/config/config.yaml.example) to guide in the creation of config.yaml and place in the config directory.\n\nCentralCli will look in \\<Users home dir\\>/.config/centralcli, and \\<Users home dir\\>\\\\.centralcli.\ni.e. on Windows `c:\\Users\\wade\\.centralcli` or on Linux `/home/wade/.config/centralcli`\n\nOnce `config.yaml` is populated per [config.yaml.example](config/config.yaml.example), run some test commands to validate the config.\n\nFor Example `cencli show all`\n\n```bash\nwade@wellswa6:~ $ cencli show all\n                                                                                       All Devices\n ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n  name                  type   model                            ip                mac                 serial       group          site             labels        version       status\n ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n  6100F-48-LAB          cx     6100 48G CL4 4SFP+ Swch          10.0.40.11        --redacted--   --redacted--    WadeLab8x                                     10.08.1010       Down\n                               (JL675A)\n  SDBranch1:7008        gw     A7008                            192.168.240.101   --redacted--   --redacted--    Branch1        Antigua          Branch View   10.3.0.0_82528   Up\n  br1-2930F-sw          sw     Aruba2930F-8G-PoE+-2SFP+         10.101.5.4        --redacted--   --redacted--    Branch1        Antigua          Branch View   16.11.0002       Up\n                               Switch(JL258A)\n  br1-315.0c88-ap       ap     315                              10.101.6.200      --redacted--   --redacted--    Branch1        Antigua          Branch View   10.3.0.0_82528   Up\n  MB1-505h              ap     505H                             10.10.1.101       --redacted--   --redacted--    MicroBranch1   Champions Hill                 10.3.0.0_82528   Up\n  6200F-Bot             cx     6200F 48G CL4 4SFP+740W Swch     10.0.40.16        --redacted--   --redacted--    WadeLab8x      Pommore                        10.08.1010       Down\n                               (JL728A)\n  6200F-Top             cx     6200F 48G CL4 4SFP+740W Swch     10.0.40.6         --redacted--   --redacted--    WadeLab8x      Pommore                        10.08.1010       Down\n                               (JL728A)\n  APGW1                 gw     A9004-LTE                        10.0.35.10        --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82528   Up\n  APGW2                 gw     A9004                            10.0.35.20        --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82528   Up\n  VPNC1                 gw     A7005                            172.30.0.242      --redacted--   --redacted--    VPNC           WadeLab          Branch View   10.3.0.0_82528   Up\n  VPNC2                 gw     A7005                            172.30.0.243      --redacted--   --redacted--    VPNC           WadeLab          Branch View   10.3.0.0_82528   Up\n  av-555.11b8-ap        ap     555                              10.0.31.155       --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82463   Down\n  barn-303p.2c30-ap     ap     303P                             10.1.30.151       --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82528   Up\n  barn-4100i            cx     4100i 12G CL4/6 POE 2SFP+ DIN    10.1.30.152       --redacted--   --redacted--    WadeLab        WadeLab                        10.08.1010       Up\n                               Sw (JL817A)\n  barn-518.2816-ap      ap     518                              10.1.30.101       --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82528   Up\n  bsmt-515.51s9-ap      ap     515                              10.0.30.233       --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82463   Down\n  craft-2930F           sw     Aruba2930F-8G-PoE+-2SFP+         10.0.30.5         --redacted--   --redacted--    WadeLab        WadeLab                        16.11.0002       Up\n                               Switch(JL258A)\n  garage-345.5136-ap    ap     345                              10.0.31.148       --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82463   Down\n  ktcn-505H.206c-ap     ap     505H                             10.0.30.212       --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82463   Down\n  lwrptio-575.0824-ap   ap     575                              10.0.30.219       --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82463   Down\n  zrm-535.70be-ap       ap     535                              10.0.31.101       --redacted--   --redacted--    WLNET          WadeLab                        10.3.0.0_82463   Down\n ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n  Show all displays fields common to all device types. To see all columns for a given device type use show <DEVICE TYPE>\n  API Rate Limit: 925 of 1000 remaining.\n\n```\n\nUse `cencli ?` to become familiar with the command options.\n\n### Auto Completion\n\nThe CLI supports auto-completion.  To configure auto-completion run `cencli --install-completion`.  This will auto-detect the type of shell you are running in, and install the necessary completion into your profile.  You'll need to exit the shell and start a new session for it to take effect.\n\n## Usage Notes\n\n### Caching & Friendly identifiers\n\n- Caching: The CLI caches information on all devices, sites, groups, and templates in Central.  It's a minimal amount per device, and is done to allow human friendly identifiers.  The API typically accepts serial #, site id, etc.  This function allows you to specify a device by name, IP, mac (any format), and serial.\n\nThe lookup sequence for a device:\n\n  1. Exact Match of any of the identifier fields (name, ip, mac, serial)\n  2. case insensitive match\n  3. case insensitive match disregarding all hyphens and underscores (in case you type 6200f_bot and the device name is 6200F-Bot)\n  4. Case insensitive Fuzzy match with implied wild-card, otherwise match any devices that start with the identifier provided. `cencli show switches 6200F` will result in a match of `6200F-Bot`.\n\n> If there is no match found, a cache update is triggered, and the match rules are re-tried.\n\n- Caching works in a similar manner for groups, templates, and sites.  Sites can match on name and nearly any address field.  So if you only had one site in San Antonio you could specify that site with `show sites 'San Antonio'`  \\<-- Note the use of quotes because there is a space in the name.\n\n- **Multiple Matches**:  It's possible to specify an identifier that returns multiple matches (if drops all the way down to the Fuzzy match/implied trailing wild-card).  If that occurs you are prompted to select the intended device from a list of the matches.\n\n### Output Formats\n\nThere are a number of output formats available.  Most commands default to what is likely the easiest to view given the number of fields.  Otherwise longer outputs are typically displayed vertically by default.  If the output can reasonably fit, it's displayed in tabular format horizontally.\n\nYou can specify the output format with command line flags `--json`, `--yaml`, `--csv`, `--table`  rich is tabular format with folding (multi line within the same row) and truncating.\n\n> Most outputs will evolve to support an output with the most commonly desired fields by default and expanded vertical output via the `-v` option (not implemented yet.).  Currently the output is tabular horizontally if the amount of data is likely to fit most displays, and vertical otherwise.\n\n### File Output\n\nJust use `--out \\<filename\\>` (or \\<path\\\\filename\\>), and specify the desired format.\n\n## CLI Tree\n\nUse `?` or `--help` from the cli, which you can do at any level.  `ccenli ?`, `cencli bounce --help` etc.\n\nYou can also see the entire supported tree via the [CLI Reference Guide](https://central-api-cli.readthedocs.io/en/latest/cli.html).\n*NOTE: The Reference Guide documents a few commands that are hidden in the CLI*\n",
    'author': 'Wade Wells (Pack3tL0ss)',
    'author_email': 'wade@consolepi.org',
    'maintainer': 'Wade Wells (Pack3tL0ss)',
    'maintainer_email': 'wade@consolepi.org',
    'url': 'https://github.com/Pack3tL0ss/central-api-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
