from rest_framework import renderers
import json

# i wrote this class to make my field errors more accessible for front end
class UserRender(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({"errors":data})
        else:
            response = json.dumps(data)

        return response