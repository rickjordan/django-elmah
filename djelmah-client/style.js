// bootstrap
require('bootstrap/dist/css/bootstrap.min.css')
require('bootstrap/js/dist/dropdown')
require('bootstrap/js/dist/modal')

// fontawesome library & icons
const { library, dom } = require('@fortawesome/fontawesome-svg-core')
const { faBars } = require('@fortawesome/free-solid-svg-icons/faBars')
const { faFile } = require('@fortawesome/free-regular-svg-icons/faFile')
const { faPlus } = require('@fortawesome/free-solid-svg-icons/faPlus')
const { faSyncAlt } = require('@fortawesome/free-solid-svg-icons/faSyncAlt')
const { faTimes } = require('@fortawesome/free-solid-svg-icons/faTimes')

// add individual icons to library
library.add(faBars, faFile, faPlus, faSyncAlt, faTimes)

// replace any existing <i> tags with <svg> as the DOM changes
dom.watch()
