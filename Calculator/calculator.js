var frist=null;
var prior_operation=null;
var old=false;
var old_latest;


function save(operator,a){
if(a==false){
frist=document.form.textview.value;
}else
{
	frist=document.form.textview.placeholder;
}
frist=parseFloat(frist);
if(frist<0==false && frist>=0 ==false)
{
	frist=0;
}
document.form.textview.value="";
prior_operation=operator;
}

function operator(operator)
{
	old=false;
	latest=parseFloat(document.form.textview.value);
	if(latest<0==false && latest>=0==false)
	{
		latest= old_latest
		prior_operation=5;
	}
	if(frist!=null){
	switch (prior_operation){
		case(1):
		document.form.textview.placeholder=add(frist,latest);
		old=true;
		break;

		case(2):
		document.form.textview.placeholder=substract(frist,latest);
		old=true;
		break;

		case(3):
		document.form.textview.placeholder=multiply_b(frist,latest);
		old=true;
		break;

		case(4):
		document.form.textview.placeholder=divide(frist,latest);
		old=true;
		break;

		case(5):
		old=false;
		break;
	}
	old_latest=latest;
	save(operator,true);
}else{
	save(operator,false);
}
}
function toNegative(){
	if(document.form.textview.value!=""){
	document.form.textview.value=(parseFloat(document.form.textview.value)*-1);
	}else
	{ if(document.form.textview.placeholder!=""){
		document.form.textview.placeholder=(parseFloat(document.form.textview.placeholder)*-1);
		frist=frist*-1;
	}
	}

}
function toPower(){
	if(document.form.textview.value!=""){
	document.form.textview.value=(parseFloat(document.form.textview.value)*document.form.textview.value);
	}else
	{ if(document.form.textview.placeholder!=""){
		document.form.textview.placeholder=(parseFloat(document.form.textview.placeholder)*document.form.textview.placeholder);
		frist=frist*frist;
	}
	}

}
function Reset(){
	document.form.textview.value="";
	document.form.textview.placeholder="";
	frist=null;
	prior_operation=null;
	latest=null;
}
function add (a,b) {
	return (a+b);	
}

function divide (a,b) {
	return (a/b);	
}

function substract (a,b) {
	return (a-b);
}


function sum (array) {
	let result=0;
	if (Array.isArray(array))
	{
		for(let i=0; i<array.length; i++)
		{
			result=array[i]+result;
		}
		return result;
	}else{
		return null;
	}
	
}
function multiply_b(a,b)
{
	return a*b
}

function multiply (array)  {
	let result=1;
	if (Array.isArray(array))
	{
		for(let i=0; i<array.length; i++)
		{
			result=array[i]*result;
		}
		return result;
	}else{
		return null;
	}
	
}

function power(a,b) {
	return Math.pow(a,b)
}

function factorial(e) {
	let a=1;
	while(e>0)
	{
		a=e*a
		e--;
	}
	return a;
}
function insert(num){
	if(old==true && document.form.textview.value=="")
	{
		Reset();
	}
	document.form.textview.value=document.form.textview.value+num;
}
function cut(){

	a=""+document.form.textview.value;
	document.form.textview.value=	a.substring(0,a.length-1);
}