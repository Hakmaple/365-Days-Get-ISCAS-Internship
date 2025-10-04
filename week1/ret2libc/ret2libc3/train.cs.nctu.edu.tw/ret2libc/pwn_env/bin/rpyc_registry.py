#!/home/zhailin/365-Days-Get-ISCAS-Internship/week1/ret2libc/ret2libc3/train.cs.nctu.edu.tw/ret2libc/pwn_env/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from rpyc.cli.rpyc_registry import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
