#!/usr/bin/python
import commands
'''
File: pythonpacman.py
Author: Vesso Somlev
Description: Simple python script to read information from pacman.
'''


def _read_ignorepkg_line():
    """ Returns the IgnorePkg line from /etc/pacman.conf """
    conf_file = open("/etc/pacman.conf", 'r')
    raw = conf_file.read()
    conf_file.close()
    lines = raw.split('\n')

    ignore_line = ""
    for line in lines:
        if line.strip().startswith("IgnorePkg"):
            ignore_line = line
            break

    return ignore_line


def get_ignored_count():
    """ Returns the count of packages in IgnorePkg from pacman.conf """
    return len(list_ignorepkg())


def list_ignorepkg():
    """ Returns a list containing the names of packages in IgnorePkg. """
    ignore_line = _read_ignorepkg_line()
    ignore_pgks = ignore_line.split("=")[1].strip().split(" ")
    if len(ignore_pgks) == 1 and ignore_pgks[0] == "":
        return []
    else:
        return ignore_pgks

def list_due_update():
    """ Returns a list containing the names of packages that can be updates. """
    status, output = commands.getstatusoutput("pacman -Qu")
    if status != 0:
        print "Error while listing packages (pacman -Qu). Status: ", status, " Output:"
        print output
        return
    
    packages_list = set(output.split('\n'))
    # convert to a list of (pkg_name, version) tuples
    packages = []
    for pkg in packages_list:
        t = pkg.split(' ')
        packages.append((t[0], t[1]))
    packages = set(packages)
    
    # filter out the ignored packages
    ignored = set(list_ignorepkg())
    packages = [x for x in packages if x[0] not in ignored]
    print len(packages), packages
    
    return packages


if __name__ == '__main__':
    #print get_ignored_count()
    #print list_ignorepkg()
    list_due_update()
