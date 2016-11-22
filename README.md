# BossConf
----------
```
When it's hard to parse it, **BossConf it!**. (config parser with token interpreter)
```

## Instalation:
  * for installation you need to use **pip install bossconf**.
  * python 2.6.6 up to 2.7.x version.

### Info:
    * for the program to run you need privileges to install packages.
    * you must run the CLI with parameters for path and filename.
    * options can be mixed in order to return more from CLI tool.

## OPTIONS:

### HELP: python bossconf -h
  * this command shows you all the options avilable.

### CAT command: cat parsing_file &#124; bossconf "level1, level2"
  * this command will read and parse data from file and outputs the content.

### ECHO command: echo '{"key":"value"}' &#124; bossconf 'key'
  * this command will parse the string containing data for parsing and display the content.

## EXAMPLES
 * given the following file you can have:

|File                                                   | Command                                          | Output        |
|:-----------------------------------------------------:|--------------------------------------------------|:-------------:|
| ![](https://s15.postimg.org/xsns4uyff/yaml.png)       |**bossconf parsing_file "anne, has"**             |**apples**     |
| ![](https://s11.postimg.org/uicqqkvlv/stringparse.png)|**bossconf parsing_file "anne, marry"**           |**has pears**  |
| ![](https://s15.postimg.org/xsns4uyff/yaml.png)       |**cat parsing_file &#124; bossconf "anne"**       |**apples**     |
| '{"anne":{"has":"apples","marry":["has pears"]}}'     |**echo '{"key":"value"}' &#124; bossconf "marry"**|**has pears**  |


