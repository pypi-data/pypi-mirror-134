/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(n){var e;n&&n.fn&&n.fn.select2&&n.fn.select2.amd&&(e=n.fn.select2.amd),e.define("select2/i18n/dsb",[],function(){function a(n,e){return 1===n?e[0]:2===n?e[1]:2<n&&n<=4?e[2]:5<=n?e[3]:void 0}var u=["znamuško","znamušce","znamuška","znamuškow"],e=["zapisk","zapiska","zapiski","zapiskow"];return{errorLoading:function(){return"Wuslědki njejsu se dali zacytaś."},inputTooLong:function(n){var e=n.input.length-n.maximum;return"Pšosym lašuj "+e+" "+a(e,u)},inputTooShort:function(n){var e=n.minimum-n.input.length;return"Pšosym zapódaj nanejmjenjej "+e+" "+a(e,u)},loadingMore:function(){return"Dalšne wuslědki se zacytaju…"},maximumSelected:function(n){return"Móžoš jano "+n.maximum+" "+a(n.maximum,e)+"wubraś."},noResults:function(){return"Žedne wuslědki namakane"},searching:function(){return"Pyta se…"},removeAllItems:function(){return"Remove all items"}}}),e.define,e.require},event=new CustomEvent("dal-language-loaded",{lang:"dsb"});document.dispatchEvent(event);