from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class FormPageLocators(object):
    FormUrl = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
    NumberField1 = (By.XPATH, '//*[@id="sum1"]')
    NumberField2 = (By.XPATH, '//*[@id="sum2"]')
    TotalButton = (By.XPATH, '//*[@id="gettotal"]/button')


class InputFormLocators(object):
    InputFormUrl = 'https://www.seleniumeasy.com/test/input-form-demo.html'
    first_name = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[1]/div/div/input')
    last_name = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[2]/div/div/input')
    email = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[3]/div/div/input')
    phone_no = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[4]/div/div/input')
    address = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[5]/div/div/input')
    city = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[6]/div/div/input')
    state = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[7]/div/div/select')
    zip_code = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[8]/div/div/input')
    website_domain_name = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[9]/div/div/input')
    radio_button = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[10]/div/div[2]/label/input')
    description = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[11]/div/div/textarea')

    valid = (By.XPATH, '//*[@id="contact_form"]/fieldset/div[1]/div/i')
    invalid = (By.XPATH, '//*[@id="contact_form"]/fieldset/div/div/small')


class TableSearchLocators(object):
    TableSearchUrl = 'https://www.seleniumeasy.com/test/table-search-filter-demo.html'
    input_filter_field = (By.XPATH, '//*[@id="task-table-filter"]')
    input_data_field = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[1]/input')
    filter_activate_button = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')


###########################33

class TablePaginationLocators(object):
    TablePaginationUrl = 'https://www.seleniumeasy.com/test/table-pagination-demo.html'
    rows = (By.XPATH, '//*[@id="myTable"]/tr')
    page_link1 = (By.XPATH, '//*[@id="myPager"]/li[2]/a')
    page_link2 = (By.XPATH, '//*[@id="myPager"]/li[3]/a')
    page_link3 = (By.XPATH, '//*[@id="myPager"]/li[4]/a')
    prev_link = (By.XPATH, '//*[@id="myPager"]/li[1]/a')
    next_link = (By.XPATH, '//*[@id="myPager"]/li[5]/a')


class ProgressBarsLocators(object):
    JqueryProgressUrl = 'https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html'
    BootstrapProgressUrl = 'https://www.seleniumeasy.com/test/bootstrap-download-progress-demo.html'
    download_button = (By.XPATH, '//*[@id="downloadButton"]')
    progress_label = (By.XPATH, '//*[@id="dialog"]/div[1]')

    circle_button = (By.XPATH, '//*[@id="cricle-btn"]')
    percent_field = (By.XPATH, '//*[@id="circle"]/div/div[1]')


class AlertsLocators(object):
    AlertsUrl = 'https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html'
    autoclosable_btn_success = (By.XPATH, '//*[@id="autoclosable-btn-success"]')
    normal_btn_success = (By.XPATH, '//*[@id="normal-btn-success"]')
    autoclosable_btn_warning = (By.XPATH, '//*[@id="autoclosable-btn-warning"]')
    normal_btn_warning = (By.XPATH, '//*[@id="normal-btn-warning"]')
    autoclosable_btn_danger = (By.XPATH, '//*[@id="autoclosable-btn-danger"]')
    normal_btn_danger = (By.XPATH, '//*[@id="normal-btn-danger"]')
    autoclosable_btn_info = (By.XPATH, '//*[@id="autoclosable-btn-info"]')
    normal_btn_info = (By.XPATH, '//*[@id="normal-btn-info"]')

    autoclosable_alert_success = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[1]')
    autoclosable_alert_warning = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]')
    autoclosable_alert_danger = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[5]')
    autoclosable_alert_info = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[7]')

    normal_alert_success = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]')
    normal_alert_warning = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[4]')
    normal_alert_danger = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[6]')
    normal_alert_info = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[8]')

    close_buttons_group = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/button')


class ModalsLocators(object):
    ModalUrl = 'https://www.seleniumeasy.com/test/bootstrap-modal-demo.html'
    # single modal
    launch_modal_button = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a')
    single_modal_title = (By.XPATH, '//*[@id="myModal0"]/div/div/div[1]/h4')
    save_changes_button = (By.XPATH, '//*[@id="myModal0"]/div/div/div[4]/a[2]')

    # multi modals
    launch_multi_modal_button1 = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/a')

    launch_multi_modal_button2 = (By.XPATH, '//*[@id="myModal"]/div/div/div[3]/a')
    save_changes_modal2_button = (By.XPATH, '//*[@id="myModal2"]/div/div/div[6]/a[2]')
    close_modal2_button = (By.XPATH, '//*[@id="myModal2"]/div/div/div[6]/a[1]')
    save_changes_modal1_button = (By.XPATH, '//*[@id="myModal"]/div/div/div[4]/a[2]')
    first_modal_title = (By.XPATH, '//*[@id="myModal"]/div/div/div[1]/h4')
    second_modal_title = (By.XPATH, '//*[@id="myModal2"]/div/div/div[1]/h4')


class ListBoxLocators(object):
    ListBoxUrl = 'https://www.seleniumeasy.com/test/jquery-dual-list-box-demo.html'
    list1_selections = (By.XPATH, '//*[@id="pickList"]/div/div[1]/select')
    list2_selections = (By.XPATH, '//*[@id="pickList"]/div/div[3]/select')

    add_button = (By.XPATH, '//*[@id="pickList"]/div/div[2]/button[1]')
    removeAll_button = (By.XPATH, '//*[@id="pickList"]/div/div[2]/button[4]')
    addAll_button = (By.XPATH, '//*[@id="pickList"]/div/div[2]/button[2]')
    remove_button = (By.XPATH, '//*[@id="pickList"]/div/div[2]/button[3]')


class ListFilterLocators(object):
    ListFilterUrl = 'https://www.seleniumeasy.com/test/data-list-filter-demo.html'
    input_search = (By.XPATH, '//*[@id="input-search"]')
