var app = angular.module('aioquiz', [
    'ngRoute',
    'ngCookies'
]);

function pad(num, size) {
    var s = "000000000" + num;
    return s.substr(s.length-size);
}

/**
 * Configure the Routes
 */
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
        .when("/live_quiz_results/:id", {
            templateUrl: "partials/live_quiz_results.html",
            controller: "LiveQuizResultsCtrl",
            controllerAs: 'vm'
        })
        .when("/lesson/:id", {
            templateUrl: function(params) {
                return 'lessons/' + pad(params.id, 4) +'.html';
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
        .when("/admin_users", {
            templateUrl: "partials/admin.html",
            controller: "AdminController",
            controllerAs: 'vm'
        })
        .when("/seats", {
            templateUrl: "partials/seats.html",
            controller: "SeatController",
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
PageCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService'];
function PageCtrl($scope, $location, $AuthenticationService, $FlashService) {
    $scope.logout = function () {
        $AuthenticationService.ClearCredentials();
        $location.path('/');
    };
    $scope.help = function () {
        console.log('halp plox')
    };
    $scope.help_stop = function () {
        console.log('stop halp plox')
    };
}

app.component("exercises", {
    templateUrl :'partials/exercises.html',
    controller: ExercisesCtrl,
    controllerAs: 'vm'
});

app.controller('ExercisesCtrl', ExercisesCtrl);
ExercisesCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http', '$routeParams'];
function ExercisesCtrl($scope, $location, $AuthenticationService, $FlashService, $injector, $http, $routeParams) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {
        $scope: $scope,
        $location: $location,
        $AuthenticationService: $AuthenticationService,
        $FlashService: $FlashService
    });
    vm.exercises = [];
    vm.answare = answare;

    $http.get('/api/exercise/' + parseInt($routeParams.id)).then(
        function (response) {
            vm.exercises = response.data;
        }
    ).catch(function (response) {
            $FlashService.Error(response.data.msg);
    });
    function answare (qwa) {
        data = {
            "answare": qwa.answare,
            "exercise": qwa.id,
            "status": "Done"
        };
        $http.post('/api/exercise/', data).then(
        function (response) {
            vm.resp = response.data;
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
            }
        );
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
        obj.forEach(function (user, index) {
            sum += user.score;
            if (user.score > 0) {
                count += 1;
            }
        });
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
                //TODO: above average for now
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
            filters();
        });
    }

    function get_rules() {
        $http.get('/api/review_rules').then(
            function (response) {
                vm.rules = response.data;
                console.log(vm.rules)
            }
        );
    }

    get_all_users();
    get_rules()
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
            response.data.forEach(
                function (a, b) {
                    a.full_id = pad(a.id, 4);
                }
            );
            vm.lessons = response.data;
        }
    );
}

app.controller('LessonMngtController', LessonMngtController);
LessonMngtController.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', '$http'];
function LessonMngtController($scope, $location, $AuthenticationService, $FlashService, $injector, $http) {
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
    //$http.get('/api/lessons').then(
    //    function (response) {
    //        vm.lessons = response.data;
    //    }
    //);
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
    $http.get('/api/user/' + $scope.globals.currentUser.username).then(
        function (response) {
            vm.user_profile = response.data;
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
                $FlashService.Error(response.data.message);
                vm.dataLoading = false;
            }
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
                $FlashService.Error(response.data.message);
                vm.dataLoading = false;
            }
        });
    }
}

app.controller('LoginController', LoginController);
LoginController.$inject = ['$location', 'AuthenticationService', 'FlashService'];
function LoginController($location, AuthenticationService, FlashService) {
    var vm = this;

    vm.login = login;

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
}
app.controller('RegisterController', RegisterController);
RegisterController.$inject = ['UserService', '$location', '$rootScope', 'FlashService'];
function RegisterController(UserService, $location, $rootScope, FlashService) {
    var vm = this;

    vm.register = register;

    function register() {
        vm.dataLoading = true;
        UserService.Create(vm.user)
            .then(function (response) {
                if (response.success) {
                    FlashService.Success('Registration successful, please check your e-mail to confirm your account', true);
                    $location.path('/login');
                } else {
                    FlashService.Error(response.message);
                    vm.dataLoading = false;
                }
            });
    }
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
                $FlashService.Error(response.message);
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
                $FlashService.Error(response.data.message);
                vm.dataLoading = false;
            }
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
    service.makeOrganiser = makeOrganiser;

    // Nie lepiej byłoby robić tak:
    // service.GetAll = function() { ... }
    // To definiowanie funkcji po return w ogóle nie powinno działać wg mnie, no ale JS :p
    return service;

    function GetAll() {
        return $http.get('/api/user/').then(handleSuccess, handleError('Error getting all users'));
    }

    function GetAllOrganisers() {
        return $http.get('/api/user/?organiser=True').then(handleSuccess, handleError('Error getting all users'));
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

    function GetByUsername(username) {
        return $http.get('/api/user/' + username).then(handleSuccess, handleError('Error getting user by username'));
    }

    function Create(user) {
        return $http.post('/api/user/', user).then(handleSuccess).catch(function (response) {
            $FlashService.Error(response.data.msg);
    });
    }

    function Update(user) {
        return $http.put('/api/user/' + user.id, user).then(handleSuccess, handleError('Error updating user'));
    }

    function Delete(id) {
        return $http.delete('/api/user/' + id).then(handleSuccess, handleError('Error deleting user'));
    }

    function makeOrganiser(user){
        var data = {
            'organiser': true,
            'uid': user.id
        };
        $http.post('/api/make_organiser', data).then(function (response) {
            if (response.data.success) {
                $FlashService.Success('Made an organiser: ' + user.name, true);;
            } else {
                $FlashService.Error(response.data.message);
                vm.dataLoading = false;
            }
        });
    }

    function handleSuccess(res) {
        return res.data;
    }

    function handleError(error) {
        return function () {
            return {success: false, message: error};
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
            clearFlashMessage();
        });

        function clearFlashMessage() {
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

    function Success(message, keepAfterLocationChange) {
        $rootScope.flash = {
            message: message,
            type: 'success',
            keepAfterLocationChange: keepAfterLocationChange
        };
        //setTimeout(function () {
        //    delete $rootScope.flash;
        //    $route.reload();
        //}, 3000);
    }

    function SuccessNoReload(message, keepAfterLocationChange) {
        $rootScope.flash = {
            message: message,
            type: 'success',
            keepAfterLocationChange: keepAfterLocationChange
        };
    }

    function Error(message, keepAfterLocationChange) {
        $rootScope.flash = {
            message: message,
            type: 'error',
            keepAfterLocationChange: keepAfterLocationChange
        };
    }
}


app.controller('AdminController', AdminController);
AdminController.$inject = ['UserService', '$rootScope'];
function AdminController(UserService, $rootScope) {
    var vm = this;

    vm.user = null;
    vm.allUsers = [];
    vm.deleteUser = deleteUser;
    vm.makeOrganiser = UserService.makeOrganiser;

    loadAllUsers();

    function loadCurrentUser() {
        UserService.GetByUsername($rootScope.globals.currentUser.username)
            .then(function (user) {
                vm.user = user;
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

run.$inject = ['$rootScope', '$location', '$cookies', '$http'];
function run($rootScope, $location, $cookies, $http) {
    // keep user logged in after page refresh
    $rootScope.globals = $cookies.getObject('globals') || {};
    if ($rootScope.globals.currentUser) {
        $http.defaults.headers.common['Authorization'] = $rootScope.globals.currentUser.session_uuid;
    }

    $rootScope.$on('$locationChangeStart', function (event, next, current) {
        // redirect to login page if not logged in and trying to access a restricted page
        var restrictedPage = $.inArray($location.path(), ['/login', '/register', '/about', '/', '/rules', '/regconfirmed']) === -1;
        var loggedIn = $rootScope.globals.currentUser;
        if (restrictedPage && !loggedIn) {
            $location.path('/');
        }
    });
}

app.run(run);