# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.
"""
Unit Tests for SampleEvent class
"""
import json
import pytest
from aws_lambda_sample_events import SampleEvent
from aws_lambda_sample_events.unknown_service_error import UnknownServiceError

JSON_SAMPLES = 'aws_lambda_sample_events/json_samples/'
SERVICES = [
    'codepipeline',
    'sns',
    'cloudformation',
    'ses',
    'scheduled',
    'dynamodb_update',
    'cognito_sync_trigger',
    'kinesis_stream',
    's3_put',
    's3_delete',
    'cloudwatch_logs',
    'cloudwatch_events',
    'config_rule'
]

def test_invalid_service_name():
    """ Tests invoking with an invalid Service Name """
    with pytest.raises(UnknownServiceError):
        SampleEvent('invalid')

@pytest.mark.parametrize("service_name", SERVICES)
def test_supported_service(service_name):
    """ Tests each supported service for a proper event """
    service = SampleEvent(service_name)
    json_event = json.load(open(JSON_SAMPLES + service_name +'.json'))
    assert service.event == json_event
