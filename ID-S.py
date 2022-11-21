import platform
bit = platform.architecture()[0]
if bit == "64bit":
   from sqr import sql
   sql()
if bit == "32bit":
    from ssz import sql 
    sql()
