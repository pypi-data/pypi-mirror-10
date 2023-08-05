r"""
# send in job name and kwargs for slurm params:
>>> s = Slurm("job-name", {"account": "ucgd-kp", "partition": "ucgd-kp"})
>>> print str(s)
#!/bin/bash
<BLANKLINE>
#SBATCH -e logs/job-name.%J.err
#SBATCH -o logs/job-name.%J.out
#SBATCH -J job-name
<BLANKLINE>
#SBATCH --account=ucgd-kp
#SBATCH --partition=ucgd-kp
<BLANKLINE>
set -eo pipefail -o nounset
<BLANKLINE>
{script}

#>>> s.run("do stuff")

"""
from __future__ import print_function

import sys
import os
import subprocess
import tempfile
import atexit
import hashlib

TMPL = """\
#!/bin/bash

#SBATCH -e logs/{name}.%J.err
#SBATCH -o logs/{name}.%J.out
#SBATCH -J {name}

{header}

set -eo pipefail -o nounset

{script}"""


def tmp(suffix=".sh"):
    t = tempfile.mktemp(suffix=suffix)
    atexit.register(os.unlink, t)
    return t


class Slurm(object):
    def __init__(self, name, slurm_kwargs=None, tmpl=None, scripts_dir="scripts/"):
        if slurm_kwargs is None:
            slurm_kwargs = {}
        if tmpl is None:
            tmpl = TMPL

        header = []
        for k, v in slurm_kwargs.items():
            if len(k) > 1:
                k = "--" + k + "="
            else:
                k = "-" + k + " "
            header.append("#SBATCH %s%s" % (k, v))
        self.header = "\n".join(header)
        self.name = "".join(x for x in name.replace(" ", "-") if x.isalnum() or x == "-")
        self.tmpl = tmpl
        self.slurm_kwargs = slurm_kwargs
        if scripts_dir is not None:
            self.scripts_dir = os.path.abspath(scripts_dir)
        else:
            self.scripts_dir = None

    def __str__(self):
        return self.tmpl.format(name=self.name, header=self.header,
                                script="{script}")

    def _tmpfile(self):
        if self.scripts_dir is None:
            return tmp()
        else:
            if not os.path.exists(self.scripts_dir):
                os.makedirs(self.scripts_dir)
            return "%s/%s.sh" % (self.scripts_dir, self.name)

    def run(self, command, name_addition=None, cmd_kwargs=None, _cmd="sbatch"):
        """
        command: a bash command that you want to run
        name_addition: if not specified, the sha1 of the command to run
                       appended to job name
        cmd_kwargs: dict of extra arguments to fill in command
                   (so command itself can be a template).
        _cmd: submit command (change to "bash" for testing).
        """
        if name_addition is None:
            name_addition = hashlib.sha1(command.encode("utf-8")).hexdigest()

        if cmd_kwargs is None:
            cmd_kwargs = {}

        n = self.name
        self.name += ("-" + name_addition).strip(" -")

        tmpl = str(self).format(script=command)

        if "logs/" in tmpl and not os.path.exists("logs/"):
            os.makedirs("logs")

        with open(self._tmpfile(), "w") as sh:
            cmd_kwargs["script"] = command
            sh.write(tmpl.format(**cmd_kwargs))

        res = subprocess.check_output([_cmd, sh.name])
        print(res, file=sys.stderr)
        self.name = n
        if not res.startswith(b"Submitted batch"):
            return None
        job_id = int(res.split()[-1])
        return job_id

if __name__ == "__main__":
    import doctest
    doctest.testmod()
