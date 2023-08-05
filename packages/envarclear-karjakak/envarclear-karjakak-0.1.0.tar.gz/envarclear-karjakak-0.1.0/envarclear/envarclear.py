# -*- coding: utf-8 -*-
# Copyright (c) 2022, KarjaKAK
# All rights reserved.

import os
import subprocess as sp


class Cleaner:
    """Functions for deleting an Environment Variable in Windows and MacOS X"""

    def wind(self, var: str):
        """
        Deleting Environment Variable in Windows
        Ref from:
        https://www.tenforums.com/tutorials/121797-delete-user-system-environment-variables-windows.html
        Using subprocess to run the powershell command.
        """

        v = f'"{var}"'
        u = '"User"'
        pnam = [
            "powershell",
            "-Command",
            f"[Environment]::SetEnvironmentVariable({v}, $null, {u})",
        ]
        with sp.Popen(
            pnam,
            stdout=sp.PIPE,
            bufsize=1,
            universal_newlines=True,
            text=True,
        ) as p:
            if not (gt := p.stdout.read()):
                print(f'{"-" * 50}')
                print(f"Var: {v}\nSuccessfully deleted!")
            else:
                print(f'{"-" * 50}')
                print(gt)
            print(f'{"-" * 50}')

    def rearr(self, st: iter) -> iter:
        """
        Arranging order of an iter state text or IOwrapperText.
        Long spaces like '\n' will not be collected.
        Format:
            '<text> \n'
            \n
            \n
            '<text> \n'
        to:
            '<text> \n'
            \n
            '<text> \n'
        """

        arr = tuple(st)
        tot = len(arr)
        seta = []
        for j in range(tot):
            if not arr[j].isspace():
                seta.append(arr[j])
            elif j + 1 < tot and not arr[j + 1].isspace():
                seta.append(arr[j])
        del arr, tot
        return iter(seta)

    def macs(self, var: str, prof: str):
        """
        MacOS X way of deleting Variable Environment
        var: str = Environment Variable Name
        prof: str = Mac file that usually start with '.' and contain the variable.
        WARNING:
        Some changes to the file cannot be undone.
        Advisable to make a backup file before deleting anything.
        """

        l1 = f"{var}="
        l2 = f"export {var}"
        fl = os.path.join(os.environ["HOME"], prof)
        fr = os.path.join(os.environ["HOME"], "._profile_temp")
        if os.path.exists(fl):
            with (open(fl, "r") as en, open(fr, "w") as ew):
                for j in en:
                    if not any(f in j for f in [l1, l2]):
                        ew.write(f"{j}")
            with (open(fr, "r") as en, open(fl, "w") as ew):
                for i in self.rearr(iter(en)):
                    ew.write(i)
            os.remove(fr)
        del l1, l2, fr, fl
