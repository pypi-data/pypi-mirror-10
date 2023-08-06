#
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json

from boundary import MetricCommon
from six.moves import http_client


class MetricList(MetricCommon):
    def __init__(self):
        MetricCommon.__init__(self)
        self.path = "v1/metrics"
        self.cli_description = "Lists the defined metrics in a Boundary account"

    def getDescription(self):
        """
        Text describing this command
        """
        return "Lists the defined metrics in a Boundary account"

    def handleResults(self, result):
        # Only process if we get HTTP result of 200
        if result.status_code == http_client.OK:
            metrics = json.loads(result.text)
            m = []
            for metric in metrics['result']:
                new_metric = self.extractFields(metric)
                m.append(new_metric)

            metrics['result'] = m
            # pretty print the JSON output
            out = json.dumps(metrics, sort_keys=True, indent=4, separators=(',', ': '))
            print(out)

