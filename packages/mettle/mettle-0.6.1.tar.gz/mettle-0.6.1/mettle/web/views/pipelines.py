import json

from mettle.models import Pipeline, Service, PipelineRun
from mettle.web.framework import JSONResponse, ApiView
from mettle.web.rabbit import state_message_stream


def pipeline_summary(pipeline, runs=None, notifications=None):
    data = dict(
        id=pipeline.id,
        name=pipeline.name,
        service_id=pipeline.service_id,
        updated_by=pipeline.updated_by,
        active=pipeline.active,
        retries=pipeline.retries,
        crontab=pipeline.crontab,
        chained_from_id=pipeline.chained_from_id,
        next_run_time=pipeline.next_run_time().isoformat(),
        last_run_time=pipeline.last_run_time().isoformat(),
    )

    if runs is not None:
        data['runs'] = {r.id:
            dict(
                id=r.id,
                succeeded=r.succeeded,
                created_time=r.created_time.isoformat(),
                ack_time=r.ack_time.isoformat() if r.ack_time else None,
                end_time=r.end_time.isoformat() if r.end_time else None
            )
            for r in runs
        }
    if notifications is not None:
        data['notifications'] = {n.id: n.as_dict() for n in notifications}
    return data


class PipelineList(ApiView):
    def get_pipelines(self, service_name):
        service = self.db.query(Service).filter_by(name=service_name).one()
        pipelines = self.db.query(Pipeline).filter_by(
            service=service
        )
        return [
            pipeline_summary(p, p.runs.filter(PipelineRun.pipeline_id==p.id,
                                              PipelineRun.end_time!=None)
                                      .order_by('-pipeline_runs.id'),
                             p.notifications.filter_by(acknowledged_by=None))
            for p in pipelines
        ]

    def get(self, service_name):
        return JSONResponse(dict(objects=self.get_pipelines(service_name)))

    def websocket(self, service_name):
        # keyed by pipeline name
        self.pipelines = {p['name']: p for p in self.get_pipelines(service_name)}

        exchange = self.app.settings['state_exchange']

        # Match all messages that have only two components in the routing key,
        # where the first one is the service_name whose pipelines we're
        # watching.
        # See publisher.py for more details on how the routing key works on this
        # exchange.
        routing_keys = [
            'services.%s.pipelines.*' % service_name,
            'services.%s.pipelines.#.runs.*' % service_name,
        ]
        self.bind_queue_to_websocket(exchange, routing_keys)

    def on_rabbit_message(self, ch, method, props, body):
        parsed = json.loads(body)
        if parsed['tablename'] == 'pipelines':
            pipeline_name = parsed['name']
            if pipeline_name not in self.pipelines:
                self.pipelines[pipeline_name] = parsed
            else:
                self.pipelines[pipeline_name].update(parsed)
        elif parsed['tablename'] == 'pipeline_runs':
            pipeline_name = parsed['pipeline_name']
            self.pipelines[pipeline_name]['runs'][parsed['id']] = parsed
        self.ws.send(json.dumps(self.pipelines[pipeline_name]))


class PipelineDetails(ApiView):
    def get(self, service_name, pipeline_name):
        pipeline = self.db.query(Pipeline).join(Service).filter(
            Service.name==service_name,
            Pipeline.name==pipeline_name,
            Service.id==Pipeline.service_id,
        ).one()
        data = pipeline.as_dict()
        return JSONResponse(data)

