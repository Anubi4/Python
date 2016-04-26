####消息闪现，flash

```
from flask import flash

flash("hello")

在模版中

{% for message in get_flashed_messages %}
{{ message }}
{% endfor %}
```
