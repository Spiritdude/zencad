#!/usr/bin/env python3
#coding: utf-8

import zencad

m = zencad.ngon(r = 10, n = 6).fillet(4)
zencad.display(m)

zencad.show()