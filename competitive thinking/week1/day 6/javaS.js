def my_function(arg):
var text = "outside";
function logIt(){
  var text;
  console.log(text);
  text = 'inside';
};

logIt();
    



# Run your function through some test cases here
# Remember: debugging is half the battle!
print my_function('test input')
