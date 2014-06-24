folderpath <- "~/Development/PAF/data/"

dfir <- "2dfir-O3-80.0M-25-EnergyData-"
blowfish <- "2dfir-O3-80.0M-25-EnergyData-"
crc <-"crc32-O3-300.0M-25-EnergyData-"
cubic <- "cubic-O3-50.0M-25-EnergyData-"
dijkstra <- "dijkstra-O3-0.7M-25-EnergyData-"
fdct <- "fdct-O3-70.0M-25-EnergyData-"
float <- "float_matmult-O3-18.0M-25-EnergyData-"
int <- "int_matmult-O3-6.5M-25-EnergyData-"
rijndael <- "rijndael-O3-150.0M-25-EnergyData-"
sha <- "sha-O3-32.0M-25-EnergyData-"
filenametab = c(dfir, blowfish, crc, cubic, dijkstra, fdct, float, int, rijndael, sha)

plotdata <- function(filename){
	frequencies <- c("0.25", "0.3", "0.35", "0.4", "0.5", "0.6", "0.8", "0.9", "1.0" ,"1.1" ,"1.2" ,"1.3" ,"1.4" ,"1.5" ,"1.6" )
	power <- matrix(ncol=15)
	energy <- matrix(ncol=15)
	time <- matrix(ncol=15)
	i <- 1
	for (frequency in frequencies) {
		filepath <- paste(c(folderpath, filename, frequency, "Ghz.txt"), collapse='')
		mydata <- read.table(filepath)
		power[i] <- mean(mydata[,20] + mydata[,23])

		time[i] <- mydata[nrow(mydata), 1] - mydata[1,1] 
		energy[i] <- time[i] * power[i]
		i <- i + 1
	}
	plot(x=frequencies, y=energy, main=filename)
}

#plotdata(rijndael)
for(filename in filenametab) {
	plotdata(filename)
	Sys.sleep(2)
}