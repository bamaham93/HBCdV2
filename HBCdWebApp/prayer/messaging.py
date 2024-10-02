"""
Adds messaging capability to the app.
"""


class Message:
    """
    """

    def __init__(self, message: str, to_list: list):
        """
        """
        self.message = message
        self.to_list = to_list

        self.failed_to_send_to = set()

    def send_all_messages(self):
        """
        """
        for person in self.to_list:
            print(person.email)

    def send_sms_messages(self):
        """
        :return:
        """

    def send_whatsapp_messages(self):
        """
        :return:
        """

    def send_email_messages(self):
        """
        :return:
        """

    def add_person_to_message_list(self, first_name: str, last_name: str, cell_number: str, services: set):
        """
        :param first_name: str
        :param last_name: str
        :param cell_number: str - The user's cell phone number to accept SMS.
        :param services: set - The messaging services allowed by the user, in the order preferred.
        :return:
        """
        self.to_list.append({'first_name': first_name, 'last_name': last_name, 'cell_number': cell_number, 'services': services})
