function add()
{
  x = document.getElementsByClassName("xVal")[0].value;
	y = document.getElementsByClassName("yVal")[0].value;
	var ans = x + y;
	document.getElementsByClassName("answer")[0].value = ans;
document.calculator.ans.value+='+'
  return ans;
}

function subtract()
{
  x = document.getElementsByClassName("xVal")[0].value;
	y = document.getElementsByClassName("yVal")[0].value;
	var ans = x - y;
	document.getElementsByClassName("answer")[0].value = ans;
}
