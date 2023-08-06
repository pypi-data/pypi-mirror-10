# dblogs
a package to add logging handlers to write logs into database in django project

# Quick start
1. Add "dblogs" to your INSTALLED_APPS settings;
2. Config loggings handlers to log stuff:
    
    'handlers':{
        'log_db':{
            'level': 'WARNING',
            'class': 'dblogs.handlers.DBHandler',
            # model and expiry can be configured to your preference
            # the default is dblogs.GeneralLog model and expiry is in no effect
            'model': 'your.data.model',
            'expiry': 10000, # unit is seconds
            'formatter': 'simple',
            },
        }

3. Include the polls URLconf in your project urls.py;
4. Run 'python manage.py migrate' to create models to store logs;
