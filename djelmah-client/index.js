const $ = require('jquery')
const token = require('django-csrf-ajax')

require('@fortawesome/fontawesome-free/css/all.min.css')
require('bootstrap/dist/css/bootstrap.min.css')
require('bootstrap/js/dist/dropdown')
require('bootstrap/js/dist/modal')

token.setTokenHeader('jquery', $)

$(document).ready(function() {
    // test log
    $('#btn-test-log').click(function() {
        $.get("/djelmah/logs/test").always(function() {
            location.reload()
        })
    })

    // delete log
    $('.btn-delete-log').click(function() {
        let url = "/djelmah/logs/delete"
        let data = { "log_id": $(this).data('id') }

        $.post(url, data, function() {
            location.reload()
        })
    })

    // create key form
    $('#btn-create-key').click(function() {
        let $userInput = $('#user_id')
        $userInput.removeClass('is-invalid').val(-1)
        $userInput.siblings('.invalid-feedback').hide()

        $('#modal-create-key').modal('show')
    })

    // create key submit
    $('#btn-create-key-submit').click(function(){
        let $userInput = $('#user_id')
        let user_id = $userInput.val()

        if (user_id > 0) {
            create_or_refresh_key(user_id)
        } else {
            $userInput.addClass('is-invalid')
            $userInput.siblings('.invalid-feedback').show()
        }
    })

    // refresh key
    $('.btn-refresh-key').click(function() {
        create_or_refresh_key($(this).data('user'))
    })

    // revoke key
    $('.btn-revoke-key').click(function() {
        let url = "/djelmah/keys/revoke"
        let data = { "key_id": $(this).data('id') }

        $.post(url, data, function() {
            location.reload()
        })
    })
})

function create_or_refresh_key(user_id) {
    let url = "/djelmah/keys/create"
    let data = { "user_id": user_id }

    $.post(url, data, function() {
        location.reload()
    })
}
