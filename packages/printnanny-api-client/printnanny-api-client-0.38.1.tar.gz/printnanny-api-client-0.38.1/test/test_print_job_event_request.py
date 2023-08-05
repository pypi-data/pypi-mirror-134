# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.print_job_event_request import PrintJobEventRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPrintJobEventRequest(unittest.TestCase):
    """PrintJobEventRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintJobEventRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.print_job_event_request.PrintJobEventRequest()  # noqa: E501
        if include_optional :
            return PrintJobEventRequest(
                ts = 1.337, 
                event_source = None, 
                event_type = None, 
                octoprint_environment = printnanny_api_client.models.octoprint_environment_request.OctoprintEnvironmentRequest(
                    os = printnanny_api_client.models.octoprint_platform_request.OctoprintPlatformRequest(
                        id = '0', 
                        platform = '0', 
                        bits = '0', ), 
                    python = printnanny_api_client.models.octoprint_python_request.OctoprintPythonRequest(
                        version = '0', 
                        pip = '0', 
                        virtualenv = '0', ), 
                    hardware = printnanny_api_client.models.octoprint_hardware_request.OctoprintHardwareRequest(
                        cores = 56, 
                        freq = 1.337, 
                        ram = 56, ), 
                    pi_support = printnanny_api_client.models.octoprint_pi_support_request.OctoprintPiSupportRequest(
                        model = '0', 
                        throttle_state = '0', 
                        octopi_version = '0', ), ), 
                octoprint_printer_data = printnanny_api_client.models.octoprint_printer_data_request.OctoprintPrinterDataRequest(
                    job = printnanny_api_client.models.octoprint_job_request.OctoprintJobRequest(
                        file = null, 
                        estimated_print_time = 1.337, 
                        average_print_time = 1.337, 
                        last_print_time = 1.337, 
                        filament = {
                            'key' : null
                            }, ), 
                    state = printnanny_api_client.models.octoprint_printer_state_request.OctoprintPrinterStateRequest(
                        text = '0', 
                        flags = printnanny_api_client.models.octoprint_printer_flags_request.OctoprintPrinterFlagsRequest(
                            operational = True, 
                            printing = True, 
                            cancelling = True, 
                            pausing = True, 
                            resuming = True, 
                            finishing = True, 
                            closed_or_error = True, 
                            error = True, 
                            paused = True, 
                            ready = True, 
                            sd_ready = True, ), ), 
                    user = '0', 
                    current_z = 1.337, 
                    progress = printnanny_api_client.models.octoprint_progress_request.OctoprintProgressRequest(
                        completion = 1.337, 
                        filepos = 56, 
                        print_time = 56, 
                        print_time_left = 56, 
                        print_time_origin = '0', ), 
                    resends = {
                        'key' : null
                        }, 
                    offsets = {
                        'key' : null
                        }, ), 
                event_data = {
                    'key' : null
                    }, 
                temperature = {
                    'key' : null
                    }, 
                print_nanny_plugin_version = '0', 
                print_nanny_client_version = '0', 
                print_nanny_beta_client_version = '0', 
                octoprint_version = '0', 
                octoprint_device = 56, 
                print_session = 56
            )
        else :
            return PrintJobEventRequest(
                octoprint_environment = printnanny_api_client.models.octoprint_environment_request.OctoprintEnvironmentRequest(
                    os = printnanny_api_client.models.octoprint_platform_request.OctoprintPlatformRequest(
                        id = '0', 
                        platform = '0', 
                        bits = '0', ), 
                    python = printnanny_api_client.models.octoprint_python_request.OctoprintPythonRequest(
                        version = '0', 
                        pip = '0', 
                        virtualenv = '0', ), 
                    hardware = printnanny_api_client.models.octoprint_hardware_request.OctoprintHardwareRequest(
                        cores = 56, 
                        freq = 1.337, 
                        ram = 56, ), 
                    pi_support = printnanny_api_client.models.octoprint_pi_support_request.OctoprintPiSupportRequest(
                        model = '0', 
                        throttle_state = '0', 
                        octopi_version = '0', ), ),
                octoprint_printer_data = printnanny_api_client.models.octoprint_printer_data_request.OctoprintPrinterDataRequest(
                    job = printnanny_api_client.models.octoprint_job_request.OctoprintJobRequest(
                        file = null, 
                        estimated_print_time = 1.337, 
                        average_print_time = 1.337, 
                        last_print_time = 1.337, 
                        filament = {
                            'key' : null
                            }, ), 
                    state = printnanny_api_client.models.octoprint_printer_state_request.OctoprintPrinterStateRequest(
                        text = '0', 
                        flags = printnanny_api_client.models.octoprint_printer_flags_request.OctoprintPrinterFlagsRequest(
                            operational = True, 
                            printing = True, 
                            cancelling = True, 
                            pausing = True, 
                            resuming = True, 
                            finishing = True, 
                            closed_or_error = True, 
                            error = True, 
                            paused = True, 
                            ready = True, 
                            sd_ready = True, ), ), 
                    user = '0', 
                    current_z = 1.337, 
                    progress = printnanny_api_client.models.octoprint_progress_request.OctoprintProgressRequest(
                        completion = 1.337, 
                        filepos = 56, 
                        print_time = 56, 
                        print_time_left = 56, 
                        print_time_origin = '0', ), 
                    resends = {
                        'key' : null
                        }, 
                    offsets = {
                        'key' : null
                        }, ),
                print_nanny_plugin_version = '0',
                print_nanny_client_version = '0',
                octoprint_version = '0',
                octoprint_device = 56,
        )

    def testPrintJobEventRequest(self):
        """Test PrintJobEventRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
