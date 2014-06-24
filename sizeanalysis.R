folderpath <- "~/Documents/PAF/data/"
firstname <- "dijkstra-O3-0.7M-"
lastname <- "-EnergyData-1.5Ghz.txt"

sizes <- c("5", "10", "15", "20", "25", "30", "35", "40")
power <- matrix(ncol=8)
energy <- matrix(ncol=8)
time <- matrix(ncol=8)
i <- 1
for (size in sizes) {
	filepath <- paste(c(folderpath, firstname, size, lastname), collapse='')
	mydata <- read.table(filepath)
	power[i] <- mean(mydata[,21] + mydata[,24])

	time[i] <- mydata[nrow(mydata), 1] - mydata[1,1] - 3
	energy[i] <- time[i] * power[i]
	i <- i + 1
}
plot(x=sizes, y=energy, main="dijkstra E(size)")

