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

from google.appengine.ext import ndb

class CpuData(ndb.Model):
  timeStamp = ndb.StringProperty(required=True)
  cpu = ndb.FloatProperty(required=True)
  system = ndb.StringProperty(required=True)
  release = ndb.StringProperty(required=True)
  version = ndb.StringProperty(required=True)
  userName = ndb.StringProperty(required=True)