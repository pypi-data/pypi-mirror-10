json-cfg
========

The goal of this project is providing a json config file loader that has
the following extras compared to the standard json.loads():

- A larger subset of javascript (and not some weird/exotic extension to json that
  would turn json into something that has nothing to do with json/javascript):

    - single and multi-line comments
    - object (dictionary) keys without quotes
    - trailing commas (allowing commas after the last item of objects and arrays)

- Providing line number information for each element of the loaded config file
  and using this to display useful error messages that help locating errors not
  only while parsing the file but also when processing/interpreting it.
- A nice config query syntax that handles default values, required elements and
  automatically raises an exception in case of error (with useful info including
  the location of the error in the config file).


Config file examples
--------------------

*Hint: use javascript syntax highlight in your text editor for json config files whenever possible - this makes reading config files much easier especially when you have a lot of comments or large commented config blocks.*

**A traditional json config file:**

.. code:: javascript

    {
        "servers": [
            {
                "ip_address": "127.0.0.1",
                "port": 8080
            },
            {
                "ip_address": "127.0.0.1",
                "port": 8081
            }
        ],
        "superusername": "tron"
    }

**The same with json-cfg:**

.. code:: javascript
    
    {
        // Note that we could get rid of most quotation marks.
        servers: [
            {
                ip_address: "127.0.0.1",
                port: 8080
            },
            // We have commented out the block of the second server below.
            // Trailing commas are allowed so the comma after the
            // first block (above) doesn't cause any problems.
            /*
            {
                ip_address: "127.0.0.1",
                port: 8081
            },  // <-- optional trailing comma
            /**/
        ],
        superusername: "tron",  // <-- optional trailing comma
    }

Building...
-----------

The beta of this library will be ready by the end of the week so visit
back if you are interested.

Sorry for the missing docs. The library is basically ready and its low
level code is quite well covered with test but I will have to add some
more high level test code along with the documentation and the examples.

Brief code examples
-------------------

TODO

Detailed API docs
-----------------

TODO
