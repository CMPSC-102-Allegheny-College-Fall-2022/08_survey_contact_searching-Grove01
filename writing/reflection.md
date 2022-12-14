# Contact Searching
Make sure that you delete all of the  markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## Xavier Grove

## Program Output

### What is the output from running the following commands?

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```
- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "neer":


Wow, we found some contacts! Email them to learn about your job!
```
- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```
from search import search_for_email_given_job
```
This import statement is taking the function from the search file and then I can use that function in the main file rather than going between both files.
#### The source code statement that extracts the current job description for a contact

 ```
 job_description: str = typer.Option(..., prompt=True)
 ```
This source code is taking the job_description from the user in the input test command which makes it produce a certain output based on what the input is if the input is a job then it might return those who share the job type.
#### Invocation of the function called `search_for_email_given_job`

```
def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    contact = []
    # iterate through the file, parsing it line by line
    with open(f"{contacts}", "{job_description}") as a_file:
        # iterate through each line of the file and extract the current job
        for line in a_file:
            contact.append(line.strip())
    # return the list of the contacts who have a job description that matches
    return contact

```
The source code is taking the input of the job description and the contacts. it is then taking the list contact and making is and itterating through the file that is contacts and iterating through it to separate the lists and then append them to the list and then return that list to the main file.
#### Test case for the function called `search_for_email_given_job`



#### Execute trace of the `contactsearcher` program

Explain each function call that takes place for the following run of the program
Write at least one paragraph to explain every function call when running `contactsearcher`

Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

I still struggle asking for help and time management especially when it comes to computer science and i have been making it slowly that I need to be better ad doing this

### Based on your experiences with this project, what is one way in which you want to improve?

I would like to be able to understand my code better and this will help be get better at doing other part of computer science because ill be able to communicate better with people inside the department.