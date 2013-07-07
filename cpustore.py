#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
import json
from cpudata import CpuData
from datetime import datetime

class CpuStoreHandler(webapp2.RequestHandler):
    def post(self):
        cpuusage = json.loads(self.request.body)
        cpuData = CpuData(
              timeStamp = cpuusage['timeStamp'],
              cpu = float(cpuusage['cpu']),
              system = cpuusage['system'],
              release = cpuusage['release'],
              version = cpuusage['version'],
              userName = cpuusage['userName']
        )
        cpuData.put()
        self.response.write('Cpu usage data is stored!')

app = webapp2.WSGIApplication([
    ('/cpustore', CpuStoreHandler)
], debug=True)
