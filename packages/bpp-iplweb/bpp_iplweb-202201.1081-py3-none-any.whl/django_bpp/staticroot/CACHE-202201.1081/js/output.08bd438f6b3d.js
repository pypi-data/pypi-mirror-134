/*!
 * Django Autocomplete Light
 */var yl=yl||{};yl.functions={};yl.registerFunction=function(name,func){if(this.functions.hasOwnProperty(name)){console.error('The DAL function "'+name+'" has already been registered.');return}
if(typeof func!='function'){throw new Error('The custom DAL function must be a function.');}
this.functions[name]=func;var event=new CustomEvent('dal-function-registered.'+name,{detail:{name:name,func:func}})
window.dispatchEvent(event);};window.addEventListener("load",function(){window.django=window.django||{};if(!django.hasOwnProperty('jQuery')&&jQuery!=='undefined'){django.jQuery=jQuery;}
(function($){$.fn.getFormPrefix=function(){var parts=$(this).attr('name').split('-');var prefix='';for(var i in parts){var testPrefix=parts.slice(0,-i).join('-');if(!testPrefix.length)continue;testPrefix+='-';var result=$(':input[name^='+testPrefix+']')
if(result.length){return testPrefix;}}
return'';}
$.fn.getFormPrefixes=function(){var parts=$(this).attr('name').split('-').slice(0,-1);var prefixes=[];for(i=0;i<parts.length;i+=2){var testPrefix=parts.slice(0,-i||parts.length).join('-');if(!testPrefix.length)
continue;testPrefix+='-';var result=$(':input[name^='+testPrefix+']')
if(result.length)
prefixes.push(testPrefix);}
prefixes.push('');return prefixes;}
if(typeof dalLoadLanguage!=='undefined'){dalLoadLanguage($);}else{document.addEventListener('dal-language-loaded',function(e){dalLoadLanguage($);})}
var event=new CustomEvent('dal-init-function');document.dispatchEvent(event);var initialized=[];$.fn.excludeTemplateForms=function(){return this.not('[id*=__prefix__]').filter(function(){return!this.id.match(/-empty-/)||this.id.match(/-\d+-empty-\d+-/);});}
function initialize(element){if(typeof element==='undefined'||typeof element==='number'){element=this;}
if(initialized.indexOf(element)>=0){return;}
var dalFunction=$(element).attr('data-autocomplete-light-function');if(yl.functions.hasOwnProperty(dalFunction)&&typeof yl.functions[dalFunction]=='function'){yl.functions[dalFunction]($,element);}else if(yl.functions.hasOwnProperty(dalFunction)){window.addEventListener('dal-function-registered.'+dalFunction,function(e){yl.functions[dalFunction]($,element);})}else{console.warn('Your custom DAL function "'+dalFunction+'" uses a deprecated event listener that will be removed in future versions. https://django-autocomplete-light.readthedocs.io/en/master/tutorial.html#overriding-javascript-code')}
$(element).trigger('autocompleteLightInitialize');initialized.push(element);}
if(!window.__dal__initialize){window.__dal__initialize=initialize;$(document).ready(function(){$('[data-autocomplete-light-function]').excludeTemplateForms().each(initialize);});if('MutationObserver'in window){new MutationObserver(function(mutations){var mutationRecord;var addedNode;for(var i=0;i<mutations.length;i++){mutationRecord=mutations[i];if(mutationRecord.addedNodes.length>0){for(var j=0;j<mutationRecord.addedNodes.length;j++){addedNode=mutationRecord.addedNodes[j];$(addedNode).find('[data-autocomplete-light-function]').excludeTemplateForms().each(initialize);}}}}).observe(document.documentElement,{childList:true,subtree:true});}else{$(document).on('DOMNodeInserted',function(e){$(e.target).find('[data-autocomplete-light-function]').excludeTemplateForms().each(initialize);});}}
function getCookie(name){var cookieValue=null;if(document.cookie&&document.cookie!=''){var cookies=document.cookie.split(';');for(var i=0;i<cookies.length;i++){var cookie=$.trim(cookies[i]);if(cookie.substring(0,name.length+1)==(name+'=')){cookieValue=decodeURIComponent(cookie.substring(name.length+1));break;}}}
return cookieValue;}
document.csrftoken=getCookie('csrftoken');if(document.csrftoken===null){var $csrf=$('form :input[name="csrfmiddlewaretoken"]');if($csrf.length>0){document.csrftoken=$csrf[0].value;}}})(django.jQuery);(function($){'use strict';var init=function($element,options){var settings=$.extend({ajax:{data:function(params){return{term:params.term,page:params.page,app_label:$element.data('app-label'),model_name:$element.data('model-name'),field_name:$element.data('field-name')};}}},options);$element.select2(settings);};$.fn.djangoAdminSelect2=function(options){var settings=$.extend({},options);$.each(this,function(i,element){var $element=$(element);init($element,settings);});return this;};$(function(){$('.admin-autocomplete').not('[name*=__prefix__]').djangoAdminSelect2();});$(document).on('formset:added',(function(){return function(event,$newFormset){return $newFormset.find('.admin-autocomplete').djangoAdminSelect2();};})(this));}(django.jQuery));(function($,yl){yl.forwardHandlerRegistry=yl.forwardHandlerRegistry||{};yl.registerForwardHandler=function(name,handler){yl.forwardHandlerRegistry[name]=handler;};yl.getForwardHandler=function(name){return yl.forwardHandlerRegistry[name];};function getForwardStrategy(element){var checkForCheckboxes=function(){var all=true;$.each(element,function(ix,e){if($(e).attr("type")!=="checkbox"){all=false;}});return all;};if(element.length===1&&element.attr("type")==="checkbox"&&element.attr("value")===undefined){return"exists";}else if(element.length===1&&element.attr("multiple")!==undefined){return"multiple";}else if(checkForCheckboxes()){return"multiple";}else{return"single";}}
yl.getFieldRelativeTo=function(element,name){var prefixes=$(element).getFormPrefixes();for(var i=0;i<prefixes.length;i++){var fieldSelector="[name="+prefixes[i]+name+"]";var field=$(fieldSelector);if(field.length){return field;}}
return $();};yl.getValueFromField=function(field){var strategy=getForwardStrategy(field);var serializedField=$(field).serializeArray();if((serializedField==false)&&($(field).prop('disabled'))){$(field).prop('disabled',false);serializedField=$(field).serializeArray();$(field).prop('disabled',true);}
var getSerializedFieldElementAt=function(index){if(serializedField.length>index){return serializedField[index];}else{return null;}};var getValueOf=function(elem){if(elem.hasOwnProperty("value")&&elem.value!==undefined){return elem.value;}else{return null;}};var getSerializedFieldValueAt=function(index){var elem=getSerializedFieldElementAt(index);if(elem!==null){return getValueOf(elem);}else{return null;}};if(strategy==="multiple"){return serializedField.map(function(item){return getValueOf(item);});}else if(strategy==="exists"){return serializedField.length>0;}else{return getSerializedFieldValueAt(0);}};yl.getForwards=function(element){var forwardElem,forwardList,forwardedData,divSelector,form;divSelector="div.dal-forward-conf#dal-forward-conf-for-"+
element.attr("id")+", "+"div.dal-forward-conf#dal-forward-conf-for_"+
element.attr("id");form=element.length>0?$(element[0].form):$();forwardElem=form.find(divSelector).find('script');if(forwardElem.length===0){return;}
try{forwardList=JSON.parse(forwardElem.text());}catch(e){return;}
if(!Array.isArray(forwardList)){return;}
forwardedData={};$.each(forwardList,function(ix,field){var srcName,dstName;if(field.type==="const"){forwardedData[field.dst]=field.val;}else if(field.type==="self"){if(field.hasOwnProperty("dst")){dstName=field.dst;}else{dstName="self";}
forwardedData[dstName]=yl.getValueFromField(element);}else if(field.type==="field"){srcName=field.src;if(field.hasOwnProperty("dst")){dstName=field.dst;}else{dstName=srcName;}
var forwardedField=yl.getFieldRelativeTo(element,srcName);if(!forwardedField.length){return;}
forwardedData[dstName]=yl.getValueFromField(forwardedField);}else if(field.type==="javascript"){var handler=yl.getForwardHandler(field.handler);forwardedData[field.dst||field.handler]=handler(element);}});return JSON.stringify(forwardedData);};})(django.jQuery,yl);});;