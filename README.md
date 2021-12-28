# loopia-dynamic-dns
DNS update script for loopia.se. Allows automatic update of a DNS record directly from a server, pc etc.

## USAGE ##

---

```python
Usage: python update.py
```

## SETUP ##

---
For anyone with some python experience this should be straight forward.

### Dependencies ###

#### Pre-requisite packages ###

- requests
- pyyaml

#### Needed softwares ####

- git
- python3.x

#### Step by step ####

1. Clone the repo
2. Install pre-requisite packages
3. Make a copy of sampleconfig.yml and name it config.yml
4. Configure config.yml with your settings (see configuration section)
5. Run script update.py

## CONFIGURATION ##

---

The script in its current form uses a yaml file for housing configuration.
A sample config has been provided and can be used as a base for your settings.

Note! You have to create an API user in loopias "Kundzon" with atleast the following 4 privileges set:
- getZoneRecords
- addZoneRecords
- updateZoneRecord
- removeZoneRecord

To update the base domain, simply put '@' as the subdomain, just as you would in any bind9 zone file.

### Logging ###

Logging is supported in the application.
As of now both file logging and stream logging (console) is added and can be enabled by configuration.

```yaml
log_level_console: 10
log_level_file: 0 
log_file: application.log
```

#### Log levels ####
|Log level|Value|
|---|---|
|Disabled|0|
|DEBUG|10|
|INFO|20|
|WARNING|30|
|ERROR|40|
|CRITICAL|50|

Setting a value to one of these numbers means you will see that level and all levels of a higher number in the console output. Example that will show Information, Warning, Error and Critical log messages:

```yaml
log_level_console: 20
```

### Configuration ###

The script will be looking for the file config.yml for its' settings.

Copy or rename the sample-config.yml to config.yml and update with your own settings.

