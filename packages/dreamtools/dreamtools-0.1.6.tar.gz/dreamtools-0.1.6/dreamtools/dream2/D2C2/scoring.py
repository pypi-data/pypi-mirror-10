
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC

class D2C2(Challenge, D3D4ROC):
    """A class dedicated to D2C2 challenge


    ::

        from dreamtools import D2C2
        s = D2C2()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D2C2, self).__init__('D2C2')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def download_template(self):
        return self._pj([self._path2data, 'templates', 'D2C2_template.txt'])

    def score(self, filename):
        gold = self._pj([self._path2data, 'goldstandard', 'D2C2_goldstandard.txt'])
        prediction = filename

        self.gold_edges =  pd.read_csv(gold, sep='\t', header=None)
        self.prediction =  pd.read_csv(prediction, sep='\t', header=None)
        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])


        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
            self.prediction, gold_index)

        #p_auroc = self._probability(self.pdf_data['auroc_X'][0], 
        #    self.pdf_data['auroc_Y'][0], AUROC)
                                                
        #p_aupr = self._probability(self.pdf_data['aupr_X'][0], 
        #    self.pdf_data['aupr_Y'][0], AUC)

        #return AUC, AUROC, prec, rec, tpr, fpr
        #p_auroc, p_aupr

        results = {'AUPR':AUC, 'AUROC':AUROC}

        return results

"""TODO


pecific precision values
TrueP = [1 2 5 20 100 500]; 
prec0 = zeros(6,1);
for i=1:length(TrueP)
    if(TrueP(i)<=P)
        rec0(i)=TrueP(i)/P;
        j=find(rec == rec0(i));
        j=min(j); %In case there is more than 1 precision values for rec(i)
        prec0(i)=prec(j);
    end
end
first = 0;
k =1;
while k < L
    if prec(k) > 0
        first = prec(k);
        k = L;
    end
    k=k+1;
end








"""









