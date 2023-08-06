angular.module('proso.feedback').run(['$templateCache', function($templateCache) {
  'use strict';

  $templateCache.put('static/tpl/feedback_modal.html',
    "<div class=\"modal-header\"><h3 class=\"modal-title\">{{ \"Napište nám\" | trans }}</h3></div><div class=\"modal-body\"><label>{{ \"Narazili jste na chybu v aplikaci? Máte nápad na vylepšení? Nebo jakýkoliv jiný postřeh či komentář? Zajímá nás všechno, co nám chcete sdělit.\" | trans }}</label><textarea ng-model=\"feedback.text\" class=\"form-control\" rows=\"8\"></textarea><label>{{ \"Vaše emailová adresa (nepovinné)\" | trans }}</label><input type=\"text\" ng-model=\"feedback.email\" class=\"form-control\"><br><alert ng-repeat=\"alert in alerts\" type=\"{{alert.type}}\" close=\"closeAlert($index)\">{{alert.msg}}</alert></div><div class=\"modal-footer\"><button ng-disabled=\"sending\" class=\"btn btn-primary\" ng-click=\"send()\">{{ \"Odeslat\" | trans }}</button> <button class=\"btn btn-danger\" ng-click=\"cancel()\">{{ \"Zavřít\" | trans }}</button></div>"
  );


  $templateCache.put('static/tpl/rating_modal.html',
    "<div class=\"modal-header text-center\"><h3 class=\"modal-title\">{% trans \"Jak těžké jsou kladené otázky?\"%}</h3>{{ \"Svou odpovědí nám pomáháte přizpůsobovat obtížnost otázek.\"%}</div><div class=\"rating modal-body\"><div class=\"text-center\" ng-hide=\"answer\"><a class=\"btn btn-lg btn-success\" ng-click=\"vote(1)\">{% trans \"Příliš lehké\"%}</a> <a class=\"btn btn-lg btn-primary\" ng-click=\"vote(2)\">{% trans \"Tak akorát\"%}</a> <a class=\"btn btn-lg btn-danger\" ng-click=\"vote(3)\">{% trans \"Příliš těžké\"%}</a> <a class=\"pull-right\" href=\"\" ng-click=\"cancel()\">{% trans \"Nevím / nechci odpovídat\"%}</a><div class=\"clearfix\"></div></div>{%verbatim%}<alert ng-repeat=\"alert in alerts\" type=\"{{alert.type}}\" close=\"closeAlert($index)\">{{alert.msg}}</alert>{%endverbatim%}</div><div class=\"modal-footer\" ng-show=\"answer\"><button class=\"btn btn-danger\" ng-click=\"cancel()\">{% trans \"Zavřít\"%}</button></div>"
  );

}]);
