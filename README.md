## BossConf
----------
### Info:
```
When it's hard to parse it, BossConf it!
- config library for python application
- CLI tool
```

### Instalation:
  * for installation you need to run **pip install bossconf**.
  * python 2.6.6 up to 2.7.x version.


### Used as CLI:

#### File as argument  
  * **bossconf /path/to/file "level1, level2"** - this command will access the level you want form file

#### Used with pipe
  * **cat example.json &#124; bossconf "level1, level2"** - this command will read and parse data from file and outputs the content.

  * **echo '{"key":"value"}' &#124; bossconf 'key'** - this command will parse the string containing data for parsing and display the content.

  * **curl curl -u user:password 'http://your/url/'** | bossconf

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

5. `curl -u guest:rate 'http://example.com/api/queues' | bossconf` will output:

    ![](https://s14.postimg.org/63murpfr5/example2_curl.png)

6. `curl -u guest:rate 'http://example.com/api/queues' | bossconf '0, back'` will display:

    ![](https://s17.postimg.org/p4622u1mn/curl_example.png)

### Used as library:
 * you just need to import the moduel and create a new instance.
 * the next step is to use `.get()` function and print the output.
 * we will use the same two file form the CLI example.

#### Examples
 * for BossConfing an json file we will do the following:
![](https://s11.postimg.org/xq5qn4dir/config_get.png)

 * for BossConfing an yaml file we will need to do:
![](https://s15.postimg.org/ipx9hvg97/config_get_yaml.png)

