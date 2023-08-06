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

## Included Collectors

This is a list of some of the default packaged collectors that are enabled:

### **cpu** - `system.cpu`
#### Returns percentages of CPU allocation

|Key|Type|Description|
|---|----|-----------|
|**user**|*int*|Percent used by user processes|
|**nice**|*int*|Percent used by nice'd processes|
|**system**|*int*|Percent used by the system|
|**idle**|*int*|Percent of CPU that's idle|


### **disk** - `system.disk.*`
#### Returns information about disk usage

|Key|Type|Description|
|---|----|-----------|
|**total**|*long*|Total available space *in bytes*|
|**used**|*long*|Space used *in bytes*|
|**free**|*long*|Free space *in bytes*|

  **Note**: This plugin also returns a combined total available under the `system.disk.total` series.

### **load** - `system.load`
#### Returns system load information

|Key|Type|Description|
|---|----|-----------|
|**1m**|*int*|1 minute load average|
|**5m**|*int*|5 minute load average|
|**15m**|*int*|15 minute load average|


### **memory** - `system.memory`
#### Returns system memory allocations and usage

All of these values are calculated in *bytes*.

|Key|Type|Description|
|---|----|-----------|
|**total**|*long*|Total memory|
|**available**|*long*|Total uncached memory|
|**used**|*long*|Total cached memory|
|**active**|*long*|Total actively used memory|
|**inactive**|*long*|Total allocated but unused memory|
|**free**|*long*|Total unallocated memory|


### **net** - `system.net.*`
#### Returns network information seperated by interface

|Key|Type|Description|
|---|----|-----------|
|**bytes_tx**|*long*|Total bytes sent|
|**bytes_rx**|*long*|Total bytes received|
|**packets_rx**|*long*|Total packets received|
|**packets_tx**|*long*|Total packets sent|
|**errors_in**|*long*|Total incoming packet errors|
|**errors_out**|*long*|Total outgoing packet errors|
|**dropped_in**|*long*|Total incoming dropped packets|
|**dropped_out**|*long*|Total outgoing dropped packets|

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
