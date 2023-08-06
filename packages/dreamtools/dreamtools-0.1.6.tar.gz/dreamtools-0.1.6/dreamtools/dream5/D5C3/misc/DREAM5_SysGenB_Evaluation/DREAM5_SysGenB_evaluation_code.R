#Evaluation code for DREAM5 Challenges 3 Systems Genetics Challenges B
#Alberto de la Fuente, Nov 2 2010

##############################################################
########Loading the Gold Standard phenotypes##################
##############################################################

GSB1 <- as.matrix(read.table("GS/DREAM5_SysGenB1_TestPhenotypeData.txt", header = TRUE))
GSB2 <- as.matrix(read.table("GS/DREAM5_SysGenB2_TestPhenotypeData.txt", header = TRUE))
GSB3 <- as.matrix(read.table("GS/DREAM5_SysGenB3_TestPhenotypeData.txt", header = TRUE))

##############################################################
######Loading the predicted phenotypes########################
##############################################################

#¡¡change to the names you use for your prediction files!!

PredictionB1 <- as.matrix(read.table("Predictions/DREAM5_SysGenB1_your_Predictions.txt", header = TRUE))
PredictionB2 <- as.matrix(read.table("Predictions/DREAM5_SysGenB2_your_Predictions.txt", header = TRUE))
PredictionB3 <- as.matrix(read.table("Predictions/DREAM5_SysGenB3_your_Predictions.txt", header = TRUE))

##############################################################
#Calculating correlations between gold standard and predicted#
#phenotypes, p-values for the correlations, overall scores####
##############################################################

CORP1 <-matrix(nrow = 1, ncol = 3)
CORP2 <-matrix(nrow = 1, ncol = 3)
PVALP1 <-matrix(nrow = 1, ncol = 3)
PVALP2 <-matrix(nrow = 1, ncol = 3)
SCORES <-matrix(nrow = 1, ncol = 3)

T1 <- cor.test(GSB1[1,], PredictionB1[1,], alternative = c("g"), method = c("s"))
T2 <- cor.test(GSB1[2,], PredictionB1[2,], alternative = c("g"),method = c("s"))

CORP1[1,1] <- as.numeric(T1[4])	#The Spearman correlation for phenotype 1 between GS and Predicted
CORP2[1,1] <- as.numeric(T2[4]) 	#The Spearman correlation for phenotype 2 between GS and Predicted
PVALP1[1,1] <- as.numeric(T1[3])	#The p-value for the test with alternative Spearman correlation for phenotype 1 > 0
PVALP2[1,1] <- as.numeric(T2[3])	#The p-value for the test with alternative Spearman correlation for phenotype 2 > 0
SCORES[1,1] <- -(log(as.numeric(T1[3]))+ log(as.numeric(T2[3])))	#The overal scores

T1 <- cor.test(GSB2[1,], PredictionB2[1,], alternative = c("g"), method = c("s"))
T2 <- cor.test(GSB2[2,], PredictionB2[2,], alternative = c("g"),method = c("s"))

CORP1[1,2] <- as.numeric(T1[4])
CORP2[1,2] <- as.numeric(T2[4])
PVALP1[1,2] <- as.numeric(T1[3])
PVALP2[1,2] <- as.numeric(T2[3])
SCORES[1,2] <- -(log(as.numeric(T1[3]))+ log(as.numeric(T2[3])))

T1 <- cor.test(GSB3[1,], PredictionB3[1,], alternative = c("g"), method = c("s"))
T2 <- cor.test(GSB3[2,], PredictionB3[2,], alternative = c("g"),method = c("s"))

CORP1[1,3] <- as.numeric(T1[4])
CORP2[1,3] <- as.numeric(T2[4])
PVALP1[1,3] <- as.numeric(T1[3])
PVALP2[1,3] <- as.numeric(T2[3])
SCORES[1,3] <- -(log(as.numeric(T1[3]))+ log(as.numeric(T2[3])))

CORP1
CORP2
PVALP1
PVALP2
SCORES

write.table(CORP1, file = "Results/CORP1.txt",sep = "\t")
write.table(CORP2, file = "Results/CORP2.txt",sep = "\t")
write.table(PVALP1, file = "Results/PVALP1.txt",sep = "\t")
write.table(PVALP2, file = "Results/PVALP2.txt",sep = "\t")

##############################################################
#######Random scores##########################################
##############################################################
x <- 1000	#increase the number of permutations as you like (100K were used for evaluations in DREAM5

RANDOMSCORES <-matrix(nrow = x, ncol = 3)
PVALS <-matrix(nrow = 1, ncol = 3)
coord <-matrix(nrow = 1, ncol = 30)
coord2 <-matrix(nrow = 1, ncol = 30)

for (i in c(1:x))
{
	#generate random coordinates
	coord <- sample.int(30, size = 30, replace = FALSE, prob = NULL) 
	coord2 <- sample.int(30, size = 30, replace = FALSE, prob = NULL)

	# Obtaining random scores
	T1 <- cor.test(GSB1[1,], PredictionB1[1,coord], alternative = c("g"), method = c("s"))
	T2 <- cor.test(GSB1[2,], PredictionB1[2,coord2], alternative = c("g"),method = c("s"))
	RANDOMSCORES[i,1] <- -(log(as.numeric(T1[3])) + log(as.numeric(T2[3])))

	T1 <- cor.test(GSB2[1,], PredictionB2[1,coord], alternative = c("g"), method = c("s"))
	T2 <- cor.test(GSB2[2,], PredictionB2[2,coord2], alternative = c("g"),method = c("s"))
	RANDOMSCORES[i,2] <- -(log(as.numeric(T1[3])) + log(as.numeric(T2[3])))

	T1 <- cor.test(GSB3[1,], PredictionB3[1,coord], alternative = c("g"), method = c("s"))
	T2 <- cor.test(GSB3[2,], PredictionB3[2,coord2], alternative = c("g"),method = c("s"))
	RANDOMSCORES[i,3] <- -(log(as.numeric(T1[3])) + log(as.numeric(T2[3])))

	}

	#Obtaining p-values
	for (k in c(1:3))
	{
		PVALS[k] <- sum(RANDOMSCORES[,k] >= SCORES[1,k])/x
	}

##############################################################
##############################################################
##############################################################
write.table(PVALS, file = "Results/PVALS.txt",sep = "\t")

CORP1
CORP2
PVALP1
PVALP2
SCORES
PVALS
