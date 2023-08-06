# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from django.utils.translation import ugettext as _

from jsonview.decorators import json_view
from watchman.decorators import auth
from watchman.utils import get_checks


@auth
@json_view
def status(request):
    response = {}

    check_list = None
    skip_list = None

    if len(request.GET) > 0:
        if 'check' in request.GET:
            check_list = request.GET.getlist('check')
        if 'skip' in request.GET:
            skip_list = request.GET.getlist('skip')

    for check in get_checks(check_list=check_list, skip_list=skip_list):
        if callable(check):
            response.update(check())

    if len(response) == 0:
        raise Http404(_('No checks found'))

    return response


@auth
def dashboard(request):
    check_types = []

    for check in get_checks(None, None):
        if callable(check):
            _check = check()

            for _type in _check:
                # For other systems (eg: email, storage) _check[_type] is a
                # dictionary of status
                #
                # Example:
                # {
                #     'ok': True,  # Status
                # }
                #
                # Example:
                # {
                #     'ok': False,  # Status
                #     'error': "RuntimeError",
                #     'stacktrace': "...",
                # }
                #
                # For some systems (eg: cache, database) _check[_type] is a
                # list of dictionaries of dictionaries of statuses
                #
                # Example:
                # [
                #     {
                #         'default': {  # Cache/database name
                #             'ok': True,  # Status
                #         }
                #     },
                #     {
                #         'non-default': {  # Cache/database name
                #             'ok': False,  # Status
                #             'error': "RuntimeError",
                #             'stacktrace': "...",
                #         }
                #     },
                # ]
                #
                statuses = []

                if type(_check[_type]) == dict:
                    result = _check[_type]
                    statuses = [{
                        'name': '',
                        'ok': result['ok'],
                        'error': '' if result['ok'] else result['error'],
                        'stacktrace': '' if result['ok'] else result['stacktrace'],
                    }]

                    type_overall_status = _check[_type]['ok']

                elif type(_check[_type]) == list:
                    for result in _check[_type]:
                        for name in result:
                            statuses.append({
                                'name': name,
                                'ok': result[name]['ok'],
                                'error': '' if result[name]['ok'] else result[name]['error'],
                                'stacktrace': '' if result[name]['ok'] else result[name]['stacktrace'],
                            })

                    type_overall_status = all([s['ok'] for s in statuses])

                check_types.append({
                    'type': _type,
                    'ok': type_overall_status,
                    'statuses': statuses})

    overall_status = all([type_status['ok'] for type_status in check_types])

    return render(request, 'watchman/dashboard.html', {
        'checks': check_types,
        'overall_status': overall_status
    })
