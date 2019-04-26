# experiment ID
exp = "exp-1"

# data directories
data_dir = "/content/datasets/original/SQuAD/"
train_dir = data_dir + "train/"
dev_dir = data_dir + "dev/"

# model paths
# spacy_en = "/Users/gdamien/Data/spacy/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0"
spacy_en = "/content/datasets/processed/SQuAD/en_core_web_sm-2.1.0"
# glove = "/Users/gdamien/Data/glove.6B/" + "glove.6B.{}d.txt"
glove = "/content/datasets/original/Glove/glove.840B.300d.txt"
squad_models = "output/" + exp

# preprocessing values
max_words = -1
word_embedding_size = 100
char_embedding_size = 8
max_len_context = 400
max_len_question = 50
max_len_word = 25

# training hyper-parameters
num_epochs = 15
batch_size = 64
learning_rate = 0.5
drop_prob = 0.2
hidden_size = 100
char_channel_width = 5
char_channel_size = 100
cuda = False
pretrained = False
