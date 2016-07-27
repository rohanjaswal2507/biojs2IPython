/* Load all the biojs libraries
This section will contain link to the source of all the installed biojs components
or code to load all the installed components to the browser */
console.log('biojs-require working');
var jsref = $('<script/>')
              .attr('src', 'https://s3.eu-central-1.amazonaws.com/cdn.bio.sh/msa/latest/msa.min.gz.js')
              .appendTo($('body'));

// Function to load biojs component script and require the module so that it could be used in ipython

function loadScript(url, callback){
  console.log('running loadScript for url: ' + url);
  var head = document.getElementsByTagName('head')[0];
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = url;

  script.onreadystatechange = callback;
  script.onload = callback;

  head.appendChild(script);

}


var requireModule = function(moduleName, url){
  var loadedModule = require(moduleName);
  var pythonClassName = moduleName.replace(/[^A-Z0-9]/ig, "");
  console.log(pythonClassName);
  window[pythonClassName] = "loadedModule";
};


// TO DO: loop to load all the scripts
var wig_url = "http://localhost:8000/biojsviswigexplorer.js";
loadScript(wig_url, requireModule('biojs-vis-wigexplorer', wig_url));

/* Load all biojs modules */
var msaModule = require(['msa'], function(msa){
  console.log('require working');
  window.msa = msa;
  console.log(window.msa);
});

console.log('execution finished');
