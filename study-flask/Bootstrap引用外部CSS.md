####Bootstrap引用外部CSS

```
{% block head %}
{{ super() }}   #调用父类方法
<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.6/spacelab/bootstrap.min.css">
{% endblock %}
```
