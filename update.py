#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Loopia DNS update client

This application is for educational purposes only.
Do no evil, do not break local or internation laws!
By using this code, you take full responisbillity for your actions.
The author have granted code access for educational purposes and is
not liable for any missuse.
"""
__author__ = "Jonas Werme"
__copyright__ = "Copyright (c) 2021 Jonas Werme"
__credits__: list = ["nsahq"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Jonas Werme"
__email__ = "jonas[dot]werme[at]hoofbite[dot]com"
__status__ = "Prototype"

import xmlrpc.client

from requests import get

from config import yaml_config_to_dict
from logger import get_logger


def clean_records(config: dict, zone_records) -> int:
    """Remove all A records except the first one"""

    count = 0
    for record in zone_records:
        status = client.removeZoneRecord(
            config["username"],
            config["password"],
            config["domain"],
            config["subdomain"],
            record["record_id"],
        )

        if status == "OK":
            count += 1
        if count != len(zone_records):
            raise Exception("Unable to remove all zone records")

    return count


def get_ip():
    """Get public IP adress"""

    return get("https://api.ipify.org/").content.decode("utf8")


def get_records(config: dict, record_type: list = ["A"]) -> list:
    """Get current A records for a subdomain in a zone"""

    if not config:
        raise ValueError("Missing or invalid configuration parameters")

    try:
        zone_records: list = client.getZoneRecords(
            config["username"],
            config["password"],
            config["domain"],
            config["subdomain"],
        )

        if "AUTH_ERROR" in zone_records:
            raise ConnectionError(
                "UNAUTHORIZED: Unable to authenticate. Please check your user/pass."
            )

        # Quit if API returns unknown error
        if "UNKNOWN_ERROR" in zone_records:
            raise ConnectionAbortedError(
                "UNKNOWN ERROR: Could not process request or requested (sub)domain does not exist"
                " in this account."
            )

        return [d for d in zone_records if d["type"] in record_type]

    except xmlrpc.client.Error:
        raise


def add_record(config: dict, ip: str) -> bool:
    """Add a new A record to a subdomains in a zone"""

    if not config or ip == "":
        raise ValueError("Missing or invalid configuration parameters")

    new_record = {
        "priority": "",
        "rdata": ip,
        "type": "A",
        "ttl": config.get("ttl", 3600),
    }

    try:
        status = client.addZoneRecord(
            config["username"],
            config["password"],
            config["domain"],
            config["subdomain"],
            new_record,
        )
        if status == "OK":
            return True

        raise Exception("Unable to add a new record")
    except xmlrpc.client.Error:
        raise


def update_record(config: dict, ip: str, record: dict) -> int:
    """Update an existing A record for a subdomain in a zone"""

    if record["rdata"] == new_ip and int(record["ttl"]) == int(config["ttl"]):
        return False
    new_record = {
        "priority": record["priority"],
        "record_id": record["record_id"],
        "rdata": new_ip,
        "type": record["type"],
        "ttl": config["ttl"],
    }

    try:
        status = client.updateZoneRecord(
            config["username"],
            config["password"],
            config["domain"],
            config["subdomain"],
            new_record,
        )

        if status == "OK":
            return True

        raise Exception("Unable to perform update action")

    except xmlrpc.client.Error:
        raise


if __name__ == "__main__":

    try:
        cfg = yaml_config_to_dict(expected_keys=["username", "password", "domain", "subdomain"])
        log = get_logger(
            name=__name__,
            log_level_console=cfg["log_level_console"],
            log_level_file=cfg["log_level_file"],
        )

        log.debug("Configuration and logging initialized")

        client = xmlrpc.client.ServerProxy(uri="https://api.loopia.se/RPCSERV", encoding="utf-8")
        log.debug("Client initialized")

        a_records = get_records(cfg, record_type=["A"])
        log.debug(f"Found {len(a_records)} A records")

        new_ip = get_ip()
        log.debug(f"Current public ip is {new_ip}")

        fqdn = cfg["domain"] if cfg["subdomain"] == "@" else f"{cfg['subdomain']}.{cfg['domain']}"

        try:
            if len(a_records) > 1:
                count_removed = clean_records(cfg, a_records[1:])
                log.info(f"Cleaned up {count_removed} A records in {fqdn}")

            if len(a_records) == 0:
                if add_record(cfg, new_ip):
                    log.info(f"Added a new A record for {new_ip} in {fqdn}")
                    exit(0)
                else:
                    log.critical("Unable to create record, exiting")
                    exit(2)

                if update_record(cfg, new_ip, a_records[0]):
                    log.info(f"Updated the A record for {new_ip} in {fqdn}")
                else:
                    log.info("Already up to date")
        except Exception as e:
            log.critical(e)
            raise

    except Exception as e:
        exit(f"{e}")
