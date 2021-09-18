function countDown(num){
	if(num<=-1) return;
	else{
		console.log(num);
		countDown(num-1);
	}
}

countDown(10);