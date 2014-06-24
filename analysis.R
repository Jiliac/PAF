folderpath <- "~/Documents/PAF/data/"

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
filenametab <- c(dfir, blowfish, crc, cubic, dijkstra, fdct, float, int, rijndael, sha)
repeattab <- c(80000000, 950000000, 300000000, 50000000, 700000, 18000000, 6500000, 150000000, 32000000)

repeattab <- function(filename){
	if (filename == dfir)
		return(80000000)
	else if(filename == blowfish)
		return(950000000)
	else if(filename == crc)
		return(300000000)
	else if(filename == cubic)
		return(50000000)
	else if(filename == dijkstra)
		return(700000)
	else if(filename == fdct)
		return(70000000)
	else if(filename == float)
		return(18000000)
	else if(filename == int)
		return(6500000)
	else if(filename == rijndael)
		return (150000000)
	else if(filename == sha)
		return(32000000)
	else
		return(1)
}

power <- matrix(ncol=15)
energy <- matrix(ncol=15)
time <- matrix(ncol=15)


plotdata <- function(filename){

	frequencies <- c("0.25", "0.3", "0.35", "0.4", "0.5", "0.6", "0.8", "0.9", "1.0" ,"1.1" ,"1.2" ,"1.3" ,"1.4" ,"1.5" ,"1.6" )
	i <- 1
	repeattime <- repeattab(filename)
	for (frequency in frequencies) {
		filepath <- paste(c(folderpath, filename, frequency, "Ghz.txt"), collapse='')
		mydata <- read.table(filepath)
		power[i] <- mean(mydata[,21] + mydata[,24]) 
		time[i] <- ( mydata[nrow(mydata), 1] - mydata[1,1] - 3 ) / repeattime
		energy[i] <- time[i] * power[i]
		i <- i + 1
	}
	plot(x=frequencies, y=energy, main=filename)
	filename <- c(frequencies, time, power, energy)
}

for(filename in filenametab) {
	plotdata(filename)
	Sys.sleep(2)
}
