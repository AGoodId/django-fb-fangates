import base64
import json


from django.views.generic import DetailView
from fb_fangates.models import FanGate


class FanGateView(DetailView):
  """A Facebook Fan Gate view. Assumes the view is rendered in a Facebook
  Fan Page Tab and that a ``signed_request`` is posted.
  """
  model = FanGate
  context_object_name = 'fangate'
  template_name = 'fb/tab.html'

  def post(self, *args, **kwargs):
    return self.get(*args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super(FanGateView, self).get_context_data(**kwargs)

    # Default values
    content = context['fangate'].non_fan_content
    liked = False

    # Parse data in the ``signed_request`` provided by Facebook
    fb_signed_request = self.request.POST.get('signed_request', None)
    if fb_signed_request:
      encoded_sig, payload = fb_signed_request.split('.')
      padded_payload = payload.replace('-_', '+/') + '=' * (4 - len(payload) % 4)
      fb_user_data = json.loads(base64.b64decode(padded_payload))
      if fb_user_data['page']['liked']:
        content = context['fangate'].fan_content
        liked = True

    # Update context and return
    context.update(locals())

    return context
