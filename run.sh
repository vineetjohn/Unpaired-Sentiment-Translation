CUDA_VISIBLE_DEVICES=2 nohup python run_summarization.py --mode=train --run_method=auto-encoder --data_path=../dataset/review_generation_dataset/train/* --vocab_path=../dataset/review_generation_dataset/vocab.txt --log_root=log_autoencoder --exp_name=myexperiment --gpuid=0 > log.txt &
