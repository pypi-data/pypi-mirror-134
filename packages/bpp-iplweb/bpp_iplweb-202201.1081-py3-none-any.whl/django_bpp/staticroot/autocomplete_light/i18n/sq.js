/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(e){var n;e&&e.fn&&e.fn.select2&&e.fn.select2.amd&&(n=e.fn.select2.amd),n.define("select2/i18n/sq",[],function(){return{errorLoading:function(){return"Rezultatet nuk mund të ngarkoheshin."},inputTooLong:function(e){var n=e.input.length-e.maximum,t="Të lutem fshi "+n+" karakter";return 1!=n&&(t+="e"),t},inputTooShort:function(e){return"Të lutem shkruaj "+(e.minimum-e.input.length)+" ose më shumë karaktere"},loadingMore:function(){return"Duke ngarkuar më shumë rezultate…"},maximumSelected:function(e){var n="Mund të zgjedhësh vetëm "+e.maximum+" element";return 1!=e.maximum&&(n+="e"),n},noResults:function(){return"Nuk u gjet asnjë rezultat"},searching:function(){return"Duke kërkuar…"},removeAllItems:function(){return"Hiq të gjitha sendet"}}}),n.define,n.require},event=new CustomEvent("dal-language-loaded",{lang:"sq"});document.dispatchEvent(event);