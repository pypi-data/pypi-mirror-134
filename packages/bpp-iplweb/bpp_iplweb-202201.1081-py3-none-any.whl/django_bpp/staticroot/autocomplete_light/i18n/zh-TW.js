/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(n){var e;n&&n.fn&&n.fn.select2&&n.fn.select2.amd&&(e=n.fn.select2.amd),e.define("select2/i18n/zh-TW",[],function(){return{inputTooLong:function(n){return"請刪掉"+(n.input.length-n.maximum)+"個字元"},inputTooShort:function(n){return"請再輸入"+(n.minimum-n.input.length)+"個字元"},loadingMore:function(){return"載入中…"},maximumSelected:function(n){return"你只能選擇最多"+n.maximum+"項"},noResults:function(){return"沒有找到相符的項目"},searching:function(){return"搜尋中…"},removeAllItems:function(){return"刪除所有項目"}}}),e.define,e.require},event=new CustomEvent("dal-language-loaded",{lang:"zh-TW"});document.dispatchEvent(event);