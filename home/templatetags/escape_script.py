from django import template
import re
from django.template.defaultfilters import escape_filter, urlizetrunc, escapejs_filter

register = template.Library()

def validate_value(value):
  results = re.findall('<script[^\n]*', value)
  for i in results:
    value = value.replace(i, escape_filter(i))
  result = re.findall('src=[\'\"][a-zA-Z0-9-._]+.js[\"\']', value)
  for i in result:
    value = value.replace(i, '')
  print("value", value)
  script_rmv = value.replace("<script>", escape_filter("<script>")).replace("</script>", escape_filter("</script>"))
  return script_rmv

def escape_only_js(value):
  new_escape = validate_value(value)
  print("new_escape", new_escape)
  return new_escape

register.filter("filterme", escape_only_js)

"<script src='sdfgh4789-_.jk78.min.js'></script>"
"src=[\'\"][a-zA-Z0-9-._]+.js[\'\"]"