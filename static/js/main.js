var app = angular.module('aioquiz', [
    'ngRoute',
    'ngCookies'
]);

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
        .when("/lessons", {
            templateUrl: "partials/lessons.html",
            controller: "LessonCtrl",
            controllerAs: 'vm'
        })
        .when("/about", {
            templateUrl: "partials/about.html",
            controller: "AboutCtrl",
            controllerAs: 'vm'
        })
        .when("/live_quiz", {
            templateUrl: "partials/live_quiz.html",
            controller: "LiveQuizCtrl",
            controllerAs: 'vm'
        })
        .when("/quiz", {
            templateUrl: "partials/quiz.html",
            controller: "QuizCtrl",
            controllerAs: 'vm'
        })
        .when("/propose", {
            templateUrl: "partials/propose.html",
            controller: "ProposeCtrl",
            controllerAs: 'vm'
        })
        .when("/review", {
            templateUrl: "partials/review.html",
            controller: "ReviewCtrl",
            controllerAs: 'vm'
        })
        .when("/create_quiz", {
            templateUrl: "partials/create_quiz.html",
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
            controller: "PageCtrl",
            controllerAs: 'vm'
        })
        .when("/admin", {
            templateUrl: "partials/admin.html",
            controller: "AdminController",
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
function PageCtrl ($scope, $location, $AuthenticationService, $FlashService) {
    // Activates the Carousel
    $('.carousel').carousel({
        interval: 5000
    });
    // Activates Tooltips for Social Links
    $('.tooltip-social').tooltip({
        selector: "a[data-toggle=tooltip]"
    });
    $scope.logout = function () {
                $AuthenticationService.ClearCredentials()
            };
}

app.controller('AboutCtrl', AboutCtrl);
AboutCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService'];
function AboutCtrl ($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {$scope: $scope, $location: $location, $AuthenticationService: $AuthenticationService, $FlashService: $FlashService});

    function loadAllUsers() {
        $UserService.GetAll().then(function (users) {
                vm.allUsers = users;
            });
    }
    loadAllUsers()
}

app.controller('LessonCtrl', LessonCtrl);
LessonCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService'];
function LessonCtrl ($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {$scope: $scope, $location: $location, $AuthenticationService: $AuthenticationService, $FlashService: $FlashService});
}

app.controller('QuizCtrl', QuizCtrl);
QuizCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService'];
function QuizCtrl ($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {$scope: $scope, $location: $location, $AuthenticationService: $AuthenticationService, $FlashService: $FlashService});
}

app.controller('LiveQuizCtrl', LiveQuizCtrl);
LiveQuizCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService'];
function LiveQuizCtrl ($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {$scope: $scope, $location: $location, $AuthenticationService: $AuthenticationService, $FlashService: $FlashService});
}


app.controller('ProposeCtrl', ProposeCtrl);
ProposeCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService'];
function ProposeCtrl ($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {$scope: $scope, $location: $location, $AuthenticationService: $AuthenticationService, $FlashService: $FlashService});
}

app.controller('ReviewCtrl', ProposeCtrl);
ReviewCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService'];
function ReviewCtrl ($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {$scope: $scope, $location: $location, $AuthenticationService: $AuthenticationService, $FlashService: $FlashService});
}

app.controller('CreateQuizCtrl', CreateQuizCtrl);
CreateQuizCtrl.$inject = ['$rootScope', '$location', 'AuthenticationService', 'FlashService', '$injector', 'UserService'];
function CreateQuizCtrl ($scope, $location, $AuthenticationService, $FlashService, $injector, $UserService) {
    var vm = this;
    $injector.invoke(PageCtrl, this, {$scope: $scope, $location: $location, $AuthenticationService: $AuthenticationService, $FlashService: $FlashService});
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
                AuthenticationService.SetCredentials(vm.username, vm.password, response.data.admin, response.data.moderator);
                $location.path('/');
            } else {
                FlashService.Error(response.data.msg);
                vm.dataLoading = false;
            }
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
                    FlashService.Success('Registration successful', true);
                    $location.path('/login');
                } else {
                    FlashService.Error(response.message);
                    vm.dataLoading = false;
                }
            });
    }
}

app.controller('NewQuestionController', NewQuestionController);

NewQuestionController.$inject = ['$http', '$location', '$rootScope', 'FlashService'];
function NewQuestionController($http, $location, $rootScope, FlashService) {
    var vm = this;

    vm.new_question = new_question;

    function new_question() {
        vm.dataLoading = true;
        $http.post('/api/question', vm.n_question).then(function (response) {
                if (response.success) {
                    FlashService.Success('New Question added successful', true);
                    $location.path('/propose');
                } else {
                    FlashService.Error(response.message);
                    vm.dataLoading = false;
                }
            });
    }
}

app.factory('AuthenticationService', AuthenticationService);

AuthenticationService.$inject = ['$http', '$cookies', '$rootScope', '$timeout', 'UserService'];
function AuthenticationService($http, $cookies, $rootScope, $timeout, UserService) {
    var service = {};

    service.Login = Login;
    service.SetCredentials = SetCredentials;
    service.ClearCredentials = ClearCredentials;

    return service;

    function Login(username, password, callback) {
        $http.post('/api/authenticate', { email: username, password: password }).then(
            function (response) {
                callback(response);
            });

    }

    function SetCredentials(username, password, admin, moderator) {
        var authdata = Base64.encode(username + ':' + password);

        $rootScope.globals = {
            currentUser: {
                username: username,
                authdata: authdata,
                admin: admin,
                moderator: moderator
            }
        };

        // set default auth header for http requests
        $http.defaults.headers.common['Authorization'] = 'Basic ' + authdata;

        // store user details in globals cookie that keeps user logged in for 1 week (or until they logout)
        var cookieExp = new Date();
        cookieExp.setDate(cookieExp.getDate() + 7);
        $cookies.putObject('globals', $rootScope.globals, {expires: cookieExp});
    }

    function ClearCredentials() {
        $rootScope.globals = {};
        $cookies.remove('globals');
        $http.defaults.headers.common.Authorization = 'Basic';
    }
}

// Base64 encoding service used by AuthenticationService
var Base64 = {
    keyStr: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=',

    encode: function (input) {
        var output = "";
        var chr1, chr2, chr3 = "";
        var enc1, enc2, enc3, enc4 = "";
        var i = 0;

        do {
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);

            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;

            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }

            output = output +
                this.keyStr.charAt(enc1) +
                this.keyStr.charAt(enc2) +
                this.keyStr.charAt(enc3) +
                this.keyStr.charAt(enc4);
            chr1 = chr2 = chr3 = "";
            enc1 = enc2 = enc3 = enc4 = "";
        } while (i < input.length);

        return output;
    },

    decode: function (input) {
        var output = "";
        var chr1, chr2, chr3 = "";
        var enc1, enc2, enc3, enc4 = "";
        var i = 0;

        // remove all characters that are not A-Z, a-z, 0-9, +, /, or =
        var base64test = /[^A-Za-z0-9\+\/\=]/g;
        if (base64test.exec(input)) {
            window.alert("There were invalid base64 characters in the input text.\n" +
                "Valid base64 characters are A-Z, a-z, 0-9, '+', '/',and '='\n" +
                "Expect errors in decoding.");
        }
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");

        do {
            enc1 = this.keyStr.indexOf(input.charAt(i++));
            enc2 = this.keyStr.indexOf(input.charAt(i++));
            enc3 = this.keyStr.indexOf(input.charAt(i++));
            enc4 = this.keyStr.indexOf(input.charAt(i++));

            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;

            output = output + String.fromCharCode(chr1);

            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3);
            }

            chr1 = chr2 = chr3 = "";
            enc1 = enc2 = enc3 = enc4 = "";

        } while (i < input.length);

        return output;
    }
};

app.factory('UserService', UserService);
UserService.$inject = ['$http'];
function UserService($http) {
    var service = {};

    service.GetAll = GetAll;
    service.GetById = GetById;
    service.GetByUsername = GetByUsername;
    service.Create = Create;
    service.Update = Update;
    service.Delete = Delete;

    return service;

    function GetAll() {
        return $http.get('/api/user/').then(handleSuccess, handleError('Error getting all users'));
    }

    function GetById(id) {
        return $http.get('/api/user/' + id).then(handleSuccess, handleError('Error getting user by id'));
    }

    function GetByUsername(username) {
        return $http.get('/api/user/' + username).then(handleSuccess, handleError('Error getting user by username'));
    }

    function Create(user) {
        return $http.post('/api/user/', user).then(handleSuccess, handleError('Error creating user'));
    }

    function Update(user) {
        return $http.put('/api/user/' + user.id, user).then(handleSuccess, handleError('Error updating user'));
    }

    function Delete(id) {
        return $http.delete('/api/user/' + id).then(handleSuccess, handleError('Error deleting user'));
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

FlashService.$inject = ['$rootScope'];
function FlashService($rootScope) {
    var service = {};
    service.Success = Success;
    service.Error = Error;
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

    initController();

    function initController() {
        loadCurrentUser();
        loadAllUsers();
    }

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
        $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata;
    }

    $rootScope.$on('$locationChangeStart', function (event, next, current) {
        // redirect to login page if not logged in and trying to access a restricted page
        var restrictedPage = $.inArray($location.path(), ['/login', '/register', '/about', '/']) === -1;
        var loggedIn = $rootScope.globals.currentUser;
        if (restrictedPage && !loggedIn) {
            $location.path('/login');
        }
    });
}

app.run(run);