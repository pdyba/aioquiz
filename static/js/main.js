var app = angular.module('aioquiz', [
    'ngRoute',
    'ngCookies',
    'oitozero.ngSweetAlert'
]);

function pad(num, size) {
    var s = "000000000" + num;
    return s.substr(s.length - size);
}


app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "partials/home.html",
            controller: "PageCtrl",
            controllerAs: 'vm'
        })
        .when("/live_quiz", {
            templateUrl: "partials/live_quiz.html",
            controller: "PageCtrl",
            controllerAs: 'vm'
        })
        .when("/lessons", {
            templateUrl: "partials/lessons.html",
            controller: "LessonsCtrl",
            controllerAs: 'vm'
        })
        .when("/about", {
            templateUrl: "partials/about.html",
            controller: "AboutCtrl",
            controllerAs: 'vm'
        })
        .when("/live_quiz", {
            templateUrl: "partials/live_quiz_list.html",
            controller: "LiveQuizCtrl",
            controllerAs: 'vm'
        })
        .when("/live_quiz/:id", {
            templateUrl: "partials/live_quiz.html",
            controller: "LiveQuizRunCtrl",
            controllerAs: 'vm'
        })
        .when("/overview_attendance/:id", {
            templateUrl: "partials/overview_attendance.html",
            controller: "OverviewAttendanceCtrl",
            controllerAs: 'vm'
        })
        .when("/live_quiz_results/:id", {
            templateUrl: "partials/live_quiz_results.html",
            controller: "LiveQuizResultsCtrl",
            controllerAs: 'vm'
        })
        .when("/lesson/:id", {
            templateUrl: function (params) {
                return 'lessons/' + pad(params.id, 4) + '.html';
            },
            controller: "LessonCtrl",
            controllerAs: 'vm'
        })
        .when("/create_live_quiz", {
            templateUrl: "partials/live_quiz_create.html",
            controller: "LiveQuizCreateCtrl",
            controllerAs: 'vm'
        })
        .when("/quiz", {
            templateUrl: "partials/quiz_list.html",
            controller: "QuizCtrl",
            controllerAs: 'vm'
        })
        .when("/question_list", {
            templateUrl: "partials/question_list.html",
            controller: "QuestionListCtrl",
            controllerAs: 'vm'
        })
        .when("/quiz/:id", {
            templateUrl: "partials/quiz.html",
            controller: "QuizStartCtrl",
            controllerAs: 'vm'
        })
        .when("/question_create", {
            templateUrl: "partials/question_create.html",
            controller: "NewQuestionController",
            controllerAs: 'vm'
        })
        .when("/lessons_new", {
            templateUrl: "partials/lessons_new.html",
            controller: "NewLessonController",
            controllerAs: 'vm'
        })
        .when("/review", {
            templateUrl: "partials/question_review.html",
            controller: "ReviewCtrl",
            controllerAs: 'vm'
        })
        .when("/create_quiz", {
            templateUrl: "partials/quiz_create.html",
            controller: "CreateQuizCtrl",
            controllerAs: 'vm'
        })
        .when("/login", {
            templateUrl: "partials/login.html",
            controller: "LoginController",
            controllerAs: 'vm'
        })
        .when("/register", {
            templateUrl: "partials/register.html",
            controller: "RegisterController",
            controllerAs: 'vm'
        })
        .when("/profile", {
            templateUrl: "partials/profile.html",
            controller: "ProfileCtrl",
            controllerAs: 'vm'
        })
        .when("/profile_edit", {
            templateUrl: "partials/profile_edit.html",
            controller: "ProfileEditCtrl",
            controllerAs: 'vm'
        })
        .when("/edit_user/:uid", {
            templateUrl: "partials/profile_edit.html",
            controller: "UserEditCtrl",
            controllerAs: 'vm'
        })
        .when("/admin_users", {
            templateUrl: "partials/admin.html",
            controller: "AdminController",
            controllerAs: 'vm'
        })
        .when("/admin_config", {
            templateUrl: "partials/admin_config.html",
            controller: "AdminConfigController",
            controllerAs: 'vm'
        })
        .when("/admin_email", {
            templateUrl: "partials/admin_email.html",
            controller: "AdminEmailController",
            controllerAs: 'vm'
        })
        .when("/seats", {
            templateUrl: "partials/seats.html",
            controller: "SeatController",
            controllerAs: 'vm'
        })
        .when("/seats_overview", {
            templateUrl: "partials/seats.html",
            controller: "SeatOverViewController",
            controllerAs: 'vm'
        })
        .when("/overview_lesson", {
            templateUrl: "partials/overview_lesson.html",
            controller: "ExerciseOverviewController",
            controllerAs: 'vm'
        })
        .when("/rules", {
            templateUrl: "partials/rules.html",
            controller: "PageCtrl",
            controllerAs: 'vm'
        })
        .when("/regconfirmed", {
            templateUrl: "partials/regconfirmed.html",
            controller: "PageCtrl",
            controllerAs: 'vm'
        })
        .when("/program", {
            templateUrl: "partials/program.html",
            controller: "PageCtrl",
            controllerAs: 'vm'
        })
        .when("/review_attendee", {
            templateUrl: "partials/attendee_review_list.html",
            controller: "ReviewAttendeeController",
            controllerAs: 'vm'
        })
        .when("/lessons_mngt", {
            templateUrl: "partials/lessons_mngt.html",
            controller: "LessonMngtController",
            controllerAs: 'vm'
        })
        .when("/attendance", {
            templateUrl: "partials/attendance.html",
            controller: "AttendanceController",
            controllerAs: 'vm'
        })
        .when("/user_summary", {
            templateUrl: "partials/user_summary.html",
            controller: "UserSummaryController",
            controllerAs: 'vm'
        })
        .otherwise("/404", {
            templateUrl: "partials/404.html",
            controller: "PageCtrl",
            controllerAs: 'vm'
        });
}]);
app.config(['$locationProvider', function ($locationProvider) {
    $locationProvider.hashPrefix('');
}]);

app.controller('PageCtrl', PageCtrl);
PageCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', 'SweetAlert', '$http'];
function PageCtrl($scope, $location, $AuthenticationService, $FlashService, SweetAlert, $http) {
    if ($scope.globals.currentUser) {
        user_seat = $scope.globals.currentUser.seat;
        if (!user_seat) {
            $http.get('/api/seats/' + $scope.globals.currentUser.id).then(
                function (response) {
                    user_seat = response.data;
                    $scope.globals.currentUser.seat = response.data;
                }
            );
        }
    }
    $scope.logout = function () {
        $AuthenticationService.ClearCredentials();
        $location.path('/');
    };
    $scope.help = function () {
        if (!user_seat) {
            SweetAlert.swal({
                title: "Nope",
                text: "You need to pick a seat before calling for help",
                type: "error",
                timer: 2000,
                showConfirmButton: false
            })
        } else {
            $http.get('/api/i_need_help/').then(
                function (response) {
                    $scope.globals.currentUser.seat.i_need_help = true;
                    SweetAlert.swal({
                        title: "Yey",
                        text: response.data.msg,
                        type: "success",
                        timer: 2000,
                        showConfirmButton: false
                    })
                }
            )
        }
    };
    $scope.help_stop = function () {
        $http.delete('/api/i_need_help/').then(
            function (response) {
                $scope.globals.currentUser.seat.i_need_help = false;
                SweetAlert.swal({
                    title: "Yey",
                    text: response.data.msg,
                    type: "success",
                    timer: 2000,
                    showConfirmButton: false
                })
            }
        )
    };

    $scope.save_attendence = function () {
        SweetAlert.swal({
            title: "Attendance",
            text: "Please provide lesson code",
            element: "input",
            type: "input",
            showConfirmButton: true,
            closeOnConfirm: false
        }, function (value) {
            var data = {'code': value};
            $http.put('/api/absence', data).then(function (response) {
                if (response.data.success) {
                    mtype = "success";
                } else {
                    mtype = "error";
                }
                SweetAlert.swal({
                    text: response.data.msg,
                    title: 'Attendance',
                    type: mtype,
                    showConfirmButton: true,
                    timer: 2000
                });

            })
        });
    };
}

app.component("exercises", {
    templateUrl: 'partials/exercises.html',
    controller: ExercisesCtrl,
    controllerAs: 'vm'
});

app.controller('ExercisesCtrl', ExercisesCtrl);
ExercisesCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$routeParams', 'SweetAlert'];
function ExercisesCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $routeParams, SweetAlert) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.exercises = [];
    vm.answare = answare;
    vm.new_answare = new_answare;

    $http.get('/api/exercise/' + parseInt($routeParams.id)).then(
        function (response) {
            vm.exercises = response.data;
        }
    ).catch(function (response) {
        $FlashService.Error(response.data.msg);
    });
    function answare(qwa) {
        data = {
            "answare": qwa.answare,
            "exercise": qwa.id,
            "status": "Done"
        };
        $http.post('/api/exercise/', data).then(
            function (response) {
                vm.resp = response.data.msg;
                if (response.data.success) {
                    mtype = "success";
                } else {
                    mtype = "error";
                }
                SweetAlert.swal({
                    title: mtype,
                    text: vm.resp,
                    type: mtype
                });
                qwa.answared = true
            }
        ).catch(function (response) {
            $FlashService.Error(response);
        });
    }
    function new_answare(qwa) {
        data = {
            "answare": qwa.answare,
            "exercise": qwa.id,
        };
        $http.put('/api/exercise/', data).then(
            function (response) {
                vm.resp = response.data.msg;
                if (response.data.success) {
                    mtype = "success";
                } else {
                    mtype = "error";
                }
                SweetAlert.swal({
                    title: mtype,
                    text: vm.resp,
                    type: mtype
                });
                qwa.answared = true
            }
        ).catch(function (response) {
            $FlashService.Error(response);
        });
    }
}


app.controller('AboutCtrl', AboutCtrl);
AboutCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService'];
function AboutCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });

    function loadAllUsers() {
        $UserService.GetAllOrganisers().then(function (users) {
            vm.allUsers = users;
        });
        $UserService.GetAllMentors().then(function (users) {
            vm.mentors = users;
        });
    }

    loadAllUsers()
}

app.controller('ReviewAttendeeController', ReviewAttendeeController);
ReviewAttendeeController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService', '$http'];
function ReviewAttendeeController($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.filter = 'notrated';
    vm.rules = [];
    vm.filters = filters;
    vm.rate = rate;
    vm.accept = accept;
    vm.unaccept = unaccept;
    vm.edit_mentor = edit_mentor;
    vm.current_user_id = $scope.globals.currentUser.id;

    function rate(user) {
        var data = {
            'users': user.id,
            'score': user.new_review
        };
        $http.post('/api/review_attendees/', data).then(
            function (response) {
                $FlashService.SuccessNoReload('Score Saved', false);
                user.score = user.score + user.new_review;
                if (vm.filter === 'notrated' || vm.filter === 'notratedbyme') {
                    user.show = false;
                }
            }
        );
    }

    function edit_mentor(uid) {
        $location.path('/edit_user/' + uid);
    }

    function accept(user) {
        var data = {
            'users': user,
            'accept': true
        };
        $http.put('/api/review_attendees/', data).then(
            function (response) {
                $FlashService.SuccessNoReload('Score Accepted', false);
                user.accept = true;
            }
        );
    }

    function unaccept(user) {
        var data = {
            'users': user,
            'accept': false
        };
        $http.put('/api/review_attendees/', data).then(
            function (response) {
                $FlashService.SuccessNoReload('Score Accepted', false);
                user.accept = false;
            }
        );
    }

    function avg(obj) {
        var sum = 0;
        var count = 0;
        if (obj.lenght > 200) {
            console.log('using 200');
            return obj[200].score;
        }
        obj.forEach(function (user, index) {
            sum += user.score;
            if (user.score > 0) {
                count += 1;
            }
        });
        console.log('using avg');
        return sum / count;
    }

    function filters() {
        vm.attendee.forEach(function (user, index) {
            if (vm.filter === 'notrated') {
                user.show = (Object.keys(user.reviews).length === 0);
            }
            else if (vm.filter === 'notratedbyme') {
                user.show = !(vm.current_user_id in user.reviews);
            }
            else if (vm.filter === 'top200') {
                user.show = (user.score >= vm.average)
            }
            else if (vm.filter === 'accepted') {
                user.show = (user.accepted)
            }
            else if (vm.filter === 'confirmed') {
                user.show = (user.accepted && user.confirmation === 'true')
            }
            else if (vm.filter === 'unconfirmed') {
                user.show = (user.accepted && user.confirmation === 'noans')
            }
            else if (vm.filter === 'mentor') {
                user.show = (user.mentor)
            }
            else if (vm.filter === 'all') {
                user.show = true
            }

        })
    }

    function get_all_users() {
        $UserService.GetAllAttendees().then(function (users) {
            vm.attendee = users;
            vm.average = avg(users);
            filters()
        });
    }

    function get_rules() {
        $http.get('/api/review_rules').then(
            function (response) {
                vm.rules = response.data;
            }
        );
    }

    get_all_users();
    get_rules();

}

app.controller('LessonsCtrl', LessonsCtrl);
LessonsCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function LessonsCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/lessons').then(
        function (response) {
            if (response.status == 401){
                $AuthenticationService.ClearCredentials();
                $location.path('/login');
            }

            response.data.forEach(
                function (a, b) {
                    a.full_id = pad(a.lesson_no, 4);
                }
            );

            vm.lessons = response.data;
        }
    );
}

app.controller('LessonMngtController', LessonMngtController);
LessonMngtController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', 'SweetAlert'];
function LessonMngtController($scope, $location, $AuthenticationService, $FlashService, $injector, $http, SweetAlert) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.activate = activate;
    vm.deactivate = deactivate;
    vm.absence = absence;
    vm.extend = extend;
    vm.attendance = attendance;

    function activate(lid) {
    }

    function deactivate(lid) {
    }

    function absence(lid) {
        $http.get('/api/absence/' + lid).then(
            function (response) {
                SweetAlert.swal({
                    title: "Lesson Code",
                    text: "<h1>" + response.data.code + "</h1><h3><br>will expire at:<br>" + response.data.time_ended + "</h3>",
                    type: "success",
                    html: true
                })
            }
        );
    }

    function extend(lid) {
        $http.post('/api/absence/' + lid, {}).then(
            function (response) {
                SweetAlert.swal({
                    title: "Lesson Code",
                    text: "<h1>" + response.data.code + "</h1><h3><br>will expire at:<br>" + response.data.time_ended + "</h3>",
                    type: "success",
                    html: true
                })
            }
        );
    }

    function attendance(lid) {
        $location.path('/overview_attendance/' + lid);
    }

    $http.get('/api/lessons').then(
        function (response) {
            vm.lessons = response.data;
        }
    );

}


app.controller('LessonCtrl', LessonCtrl);
LessonCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function LessonCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/lessons').then(
        function (response) {
            vm.lessons = response.data;
        }
    );
}

app.controller('QuizCtrl', QuizCtrl);
QuizCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function QuizCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/quiz').then(
        function (response) {
            vm.quizes = response.data;
        }
    );
    vm.start = start;
    function start(id) {
        $location.path('/quiz/' + id);
    }
}

app.controller('QuestionListCtrl', QuestionListCtrl);
QuestionListCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function QuestionListCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/question').then(
        function (response) {
            vm.questions = response.data;
        }
    );
}

app.controller('LiveQuizCtrl', LiveQuizCtrl);
LiveQuizCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function LiveQuizCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/live_quiz').then(
        function (response) {
            vm.live_quzies = response.data;
        }
    );
    vm.start = start;
    function start(id) {
        $location.path('/live_quiz/' + id);
    }

    vm.show_results = show_results;
    function show_results(id) {
        $location.path('/live_quiz_results/' + id);
    }
}


app.controller('ReviewCtrl', ReviewCtrl);
ReviewCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$route'];
function ReviewCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $route) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.user = $scope.globals.currentUser.username;
    $http.get('/api/question?review=true').then(
        function (response) {
            vm.questions = response.data;
        }
    );
    vm.accept = accept;
    function accept(id) {
        var data = {
            'reviewer': vm.user,
            'accept': true
        };
        $http.put('/api/question/' + id, data).then(
            function (response) {
                vm.questions = response.data;
                $FlashService.Success('Question accepted', true);
                $route.reload();
            }
        );
    }

    vm.reject = reject;
    function reject(id) {
        var data = {
            'reviewer': vm.user,
            'accept': false
        };
        $http.put('/api/question/' + id, data).then(
            function (response) {
                vm.questions = response.data;
                $FlashService.Success('Question Rejected', true);
                $route.reload();
            }
        );
    }
}


app.controller('ProfileCtrl', ProfileCtrl);
ProfileCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function ProfileCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/user/' + $scope.globals.currentUser.id).then(
        function (response) {
            vm.user_profile = response.data;
        }
    );
    $http.get('/api/attendance').then(
        function (response) {
            vm.user_attendence = response.data;
        }
    );
}


app.controller('LiveQuizResultsCtrl', LiveQuizResultsCtrl);
LiveQuizResultsCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$route', '$routeParams', '$timeout'];
function LiveQuizResultsCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $route, $routeParams, $timeout) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.questions = {};
    $http.get('/api/question/').then(
        function (response) {
            vm.questions = response.data;
            refresh();
        }
    );
    $http.get('/api/live_quiz/' + $routeParams.id).then(
        function (response) {
            vm.live_quiz = response.data;
            vm.live_quiz.questions.forEach(
                function (a, b) {
                    get_question(a);
                }
            );
            refresh();
        }
    );
    function get_question(qid) {
        $http.get('/api/question/' + qid).then(
            function (response) {
                vm.questions[qid] = response.data.question;
            }
        );
    }

    function refresh() {
        $http.get('/api/live_quiz/' + $routeParams.id).then(
            function (response) {
                vm.live_quiz.answares = response.data.answares;
                //$timeout(refresh, 2000);
            }
        );
    }
}


app.controller('QuizStartCtrl', QuizStartCtrl);
QuizStartCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$route', '$routeParams'];
function QuizStartCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $route, $routeParams) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.user = $scope.globals.currentUser.username;
    $http.get('/api/quiz/' + $routeParams.id).then(
        function (response) {
            vm.question = response.data;
            vm.quiz_title = response.data.quiz_title;
            vm.current_question = 0;
        }
    );

    vm.answare_question = answare_question;
    function answare_question() {
        var data = {
            'question': vm.question.id,
            'answare': vm.answare,
            'user_id': $scope.globals.currentUser.id,
            'current_question': vm.current_question
        };
        $http.post('/api/quiz/' + $routeParams.id, data).then(
            function (response) {
                $FlashService.SuccessNoReload('Answare Saved', false);
                vm.current_question += 1;
                if (response.data.last) {
                    vm.question.question = response.data.msg;
                    vm.question.last = response.data.last;
                } else {
                    vm.question = response.data;
                }
            }
        );
    }
}


app.controller('LiveQuizRunCtrl', LiveQuizRunCtrl);
LiveQuizRunCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$route', '$routeParams'];
function LiveQuizRunCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $route, $routeParams) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.user = $scope.globals.currentUser.username;
    $http.get('/api/live_quiz/' + $routeParams.id).then(
        function (response) {
            vm.question = response.data;
            vm.quiz_title = response.data.quiz_title;
            vm.current_question = 0;
        }
    );

    vm.answare_question = answare_question;
    function answare_question() {
        var data = {
            'question': vm.question.id,
            'answare': vm.answare,
            'user_id': $scope.globals.currentUser.id,
            'current_question': vm.current_question
        };
        $http.post('/api/live_quiz/' + $routeParams.id, data).then(
            function (response) {
                $FlashService.SuccessNoReload('Answare Saved', false);
                vm.current_question += 1;
                if (response.data.last) {
                    vm.question.question = response.data.msg;
                    vm.question.last = response.data.last;
                } else {
                    vm.question = response.data;
                }
            }
        );
    }
}

app.controller('UserEditCtrl', UserEditCtrl);
UserEditCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$route', '$routeParams', 'UserService'];
function UserEditCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $route, $routeParams, UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.update_user = update_user;
    vm.user = {};

    $http.get('/api/user/' + $routeParams.uid).then(
        function (response) {
            vm.user = response.data;
        }
    );
    function update_user() {
        vm.dataLoading = true;
        UserService.Update(vm.user)
            .then(function (response) {
                if (response.success) {
                    $FlashService.Success(response.msg, true);
                } else {
                    $FlashService.Error(response.msg);
                }
                vm.dataLoading = false;
            });
    }
}

app.controller('CreateQuizCtrl', CreateQuizCtrl);
CreateQuizCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function CreateQuizCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    vm.questions = [];
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/question?review=False').then(
        function (response) {
            vm.questions = response.data;
        }
    );
    vm.create_quiz = create_quiz;

    function create_quiz() {
        vm.dataLoading = true;
        vm.lesson.creator = $scope.globals.currentUser.username;
        $http.post('/api/quiz_manage', vm.lesson).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('New Quiz added successful', true);
                $location.path('/quiz');
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }
}

app.controller('SeatController', SeatController);
SeatController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', 'SweetAlert'];
function SeatController($scope, $location, $AuthenticationService, $FlashService, $injector, $http, SweetAlert) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.current_user = $scope.globals.currentUser;
    vm.seats = false;
    vm.user_seat = $scope.globals.currentUser.seat;
    vm.take_or_relese_seat = take_or_relese_seat;
    $http.get('/api/seats').then(
        function (response) {
            vm.seats = response.data;
        }
    );
    if (!vm.user_seat) {
        $http.get('/api/seats/' + $scope.globals.currentUser.id).then(
            function (response) {
                vm.user_seat = response.data;
            }
        );
    }
    function take_or_relese_seat(raw, number, user) {
        if (vm.user_seat.users && user.user_id === vm.user_seat.users) {
            release_seat(raw, number)
        } else {
            take_seat(raw, number)
        }
    }

    function take_seat(raw, number) {
        var seat = {
            'row': raw,
            'number': number,
            'users': $scope.globals.currentUser.id
        };
        SweetAlert.swal({
                title: "Are you sure?",
                text: "You are taking seat: " + raw + number,
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes",
                cancelButtonText: "No",
                closeOnConfirm: false,
                closeOnCancel: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    $http.post('/api/seats', seat).then(function (response) {
                        if (response.data.success) {
                            SweetAlert.swal("Success!", "Seat taken", "success");
                            $scope.globals.currentUser.seat = {
                                'raw': raw,
                                'number': number
                            };
                            vm.user_seat = seat;
                            vm.seats[raw][number].user = $scope.globals.currentUser.name + ' ' + $scope.globals.currentUser.surname;
                            vm.seats[raw][number].user_id = seat.users;
                        } else {
                            SweetAlert.swal("Cancelled", response.data.msg, "error");
                        }
                    });
                } else {
                    SweetAlert.swal("Cancelled", "OK pick another", "error");
                }
            });
    }

    function release_seat(raw, number) {
        SweetAlert.swal({
                title: "Are you sure ?",
                text: "You are leaving seat: " + raw + number,
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes",
                cancelButtonText: "No",
                closeOnConfirm: false,
                closeOnCancel: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    $http.delete('/api/seats').then(function (response) {
                        if (response.data.success) {
                            SweetAlert.swal("Success!", "Seat released", "success");
                            $scope.globals.currentUser.seat = {};
                            vm.user_seat = {};
                            vm.seats[raw][number].user = false;
                            vm.seats[raw][number].user_id = false;
                        } else {
                            SweetAlert.swal("Cancelled", response.data.msg, "error");
                        }
                    });
                } else {
                    SweetAlert.swal("Cancelled", "OK pick another", "error");
                }
            });

    }
}


app.controller('SeatOverViewController', SeatOverViewController);
SeatOverViewController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$interval'];
function SeatOverViewController($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $interval) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.overview = true;
    vm.seats = {};
    function refresh_seats() {
        $http.get('/api/seats').then(
            function (response) {
                vm.seats = response.data;
            }
        )
    }

    refresh_seats();
    $interval(refresh_seats, 3000)

}

app.controller('ExerciseOverviewController', ExerciseOverviewController);
ExerciseOverviewController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$interval'];
function ExerciseOverviewController($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $interval) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.overview = true;
    vm.exercises_overview = {};
    function refresh_seats() {
        $http.get('/api/exercises_overview').then(
            function (response) {
                vm.exercises_overview = response.data;
            }
        )
    }

    refresh_seats();
    $interval(refresh_seats, 3000)

}

app.controller('OverviewAttendanceCtrl', OverviewAttendanceCtrl);
OverviewAttendanceCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$interval', '$routeParams'];
function OverviewAttendanceCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $interval, $routeParams) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    function refresh_absence() {
        $http.get('/api/attendance/' + parseInt($routeParams.id)).then(
            function (response) {
                vm.absence_overview = response.data;
            }
        )
    }

    refresh_absence();
    $interval(refresh_absence, 3000)

}


app.controller('AdminConfigController', AdminConfigController);
AdminConfigController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function AdminConfigController($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    vm.questions = [];
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/admin_config').then(
        function (response) {
            vm.config = response.data;
        }
    );
    vm.save_config = save_config;

    function save_config() {
        vm.dataLoading = true;
        $http.post('/api/admin_config', vm.config).then(function (response) {
            if (response.data.success) {
                $FlashService.SuccessNoReload(response.data.msg);
            } else {
                $FlashService.Error(response.data.msg);
            }
            vm.dataLoading = false;
        });
    }
}

app.controller('AdminEmailController', AdminEmailController);
AdminEmailController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function AdminEmailController($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    vm.questions = [];
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/email').then(
        function (response) {
            vm.email_options = response.data;
        }
    );
    vm.email = {};
    vm.send_email = send_email;

    function send_email(mail) {
        vm.dataLoading = true;
        $http.post('/api/email', mail).then(function (response) {
            if (response.data.success) {
                $FlashService.SuccessNoReload(response.data.msg);
            } else {
                $FlashService.Error(response.data.msg);
            }
            vm.dataLoading = false;
        });
    }
}

app.controller('LiveQuizCreateCtrl', LiveQuizCreateCtrl);
LiveQuizCreateCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function LiveQuizCreateCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    vm.questions = [];
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    $http.get('/api/question?review=False').then(
        function (response) {
            vm.questions = response.data;
        }
    );
    vm.create_quiz = create_quiz;

    function create_quiz() {
        vm.dataLoading = true;
        vm.lesson.creator = $scope.globals.currentUser.username;
        $http.post('/api/live_quiz_manage', vm.lesson).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('New Live Quiz added successful', true);
                $location.path('/live_quiz');
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }
}

app.controller('LoginController', LoginController);
LoginController.$inject = ['$location', 'AuthenticationService', 'SweetAlert', '$http'];
function LoginController($location, AuthenticationService, SweetAlert, $http) {
    var vm = this;

    vm.login = login;
    vm.forgotPassword = forgotPassword;

    (function initController() {
        AuthenticationService.ClearCredentials();
    })();

    function login() {
        vm.dataLoading = true;
        AuthenticationService.Login(vm.username, vm.password, function (response) {
            if (response.data.success) {
                AuthenticationService.SetCredentials(response.data, response.data.session_uuid);
                $location.path('/');
            } else {
                $location.path('/login');
            }
            vm.dataLoading = false;
        });
    }

    function forgotPassword() {
        SweetAlert.swal({
            title: "Password recovery",
            text: "Please provide valid email",
            element: "input",
            type: "input",
            showConfirmButton: true,
            closeOnConfirm: false
        }, function (value) {
            var data = {'email': value};
            $http.post('/api/forgot_password', data).then(function (response) {
                var txt = response.data.msg;
                SweetAlert.swal({text: txt, title: ''});
            })
        });
    }

}

app.controller('RegisterController', RegisterController);
RegisterController.$inject = ['UserService', '$location', '$rootScope', 'FlashService', '$http'];
function RegisterController(UserService, $location, $rootScope, FlashService, $http) {
    var vm = this;

    $http.get('/api/reg_active').then(function (response) {
        vm.reg = response.data.registration;
        console.log(response.data)
    });

    vm.register = register;

    function register() {
        vm.dataLoading = true;
        UserService.Create(vm.user)
            .then(function (response) {
                if (response.success) {
                    FlashService.Success('Registration successful, please check your e-mail to confirm your account', true);
                    $location.path('/login');
                } else {
                    FlashService.Error(response.msg);
                    vm.dataLoading = false;
                }
            });
    }
}


app.controller('ProfileEditCtrl', ProfileEditCtrl);
ProfileEditCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', 'UserService', 'SweetAlert'];
function ProfileEditCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, UserService, SweetAlert) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.user = {};
    vm.update_user = update_user;
    vm.remove_accout = remove_accout;
    uid = $scope.globals.currentUser.id;


    function get_user_data() {
        UserService.GetById(uid).then(
            function (resp) {
                vm.user = resp;
            }
        )
    }


    function remove_accout() {
        SweetAlert.swal({
            title: "Delete account",
            type: "warning",
            text: "Are You sure You want to delete your account",
            showCancelButton: true,
            confirmButtonText: "Yes",
            cancelButtonText: "No",
            showConfirmButton: true,
            closeOnCancel: false,
            closeOnReject: false
        }, function (isConfirmed) {
            if (isConfirmed) {
                UserService.Delete(uid).then(
                    function (resp) {
                        SweetAlert.swal({
                            text: response.data.msg,
                            title: 'Absence',
                            type: 'error',
                            showConfirmButton: true,
                            timer: 2000
                        });
                    }
                )
            } else {
                SweetAlert.swal({
                    text: "Thanks for trusting in us",
                    title: 'Cancleation',
                    type: 'success',
                    showConfirmButton: true,
                    timer: 3000
                });
            }
        })
    }

    function update_user() {
        vm.dataLoading = true;
        UserService.Update(vm.user)
            .then(function (response) {
                if (response.success) {
                    $FlashService.Success(response.msg, true);
                    $location.path('/profile');
                } else {
                    $FlashService.Error(response.msg);
                }
                vm.dataLoading = false;
            });
    }

    get_user_data()
}

app.controller('NewQuestionController', NewQuestionController);
NewQuestionController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function NewQuestionController($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });

    vm.new_question = new_question;
    function new_question() {
        vm.dataLoading = true;
        vm.n_question.users = $scope.globals.currentUser.id;
        $http.post('/api/question', vm.n_question).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('New Question added successful', true);
                $location.path('/question_create');
                vm.dataLoading = false;
            } else {
                $FlashService.Error(response.msg);
                vm.dataLoading = false;
            }
        });
    }
}

app.controller('NewLessonController', NewLessonController);
NewLessonController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function NewLessonController($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });

    vm.new_lesson = new_lesson;
    function new_lesson() {
        vm.dataLoading = true;
        vm.lesson.creator = $scope.globals.currentUser.username;
        $http.post('/api/lessons', vm.lesson).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('New Lesson added successful', true);
                $location.path('/lessons');
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }
}


app.controller('AdminController', AdminController);
AdminController.$inject = ['UserService', '$rootScope'];
function AdminController(UserService, $rootScope) {
    var vm = this;

    vm.user = null;
    vm.allUsers = [];
    vm.users_stats = {};
    vm.deleteUser = deleteUser;
    vm.makeOrganiser = UserService.makeOrganiser;
    vm.removeOrganiser = UserService.removeOrganiser;
    vm.makeActive = UserService.makeActive;
    vm.makeInactive = UserService.makeInactive;
    vm.makeMentor = UserService.makeMentor;
    vm.removeMentor = UserService.removeMentor;

    loadAllUsers();
    getStats();

    function getStats() {
        UserService.GetStats()
            .then(function (stats) {
                vm.users_stats = stats;
            });
    }

    function loadAllUsers() {
        UserService.GetAll()
            .then(function (users) {
                vm.allUsers = users;
            });
    }

    function deleteUser(id) {
        UserService.Delete(id)
            .then(function () {
                loadAllUsers();
            });
    }

}


app.controller('UserSummaryController', UserSummaryController);
UserSummaryController.$inject = ['UserService', '$rootScope'];
function UserSummaryController(UserService, $rootScope) {
    var vm = this;
    vm.allAttendes = [];
    vm.pymocniks = [];
    vm.mentors = [];
    vm.admin = [];

    loadAllAcceptedUsers();

    function loadAllAcceptedUsers() {
        UserService.GetAllAccepted()
            .then(function (users) {
                vm.allAttendes = users;
            });
        UserService.GetAllOrganisers()
            .then(function (users) {
                vm.pymocniks = users;
            });
        UserService.GetAllMentors()
            .then(function (users) {
                vm.mentors = users;
            });
        UserService.GetAllAdmins()
            .then(function (users) {
                vm.admins = users;
            });
    }

}

app.factory('AuthenticationService', AuthenticationService);
AuthenticationService.$inject = ['$http', '$cookies', '$rootScope', '$timeout', 'UserService', 'FlashService'];
function AuthenticationService($http, $cookies, $rootScope, $timeout, UserService, $FlashService) {
    var service = {};

    service.Login = Login;
    service.SetCredentials = SetCredentials;
    service.ClearCredentials = ClearCredentials;

    return service;

    function Login(username, password, callback) {
        $http.post('/api/authenticate', {
            email: username,
            password: password
        }).then(
            function (response) {
                callback(response);
            }).catch(function (err) {
            $FlashService.Error(err.data.msg);
            callback(err);
        });
    }

    function SetCredentials(data, session_uuid) {
        var authdata = session_uuid;
        $http.get('/api/seats/' + data.id).then(
            function (response) {
                data.seat = response.data;
            }
        );
        $rootScope.globals = {
            currentUser: data
        };
        // set default auth header for http requests
        $http.defaults.headers.common['Authorization'] = authdata;

        // store user details in globals cookie that keeps user logged in for 1 week (or until they logout)
        var cookieExp = new Date();
        cookieExp.setDate(cookieExp.getDate() + 10);
        $cookies.putObject('globals', $rootScope.globals, {expires: cookieExp});
    }

    function ClearCredentials() {
        $rootScope.globals = {};
        $cookies.remove('globals');
        $http.defaults.headers.common.Authorization = 'Basic';
    }
}

app.factory('UserService', UserService);
UserService.$inject = ['$http', 'FlashService'];
function UserService($http, $FlashService) {
    var service = {};

    service.GetAll = GetAll;
    service.GetById = GetById;
    service.GetByUsername = GetByUsername;
    service.GetAllOrganisers = GetAllOrganisers;
    service.GetAllMentors = GetAllMentors;
    service.GetAllAttendees = GetAllAttendees;
    service.Create = Create;
    service.Update = Update;
    service.Delete = Delete;
    service.GetStats = GetStats;
    service.makeOrganiser = makeOrganiser;
    service.removeOrganiser = removeOrganiser;
    service.makeActive = makeActive;
    service.makeInactive = makeInactive;
    service.makeMentor = makeMentor;
    service.removeMentor = removeMentor;
    service.GetAllAccepted = GetAllAccepted;
    service.GetAllAdmins = GetAllAdmins;


    return service;

    function GetAll() {
        return $http.get('/api/user/').then(handleSuccess, handleError('Error getting all users'));
    }

    function GetAllOrganisers() {
        return $http.get('/api/user/?organiser=True&sort_by=surname').then(handleSuccess, handleError('Error getting all users'));
    }

    function GetAllAdmins() {
        return $http.get('/api/user/?admin=True&sort_by=surname').then(handleSuccess, handleError('Error getting all users'));
    }

    function GetAllAccepted() {
        return $http.get('/api/user/?mentor=False&confirmation=ack&sort_by=surname').then(handleSuccess, handleError('Error getting all users'));
    }

    function GetAllAttendees() {
        return $http.get('/api/review_attendees/').then(handleSuccess, handleError('Error getting all users'));
    }

    function GetAllMentors() {
        return $http.get('/api/user/?mentor=True').then(handleSuccess, handleError('Error getting all users'));
    }

    function GetById(id) {
        return $http.get('/api/user/' + id).then(handleSuccess, handleError('Error getting user by id'));
    }

    function GetStats(id) {
        return $http.get('/api/users_stats').then(handleSuccess, handleError('Error getting user by id'));
    }

    function GetByUsername(username) {
        return $http.get('/api/user/' + username).then(handleSuccess, handleError('Error getting user by username'));
    }

    function Create(user) {
        return $http.post('/api/user/', user).then(handleSuccess).catch(function (response) {
            $FlashService.Error(response.data.msg);
        });
    }

    function Update(user) {
        return $http.put('/api/user/', user).then(handleSuccess, handleError('Error updating user'));
    }

    function Delete(id) {
        return $http.delete('/api/user/' + id).then(handleSuccess, handleError('Error deleting user'));
    }

    function makeOrganiser(user) {
        var data = {
            'organiser': true,
            'uid': user.id
        };
        $http.post('/api/make_organiser', data).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('Made an organiser: ' + user.name, true);
                user.organiser = true;
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }

    function removeOrganiser(user) {
        var data = {
            'organiser': false,
            'uid': user.id
        };
        $http.post('/api/make_organiser', data).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('Made an organiser: ' + user.name, true);
                user.organiser = false;
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }

    function makeActive(user) {
        var data = {
            'active': true,
            'uid': user.id
        };
        $http.post('/api/change_active', data).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('Made active: ' + user.name, true);
                user.active = true;
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }

    function makeInactive(user) {
        var data = {
            'active': false,
            'uid': user.id
        };
        $http.post('/api/change_active', data).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('Made inactive: ' + user.name, true);
                user.active = false;
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }

    function makeMentor(user) {
        var data = {
            'mentor': true,
            'uid': user.id
        };
        $http.post('/api/change_mentor', data).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('Made mentor of: ' + user.name, true);
                user.mentor = true;
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }

    function removeMentor(user) {
        var data = {
            'mentor': false,
            'uid': user.id
        };
        $http.post('/api/change_mentor', data).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('Removed mentor from: ' + user.name, true);
                user.mentor = false;
            } else {
                $FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
        });
    }

    function handleSuccess(res) {
        return res.data;
    }

    function handleError(error) {
        return function () {
            return {success: false, msg: error.msg};
        };
    }
}


app.factory('FlashService', FlashService);

FlashService.$inject = ['$rootScope', '$route'];
function FlashService($rootScope, $route) {
    var service = {};
    service.Success = Success;
    service.Error = Error;
    service.SuccessNoReload = SuccessNoReload;
    initService();

    return service;

    function initService() {
        $rootScope.$on('$locationChangeStart', function () {
            clearFlashmsg();
        });

        function clearFlashmsg() {
            var flash = $rootScope.flash;
            if (flash) {
                if (!flash.keepAfterLocationChange) {
                    delete $rootScope.flash;

                } else {
                    flash.keepAfterLocationChange = false;
                }
            }
        }
    }

    function Success(msg, keepAfterLocationChange) {
        $rootScope.flash = {
            msg: msg,
            type: 'success',
            keepAfterLocationChange: keepAfterLocationChange
        };
        //setTimeout(function () {
        //    delete $rootScope.flash;
        //    $route.reload();
        //}, 3000);
    }

    function SuccessNoReload(msg, keepAfterLocationChange) {
        $rootScope.flash = {
            msg: msg,
            type: 'success',
            keepAfterLocationChange: keepAfterLocationChange
        };
    }

    function Error(msg, keepAfterLocationChange) {
        $rootScope.flash = {
            msg: msg,
            type: 'error',
            keepAfterLocationChange: keepAfterLocationChange
        };
    }
}

run.$inject = ['$rootScope', '$location', '$cookies', '$http'];
function run($rootScope, $location, $cookies, $http) {
    // keep user logged in after page refresh
    $rootScope.globals = $cookies.getObject('globals') || {};
    if ($rootScope.globals.currentUser) {
        $http.defaults.headers.common['Authorization'] = $rootScope.globals.currentUser.session_uuid;
    }

    $rootScope.$on('$locationChangeStart', function (event, next, current) {
        // redirect to login page if not logged in and trying to access a restricted page
        var restrictedPage = $.inArray($location.path(), ['/login', '/register', '/about', '/', '/rules', '/program', '/regconfirmed']) === -1;
        var loggedIn = $rootScope.globals.currentUser;
        if (restrictedPage && !loggedIn) {
            $location.path('/');
        }
    });
}

app.run(run);