CUDA_VISIBLE_DEVICES=2 nohup python run_summarization.py --mode='test' --data_path=train/* --vocab_path=vocab.txt --log_root=log --exp_name=myexperiment --gpuid=0