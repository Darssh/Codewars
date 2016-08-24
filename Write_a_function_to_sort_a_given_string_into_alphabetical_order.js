'''Task :

Write a function to sort a given string into alphabetical order. 
Upper case and lower case should be sorted together (upper case first) and 
other characters should be sorted to the end, numbers first in ascending order, 
followed by punctuation. Spaces should be ignored.

For example:

Input string:

The cat sat on the mat

Output:

aaaceehhmnosTtttt

Input string:

“Happy 21st Birthday!”

Output:

aaBdHhipprsttyy12!””'''

function sort(str) {
  updated = str.replace(/[^a-zA-Z]/gi,'').toLowerCase().split('').sort();
  alpha = [];
  numeric = [];
  special = [];
  
  str.replace(/\s/g, '').split('').forEach(function(element){
    if(element == element.toUpperCase()){
       updated[updated.indexOf(element.toLowerCase())] = element;
    }
    if(isNumeric(element)){
      numeric.push(element);
    } else if(isValid(element)){
      special.push(element);
    } 
  });
  return updated.join('')+ numeric.sort().join('') + special.sort().join('') ;
}

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function isValid(str){
 return !/^[a-z0-9]+$/i.test(str);
}


/*function sort(str) {
  const CHARS = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!?’\'()*+,.…:"@#$%&^-;<>=[]_{}~“”£ '
  return str.split('').sort((a,b) => CHARS.indexOf(a) - CHARS.indexOf(b)).join('').trim()
}


function sort(str) {
  var st=(s)=>s==null ? [] : s.sort((a,b)=>a.toLowerCase().charCodeAt()*1000-/[A-Z]/.test(a)-b.toLowerCase().charCodeAt()*1000+/[A-Z]/.test(b));
  return st(str.match(/[A-Za-z]/gm)).concat(st(str.match(/\d/gm))).concat(st(str.match(/[^A-Za-z0-9 \n]/gm))).join("")
}*/