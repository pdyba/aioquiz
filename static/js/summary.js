/**
 * Created by Piotr on 24/02/2017.
 */
var session_id = '';
var chart;
var qid = 0;

function create_graph(data) {
    chart = c3.generate({
        data: {
            columns: data.columns,
            type: 'donut'
        },
        donut: {
            label: {
                show: true
            }
        },
        size: {height: 600, width: 400},
        transition: {
            duration: 50
        }
    });
}

function refresh_graph_graphics(data) {
    chart.load({
        unload: true,
        columns: data.columns
    });
}

function start() {
    $.get("./api/summary",
        function (data) {
            session_id = data.session_id;
            qid = data.qid;
            create_graph(data);
            $('#title').text(data.qid.toString() + '. ' + data.question);
        });
    next_question_stats();
}

function refresh_graph() {
    $.post("./api/summary",
        JSON.stringify({
            qid: qid,
            session_id: session_id
        }),
        function (data) {
            qid = data.qid;
            $('#title').text(data.qid.toString() + '. ' + data.question);
            refresh_graph_graphics(data);
            next_question_stats();
        })
}

function next() {
    qid += 1;
    refresh_graph();
}
function previous() {
    qid -= 1;
    if (qid <= 0) {
        qid = 0;
    }
    refresh_graph()
}

function next_question_stats(){
        $.get("./api/stats/" + (qid+1).toString(),
        function (data) {
            $('#stats').text(data.done.toString() + ' / ' + data.max.toString());
        })
}

start();
setInterval(refresh_graph, 5000);
