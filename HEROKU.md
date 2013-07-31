# Launch on Heroku

## Create app

For existing Heroku app with `app_name`

```
heroku git:remote -a app_name
```

Or create a new Heroku app:

```
heroku create
```

Rename the app to what seems more appropriate:

```
heroku apps:rename app_name
```

## Set up database

```
heroku addons:add heroku-postgresql:dev
heroku pg:promote YOUR_DATABSE_URL (generated and shown during previous step)
```

## Set up necessary variables

```
heroku config:add PYTHONPATH=/mukuwiki
heroku config:add DJANGO_SETTINGS_MODULE=mukuwiki.settings.heroku
```

## Set up secret keys

[Register new Twitter app](https://dev.twitter.com/apps/new)

[Register new Github app](https://github.com/settings/applications) (click button "Regsiter new application").

Callback URLs end with `/complete/<backend>/`, where `<backend>` is `twitter` or `github` correspondingly.

```
heroku config:set TWITTER_CONSUMER_KEY=YOUR_TWITTER_CONSUMER_KEY
heroku config:set TWITTER_CONSUMER_SECRET=YOUR_TWITTER_CONSUMER_SECRET
heroku config:set GITHUB_APP_ID=YOUR_GITHUB_APP_ID
heroku config:set GITHUB_API_SECRET=YOUR_GITHUB_API_SECRET
```

## Sync database

```
heroku run python mukuwiki/manage.py syncdb
```
