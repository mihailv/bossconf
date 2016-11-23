## BossConf
----------
```
When it's hard to parse it, BossConf it!
(config parser with token interpreter)
```

### Instalation:
  * for installation you need to use **pip install bossconf**.
  * python 2.6.6 up to 2.7.x version.

### Info:
    * you must run the CLI with parameters for path and filename.
    * you can also use it as module and just create instances.
    * options can be mixed in order to return more from CLI tool.


### Used as CLI:

#### bossconf:  
  * **bossconf /path/to/file "level1, level2"** - this command will access the level you want form file

#### CAT command:
  * **cat example.json &#124; bossconf "level1, level2"** - this command will read and parse data from file and outputs the content.

#### ECHO command:
  * **echo '{"key":"value"}' &#124; bossconf 'key'** - this command will parse the string containing data for parsing and display the content.

#### Examples
 * given the following files you can have:

![](https://s22.postimg.org/f11tyxzox/json_dev.png)

1. `bossconf example.yaml "anne, has"` and the output will be:

    ![](https://s17.postimg.org/p70db1ozj/parser_yaml.png)

2. `bossconf example.json "anne, marry"` and the output:

    ![](https://s22.postimg.org/3r943zunl/parser_json.png)

3. `cat example.json "anne, has"` the output will be:

    ![](https://s21.postimg.org/rnyka46x3/catcommand.png)

4. `echo '{"anne":{"has":"apples","marry":["has pears"]}}' | bossconf "anne, marry"` and the output:

    ![](https://s17.postimg.org/7iyco8sb3/echocommand.png)

### Used as library:
 * you just need to import the moduel and create a new instance.
 * the next step is to use `.get()` function and print the output.
 * we will use the same two file form the CLI example.

#### Examples
 * for BossConfing an json file we will do the following:
![](https://s11.postimg.org/xq5qn4dir/config_get.png)

 * for BossConfing an yaml file we will need to do:
![](https://s15.postimg.org/ipx9hvg97/config_get_yaml.png)

