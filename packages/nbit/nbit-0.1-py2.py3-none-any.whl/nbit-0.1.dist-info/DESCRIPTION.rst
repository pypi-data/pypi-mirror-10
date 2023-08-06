==================================================================
NBit: Node! Build IT!
==================================================================

NBit: Build tool for node.js projects

This is simple build tool allows you to make one js file from sources listed in template.


Installation
------------

    $ pip install nbit

Usage
-----

- Create template file with sources listed at JsDoc with tag @src, as follows:
```
/**
 * @src
 *
 * path/to/src/1.js
 * path/to/src/1.js
 * path/to/src/1.js
 */
```

- Run nbit:   

        $ nbit path/to/templte.js

    also you can specify output direcroty (defauld: ./bin):

        $ nbit path/to/template.js --out path/to/out/dir

    if you want to build many templates, you can list them all:   

        $ nbit path/to/template1.js path/to/template2.js

    nbit names output files with names of templates   

- You can use it with npm. Just add nbit into scripts to your package.json:   
```
    ...,
    "scripts": {
        "build": "nbit path/to/template.js"
    },
    ...
```


