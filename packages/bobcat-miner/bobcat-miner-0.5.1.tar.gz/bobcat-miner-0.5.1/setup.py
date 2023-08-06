# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bobcat_miner']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=1.11.1,<2.0.0', 'filelock>=3.4.2,<4.0.0', 'requests>=2.27.0,<3.0.0']

entry_points = \
{'console_scripts': ['bobcat-autopilot = bobcat_miner.cli:autopilot',
                     'bobcat-dig = bobcat_miner.cli:dig',
                     'bobcat-fastsync = bobcat_miner.cli:fastsync',
                     'bobcat-miner = bobcat_miner.cli:miner',
                     'bobcat-ping = bobcat_miner.cli:ping',
                     'bobcat-reboot = bobcat_miner.cli:reboot',
                     'bobcat-reset = bobcat_miner.cli:reset',
                     'bobcat-resync = bobcat_miner.cli:resync',
                     'bobcat-speed = bobcat_miner.cli:speed',
                     'bobcat-status = bobcat_miner.cli:status']}

setup_kwargs = {
    'name': 'bobcat-miner',
    'version': '0.5.1',
    'description': 'A python SDK for interacting with the bobcat miner.',
    'long_description': '[![PyPI](https://img.shields.io/pypi/v/bobcat_miner.svg)](https://pypi.org/project/bobcat-miner/)\n[![Tests](https://github.com/aidanmelen/bobcat-miner-python/actions/workflows/tests.yaml/badge.svg)](https://github.com/aidanmelen/bobcat-miner-python/actions/workflows/tests.yaml)\n\n# bobcat-miner\n\nA python SDK for interacting with the bobcat miner.\n\n## Install\n\n```bash\npip install bobcat-miner\n```\n\n## Autopilot Usage\n\nFollow these [instructions](https://bobcatminer.zendesk.com/hc/en-us/articles/4412905935131-How-to-Access-the-Diagnoser) to find the bobcat miner\'s ip address.\n\n```bash\nBOBCAT_IP_ADDRESS="192.168.1.100" bobcat-autopilot\n```\n\n## Bobcat Usage\n\n```python\nimport bobcat_miner\n\nbobcat = bobcat_miner.Bobcat("192.168.1.100")\n\n# refresh\nbobcat.refresh_status()\nbobcat.refresh_miner()\nbobcat.refresh_speed()\nbobcat.refresh_temp()\nbobcat.refresh_dig()\nbobcat.refresh()\n\n# properties\nbobcat.status\nbobcat.gap\nbobcat.miner_height\nbobcat.blockchain_height\nbobcat.epoch\nbobcat.tip\nbobcat.ota_version\nbobcat.region\nbobcat.frequency_plan\nbobcat.animal\nbobcat.name\nbobcat.pubkey\nbobcat.state\nbobcat.miner_status\nbobcat.names\nbobcat.image\nbobcat.created\nbobcat.p2p_status\nbobcat.ports_desc\nbobcat.ports\nbobcat.private_ip\nbobcat.public_ip\nbobcat.peerbook\nbobcat.peerbook_miner\nbobcat.peerbook_listen_address\nbobcat.peerbook_peers\nbobcat.timestamp\nbobcat.error\nbobcat.temp0\nbobcat.temp1\nbobcat.temp0_c\nbobcat.temp1_c\nbobcat.temp0_f\nbobcat.temp1_f\nbobcat.download_speed\nbobcat.upload_speed\nbobcat.latency\nbobcat.dig_name\nbobcat.dig_message\nbobcat.dig_dns\nbobcat.dig_records\n\n# actions\nbobcat.ping()\nbobcat.reboot()\nbobcat.reset()\nbobcat.resync()\nbobcat.fastsync()\n```\n\n## Advanced Usage\n\n```python\nimport bobcat_miner\n\nbobcat = bobcat_miner.Bobcat("192.168.1.100")\nautopilot = bobcat_miner.Autopilot(bobcat)\n\n# diagnostics\nautopilot.diagnose_relay()\nautopilot.diagnose_temp()\nautopilot.diagnose_network_speed()\nautopilot.diagnose_sync()\n\n# actions\nautopilot.ping()        # repeat ping attempts until bobcat is reached or exceeds max attempts\nautopilot.reboot()      # reset and wait for bobcat to connect\nautopilot.reset()       # reset and wait for health check\nautopilot.resync()      # resync and wait for health check\nautopilot.fastsync()    # repeat fastsync attempts until gap is less than 400 or exceeds max attempts\nautopilot.autosync()    # check sync -> reboot -> check sync -> fastsync -> check sync\nautopilot.is_syncing()  # Poll the Bobcat\'s gap to see if it is syncing over time\n\nautopilot.run()         # reboot -> reset -> fastsync when bobcat is unhealthy and diagnostics\n```\n\n## Troubleshooting\n\nPlease see [No Witness\'s Troubleshooting Guide](https://www.nowitness.org/troubleshooting/) for more information troubleshooting your bobcat miner.\n\nhttps://bobcatminer.zendesk.com/hc/en-us/articles/4408443160347-Troubleshooting-your-Bobcat-hotspot\n\n## Donations\n\nDonations are welcome and appreciated! :gift: :tada:\n\n[![HNT: 14HmckNU4WHDDtGH29FMqVENzZAYh5a9XRiLfY2AN6ghfHMvAuR](./images/wallet.jpg)](https://explorer-v1.helium.com/accounts/14HmckNU4WHDDtGH29FMqVENzZAYh5a9XRiLfY2AN6ghfHMvAuR)\n\nHNT: [14HmckNU4WHDDtGH29FMqVENzZAYh5a9XRiLfY2AN6ghfHMvAuR](https://explorer-v1.helium.com/accounts/14HmckNU4WHDDtGH29FMqVENzZAYh5a9XRiLfY2AN6ghfHMvAuR)\n',
    'author': 'Aidan Melen',
    'author_email': 'aidanmelen@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aidanmelen/bobcat-miner-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
