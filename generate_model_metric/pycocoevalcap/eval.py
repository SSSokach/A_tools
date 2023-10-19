from .dist.dist import Dist
from .bleu.bleu import Bleu
from .meteor.meteor import Meteor
from .rouge.rouge import Rouge
from .cider.cider import Cider
from transformers import AutoTokenizer
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
class COCOEvalCap:
    def evaluate(self,cands, refs):

        tokenizer = AutoTokenizer.from_pretrained("/home/shilongwang/workplace/A_pretrain_models/bert_base_chinese")
        refs  = {i:[' '.join(tokenizer.tokenize(ref))] for i,ref in enumerate(refs)}
        cands = {i:[' '.join(tokenizer.tokenize(cand))] for i,cand in enumerate(cands)}

        # =================================================
        # Set up scorers
        # =================================================
        scorers = [
            (Dist(3,cal_ref=True), ["Dist_1_ref", "Dist_2_ref", "Dist_3_ref"]),
            (Dist(3), ["Dist_1", "Dist_2", "Dist_3"]),
            (Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
            (Meteor(),"METEOR"),
            (Rouge(), "ROUGE_L"),
            (Cider(), "CIDEr")
        ]

        # =================================================
        # Compute scores
        # =================================================
        result={}
        for scorer, method in scorers:
            score, scores = scorer.compute_score(refs, cands)
            if type(method) == list:
                for sc, scs, m in zip(score, scores, method):
                    print ("%s: %0.2f"%(m, sc*100))
                    result[m]=round(sc*100,2)
            else:
                print ("%s: %0.2f"%(method, score*100))
                result[method]=round(score*100,2)
        return result