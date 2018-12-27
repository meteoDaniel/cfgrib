#
# Copyright 2017-2018 European Centre for Medium-Range Weather Forecasts (ECMWF).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors:
#   Alessandro Amici - B-Open - https://bopen.eu
#

from __future__ import absolute_import, division, print_function, unicode_literals


CDS = {
    'latitude': {
        'out_name': 'lat',
        'stored_direction': 'increasing',
    },
    'longitude': {
        'out_name': 'lon',
        'stored_direction': 'increasing',
    },
    'isobaricInhPa': {
        'out_name': 'plev',
        'units': 'Pa',
        'stored_direction': 'decreasing',
    },
    'isobaricInPa': {
        'out_name': 'plev',
        'units': 'Pa',
        'stored_direction': 'decreasing',
    },
    'number': {
        'out_name': 'realization',
        'stored_direction': 'increasing',
    },
    'time': {
        'out_name': 'forecast_reference_time',
        'stored_direction': 'increasing',
    },
    'valid_time': {
        'out_name': 'time',
        'stored_direction': 'increasing',
    },
    'step': {
        'out_name': 'leadtime',
        'stored_direction': 'increasing',
    },
}


ECMWF = {
    'isobaricInhPa': {
        'out_name': 'level',
        'units': 'hPa',
        'stored_direction': 'decreasing',
    },
    'isobaricInPa': {
        'out_name': 'level',
        'units': 'hPa',
        'stored_direction': 'decreasing',
    },
    'hybrid': {
        'out_name': 'level',
        'stored_direction': 'increasing',
    },
}