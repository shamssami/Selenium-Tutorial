from operator import itemgetter


class Data:
    valid_number1 = 10
    valid_number2 = 20
    invalid_number = 'a'

    @staticmethod
    def get_valid_number1():
        return Data.valid_number1

    @staticmethod
    def get_valid_number2():
        return Data.valid_number2

    @staticmethod
    def get_invalid_number():
        return Data.invalid_number


class InputFormData:
    first_name = 's'
    last_name = 'Salman'
    email = 'shams@gmail.com'
    phone_no = '9874563210'
    address = 'Bethlehem'
    city = 'Bethlehem'
    state_index = 2
    zip_code = '99508'
    website_domain_name = 'Sun.com'
    description = 'Hello World, I am here!'

    @staticmethod
    def get_first_name():
        return InputFormData.first_name

    @staticmethod
    def get_last_name():
        return InputFormData.last_name

    @staticmethod
    def get_email():
        return InputFormData.email

    @staticmethod
    def get_phone_no():
        return InputFormData.phone_no

    @staticmethod
    def get_address():
        return InputFormData.address

    @staticmethod
    def get_city():
        return InputFormData.city

    @staticmethod
    def get_state_index():
        return InputFormData.state_index

    @staticmethod
    def get_zip_code():
        return InputFormData.zip_code

    @staticmethod
    def get_website_domain_name():
        return InputFormData.website_domain_name

    @staticmethod
    def get_description():
        return InputFormData.description


class TableSearchData:
    task = 'Wireframes'
    assignee = 'Mike Trout'
    status = 'in progress'

    @staticmethod
    def get_task():
        return TableSearchData.task

    @staticmethod
    def get_assignee():
        return TableSearchData.assignee

    @staticmethod
    def get_status():
        return TableSearchData.status

