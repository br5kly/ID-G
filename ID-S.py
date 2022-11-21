import platform
bit = platform.architecture()[0]
if bit == "64bit":
   from srq import sql
   sql()
if bit == "32bit":
    from ssz import sql 
    sql()
