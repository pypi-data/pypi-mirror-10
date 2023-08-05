from __future__ import absolute_import

from .response import Response


class Resource(object):

    def dispatch_request(self, action_map, request, *args, **kwargs):
        def get_action_name(method):
            try:
                action_name = action_map[method]
            except KeyError as e:
                e.message = (
                    'Config `ACTION_MAP` has no mapping for %r' % method
                )
                raise
            return action_name

        action_name = get_action_name(request.method)
        action = getattr(self, action_name, None)

        # If the request method is HEAD and there's no handler for it,
        # retry with GET.
        if action is None and request.method == 'HEAD':
            action_name = get_action_name('GET')
            action = getattr(self, action_name, None)

        assert action is not None, 'Unimplemented action %r' % action_name

        rv = action(request, *args, **kwargs)
        return self.make_response(rv)

    def make_response(self, rv):
        status = None
        headers = None

        if isinstance(rv, tuple):
            rv_len = len(rv)
            if rv_len == 2:
                rv, status = rv
            elif rv_len == 3:
                rv, status, headers = rv
            else:
                raise ValueError('Resource action return a wrong response')

        if rv is None:
            raise ValueError('Resource action did not return a response')
        elif not isinstance(rv, Response):
            rv = Response(rv, status=status, headers=headers)

        return rv
