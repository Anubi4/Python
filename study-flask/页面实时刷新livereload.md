####页面实时刷新

```
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/'*.*')    #实时监控所有页面
    live_server.serve(open_url=True)
```

```
python app.py dev
```
