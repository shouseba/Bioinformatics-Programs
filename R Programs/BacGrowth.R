#Program plots the growth curve of bacteria given the growth rate
#as a parameter. Shows theoretical exponential growth.
grow = function(growth.rate){
	num_gen=10
	N = rep(0,num_gen)
	generation=rep(0,num_gen)
	N[1]=1
	for (i in 2:num_gen) {
		N[i] = growth.rate*N[i-1] #we replace "2" with "growth.rate"
		generation[i]=i
	}
	plot(N~generation, typ = "b")
	}
