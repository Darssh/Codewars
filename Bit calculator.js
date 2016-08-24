'''In this kata your task is to create bit calculator. Function arguments are two bit representation of numbers ("101","1","10"...), and you must return their sum in decimal representation.

Test.expect(calculate("10","10") == 4);
Test.expect(calculate("10","0") == 2);
Test.expect(calculate("101","10") == 7);
parseInt and some Math functions are disabled.

Those Math functions are enabled: pow,round,random'''


function calculate(num1,num2){
  num1 = num1.split('').reverse();
  num2 = num2.split('').reverse();
  var n1 = 0;
  var mul = 1;
  num1.forEach(function(entry) {
    n1 += entry * mul;
    mul = mul * 2;
  });
  var n2 = 0;
  var mul = 1;
  num2.forEach(function(entry) {
    n2 += entry * mul;
    mul = mul * 2;
  });
  return (n1 + n2);
}



'''Test case:

describe("calculate",function(){
  it("should work for positive numbers",function(){
    Test.expect(calculate("1","1")==2);
    Test.expect(calculate("10","10")==4);
    Test.expect(calculate("10","0")==2);
    Test.expect(calculate("10","1")==3);
  });
});'''


'''
Other solitions:

function calculate(num1,num2){
   return binaryToDecimal(num1)+binaryToDecimal(num2);
}

function binaryToDecimal(b){
    var arr = b.split('');
    var d = 0;
    for (var i = arr.length, j = 0; i > 0; i--, j++){
       if (arr[i-1] == 1){d += Math.pow(2, j)}
    }
    return d;
}'''