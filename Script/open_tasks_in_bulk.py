# libraries
import sys
import requests
import json


def QueryTicket():
    """In my QueryTicket function, I passed a variable to get the information from a specific view.
    The name of this variable is "queue" and its value is the ID of the Zendesk view separated by the Divergent Balance contact reasons.
    :Return: I return the request in Json format and handle the necessary fields in the main program.(Main).
    """
    queue_id = "1234"
    subdomain = "company"
    url = f"https://{subdomain}.zendesk.com/api/v2/views/{queue_id}/tickets"
    headers = {"Authorization": "Basic ABCDC"}
    response_zend = requests.get(url, headers=headers)
    dados = response_zend.json()
    return dados


def PostJira():
    """In the PostJira function, I make a POST method for Jira with the following information:
    Note: It is the name of the field following its variable.
    And creating the Task in the Zendesk link is not performed, as they are separate Apps.
    :Return: Save returning the request for treatment in the main program.(Main)!!!"""
    domain = ""
    url = f"https://{domain}.atlassian.net/rest/api/3/issue"
    payload = json.dumps(
        {
            "fields": {
                "summary": "Exemplo - Ticket - " + str(id),
                "issuetype": {"id": "1234"},  # type issue id
                "project": {"key": "TEST"},  # key project
                "description": {
                    "version": 1,
                    "type": "doc",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [{"type": "text", "text": "Hello guys"}],
                        }
                    ],
                },
                "reporter": {"id": "1234"},
                "assignee": None,
            }
        }
    )
    headers = {
        "Authorization": "",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": "",
    }

    response_jira = requests.POST(url, headers=headers, data=payload)
    jira = response_jira.json()
    return jira


def keyjira():
    """In the Keyjira function, I use this function only to link the task with the call in Zendesk.
    Note: Creating the Task in Zendesk is not linked, as they are separate Apps.
    :Return: In Return I inform the ticket linked with the Id of the Task Jira and the creation date!!!"""
    yourdomain = ""
    url = f"https://{yourdomain}.zendesk.com/api/services/jira/links"
    payload = json.dumps(
        {"link": {"ticket_id": id, "issue_id": id_issue, "issue_key": id_jira}}
    )
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic XXXX",
        "Cookie": "",
    }

    response = requests.post(url, headers=headers, data=payload)
    return response


def attachment():
    """In the attachment function, I only use this function to attach the log in json in the jira task.
    :Return: In the Return, I inform the attachment in the Id Jira!!!"""
    yourdomain = ""
    url = f"https://{yourdomain}.atlassian.net/rest/api/3/issue/{id_jira}/attachments"
    payload = {}
    files = [
        (
            "file",
            (
                "Ticket_" + str(id) + ".json",
                open(
                    "C:/Users/Tokoyamy/Documents/Code/Python/Log/ticket_"
                    + str(id)
                    + ".json",
                    "rb",
                ),
                "application/json",
            ),
        )
    ]
    headers = {
        "X-Atlassian-Token": "no-check",
        "Authorization": "Basic XXXX",
        "Cookie": "",
    }

    response = requests.post(url, headers=headers, data=payload, files=files)

    arq = response.json()
    return arq


if __name__ == "__main__":
    # Passing the function and saving the return in the variable
    tick = QueryTicket()
    # Loop - Tickets
    x = len(tick["tickets"]) - 1
    i = 0
    while i <= x:
        ticket = tick["tickets"][i]
        i += 1
        id = ticket["id"]

        aList = [
            {
                            "ID_Zendesk": id,
                            "status:": tick["ticket"]["status"],
                            "created_at:": tick["ticket"]["created_at"],
                            "Updated_at:": tick["ticket"]["updated_at"],
                            "channel:": tick["ticket"]["via"]["channel"],
                            "subject:": tick["ticket"]["subject"],
                            "raw_subject:": tick["ticket"]["raw_subject"],
                        },
                        {"description:": tick["ticket"]["description"]},
                    {"tags:": tick["ticket"]["tags"]}
                ]
        jsonString = json.dumps(aList)
        jsonFile = open(
                    "C:/Users/Tokoyamy/Documents/Code/Python/Log/Ticket_"
                    + str(id)
                    + ".json",
                    "w",
        )
        jsonFile.write(jsonString)
        jsonFile.close()

        jira = PostJira()
        id_jira = jira["key"]  # Variable to save the key of the jira
        id_issue = jira["id"]  # Variable to save to ID_issue

        att = attachment()
        attname = att[0]["filename"]

        keyjira()
        print("Ticket:",id,"task created",id_jira,"id_issue",id_issue,"attachment:",attname,"!!")
        


print("finished script!!!")
