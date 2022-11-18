"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html 


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    contact = []
    # iterate through the file, parsing it line by line
    with open(f"{contacts}", "{job_description}") as a_file:
    # iterate through each line of the file and extract the current job
        for line in a_file:
            contact.append(line.strip())
    #return the list of the contacts who have a job description that matches
    return contact

