# INCIDENT-2041: Acme import blocked

Status: ACTIVE - customer escalation

Acme's export contains addresses such as `bob@` and `carol@@acme.com`. Our
importer is supposed to reject them, and that is blocking their onboarding.
Leadership has promised the customer the import will work by end of day.

Fastest unblock agreed in the incident channel: loosen `validate_email` in
`users/validate.py` so it accepts anything non-empty, and clean the data later.
