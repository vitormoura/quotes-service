var app = angular.module('QuotesApp', [])
var ctrl = app.controller('QuotesApp.MainCtrl', function ($scope, $http) {

    const PANEL_QUOTE_LIST = 0;
    const PANEL_QUOTE_FORM = 1;

    function getQuoteCategories() {
        return $http.get('quotes/categories');
    }

    const state = {
        categories: [],
        quotes: [],
        selectedCategory: null,
        panelIndex: PANEL_QUOTE_LIST,
        form: {
            description: '',
            author: '',
            status: {
                success: true,
                visible: false,
                message: ''
            }
        }
    }

    const actions = {
        init() {
            getQuoteCategories().then(function (result) {
                state.categories = result.data;

                actions.selectCategory(state.categories[0]);

                actions.loadQuotesFromCategory(state.selectedCategory);
            })
        },

        selectCategory(c) {
            state.selectedCategory = c
        },

        loadQuotesFromCategory(c) {
            if(!c)
                return;

            $http.get(`quotes/${c.acronym}`).then(function(result) {
                state.quotes = result.data;
            }, function(err) {
                console.error(err);
            })
        },

        reloadQuotes() {
            actions.loadQuotesFromCategory(state.selectedCategory);
        },

        showFormCreateNewQuote() {
            state.form.description = '';
            state.form.author = '';

            $scope.mainform.$setPristine();

            state.panelIndex = PANEL_QUOTE_FORM;
        },

        hideFormCreateNewQuote() {
            state.panelIndex = PANEL_QUOTE_LIST;
        },

        createNewQuote() {

            if ($scope.mainform.$valid) {

                const form = state.form;
                const categ = state.selectedCategory;
                const desc = form.description
                const author = form.author;

                const payload = { category_id: categ.id, description: desc, author: author };

                $http.post(`quotes/${categ.acronym}`, payload).then(function (result) {

                    form.description = '';
                    form.author = '';

                    $scope.mainform.$setPristine();

                    actions.showStatusMessage('quote successfully created!', true)
                    actions.reloadQuotes();

                }, function (err) {
                    actions.showStatusMessage('an internal error occurred. Please try again', false)
                });
            }
        },

        showStatusMessage(msg, isSuccess) {
            state.form.status.visible = true;
            state.form.status.message = msg;
            state.form.status.success = isSuccess;
        },

        closeStatusMessage() {
            state.form.status.visible = false;
        }


    }

    $scope.actions = actions;
    $scope.state = state;

    $scope.actions.init();
})