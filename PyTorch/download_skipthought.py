import os

print ('Downloading Skip-Thought Model ...........')
os.system('wget http://www.cs.toronto.edu/~rkiros/models/dictionary.txt')
os.system('wget http://www.cs.toronto.edu/~rkiros/models/utable.npy')
os.system('wget http://www.cs.toronto.edu/~rkiros/models/btable.npy')
os.system('wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz')
os.system('wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl')
os.system('wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz')
os.system('wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl')

print ('Download Completed ............')