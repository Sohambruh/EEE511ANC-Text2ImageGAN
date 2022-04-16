from trainer import Trainer
import argparse
from PIL import Image
import os
def main(type_m='gan',lr=0.0002,l1_coef=50,l2_coef=50,diter=5,cls_m=False,vis_screen='gan',save_path='',inference=False,pre_trained_disc=None,pre_trained_gen=None,dataset='birds',split=0,batch_size=64,num_workers=8,epochs=10):
    
    
    trainer = Trainer(type=type_m,
                      dataset=dataset,
                      split=split,
                      lr=lr,
                      diter=diter,
                      vis_screen=vis_screen,
                      save_path=save_path,
                      l1_coef=l1_coef,
                      l2_coef=l2_coef,
                      pre_trained_disc=pre_trained_disc,
                      pre_trained_gen=pre_trained_gen,
                      batch_size=batch_size,
                      num_workers=num_workers,
                      epochs=epochs
                      )
    
    if not args.inference:
        trainer.train(cls_m)
    else:
        trainer.predict()
