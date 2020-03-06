import falcon
import structlog
import yaml

log = structlog.getLogger(__name__)


class SwaggerResource(object):
    """Simple status - always un-authenticated endpoint"""

    def on_get(self, req, resp):

        resp.content_type = "application/json"
        with open("swagger.yaml", "r") as f:
            swagger = yaml.load(f, Loader=yaml.SafeLoader)

        resp.media = swagger
        resp.status = falcon.HTTP_200
