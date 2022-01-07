import os
import sys
import webbrowser
import time
import json

#########################################################
# Performs pip install if default import fails :)
########################################################
#https://docs.splunk.com/Documentation#search.2Fjobs.2F.7Bsearch_id.7D.2Fevents

try:
    import datadog
except ModuleNotFoundError:
    os.system('pip3 install datadog')
    import datadog
except ModuleNotFoundError:
    os.system('pip install datadog')
    import datadog
try:
    from datadog_api_client.v1.api import synthetics_api
except ModuleNotFoundError:
    os.system('pip3 install datadog-api-client')
    from datadog_api_client.v1.api import synthetics_api
except ModuleNotFoundError:
    os.system('pip install datadog-api-client')
    from datadog_api_client.v1.api import synthetics_api
try:
    from colorama import Fore, init, Style
except ModuleNotFoundError:
    os.system('pip3 install colorama')
    from colorama import Fore, init, Style
except ModuleNotFoundError:
    os.system('pip install colorama')
    from colorama import Fore, init, Style


class Datadog:

    def __init__(self):
        init()
        api_key = os.getenv('DATADOG_API_KEY')
        app_key = os.getenv('DATADOG_APP_KEY')
        if api_key and app_key:
            options = {
                'api_key': api_key,
                'app_key': app_key
            }
            datadog.initialize( **options )
        else:
            print(Fore.RED + "Need to configure datadog's api & app key" + Style.RESET_ALL)
            print(Fore.BLUE + "Follow the steps here to  datadog's api & app key.")
            webbrowser.open('https://app.datadoghq.com/account/settings#api', new=2)
            print(Fore.RED + "Closing Script, re-run with correct configurations!" + Style.RESET_ALL)
            sys.exit(-1)

        self.api_comment = datadog.api.Comment
        self.api_downtime = datadog.api.Downtime
        self.api_event = datadog.api.Event
        self.api_graph = datadog.api.Graph
        self.api_host = datadog.api.Host
        self.api_hosts = datadog.api.Hosts
        self.api_infrastructure = datadog.api.Infrastructure
        self.api_metric = datadog.api.Metric
        self.api_monitor = datadog.api.Monitor
        self.api_screen = datadog.api.Screenboard
        self.api_screen_board = datadog.api.Screenboard
        self.api_service_check = datadog.api.ServiceCheck
        self.api_time_board = datadog.api.Timeboard
        self.api_dashboard = datadog.api.Dashboard
        self.api_dashboard_list = datadog.api.DashboardList
        self.api_user = datadog.api.User

        # Splunk

    def header(self):
        print(Fore.MAGENTA + 'Datadog API Tool' + Style.RESET_ALL)

    def get_api_timeboard(self):
        return self.api_time_board.get_all()

    def get_api_dashboard(self):
        return self.api_dashboard.get_all()

    def get_api_monitor_list_trimmed(self):
        dict = {}
        for item in self.api_monitor.get_all():
            dict[item['name']] = item['overall_state']
        return dict

    def get_api_monitor_list_full(self):
        return self.api_monitor.get_all()

    def get_api_mon(self):
        return self.api_monitor.

    def get_api_metric_list(self):
        return self.api_metric.list(time.time())

    def get_api_downtime_list(self):
        return self.api_downtime.get_all()

    def get_all_infrastructure_list(self):
        return self.api_infrastructure.search(q='.')

    def get_all_dashboard_list(self):
        return self.api_dashboard_list.get_all()['dashboard_lists']

    def get_all_users(self):
        return self.api_user.get_all()['users']

    def get_total_matching(self):
        return self.api_hosts.search()['total_matching']

    def get_exact_total_matching(self):
        return self.api_hosts.search()['exact_total_matching']

    def get_total_returned(self):
        return self.api_hosts.search()['total_returned']

    def get_host_list(self):
        return self.api_hosts.search()

    def get_total_up_full(self):
        return self.api_hosts.totals()

    def get_total_up(self):
        return self.api_hosts.totals()['total_up']

    def get_total_active(self):
        return self.api_hosts.totals()['total_active']

    def color_magenta(self, word):
        print(Fore.MAGENTA + str(word) + Style.RESET_ALL)

    def color_cyan(self, word):
        print(Fore.CYAN + str(word) + Style.RESET_ALL)

    def write_to_file(self, name, api_list):
        with open(f'{name}.json', 'w+') as file:
            json.dump(api_list, file)

    def api_output(self, header, info):
        self.color_cyan(f"Creating json file for: {header}")
        self.color_magenta(info)
        self.write_to_file(header, info)


    def datadog_api_controller(self):
        #modify to run specific sequence of commands.
        pass
        '''
        self.header()
        print(self.get_total_up_full())
        #self.api_output("downtime_list", self.get_api_downtime_list())
        self.api_output('monitor_list_trimmed', self.get_api_monitor_list_trimmed())
        self.api_output('timeboard_list', self.get_api_timeboard())
        self.api_output('dashboard_list', self.get_api_dashboard())
        self.api_output('monitor_list_full', self.get_api_monitor_list_full())
        self.api_output("downtime_list", self.get_api_downtime_list())
        self.api_output("user_list", self.get_all_users())
        self.api_output("dashboard_list", self.get_all_dashboard_list())
        self.api_output("host_list", self.get_host_list())
        self.api_output("infrastructure_list", self.get_all_infrastructure_list())
        '''



if __name__ == '__main__':
    dog = Datadog()
    dog.datadog_api_controller()



