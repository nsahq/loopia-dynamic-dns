# loopia-dynamic-dns

DNS update script for loopia.se. Allows automatic update of a DNS record directly from a server, pc etc.

- [loopia-dynamic-dns](#loopia-dynamic-dns)
  - [Usage](#usage)
  - [Setup](#setup)
    - [Dependencies](#dependencies)
      - [Needed softwares](#needed-softwares)
      - [Step by step](#step-by-step)
  - [CONFIGURATION](#configuration)
    - [Logging](#logging)
      - [Log levels](#log-levels)
    - [Configuration](#configuration-1)

## Usage

```python
Usage: python update.py
```

## Setup

For anyone with some python experience this should be straight forward.

### Dependencies

- requests
- pyyaml

#### Needed softwares

- python3.x

#### Step by step

1. Clone the repo or get the script files to your hard drive in 2ome other way
2. Install pre-requisite packages locally or in your virtual environment

```python
pip install -r requirements.txt
```

3. Make a copy of sampleconfig.yml and name it config.yml

```bash
cp sample-config.yml config.yml
```

4. Configure config.yml with your settings (see configuration section)
5. Run script update.py

```python
python3 update.py
```

## CONFIGURATION

The script in its current form uses a yaml file for housing configuration.
A sample config has been provided and can be used as a base for your settings.

Note! You have to create an API user in loopias "Kundzon" with atleast the following 4 privileges set:

- getZoneRecords
- addZoneRecords
- updateZoneRecord
- removeZoneRecord

To update the base domain, simply put '@' as the subdomain, just as you would in any bind9 zone file.

### Logging

Logging is supported in the application.
As of now both file logging and stream logging (console) is added and can be enabled by configuration.

```yaml
log_level_console: 10
log_level_file: 0 
log_file: application.log
```

#### Log levels

| Log level | Value |
| --------- | ----- |
| Disabled  | 0     |
| DEBUG     | 10    |
| INFO      | 20    |
| WARNING   | 30    |
| ERROR     | 40    |
| CRITICAL  | 50    |

Setting a value to one of these numbers means you will see that level and all levels of a higher number in the console output. Example that will show Information, Warning, Error and Critical log messages:

```yaml
log_level_console: 20
```

### Configuration

The script will be looking for the file config.yml for its' settings.

Copy or rename the sample-config.yml to config.yml and update with your own settings.
