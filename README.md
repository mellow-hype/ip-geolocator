# About
This is a simple script to lookup the geolocation of an IP address, limited to city and country. It uses the geoip2 Python module for and the open source MaxMind GeoLite2 City database for lookups. These will need to be present before using the script.

# Requirements
- geoip2 Python module
- [MaxMind Database C API](https://github.com/maxmind/libmaxminddb)
- [MaxMind GeoLite2 City DB](http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz)

# Setup
Before using the script, you must install the requirements listed above. The installation instructions in the links above are simple to follow and should work out of the box with most Linux distributions.  

`geoip2` can be installed via:

```
pip install geoip2
```

# Usage
```
python3 geoip.py -d <database> -t <target_ip>
```

