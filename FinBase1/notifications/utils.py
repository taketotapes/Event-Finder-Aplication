def send_notification_email(subject, message, from_email, to_emails):
    """
    Layout of the function for sending notifications by mail.
    It simply displays information about the supposed sent letter.

    :param subject: Subject of the letter.
    :param message: Contents of the letter.
    :param from_email: Sender address.
    :param to_emails: List of recipient addresses.
    """
    print("Mocking email sending:")
    print(f"Subject: {subject}")
    print(f"Message: {message}")
    print(f"From: {from_email}")
    print(f"To: {', '.join(to_emails)}")