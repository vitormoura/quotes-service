
var app = angular.module('QuotesApp', [])
var ctrl = app.controller('QuotesApp.MainCtrl', function ($scope, $http) {


    function getQuoteCategories() {
        return $http.get('quotes/categories');
    }

    const state = {
        categories: [],
        selectedCategory: null,
        description: '',
        author: '',
        status: {
            success: true,
            visible: false,
            message: ''
        }
    }

    const actions = {
        init() {
            getQuoteCategories().then(function (result) {
                state.categories = result.data;

                actions.selectCategory(state.categories[0])
            })
        },

        selectCategory(c) {
            state.selectedCategory = c
        },

        createNewQuote() {

            if ($scope.mainform.$valid) {

                const categ = state.selectedCategory;
                const desc = state.description
                const author = state.author;

                const payload = { category_id: categ.id, description: desc, author: author };

                $http.post(`quotes/${categ.acronym}`, payload).then(function (result) {
                    
                    state.description = '';
                    state.author = '';
                    
                    $scope.mainform.$setPristine();

                    actions.showStatusMessage('quote successfully created!', true)

                }, function (err) {
                    actions.showStatusMessage('an internal error occurred. Please try again', false)
                });
            }
        },

        showStatusMessage(msg, isSuccess){
            state.status.visible = true;
            state.status.message = msg;
            state.status.success = isSuccess;
        },

        closeStatusMessage() {
            state.status.visible = false;
        }


    }

    $scope.actions = actions;
    $scope.state = state;

    $scope.actions.init();
})