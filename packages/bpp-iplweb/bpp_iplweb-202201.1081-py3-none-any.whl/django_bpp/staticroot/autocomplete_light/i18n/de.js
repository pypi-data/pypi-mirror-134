/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(e){var n;e&&e.fn&&e.fn.select2&&e.fn.select2.amd&&(n=e.fn.select2.amd),n.define("select2/i18n/de",[],function(){return{errorLoading:function(){return"Die Ergebnisse konnten nicht geladen werden."},inputTooLong:function(e){return"Bitte "+(e.input.length-e.maximum)+" Zeichen weniger eingeben"},inputTooShort:function(e){return"Bitte "+(e.minimum-e.input.length)+" Zeichen mehr eingeben"},loadingMore:function(){return"Lade mehr Ergebnisse…"},maximumSelected:function(e){var n="Sie können nur "+e.maximum+" Element";return 1!=e.maximum&&(n+="e"),n+" auswählen"},noResults:function(){return"Keine Übereinstimmungen gefunden"},searching:function(){return"Suche…"},removeAllItems:function(){return"Entferne alle Elemente"}}}),n.define,n.require},event=new CustomEvent("dal-language-loaded",{lang:"de"});document.dispatchEvent(event);