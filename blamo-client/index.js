var axios = require('axios')
var token = require('django-csrf-ajax')

token.setTokenHeader('axios', axios)
