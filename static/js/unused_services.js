

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