/* Load all the biojs libraries
This section will contain link to the source of all the installed biojs components */
console.log('biojs-require loaded');
var jsref = $('<script/>')
              .attr('src', 'http://localhost:8000/msa_bundle.js')
              .appendTo($('body'));

/* Load all biojs modules */
var msa = require(['msa']);
//var msa = require('msa');
console.log(msa);
