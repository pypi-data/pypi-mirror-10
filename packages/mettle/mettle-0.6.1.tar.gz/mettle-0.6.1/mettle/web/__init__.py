from mettle.web.green import patch; patch()

import os

from werkzeug.wsgi import SharedDataMiddleware
from sqlalchemy.orm import scoped_session

from mettle.web.framework import App
from mettle.settings import get_settings
from mettle.db import make_session_cls
from mettle.web.views import (logs, examples, services, pipelines, runs,
                              targets, index, notifications)


routes = [
    # The one view that returns HTML.  Everything else is JSON API.
    ('/', 'index', index.Index),

    # Global notifications
    ('/api/notifications/', 'notification_list', notifications.List),
    ('/api/notifications/<int:notification_id>/', 'notification_detail', notifications.Detail),

    # Services
    ('/api/services/', 'service_list', services.ServiceList),
    ('/api/services/<service_name>/', 'service_detail', services.ServiceDetail),
    ('/api/services/<service_name>/notifications/', 'service_notifications',
     notifications.ByService),


    # Pipelines
    ('/api/services/<service_name>/pipelines/', 'pipeline_list',
     pipelines.PipelineList),
    ('/api/services/<service_name>/pipelines/<pipeline_name>/',
     'pipeline_detail', pipelines.PipelineDetails),
    ('/api/services/<service_name>/pipelines/<pipeline_name>/notifications/',
     'pipeline_notifications', notifications.ByPipeline),

    # Runs
    ('/api/services/<service_name>/pipelines/<pipeline_name>/runs/',
     'run_list', runs.RunList),
    ('/api/services/<service_name>/pipelines/<pipeline_name>/runs/<int:run_id>/',
     'run_detail', runs.RunDetails),
    ('/api/services/<service_name>/pipelines/<pipeline_name>/runs/<int:run_id>/logs/',
     'run_logs', logs.Log),
    ('/api/services/<service_name>/pipelines/<pipeline_name>/runs/<int:run_id>/notifications/',
    'run_notifications', notifications.ByRun),

    # Jobs
    ('/api/services/<service_name>/pipelines/<pipeline_name>/runs/<int:run_id>/jobs/',
     'run_job_list', runs.RunJobs),
    ('/api/services/<service_name>/pipelines/<pipeline_name>/runs/<int:run_id>/jobs/<int:job_id>/',
     'run_job_detail', runs.RunJob),
    ('/api/services/<service_name>/pipelines/<pipeline_name>/runs/<int:run_id>/jobs/<int:job_id>/logs/',
     'run_job_logs', logs.Log),
    ('/api/services/<service_name>/pipelines/<pipeline_name>/runs/<int:run_id>/targets/<target>/jobs/',
     'target_job_list', targets.TargetJobs),

]


def import_class(path):
    try:
        module, dot, klass = path.rpartition('.')
        imported = __import__(module, globals(), locals(), [klass, ], -1)
        return getattr(imported, klass)
    except Exception, e:
        raise ImportError(e)


if 'app' not in globals():
    settings = get_settings()
    app = App(routes, settings)
    app.db = scoped_session(make_session_cls(settings.db_url))
    app = SharedDataMiddleware(app, {
        '/static': ('mettle', 'static')
    })

    # also wrap the app in each middleware specified in settings.
    for cls_string, config in settings.wsgi_middlewares:
        cls = import_class(cls_string)
        app = cls(app, config)

if __name__ == "__main__":
    from gevent import pywsgi
    from gwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', int(os.getenv('PORT', 8000))), app,
                               handler_class=WebSocketHandler)
    server.serve_forever()
