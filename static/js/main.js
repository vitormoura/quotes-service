
var app = angular.module('QuotesApp', [])
var ctrl = app.controller('QuotesApp.MainCtrl', function ($scope, $http) {


    function getQuoteCategories() {
        return $http.get('quotes/categories');
    }
    
    const state = {
        categories: [],
    }

    const actions = {
        init() {
            getQuoteCategories().then(function (result) {
                state.categories = result.data;

                actions.selectCategory(state.categories[0])
            })
        },      
    }

    $scope.actions = actions;
    $scope.state = state;

    $scope.actions.init();
})