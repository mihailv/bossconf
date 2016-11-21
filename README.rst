BossConf
=======================
Configs parsing with token interpreter

Used as library :

  Yaml file:

    ``x:``
     ``y:1``
    

  Code:

    Get y value

    `from bossconf import BossConf`

    conf = BossConf(absolute_path)`

    `print conf.get(['x', 'y'])`

  Return data:

    if found value ( from conf )
    
    if not found None value

---
