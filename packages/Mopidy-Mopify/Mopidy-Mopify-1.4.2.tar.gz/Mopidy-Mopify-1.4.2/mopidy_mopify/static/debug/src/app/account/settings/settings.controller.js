'use strict';
angular.module('mopify.account.settings', [
  'ngRoute',
  'LocalStorageModule',
  'mopify.services.settings',
  'mopify.services.autoupdate',
  'mopify.services.versionmanager',
  'llNotifier'
]).config([
  '$routeProvider',
  function ($routeProvider) {
    $routeProvider.when('/account/settings', {
      templateUrl: 'account/settings/settings.tmpl.html',
      controller: 'SettingsController'
    });
  }
]).controller('SettingsController', [
  '$scope',
  '$rootScope',
  '$timeout',
  '$http',
  'localStorageService',
  'Settings',
  'VersionManager',
  'AutoUpdate',
  'notifier',
  function SettingsController($scope, $rootScope, $timeout, $http, localStorageService, Settings, VersionManager, AutoUpdate, notifier) {
    // bind settings with the $scope
    Settings.bind($scope);
    $scope.buttonactive = false;
    $scope.autoupdate = false;
    /**
     * Temporarily highlight the save button
     * @return {[type]} [description]
     */
    $scope.highlightSaveButton = function () {
      $scope.buttonactive = true;
      $timeout(function () {
        $scope.buttonactive = false;
      }, 500);
    };
    /**
     * Check for a newer Mopify version
     */
    function checkVersion() {
      VersionManager.checkVersion().then(function (version) {
        $scope.newversion = VersionManager.newVersion;
        $scope.newversionnumber = VersionManager.lastversion;
      });
    }
    // Run at init
    checkVersion();
    // check if we can automatically update
    AutoUpdate.check().then(function (canupdate) {
      $scope.autoupdate = canupdate === true;
    });
    /**
     * Update Mopify
     * @return void
     */
    $scope.update = function () {
      // Show notifcation
      notifier.notify({
        type: 'custom',
        template: 'Started updating...',
        delay: 3000
      });
      // Start updating
      AutoUpdate.runUpdate().then(function (data) {
        notifier.notify({
          type: 'custom',
          template: 'Update succesfull. You might need to restart Mopidy before changes are visible. ',
          delay: 3000
        });
        // Recheck version
        checkVersion();
      }, function (data) {
        notifier.notify({
          type: 'custom',
          template: 'Update failed. Mopify returned: ' + data.response,
          delay: 3000
        });
      });
    };
  }
]);