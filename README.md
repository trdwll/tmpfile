Before deploying you need to do some things to the ```files/settings.py``` file.
- Set a ```SECRET_KEY```
- Set your domain in ```MY_HOST_DOMAIN``` (this is used for the templates and the JsonResponse)
- Set a ```MAX_FILES_SIZE``` default: 1GB
- Set a ```MAX_PASTES_SIZE``` default: 20MB

Update/change the FAQ page under ```templates/faq.html``` to reflect your site etc.

You're also going to need to setup a cronjob to delete the files after 24 hours.
- Create a [cronjob](https://crontab.guru/every-hour) to run hourly with the command as ```find /path/to/uploads -type f -mmin +1440 -delete```


# Changelog (kinda)
Sept 21, 2017
- update Bulma to 0.5.3
- HTTP Error Pages
- Commented some code

Sept 3, 2017
- CSP stuff
- Pastes

Aug 12, 2017
- cleanup more code
- when uploading the button does a spinner and a progressbar appears to show you're uploading
- update Bulma to 0.5.1