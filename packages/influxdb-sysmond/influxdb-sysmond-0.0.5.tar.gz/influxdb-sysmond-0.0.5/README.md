# InfluxDB-sysmond

A system monitoring daemon for recording server statistics in [InfluxDB](http://influxdb.com/).

## WIP

This software is a WIP and the configuration file is most likely going to change often, so errors might happen and other weird things. So just be warned.

## Installation

You can install this via PyPI, like so:

```sh
sudo pip install influxdb-sysmond
```

And then all you have to do is go to **/etc/influxdb-sysmond/** and edit the **config.ini.dist** file there and you should be ready to log.

Assuming that you renamed the config file to **config.ini**, you can go ahead and run this:

```sh
influxdb-sysmond /etc/influxdb-sysmond/config.ini
```

And the daemon will start logging everything to the InfluxDB server you specified.

## Custom Collectors
You can go ahead and add collectors to the **/etc/influxdb-sysmond/collectors/** (making sure to import them in the **__init__.py** file) and we will automatically run them in the cycles and report their values.

Here's some examples:
**collectors/example.py**:

```python
import rand

class ExampleCollector(CollectorThread):
  identifier = 'example' # This is required!

  def collect(self, cache):
      # Stateful cache (across collections)
      if last in cache:
        cache['last'] = rand.randint(0, 100)

      return [{
          "name": "your.point",
          "columns": [
              "walk"
          ],
          "points": [
              rand.randint(0, 100)
          ]
      }]
```

And import it in **collectors/__init__.py**:

```python
from .example import *
```

## License

MIT license, see the **LICENSE** file.
