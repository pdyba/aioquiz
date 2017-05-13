/**
 * Created by Piotr on 23/02/2017.
 */
var session_id = '';
var name = '';
var gdata;

function start(id) {
    $.get("./api/live_quiz/" + id,
        function (data) {
            session_id = data.session_id;
            next_question(data);
        });
}

function next_question(data) {
    gdata = data;
    if (data.qtype === 'end') {
        finish_quiz(data);
    }
    else if (data.qtype === 'abcd') {
        question_abcd(data);
    }
    else if (data.qtype === 'bool') {
        question_bool(data);
    } else {
        question_plain(data);
    }
}

function get_next_question(answare) {
    $.post("./api/quiz",
        JSON.stringify({
            qid: gdata.qid,
            name: name,
            answare: answare,
            session_id: session_id
        }),
        function (data) {
            next_question(data);
        })
}

function question_abcd(data) {
    settings = {
        title: "Question: " + data.qid,
        text: data.question + '<p>' + data.answares,
        html: true,
        allowOutsideClick: false,
        type: "input",
        showConfirmButton: true,
        confirmButtonColor: '#DD6B55',
        confirmButtonText: 'submit',
        closeOnConfirm: false,
        closeOnCancel: false
    };
    if (data.img === true) {
        settings.imageUrl = './images/' + data.qid + '.png';
        settings.imageSize = "400x400";
    }
    swal(settings, function (inputValue) {
            if (inputValue.length > 0) {
                get_next_question(inputValue);
            }
            else {
                question_abcd(data);
            }
        }
    );
}

function question_bool(data) {
    settings = {
        title: "Question: " + data.qid,
        text: data.question,
        html: true,
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "True",
        cancelButtonText: "False",
        closeOnConfirm: false,
        closeOnCancel: false
    };
    if (data.img === true) {
        settings.imageUrl = './images/' + data.qid + '.png';
        settings.imageSize = "400x400";
    }
    swal(settings,
        function (inputValue) {
            get_next_question(inputValue);
        }
    );
}

function question_plain(data) {
    settings = {
        title: "Question: " + data.qid,
        type: "input",
        text: data.question,
        html: true,
        showCancelButton: false,
        confirmButtonColor: '#DD6B55',
        confirmButtonText: 'submit',
        animation: "slide-from-top",
        inputPlaceholder: "Write answare",
        allowOutsideClick: false,
        closeOnConfirm: false,
        closeOnCancel: false
    };
    if (data.img === true) {
        settings.imageUrl = './images/' + data.qid + '.png';
        settings.imageSize = "400x400";
    }
    swal(settings,
        function (inputValue) {

            if (inputValue.length > 0) {
                if (gdata.qid === 0) {
                    name = inputValue;
                }
                get_next_question(inputValue);
            }
            else {
                question_plain(data);
            }
        }
    );
}

function finish_quiz(data) {
    swal({
        title: "Finished",
        type: "info",
        text: name + data.question,
        showCancelButton: false,
        animation: "slide-from-top",
        allowOutsideClick: false,
        closeOnConfirm: false,
        closeOnCancel: false
    })
}