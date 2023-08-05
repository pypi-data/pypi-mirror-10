# -*- coding: utf-8 -*-
#
# satcfe/util.py
#
# Copyright 2015 Base4 Sistemas Ltda ME
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

from datetime import datetime
from unidecode import unidecode


as_ascii = lambda p: unidecode(p) if isinstance(p, unicode) else p

a2date = lambda p: datetime.strptime(p, '%Y%m%d').date()

a2datetime = lambda p: datetime.strptime(p, '%Y%m%d%H%M%S')

normalizar_ip = lambda p: '.'.join([str(int(i, 10)) for i in p.split('.')])
