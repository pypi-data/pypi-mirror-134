# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['offlinemsmtp']

package_data = \
{'': ['*']}

install_requires = \
['PyGObject>=3.38.0,<4.0.0', 'watchdog>=0.10.3,<0.11.0']

entry_points = \
{'console_scripts': ['offlinemsmtp = offlinemsmtp.__main__:main']}

setup_kwargs = {
    'name': 'offlinemsmtp',
    'version': '0.3.9',
    'description': 'msmtp wrapper allowing for offline use',
    'long_description': '![offlinemsmtp](./logo/logo.png)\n\nAllows you to use `msmtp` offline by queuing email until you have an internet\nconnection.\n\n[![builds.sr.ht status](https://builds.sr.ht/~sumner/offlinemsmtp/commits/build.yml.svg)](https://builds.sr.ht/~sumner/offlinemsmtp/commits/build.yml)\n[![PyPi Version](https://img.shields.io/pypi/v/offlinemsmtp?color=4DC71F&logo=python&logoColor=fff)](https://pypi.org/project/offlinemsmtp/)\n[![AUR Version](https://img.shields.io/aur/version/offlinemsmtp?logo=linux&logoColor=fff)](https://aur.archlinux.org/packages/offlinemsmtp/)\n[![LiberaPay Donation Status](https://img.shields.io/liberapay/receives/sumner.svg?logo=liberapay)](https://liberapay.com/sumner/donate)\n\n## Features\n\n* Runs as a daemon and (at a configurable time interval) attempts to send the\n  mail in the queue directory.\n* Drop-in replacement for `msmtp` in your mutt config.\n* Only attempts to send the queued email message if it can connect to the\n  configured SMTP server.\n* When a new email message comes into the queue and you are already online,\n  `offlinemsmtp` will send it immediately.\n* Integrates with system notifications so that you are notified when mail is\n  being sent.\n* Disable/enable sending of mail by the presence/absence of a file. This is\n  useful if you want to have some sort of "offline mode".\n\n## Installation\n\nUsing [PyPi](https://pypi.org/project/offlinemsmtp/):\n\n    pip install --user offlinemsmtp\n\nOn Arch Linux, you can install the `offlinemsmtp` package from the\n[AUR](https://aur.archlinux.org/packages/offlinemsmtp/). For example, if you use\n`yay`:\n\n    yay -S offlinemsmtp\n\n## Run the daemon using systemd\n\nCreate a file called ``~/.config/systemd/user/offlinemsmtp.service`` with the\nfollowing content (if you installed via the AUR package, a service file was\nalready created for you in ``/usr/lib/systemd/user`` so you only need to do this\nstep if you want to customize the parameters passed to the daemon):\n\n    [Unit]\n    Description=offlinemsmtp\n\n    [Service]\n    ExecStart=/usr/bin/offlinemsmtp --daemon\n\n    [Install]\n    WantedBy=default.target\n\nThen, enable and start `offlinemsmtp` using systemd:\n\n    systemctl --user daemon-reload\n    systemctl --user enable --now offlinemsmtp\n\n## Usage\n\n`offlinemsmtp` has two components: a daemon for listening to the outbox folder\nand sending the mail when the network is available and a enqueuer for adding\nmail to the send queue.\n\nTo run the daemon in the current command line (this is useful for testing), run\nthis command::\n\n    offlinemsmtp --daemon\n\nTo enqueue emails, use the `offlinemsmtp` executable without `--daemon`. All\nparameters (with a few caveats described below in [Command Line\nArguments](#command-line-arguments)) are forwarded on to `msmtp`. Anything\npassed in via standard in will be forwarded over standard in to `msmtp` when the\nmail is sent.\n\n### Configuration with Mutt\n\nTo use offlinemsmtp with mutt, just replace `msmtp` in your mutt configuration\nfile with `offlinemsmtp`. Here is an example:\n\n    set sendmail = "offlinemsmtp -a personal"\n\n### Command Line Arguments\n\nofflinemsmtp accepts a number of command line arguments:\n\n- `-h`, `--help` - shows a help message and exits.\n- `-o DIR`, `--outbox-directory DIR` - set the directory to use as the outbox.\n  Defaults to `~/.offlinemsmtp-outbox`.\n- `-d`, `--daemon` - run the offlinemsmtp daemon.\n- `-s`, `--silent` - set to disable all logging and notifications.\n- `-i INTERVAL`, `--interval INTERVAL` - set the interval (in seconds) at which\n  to attempt to flush the send queue. Defaults to 60.\n- `-C FILE`, `--file FILE` - the msmtp configuration file to use.\n- `--send-mail-file FILE` - only send mail if this file exists (defaults to\n  `None` meaning that no file is required for mail sending to be enabled)\n- All remaining arguments are passed to `msmtp`. The `-C` argument is\n  automatically passed to `msmtp`.\n- Anything after a special `--` argument will be passed to `msmtp`. This allows\n  you to pass arguments that may conflict with `offlinemsmtp` arguments to\n  `msmtp`.\n\n## Contributing\n\nSee the [CONTRIBUTING.md](./CONTRIBUTING.md) document for details on how to\ncontribute to the project.\n\n## Other projects\n\n- https://github.com/marlam/msmtp-mirror/tree/master/scripts/msmtpqueue - this\n  is included with `msmtp`, but doesn\'t have all of the features that I want.\n- https://github.com/dcbaker/py-mailqueued - looks cool, I didn\'t see it when I\n  was researching, but it\'s probably better than my implementation, even thought\n  I had a lot of fun doing mine.\n- https://github.com/venkytv/msmtp-offline - it\'s written in Ruby.\n',
    'author': 'Sumner Evans',
    'author_email': 'inquiries@sumnerevans.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://sr.ht/~sumner/offlinemsmtp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
