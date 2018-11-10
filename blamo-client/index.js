const $ = require('jquery')
const token = require('django-csrf-ajax')
require('bootstrap/js/dist/dropdown')

token.setTokenHeader('jquery', $)

$(document).ready(function() {
    // delete log
    $('.btn-delete-log').click(function() {
        let url = "/blamo/logs/delete"
        let data = {
            "log_id": $(this).data('id')
        }

        $.post(url, data, function() {
            location.reload()
        })
    })

    // refresh key
    $('.btn-refresh-key').click(function() {
        let url = "/blamo/keys/create"
        let data = {
            "user_id": $(this).data('user')
        }

        $.post(url, data, function() {
            location.reload()
        })
    })

    // revoke key
    $('.btn-revoke-key').click(function() {
        let url = "/blamo/keys/revoke"
        let data = {
            "key_id": $(this).data('id')
        }

        $.post(url, data, function() {
            location.reload()
        })
    })
})
