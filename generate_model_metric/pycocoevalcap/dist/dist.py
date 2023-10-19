
class Dist():
    '''
    Class for computing Distinct

    '''
    def __init__(self, n, cal_ref=False):
        # vrama91: updated the value below based on discussion with Hovey
        self._n=n
        self.cal_ref=cal_ref

    def compute_score(self, refs, candidates):
        """
        Computes Rouge-L score given a set of reference and candidate sentences for the dataset
        Invoked by evaluate_captions.py 
        :param hypo_for_image: dict : candidate / test sentences with "image name" key and "tokenized sentences" as values 
        :param ref_for_image: dict : reference MS-COCO sentences with "image name" key and "tokenized sentences" as values
        :returns: average_score: float (mean ROUGE-L score computed by averaging scores for all the images)
        """

        if self.cal_ref==False:
            need_cal_list=candidates
        else:
            need_cal_list=refs

        score=[]
        for k in range(1,self._n+1):
            d = {}
            tot = 0
            for sen in need_cal_list.values():
                sen=sen[0].split(' ')
                for i in range(0, len(sen)-k):
                    key = tuple(sen[i:i+k])
                    d[key] = 1
                    tot += 1
            if tot > 0:
                dist = len(d) / tot
            else:
                dist = 0.
            score.append(dist)
        return score, score

    def method(self):
        return "Rouge"
