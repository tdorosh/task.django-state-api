Telegram bot: @tdorosh_state_bot

Supported commands:

/random - return info about random state from database


Web page with api swagger: http://tdorosh.pythonanywhere.com/

API endpoint: http://tdorosh.pythonanywhere.com/api/v1/states/random/

Hosted on: www.pythonanywhere.com

Used libraries (details in pyproject.toml):

django

django rest framework

drf-spectacular - for swagger page

dj-database-url - for handling database settings regardless of database (sqlite on local and mysql on deployment)

pytelegrambotapi and requests - to create telegram bot
