## Простое приложение для выполнения команды git pull

### Для использования просто добавьте в файл url.py
```
  urlpatterns = patterns('',
    ...
    url(r'^git/', include('git_hooks.urls')),
    ...
  )
```
### Далее добавьте в Вашем репозитории Hook - для отправки запроса при push-е 
    
  http://example.com/git/pull/ 
    