# pylint: disable=too-few-public-methods
"""Module for creating SNOW tickets."""
import logging
import json
import requests


class Snow:
    """Class to handle SNOW operations

    This module creates SNOW tickets, the attributes are taken from the
    config object passed
    """
    def __init__(self, config: dict = None):
        """Initialize config object

        Parameters
        ----------
        config: cerndb.config
            A config object for connecting with SNOW
        """
        self.config = config

    def make_incident(self, mail_message: str, mail_title: str):
        """Creates a SNOW Ticket with information about the event

        Parameters
        ----------
        mail_message: str
            The string containing the ticket message
        mail_title: str
            The string containing the title/subject of the ticket
        """
        # Authentication details
        usr = self.config['SNOW_USER']
        psw = self.config['SNOW_PASS']

        # Proxy for https since service-now is hosted outside CERN
        proxies = {
            'https': self.config['SNOW_PROXY']
        }

        # Creating session
        session = requests.Session()
        session.auth = (usr, psw)
        session.proxies.update(proxies)

        # SNOW API Endpoint
        url = f"https://{self.config['SNOW_HOST']}/api/now/v1/table/incident"
        # Timeout (in seconds)
        timeout = int(self.config.get('SNOW_CONNECTION_TIMEOUT_SECONDS', '20'))
        # Standard Headers
        headers = {
            'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Payload for SNOW ticket creation
        data = {
            "short_description": f"{mail_title}",
            "description": f"{mail_message}",
            "comments": f"{mail_message}",
            "u_functional_element": self.config.get(
                'SNOW_DEFAULT_FUNCTIONAL_ELEMENT'),
            "assignment_group": self.config.get(
                'SNOW_DEFAULT_ASSIGNMENT_GROUP'),
            "u_business_service": self.config.get(
                'SNOW_DEFAULT_SERVICE_ELEMENT')
        }

        # Response from SNOW API
        response = session.post(url, headers=headers, data=json.dumps(data),
                                timeout=timeout)

        # Error Handling
        if response.status_code != 201:
            logging.debug("Can't create SNOW ticket : %s", response.json())

        # Get Ticket Number and log it
        incident = response.json()
        ticket_id = incident["result"].get("task_effective_number")
        logging.debug("Ticket ID : %s", ticket_id)

        session.close()
