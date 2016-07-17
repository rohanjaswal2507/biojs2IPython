/* Load all the biojs libraries
This section will contain link to the source of all the installed biojs components */
console.log('biojs-require loaded');

var jsref = $('<script/>')
              .attr('src', 'https://s3.eu-central-1.amazonaws.com/cdn.bio.sh/msa/latest/msa.min.gz.js')
              .appendTo($('body'));

/* Load all biojs modules */
var msaModule = require(['msa'], function(msa){
  console.log('require working');
  window.msa = msa;
  console.log(window.msa);
});
