logGrowth = function(growth.rate, numGen, caryCap) {
	N = rep(0, numGen)
	Index = rep(0, numGen)
	N[1] = 1
	for(i in 2:numGen) {
		N[i] = (growth.rate*N[i-1]*((caryCap-(N[i-1]))/caryCap))
		Index[i] = i
	}
	plot(N~Index, typ="b")
}