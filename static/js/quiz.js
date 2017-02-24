/**
 * Created by Piotr on 23/02/2017.
 */
var session_id = '';
var name = '';
var gdata;

function start() {
    $.get("./api/quiz",
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
    swal({
            title: "Question: " + data.qid,
            text: data.question,
            html: true,
            allowOutsideClick: false,
            type: "input",
            showConfirmButton: true,
            confirmButtonColor: '#DD6B55',
            confirmButtonText: 'submit',
            closeOnConfirm: false,
            closeOnCancel: false
        }, function (inputValue) {
            get_next_question(inputValue);
        }
    );
}

function question_bool(data) {
    swal({
            title: "Question: " + data.qid,
            text: data.question,
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "True",
            cancelButtonText: "False",
            closeOnConfirm: false,
            closeOnCancel: false
        },
        function (inputValue) {
            get_next_question(inputValue);
        }
    );
    console.log(data);
}

function question_plain(data) {
    swal({
            title: "Question: " + data.qid,
            type: "input",
            text: data.question,
            showCancelButton: false,
            confirmButtonColor: '#DD6B55',
            confirmButtonText: 'submit',
            animation: "slide-from-top",
            inputPlaceholder: "Write answare",
            allowOutsideClick: false,
            closeOnConfirm: false,
            closeOnCancel: false
        },
        function (inputValue) {
            if (gdata.qid === 0) {
                name = inputValue;
            }
            get_next_question(inputValue);
        }
    );
}

function finish_quiz(data) {
    swal({
            title: "Finished",
            type: "info",
            text: data.name + data.question,
            showCancelButton: false,
            animation: "slide-from-top",
            allowOutsideClick: false,
            closeOnConfirm: false,
            closeOnCancel: false
        })
}