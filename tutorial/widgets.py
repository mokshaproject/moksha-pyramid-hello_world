import moksha.wsgi.widgets.api
import tw2.jqplugins.gritter

class PopupNotification(moksha.wsgi.widgets.api.LiveWidget):
    topic = "*"
    onmessage = "$.gritter.add({'title': 'Received', 'text': json});"
    resources = moksha.wsgi.widgets.api.LiveWidget.resources + \
            tw2.jqplugins.gritter.gritter_resources
    backend = "websocket"

    # Don't actually produce anything when you call .display() on this widget.
    inline_engine_name = "mako"
    template = ""

